"""The check digit: verification you already carry in your wallet.

A bank card's last digit is chosen so that the Luhn sum is a multiple of ten;
an ISBN-10's last character so that the weighted sum is a multiple of eleven.
Neither digit stores any information -- it exists only to let a machine that
knows nothing about you refuse a mistyped number.  This script generates the
digit, verifies it, then makes the two commonest human errors (one wrong
digit, two adjacent digits swapped) and reports which the check catches.

Run:  python3 learning-as-verification-checkdigit.py
"""
import random

def luhn_ok(num):
    d = [int(ch) for ch in num][::-1]
    total = 0
    for i, v in enumerate(d):
        if i % 2 == 1:
            v *= 2
            if v > 9: v -= 9
        total += v
    return total % 10 == 0

def luhn_complete(body):
    for cd in "0123456789":
        if luhn_ok(body + cd): return body + cd

def isbn10_ok(s):
    vals = [10 if ch == "X" else int(ch) for ch in s]
    return sum((10 - i) * v for i, v in enumerate(vals)) % 11 == 0

random.seed(11)
body = "4539" + "".join(random.choice("0123456789") for _ in range(11))
card = luhn_complete(body)
print(f"card number   {card}   Luhn valid: {luhn_ok(card)}")
# single-digit errors: every position, every wrong digit
caught = total = 0
for i in range(16):
    for wrong in "0123456789":
        if wrong == card[i]: continue
        total += 1; caught += not luhn_ok(card[:i] + wrong + card[i+1:])
print(f"single wrong digit : caught {caught} of {total}")
caught = total = 0; missed = []
for i in range(15):
    if card[i] == card[i+1]: continue
    total += 1; sw = card[:i] + card[i+1] + card[i] + card[i+2:]
    if luhn_ok(sw): missed.append((card[i], card[i+1]))
    else: caught += 1
print(f"adjacent swap      : caught {caught} of {total}   missed pairs: {missed or 'none'}   (Luhn always misses 09/90)")

isbn = "0306406152"                                  # a real ISBN-10
print(f"\nISBN-10 {isbn}   valid: {isbn10_ok(isbn)}")
caught = total = 0
for i in range(9):
    for wrong in "0123456789":
        if wrong == isbn[i]: continue
        total += 1; caught += not isbn10_ok(isbn[:i] + wrong + isbn[i+1:])
print(f"single wrong digit : caught {caught} of {total}")
caught = total = 0
for i in range(9):
    if isbn[i] == isbn[i+1]: continue
    total += 1; caught += not isbn10_ok(isbn[:i] + isbn[i+1] + isbn[i] + isbn[i+2:])
print(f"adjacent swap      : caught {caught} of {total}   (weights 10..1 are all different, and 11 is prime)")
