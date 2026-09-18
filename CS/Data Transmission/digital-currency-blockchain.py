#!/usr/bin/env python3
"""Offline teaching ledger: real SHA-256, tiny PoW, balance/replay checks.
NOT a currency or network. Transactions are unsigned in the ledger model.
Optional --signatures demonstrates real Ed25519 separately (cryptography).
All state is disposable and in memory; no keys, money or network are used.
"""
import argparse
import copy
import hashlib
import itertools
import json

DIFFICULTY = 2  # hexadecimal zeroes, deliberately tiny
INITIAL = {"Alice": 10, "Bob": 0, "Cara": 0}


def encode(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"),
                      ensure_ascii=True, allow_nan=False).encode("utf-8")


def digest(value):
    return hashlib.sha256(encode(value)).hexdigest()


def block_hash(block):
    return digest({k: v for k, v in block.items() if k != "hash"})


def tx(sender, receiver, amount, sequence=0):
    return dict(sender=sender, receiver=receiver, amount=amount, sequence=sequence)


def mine(previous, transactions, height):
    block = dict(previous=previous, transactions=copy.deepcopy(transactions),
                 height=height, timestamp=f"lesson-step-{height}", nonce=0)
    for nonce in itertools.count():
        block["nonce"] = nonce
        h = block_hash(block)
        if h.startswith("0" * DIFFICULTY):
            block["hash"] = h
            return block


GENESIS = mine("0" * 64, [], 0)  # fixed starting point, not arbitrary user input


def append(chain, transactions):
    return chain + [mine(chain[-1]["hash"], transactions, len(chain))]


def apply_transaction(balances, sequences, payment):
    """Assumes authorisation has ALREADY been checked; does not verify signatures."""
    sender, receiver = payment["sender"], payment["receiver"]
    amount, sequence = payment["amount"], payment["sequence"]
    if sender not in balances or receiver not in balances:
        raise ValueError("unknown account")
    if type(amount) is not int or amount <= 0:
        raise ValueError("amount must be a positive integer")
    if type(sequence) is not int or sequence != sequences[sender]:
        raise ValueError("replay or wrong sender sequence")
    if balances[sender] < amount:
        raise ValueError("insufficient funds")
    balances[sender] -= amount
    balances[receiver] += amount
    sequences[sender] += 1


def validate(chain):
    if not chain or chain[0] != GENESIS:
        raise ValueError("wrong genesis")
    balances, sequences = INITIAL.copy(), dict.fromkeys(INITIAL, 0)
    for i, block in enumerate(chain):
        if block["height"] != i:
            raise ValueError("wrong height")
        if block_hash(block) != block["hash"]:
            raise ValueError(f"block {i}: stored hash does not match")
        if not block["hash"].startswith("0" * DIFFICULTY):
            raise ValueError("insufficient proof of work")
        if i and block["previous"] != chain[i - 1]["hash"]:
            raise ValueError(f"block {i}: previous hash does not match")
        for payment in block["transactions"]:
            apply_transaction(balances, sequences, payment)
    return balances


def choose(candidates):
    """Among VALID chains, fixed difficulty makes length proportional to work.
    Retains the first candidate on a tie; this is NOT distributed consensus.
    """
    valid = []
    for chain in candidates:
        try:
            validate(chain)
            valid.append(chain)
        except (ValueError, KeyError, TypeError):
            pass
    if not valid:
        raise ValueError("no valid candidate")
    return max(valid, key=len)


def reject(chain):
    try:
        validate(chain)
    except ValueError as e:
        return str(e)
    raise AssertionError("invalid chain was accepted")


def demonstrations():
    base = [copy.deepcopy(GENESIS)]
    honest = append(append(base, [tx("Alice", "Bob", 7)]), [tx("Bob", "Cara", 3)])
    print("Honest ledger:", validate(honest))
    print("PoW search attempts for its payment blocks:", [b["nonce"] + 1 for b in honest[1:]])
    tampered = copy.deepcopy(honest)
    tampered[1]["transactions"][0]["amount"] = 6
    print("Edit 7 to 6:", reject(tampered))
    repaired = append(append(base, [tx("Alice", "Bob", 6)]), [tx("Bob", "Cara", 3)])
    print("Re-mine the edited suffix:", validate(repaired))
    print("Both histories pass locally. Hash links alone cannot choose a history.")
    a = append(base, [tx("Alice", "Bob", 7)])
    b = append(base, [tx("Alice", "Cara", 7)])
    print("Competing individually valid payments:", validate(a), validate(b))
    print("Try accepting both:", reject(append(a, [tx("Alice", "Cara", 7)])))
    longer_b = append(b, [tx("Cara", "Bob", 2)])
    print("Extend branch B; fixed-work choice:", validate(choose([a, longer_b])))
    print("Ledger model assumes authorisation; run --signatures for the separate real-signature demo.")


def verify():
    base = [copy.deepcopy(GENESIS)]
    # Exercise state transitions in many orders; invalid steps cannot change state.
    attempts = list(itertools.product(INITIAL, INITIAL, [-1, 0, 1, 7, 10, 11]))
    checked = 0
    for sender, receiver, amount in attempts:
        balances, sequences = INITIAL.copy(), dict.fromkeys(INITIAL, 0)
        before = balances.copy(), sequences.copy()
        should_accept = 0 < amount <= INITIAL[sender]
        try:
            apply_transaction(balances, sequences, tx(sender, receiver, amount))
        except ValueError:
            assert not should_accept
            assert (balances, sequences) == before
        else:
            assert should_accept and sum(balances.values()) == 10
            assert min(balances.values()) >= 0 and sequences[sender] == 1
        checked += 1
    good = append(append(base, [tx("Alice", "Bob", 7)]), [tx("Bob", "Cara", 3)])
    assert validate(good) == {"Alice": 3, "Bob": 4, "Cara": 3}
    for amount in [1, 2, 3, 4, 5, 6, 8, 9, 10]:
        damaged = copy.deepcopy(good)
        damaged[1]["transactions"][0]["amount"] = amount
        assert "stored hash" in reject(damaged)
    bad_link = copy.deepcopy(good)
    bad_link[2] = mine("1" * 64, bad_link[2]["transactions"], 2)
    assert "previous hash" in reject(bad_link)
    forged_origin = copy.deepcopy(good)
    forged_origin[0] = mine("2" * 64, [], 0)
    assert reject(forged_origin) == "wrong genesis"
    assert "replay" in reject(append(good, [tx("Alice", "Cara", 1)]))
    assert "insufficient" in reject(append(good, [tx("Alice", "Cara", 4, 1)]))
    bad = append(good, [tx("Alice", "Cara", 100, 1)])
    assert choose([bad, good]) == good  # more work never legitimises an invalid spend
    repaired = append(append(base, [tx("Alice", "Bob", 6)]), [tx("Bob", "Cara", 3)])
    assert validate(repaired) == {"Alice": 4, "Bob": 3, "Cara": 3}
    for malformed in [True, 1.5, "7"]:
        assert "positive integer" in reject(append(base, [tx("Alice", "Bob", malformed)]))
    assert len(digest({"x": 1})) == 64
    assert digest({"x": 1, "y": 2}) == digest({"y": 2, "x": 1})
    assert digest({"x": 1}) != digest({"x": 2})
    assert 16 ** DIFFICULTY == 256
    print(f"Checks passed: {checked} account/amount cases, conservation, replay, tampering, links, genesis and valid-chain selection.")


def signature_demo():
    try:
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
        from cryptography.exceptions import InvalidSignature
    except ImportError:
        raise SystemExit("Optional demo needs cryptography: python3 -m pip install cryptography")
    private = Ed25519PrivateKey.generate()
    public = private.public_key()
    payment = tx("Alice", "Bob", 7)
    signature = private.sign(encode(payment))
    public.verify(signature, encode(payment))
    print("Ed25519: original payment verifies with the public key.")
    edited = tx("Alice", "Bob", 6)
    try:
        public.verify(signature, encode(edited))
    except InvalidSignature:
        print("Ed25519: edited amount fails, even if block hashes are recomputed.")
    else:
        raise AssertionError("changed message verified")
    try:
        Ed25519PrivateKey.generate().public_key().verify(signature, encode(payment))
    except InvalidSignature:
        print("Ed25519: a different public key also fails.")
    else:
        raise AssertionError("wrong public key verified")
    public.verify(signature, encode(payment))
    print("The same original signature still verifies on replay: freshness is the ledger's job.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--signatures", action="store_true")
    args = parser.parse_args()
    verify()
    demonstrations()
    if args.signatures:
        signature_demo()
