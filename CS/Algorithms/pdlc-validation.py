"""Validation and verification, written out and tested with the four kinds of data.

Validation asks "is this input reasonable?" -- six checks from the 0478 syllabus.
Verification asks "is this input what the source said?" -- double entry, visual.
Neither asks "is it correct".  Then the June 2025 Paper 22 temperature check
(-100 to 0 inclusive) gets a test plan of normal, abnormal, extreme and
boundary data, and every row is run.

Run:  python3 pdlc-validation.py
"""
import re

def range_check(v, lo, hi):    return lo <= v <= hi
def length_check(s, n):        return len(s) == n
def type_check(s, kind=int):
    try: kind(s); return True
    except (TypeError, ValueError): return False
def presence_check(s):         return s is not None and str(s).strip() != ""
def format_check(s, pattern):  return re.fullmatch(pattern, s) is not None
def check_digit_isbn10(s):     # weights 10..1, valid when the sum is a multiple of 11
    v = [10 if c == "X" else int(c) for c in s]
    return len(v) == 10 and sum((10 - i) * d for i, d in enumerate(v)) % 11 == 0

print("VALIDATION -- 'is it reasonable?'\n")
tests = [
    ("range    ", "age 17 in 0..120",              range_check(17, 0, 120)),
    ("range    ", "age 130 in 0..120",             range_check(130, 0, 120)),
    ("length   ", "password 'abc123def456' is 12", length_check("abc123def456", 12)),
    ("type     ", "'42' as integer",               type_check("42")),
    ("type     ", "'forty' as integer",            type_check("forty")),
    ("presence ", "name '' entered",               presence_check("")),
    ("format   ", "ID 'AB1234' as 2 letters + 4 digits", format_check("AB1234", r"[A-Z]{2}\d{4}")),
    ("format   ", "ID 'A12345' as 2 letters + 4 digits", format_check("A12345", r"[A-Z]{2}\d{4}")),
    ("check dig", "ISBN 0306406152",               check_digit_isbn10("0306406152")),
    ("check dig", "ISBN 0306406153 (last digit wrong)", check_digit_isbn10("0306406153")),
]
for name, what, ok in tests:
    print(f"  {name}  {what:<42} {'accepted' if ok else 'REJECTED'}")

print("\nVERIFICATION -- 'is it what the source said?'\n")
def double_entry(first, second): return first == second
print(f"  double entry  typed 'ada@ex.com' twice, second 'ada@ex.con'   {'match' if double_entry('ada@ex.com','ada@ex.con') else 'MISMATCH -> re-enter'}")
print("  visual check  the screen shows the value; the user compares it with the paper form and confirms")
print("  note: 'ada@ex.con' passes every validation check -- only verification sees the typo")

print("\nTEST PLAN -- range check, integer between -100 and 0 inclusive (0478 June 2025 P22 Q3)\n")
def temperature_ok(s):
    return type_check(s) and range_check(int(s), -100, 0)
plan = [("normal", "-50", True), ("normal", "-1", True),
        ("abnormal", "50", False), ("abnormal", "cold", False), ("abnormal", "-3.5", False),
        ("extreme", "0", True), ("extreme", "-100", True),
        ("boundary", "0", True), ("boundary", "1", False), ("boundary", "-100", True), ("boundary", "-101", False)]
print(f"  {'type':<9} {'input':>6}  expected  actual   result")
for kind, s, exp in plan:
    got = temperature_ok(s)
    print(f"  {kind:<9} {s:>6}  {str(exp):<8}  {str(got):<7}  {'pass' if got == exp else 'FAIL'}")
print("\n  extreme  = the largest and smallest ACCEPTED values (0 and -100)")
print("  boundary = each extreme together with its neighbour just outside (0 | 1, -100 | -101)")
