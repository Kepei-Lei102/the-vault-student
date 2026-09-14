"""
file-processing-records.py — the three file organisations, built for real.

Companion to [[File Processing and Exception Handling]].

Everything the syllabus names is done on an actual file on disk, not on a
list pretending to be one:

  * a RECORD serialised to a fixed number of bytes with `struct` — the thing
    that makes "address = slot × record size" work at all;
  * a SERIAL file: records appended in arrival order, found by scanning;
  * a SEQUENTIAL file: records kept in key order, updated by the classic
    master + transaction MERGE (a whole new file is written);
  * a RANDOM file: slot computed from the key by a hash, reached with one
    `seek`, collisions resolved by linear probing, deletion by tombstone.

The random-file engine is then fuzzed against a Python `dict` — thousands of
random puts, gets and deletes, every answer compared — so the claims in the
card are checked, not asserted.  Run:  python3 file-processing-records.py
"""
from __future__ import annotations

import os
import random
import struct
import tempfile
from dataclasses import dataclass

# ----------------------------------------------------------------------------
# 1. A record with a fixed size on disk
# ----------------------------------------------------------------------------
# The exam's TYPE:  AccountNumber : INTEGER, Name : STRING, Balance : REAL
# `struct` format:   i = 4-byte int, 24s = 24 bytes of text, d = 8-byte float,
#                    ? = 1-byte flag (0 empty, 1 live, 2 deleted).
# Fixed length is the whole point: slot k begins at byte k * RECORD_SIZE.
FMT = "<Bi24sd"
RECORD_SIZE = struct.calcsize(FMT)     # 37 bytes
EMPTY, LIVE, DELETED = 0, 1, 2


@dataclass
class Account:
    number: int
    name: str
    balance: float


def pack(rec: Account | None, flag: int = LIVE) -> bytes:
    if rec is None:                      # an empty or tombstoned slot
        return struct.pack(FMT, flag, 0, b"", 0.0)
    return struct.pack(FMT, flag, rec.number, rec.name.encode("utf-8")[:24], rec.balance)


def unpack(raw: bytes) -> tuple[int, Account | None]:
    flag, number, name, balance = struct.unpack(FMT, raw)
    if flag != LIVE:
        return flag, None
    return flag, Account(number, name.rstrip(b"\x00").decode("utf-8"), balance)


# ----------------------------------------------------------------------------
# 2. SERIAL — arrival order; find = scan from the top
# ----------------------------------------------------------------------------
def serial_append(path: str, rec: Account) -> None:
    with open(path, "ab") as f:          # APPEND: the file pointer starts at the end
        f.write(pack(rec))


def serial_find(path: str, key: int) -> tuple[Account | None, int]:
    """Return (record, number of records read). O(n): there is no shortcut."""
    reads = 0
    with open(path, "rb") as f:
        while raw := f.read(RECORD_SIZE):
            reads += 1
            _, rec = unpack(raw)
            if rec is not None and rec.number == key:
                return rec, reads
    return None, reads


# ----------------------------------------------------------------------------
# 3. SEQUENTIAL — key order; update = merge master with a sorted transaction file
# ----------------------------------------------------------------------------
def read_all(path: str) -> list[Account]:
    out = []
    with open(path, "rb") as f:
        while raw := f.read(RECORD_SIZE):
            _, rec = unpack(raw)
            if rec is not None:
                out.append(rec)
    return out


def sequential_write(path: str, records: list[Account]) -> None:
    with open(path, "wb") as f:          # WRITE: truncates — a new file every time
        for rec in sorted(records, key=lambda r: r.number):
            f.write(pack(rec))


def sequential_find(path: str, key: int) -> tuple[Account | None, int]:
    """Still a scan — but it can STOP as soon as the keys pass the target."""
    reads = 0
    with open(path, "rb") as f:
        while raw := f.read(RECORD_SIZE):
            reads += 1
            _, rec = unpack(raw)
            if rec is None:
                continue
            if rec.number == key:
                return rec, reads
            if rec.number > key:         # sorted, so it cannot be further on
                return None, reads
    return None, reads


def sequential_merge_update(master: str, transactions: list[tuple[str, Account]], out: str) -> None:
    """The batch job: old master + sorted transactions -> new master.
    Each transaction is ('add', rec), ('update', rec) or ('delete', rec).
    Both inputs are read once, in key order; the new file is written once."""
    olds = read_all(master)
    trans = sorted(transactions, key=lambda t: t[1].number)
    i = j = 0
    with open(out, "wb") as f:
        while i < len(olds) or j < len(trans):
            if j == len(trans) or (i < len(olds) and olds[i].number < trans[j][1].number):
                f.write(pack(olds[i])); i += 1          # unchanged record copies across
            else:
                op, rec = trans[j]; j += 1
                if op == "add":
                    f.write(pack(rec))
                elif op == "update":
                    f.write(pack(rec)); i += 1          # replaces the old one
                elif op == "delete":
                    i += 1                              # simply not copied


# ----------------------------------------------------------------------------
# 4. RANDOM — slot from the key by a hash; one seek to reach it
# ----------------------------------------------------------------------------
class RandomFile:
    """OPENFILE ... FOR RANDOM, SEEK, GETRECORD, PUTRECORD — in Python.

    A file of `slots` fixed-length records.  The hash gives a home slot;
    a collision probes forward (wrapping) to the next free slot.  Deleting
    leaves a tombstone so that later probes keep walking past it.
    """

    def __init__(self, path: str, slots: int):
        self.path, self.slots = path, slots
        with open(path, "wb") as f:                   # pre-size: every slot exists, empty
            f.write(pack(None, EMPTY) * slots)
        self.f = open(path, "r+b")                    # read AND write, no truncation
        self.probes_last = 0

    def close(self):
        self.f.close()

    def hash(self, key: int) -> int:
        return key % self.slots                       # the exam's "MOD table size"

    # --- the four primitives -------------------------------------------------
    def seek(self, slot: int) -> None:                # SEEK file, address
        self.f.seek(slot * RECORD_SIZE)               # address arithmetic, not a search

    def get_record(self) -> tuple[int, Account | None]:   # GETRECORD file, variable
        return unpack(self.f.read(RECORD_SIZE))

    def put_record(self, rec: Account | None, flag: int = LIVE) -> None:  # PUTRECORD
        self.f.write(pack(rec, flag))

    # --- the operations built from them -------------------------------------
    def _probe(self, key: int):
        """Walk from the home slot; yield (slot, flag, record) until an EMPTY slot."""
        start = self.hash(key)
        for step in range(self.slots):
            slot = (start + step) % self.slots
            self.seek(slot)
            flag, rec = self.get_record()
            self.probes_last = step + 1
            yield slot, flag, rec
            if flag == EMPTY:
                return

    def find(self, key: int) -> Account | None:
        for slot, flag, rec in self._probe(key):
            if flag == LIVE and rec.number == key:
                return rec
        return None

    def put(self, rec: Account) -> None:
        first_tomb = None
        for slot, flag, old in self._probe(rec.number):
            if flag == LIVE and old.number == rec.number:   # update in place
                self.seek(slot); self.put_record(rec); return
            if flag == DELETED and first_tomb is None:
                first_tomb = slot                             # reusable, but keep probing
            if flag == EMPTY:
                target = first_tomb if first_tomb is not None else slot
                self.seek(target); self.put_record(rec); return
        if first_tomb is not None:
            self.seek(first_tomb); self.put_record(rec); return
        raise OSError("random file is full")                   # the file's own exception

    def delete(self, key: int) -> bool:
        for slot, flag, rec in self._probe(key):
            if flag == LIVE and rec.number == key:
                self.seek(slot); self.put_record(None, DELETED); return True
        return False


# ----------------------------------------------------------------------------
# 5. Demonstrations and the fuzz
# ----------------------------------------------------------------------------
def main() -> None:
    random.seed(20260914)
    tmp = tempfile.mkdtemp()
    serial, seqf, seqf2, rnd = (os.path.join(tmp, n) for n in ("serial.dat", "seq.dat", "seq2.dat", "random.dat"))

    people = ["Ada", "Grace", "Linus", "Guido", "Margaret", "Ken", "Dennis", "Barbara"]
    keys = random.sample(range(1000, 9999), 50)          # real-looking account numbers, no pattern
    accounts = [Account(k, people[i % 8], round(random.uniform(0, 5000), 2)) for i, k in enumerate(keys)]

    print(f"record size on disk: {RECORD_SIZE} bytes  (format {FMT})")

    # SERIAL
    for a in accounts:
        serial_append(serial, a)
    target = accounts[39].number                          # the 40th record written
    rec, reads = serial_find(serial, target)
    print(f"serial: found {target} after reading {reads} of {len(accounts)} records "
          f"(it was the 40th written, so 40 reads — arrival order is the only order)")
    _, reads = serial_find(serial, 999999)
    print(f"serial: a missing key costs {reads} reads — the whole file")

    # SEQUENTIAL
    sequential_write(seqf, accounts)
    rec, reads = sequential_find(seqf, target)
    print(f"sequential: found {target} after {reads} reads (it sorts to position {reads})")
    lo = sorted(keys)[0]
    _, reads = sequential_find(seqf, lo + 1)           # just above the smallest key
    print(f"sequential: missing key {lo + 1} rejected after {reads} reads — sorted order lets it stop early")
    k_upd, k_del = sorted(keys)[0], sorted(keys)[1]
    k_add = k_upd + 1 if k_upd + 1 not in keys else k_upd + 2
    trans = [("update", Account(k_upd, "Ada", 1.00)), ("delete", Account(k_del, "", 0)),
             ("add", Account(k_add, "Newcomer", 250.0))]
    sequential_merge_update(seqf, trans, seqf2)
    after = read_all(seqf2)
    assert [a.number for a in after] == sorted(a.number for a in after)
    assert len(after) == len(accounts) - 1 + 1
    assert next(a for a in after if a.number == k_upd).balance == 1.00
    assert all(a.number != k_del for a in after)
    print(f"sequential: merge update wrote a new master of {len(after)} records — still sorted; "
          f"{k_upd} updated, {k_del} deleted, {k_add} added")

    # RANDOM
    rf = RandomFile(rnd, slots=101)
    for a in accounts:
        rf.put(a)
    rec = rf.find(target)
    print(f"random: found {target} at home slot {rf.hash(target)} with {rf.probes_last} probe(s)")
    probes = []
    for a in accounts:
        rf.find(a.number); probes.append(rf.probes_last)
    print(f"random: 50 keys in 101 slots (load factor 0.50): {sum(p == 1 for p in probes)} found in 1 probe, "
          f"mean {sum(probes)/len(probes):.2f}, worst {max(probes)} — collisions happen, the probe absorbs them")
    print(f"random: file is exactly {os.path.getsize(rnd)} bytes = 101 x {RECORD_SIZE}, sized before any record existed")

    # FUZZ: the random file versus a dict, thousands of operations
    truth: dict[int, Account] = {}
    ops = 0
    rf2 = RandomFile(os.path.join(tmp, "fuzz.dat"), slots=257)
    for _ in range(6000):
        k = random.randint(1, 400)
        op = random.random()
        if op < 0.45 and len(truth) < 200:
            a = Account(k, random.choice(people), round(random.uniform(0, 100), 2))
            rf2.put(a); truth[k] = a
        elif op < 0.75:
            got = rf2.find(k)
            assert got == truth.get(k), (k, got, truth.get(k))
        else:
            assert rf2.delete(k) == (k in truth)
            truth.pop(k, None)
        ops += 1
    for k in range(1, 401):
        assert rf2.find(k) == truth.get(k)
    rf.close(); rf2.close()
    print(f"fuzz: {ops} random put/find/delete operations against a dict — never a disagreement "
          f"({len(truth)} live records at the end, tombstones included along the way)")


if __name__ == "__main__":
    main()
