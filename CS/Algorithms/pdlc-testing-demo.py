"""The three kinds of error, a test plan, and a stub -- all runnable.

Part 1 shows a syntax error (caught by the translator before anything runs),
a run-time error (the program runs and then performs an illegal operation) and
a logic error (the program runs to the end and is simply wrong).  Part 2 turns
the June 2025 Paper 22 bonus-pay module into a white-box test plan that walks
every path, adds boundary data, and finds the planted bug.  Part 3 is a stub.

Run:  python3 pdlc-testing-demo.py
"""
print("PART 1 -- three kinds of error\n")
# 1. syntax: the translator refuses it; nothing runs
src = "total = 0\nfor i in range(5)\n    total += i\n"
try:
    compile(src, "<bad>", "exec")
except SyntaxError as e:
    print(f"syntax error   : line {e.lineno}: {e.msg}   (found by the translator, before running)")
# 2. run-time: it runs, then performs an illegal operation
def average(xs): return sum(xs) / len(xs)
try:
    average([])
except ZeroDivisionError as e:
    print(f"run-time error : {type(e).__name__}: {e}   (found only when that input arrives)")
# 3. logic: it runs, it finishes, it is wrong -- only a test with an expected output sees it
def is_leap(y): return y % 4 == 0            # forgets the century rule
print(f"logic error    : is_leap(1900) = {is_leap(1900)}, expected False   (no crash; only a test catches it)")

print("\nPART 2 -- white-box test plan for the bonus-pay module (9618 June 2025 P22 Q2)\n")
def bonus(hours, sales):
    """Bonus: 1-40 h and sales <= 2000 -> 0; 1-40 h and > 2000 -> 50; > 40 h and <= 2000 -> 10; > 40 h and > 2000 -> 100."""
    if hours <= 40:                # planted bug: should be 1 <= hours <= 40; hours = 0 falls in here
        return 0 if sales <= 2000 else 50
    else:
        return 10 if sales < 2000 else 100      # planted bug: should be <= 2000
plan = [  # (hours, sales, expected, kind)
    (20, 1000,   0, "normal   path 1: 1-40 h, sales <= 2000"),
    (20, 3000,  50, "normal   path 2: 1-40 h, sales >  2000"),
    (50, 1000,  10, "normal   path 3: >40 h,  sales <= 2000"),
    (50, 3000, 100, "normal   path 4: >40 h,  sales >  2000"),
    (40, 2000,   0, "boundary hours 40 / sales 2000 (both on the limit)"),
    (41, 2000,  10, "boundary hours 41 / sales 2000"),
    (41, 2001, 100, "boundary hours 41 / sales 2001"),
    ( 1, 2001,  50, "boundary hours 1  / sales 2001"),
]
fails = 0
print(f"{'hours':>5} {'sales':>6} {'expected':>8} {'actual':>7}  result   test")
for h, s_, exp, kind in plan:
    got = bonus(h, s_); ok = got == exp; fails += not ok
    print(f"{h:>5} {s_:>6} {exp:>8} {got:>7}  {'pass ' if ok else 'FAIL '}   {kind}")
print(f"\n{len(plan) - fails} passed, {fails} failed -- the four normal-path tests all pass; only the boundary row 41/2000 exposes '<' for '<='.")

print("\nPART 3 -- a stub\n")
def get_sales_from_database(employee):      # STUB: the real module is not written yet
    print(f"   [stub] get_sales_from_database({employee!r}) called -> returning 2500")
    return 2500
def weekly_bonus(employee, hours):
    return bonus(hours, get_sales_from_database(employee))
print("weekly_bonus('Ada', 45) =", weekly_bonus("Ada", 45), "  (the caller can be tested before the database module exists)")
