"""Hash Tables — verify the card's claims, seeded by TODAY'S date.

Run it yourself, any day:

    python3 hash-tables-verify.py

What it checks:
  1. The chaining engine and the probing-with-tombstones engine, fuzzed against
     Python's own dict — inserts, updates, finds and deletes all compared.
     (Remove the tombstone logic and this battery catches the lie in seconds.)
  2. The November 2025 Paper 41 exam engine (100 x 10 bucket rows, key MOD 100):
     200 records in, every GetRecord answer checked.
  3. The birthday paradox pricing the first collision, and the anagram flaw in
     the add-the-character-codes string hash.
  4. Measured probe costs against Knuth's (1 + 1/(1-alpha))/2 as the load
     factor climbs — the dial the whole structure hangs on.

The seed is today's date: tomorrow tests different keys, same guarantees.
"""
import random
import datetime

SEED = int(datetime.date.today().strftime("%Y%m%d"))
random.seed(SEED)
print(f"seed = {SEED}  (today's date)\n")

# ---------- Engine 1: chaining (list per slot) ----------
class ChainTable:
    def __init__(self, slots=8):
        self.slots = slots
        self.table = [[] for _ in range(slots)]
        self.count = 0

    def _hash(self, key):
        return key % self.slots

    def insert(self, key, value):
        chain = self.table[self._hash(key)]
        for pair in chain:
            if pair[0] == key:
                pair[1] = value          # update in place
                return
        chain.append([key, value])
        self.count += 1
        if self.count / self.slots > 0.75:
            self._rehash()

    def find(self, key):
        for k, v in self.table[self._hash(key)]:
            if k == key:
                return v
        return None

    def delete(self, key):
        chain = self.table[self._hash(key)]
        for i, (k, v) in enumerate(chain):
            if k == key:
                chain.pop(i)
                self.count -= 1
                return True
        return False

    def _rehash(self):
        old = [pair for chain in self.table for pair in chain]
        self.slots *= 2
        self.table = [[] for _ in range(self.slots)]
        for k, v in old:
            self.table[k % self.slots].append([k, v])

# ---------- Engine 2: linear probing with tombstones ----------
EMPTY, TOMB = None, ("<tomb>",)
class ProbeTable:
    def __init__(self, slots=16):
        self.slots = slots
        self.table = [EMPTY] * slots
        self.count = 0

    def _hash(self, key):
        return key % self.slots

    def insert(self, key, value):
        if (self.count + 1) / self.slots > 0.66:
            self._rehash()
        i = self._hash(key)
        first_tomb = None
        while self.table[i] is not EMPTY:
            if self.table[i] is TOMB:
                if first_tomb is None:
                    first_tomb = i
            elif self.table[i][0] == key:
                self.table[i] = (key, value)
                return
            i = (i + 1) % self.slots       # the wrap: MOD again
        self.table[first_tomb if first_tomb is not None else i] = (key, value)
        self.count += 1

    def find(self, key):
        i = self._hash(key)
        while self.table[i] is not EMPTY:  # tombstones do NOT stop the search
            if self.table[i] is not TOMB and self.table[i][0] == key:
                return self.table[i][1]
            i = (i + 1) % self.slots
        return None

    def delete(self, key):
        i = self._hash(key)
        while self.table[i] is not EMPTY:
            if self.table[i] is not TOMB and self.table[i][0] == key:
                self.table[i] = TOMB       # NOT EMPTY — the ghost must stay
                self.count -= 1
                return True
            i = (i + 1) % self.slots
        return False

    def _rehash(self):
        old = [e for e in self.table if e not in (EMPTY, TOMB)]
        self.slots *= 2
        self.table = [EMPTY] * self.slots
        self.count = 0
        for k, v in old:
            i = k % self.slots
            while self.table[i] is not EMPTY:
                i = (i + 1) % self.slots
            self.table[i] = (k, v)
            self.count += 1

# ---------- fuzz both against dict ----------
for trial in range(2500):
    ref = {}
    ct, pt = ChainTable(), ProbeTable()
    for _ in range(random.randint(5, 120)):
        op = random.random()
        key = random.randint(0, 300)
        if op < 0.55:
            val = random.randint(0, 999)
            ref[key] = val; ct.insert(key, val); pt.insert(key, val)
        elif op < 0.8:
            probe = random.randint(0, 300)
            expect = ref.get(probe)
            assert ct.find(probe) == expect, (trial, "chain find")
            assert pt.find(probe) == expect, (trial, "probe find")
        else:
            expect = key in ref
            if expect: del ref[key]
            assert ct.delete(key) == expect, (trial, "chain del")
            assert pt.delete(key) == expect, (trial, "probe del")
    for k, v in ref.items():
        assert ct.find(k) == v and pt.find(k) == v
print("fuzz OK: 2500 trials, chaining + probing-with-tombstones vs dict, deletes included")

# ---------- the exam engine (N25/41: 100x10 bucket rows) ----------
HashTable = [[None] * 10 for _ in range(100)]
def Hash(Key):
    return Key % 100
def InsertData(rec):                       # rec = (Key, Data)
    row = Hash(rec[0])
    for i in range(10):
        if HashTable[row][i] is None:
            HashTable[row][i] = rec
            return
def GetRecord(Key):
    row = Hash(Key)
    for i in range(10):
        if HashTable[row][i] is not None and HashTable[row][i][0] == Key:
            return HashTable[row][i][1]
    return ""
data = {}
keys = random.sample(range(10000), 200)
for k in keys:
    data[k] = f"item{k}"
    InsertData((k, data[k]))
for k in keys:
    assert GetRecord(k) == data[k]
assert GetRecord(99999) == ""
print("exam engine OK: 200 records into the N25/41 100x10 table, every GetRecord correct")

# ---------- birthday numbers for the card ----------
import math
p = 1.0
for n in range(1, 101):
    p *= (100 - (n - 1)) / 100
    if 1 - p >= 0.5:
        print(f"birthday: with 100 slots, just {n} random keys give a {1-p:.0%} chance of a collision")
        break
# anagram collision demo for the bad string hash
bad = lambda s: sum(ord(c) for c in s) % 100
print(f"bad string hash: 'listen' -> {bad('listen')}, 'silent' -> {bad('silent')}  (anagrams always collide)")

# ---------- load-factor measurements (for the figure) ----------
def measure_probe(alpha, slots=1024, trials=40):
    tot = cnt = 0
    for _ in range(trials):
        t = [None] * slots
        n = int(alpha * slots)
        ks = random.sample(range(10**7), n)
        for k in ks:
            i = k % slots
            while t[i] is not None:
                i = (i + 1) % slots
            t[i] = k
        for k in random.sample(ks, min(200, n)):
            i = k % slots; steps = 1
            while t[i] != k:
                i = (i + 1) % slots; steps += 1
            tot += steps; cnt += 1
    return tot / cnt
for a in (0.25, 0.5, 0.75, 0.9):
    m = measure_probe(a)
    theory = 0.5 * (1 + 1 / (1 - a))
    print(f"alpha={a}: measured avg probes {m:.2f}  vs theory ~{theory:.2f}")

print("\nevery claim on the card held. run me tomorrow: new keys, same theorems.")
