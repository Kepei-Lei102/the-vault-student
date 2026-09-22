"""RAID teaching lab. Pure in-memory bytes: never opens a disk or file.
Run: python3 raid-lab.py
RAID-5 layout: parity column (n - 1 - stripe_index % n).
RAID-6 exercise: one stripe with fixed P,Q columns, GF(256), polynomial 0x11d.
"""
from functools import reduce
from itertools import combinations
from operator import xor
import random


def xor_blocks(*blocks):
    if not blocks or len({len(b) for b in blocks}) != 1:
        raise ValueError('Supply one or more equally sized blocks')
    return bytes(reduce(xor, values, 0) for values in zip(*blocks))


def encode5(data, drives=4):
    if drives < 3 or not data or len(data) % (drives - 1):
        raise ValueError('Complete stripes and at least three drives required')
    if len({len(b) for b in data}) != 1:
        raise ValueError('All blocks must have the same length')
    rows = []
    for r in range(len(data) // (drives - 1)):
        group = data[r*(drives-1):(r+1)*(drives-1)]
        p = drives - 1 - r % drives
        it = iter(group)
        rows.append([xor_blocks(*group) if d == p else next(it)
                     for d in range(drives)])
    return rows


def rebuild5(rows):
    result = []
    for row in rows:
        missing = [i for i, b in enumerate(row) if b is None]
        if len(missing) > 1:
            raise ValueError('One parity equation cannot determine two missing blocks')
        restored = row.copy()
        if missing:
            restored[missing[0]] = xor_blocks(*(b for b in row if b is not None))
        result.append(restored)
    return result


def mul(a, b):
    """GF(256) multiplication, not ordinary integer multiplication."""
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 0x100:
            a ^= 0x11d
    return out


def power(a, n):
    out = 1
    for _ in range(n):
        out = mul(out, a)
    return out


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('Zero has no field inverse')
    return mul(a, power(b, 254))


def encode6(data):
    """One-byte data symbols followed by P and Q; not a whole disk layout."""
    if not 1 <= len(data) <= 255 or any(not 0 <= v <= 255 for v in data):
        raise ValueError('Require 1..255 byte-valued data symbols')
    p = reduce(xor, data, 0)
    q = reduce(xor, (mul(power(2, i), v) for i, v in enumerate(data)), 0)
    return data + [p, q]


def rebuild6(symbols):
    """Repair up to two known erasures, including P/Q erasures."""
    out = symbols.copy()
    k = len(out) - 2
    missing = [i for i, v in enumerate(out) if v is None]
    if len(missing) > 2:
        raise ValueError('At most two erasures')
    lost_data = [i for i in missing if i < k]
    known_p = reduce(xor, (v for v in out[:k] if v is not None), 0)
    known_q = reduce(xor, (mul(power(2, i), v) for i, v in enumerate(out[:k])
                          if v is not None), 0)
    if len(lost_data) == 2:
        i, j = lost_data
        s, t = out[k] ^ known_p, out[k+1] ^ known_q
        ai, aj = power(2, i), power(2, j)
        out[i] = divide(t ^ mul(aj, s), ai ^ aj)
        out[j] = s ^ out[i]
    elif len(lost_data) == 1:
        i = lost_data[0]
        out[i] = (out[k] ^ known_p if out[k] is not None else
                  divide(out[k+1] ^ known_q, power(2, i)))
    return encode6(out[:k])


def main():
    original = [bytes([x]) for x in (0x3c, 0xa5, 0x66, 0x0f, 0x33, 0xcc,
                                     0xaa, 0x55, 0x0f)]
    rows = encode5(original)
    damaged = [[None if d == 1 else b for d, b in enumerate(row)] for row in rows]
    restored = rebuild5(damaged)
    assert restored == rows
    print('RAID-5: drive 1 rebuilt:', [row[1].hex() for row in restored])
    rng = random.Random(20260922)
    checks5 = checks6 = 0
    for drives in range(3, 9):
        data = [rng.randbytes(64) for _ in range((drives-1)*drives)]
        rows = encode5(data, drives)
        for missing in range(drives):
            damaged = [[None if d == missing else b for d,b in enumerate(r)] for r in rows]
            assert rebuild5(damaged) == rows
            checks5 += 1
    for k in range(2, 9):
        for _ in range(12):
            symbols = encode6([rng.randrange(256) for _ in range(k)])
            for count in (1, 2):
                for lost in combinations(range(k+2), count):
                    damaged = [None if i in lost else v for i,v in enumerate(symbols)]
                    assert rebuild6(damaged) == symbols
                    checks6 += 1
    assert all(mul(a, divide(1, a)) == 1 for a in range(1, 256))
    try:
        rebuild5([[None, None, b'\x01', b'\x02']])
    except ValueError:
        pass
    else:
        raise AssertionError('Must reject two erasures')
    # One relation admits 256 different pairs of missing bytes.
    assert len([(a, a ^ 0x99) for a in range(256)]) == 256
    print(f'PASS: {checks5} whole-drive RAID-5 recoveries; {checks6} RAID-6 erasure cases')
    print('PASS: all 255 nonzero field inverses; two-erasure RAID-5 rejection')
    print('Two 8 TB mirrors: 8 TB. Four-drive RAID-5: 24 TB. RAID-6/10: 16 TB.')
    print('8 TB / 150 MB/s =', round(8e12/150e6/3600, 2), 'hours (ideal lower bound)')


if __name__ == '__main__':
    main()
