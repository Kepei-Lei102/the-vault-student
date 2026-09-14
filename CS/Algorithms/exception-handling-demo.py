"""
exception-handling-demo.py — what an exception actually does, checked live.

Companion to [[File Processing and Exception Handling]].

Each numbered demo makes one claim from the card and then proves it by
running the code and inspecting the result:

  1. an unhandled exception unwinds the call stack and halts the program;
  2. a handler further UP the stack catches it — detection and decision
     are different places;
  3. `finally` runs whether or not the exception fires (and even on `return`);
  4. `with open(...)` closes the file even when the body raises;
  5. the examiner's bug: `close()` outside the `try` fails when `open()` failed;
  6. a bare `except:` swallows Ctrl-C and SystemExit, not only errors;
  7. `raise` lets YOUR code report an impossible state, with its own class;
  8. check-then-act (LBYL) has a hole that try-and-recover (EAFP) does not.

Run:  python3 exception-handling-demo.py
"""
from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import textwrap

results: list[str] = []


def check(label: str, ok: bool, detail: str = "") -> None:
    results.append(f"{'PASS' if ok else 'FAIL'}  {label}{'  — ' + detail if detail else ''}")
    assert ok, label


# ---------------------------------------------------------------- 1 and 2
def parse_line(line: str) -> tuple[str, int]:
    name, qty = line.split(",")
    return name, int(qty)             # int("ten") raises ValueError right here


def load(lines: list[str]) -> list[tuple[str, int]]:
    return [parse_line(l) for l in lines]   # no try here: the error passes THROUGH


def demo_1_unhandled_halts() -> None:
    """Run a tiny program in a subprocess so we can watch it die."""
    prog = textwrap.dedent("""
        def parse_line(line):
            name, qty = line.split(",")
            return name, int(qty)
        def load(lines):
            return [parse_line(l) for l in lines]
        print("before")
        load(["apple,3", "pear,ten"])
        print("after")          # never reached
    """)
    r = subprocess.run([sys.executable, "-c", prog], capture_output=True, text=True)
    check("1 unhandled exception halts the program",
          r.returncode == 1 and "before" in r.stdout and "after" not in r.stdout
          and "ValueError" in r.stderr and "invalid literal" in r.stderr,
          f"exit code {r.returncode}; traceback names parse_line, load and the main line: "
          f"{[fn for fn in ('parse_line', 'load', '<module>') if fn in r.stderr]}")


def demo_2_caught_upstairs() -> None:
    caught_in = None
    try:
        load(["apple,3", "pear,ten"])       # raised two frames DOWN, in parse_line
    except ValueError as e:                  # caught HERE, where a decision can be made
        caught_in = "main"
        detail = str(e)
    check("2 exception raised in parse_line, caught in the caller's caller",
          caught_in == "main" and "ten" in detail, f"message carried up: {detail!r}")


# ---------------------------------------------------------------- 3
def demo_3_finally_always_runs() -> None:
    trace: list[str] = []

    def attempt(bad: bool) -> str:
        try:
            trace.append("try")
            if bad:
                raise ZeroDivisionError
            return "returned"
        except ZeroDivisionError:
            trace.append("except")
            return "recovered"
        finally:
            trace.append("finally")   # runs after the return value is decided

    a, b = attempt(False), attempt(True)
    check("3 finally runs on the clean path and on the exception path",
          a == "returned" and b == "recovered" and trace == ["try", "finally", "try", "except", "finally"],
          f"trace {trace}")


# ---------------------------------------------------------------- 4 and 5
def demo_4_with_closes_on_error() -> None:
    path = os.path.join(tempfile.mkdtemp(), "data.txt")
    with open(path, "w") as f:
        f.write("apple,3\npear,ten\n")
    handle = None
    try:
        with open(path) as f:
            handle = f
            for line in f:
                parse_line(line.strip())   # raises on line 2, inside the with-block
    except ValueError:
        pass
    check("4 `with` closed the file although the body raised", handle is not None and handle.closed)


def demo_5_close_outside_try() -> None:
    """The June 2024 examiner's complaint, reproduced."""
    missing = os.path.join(tempfile.mkdtemp(), "nowhere.txt")
    f = None
    second_error = None
    try:
        f = open(missing)          # FileNotFoundError: f stays None
        data = f.read()
    except FileNotFoundError:
        print("      (handler ran: 'File not found')")
    try:
        f.close()                  # the 'tidy-up' placed OUTSIDE the try
    except AttributeError as e:    # 'NoneType' object has no attribute 'close'
        second_error = type(e).__name__
    check("5 close() after the except crashes when open() never succeeded",
          second_error == "AttributeError", "the handler ran, then the program died anyway")


# ---------------------------------------------------------------- 6
def demo_6_bare_except_swallows_exit() -> None:
    swallowed = []
    for exc in (KeyboardInterrupt, SystemExit):
        try:
            raise exc
        except:                    # bare: catches BaseException, not just Exception
            swallowed.append(exc.__name__)
    not_swallowed = []
    for exc in (KeyboardInterrupt, SystemExit):
        try:
            try:
                raise exc
            except Exception:      # the honest form: errors only
                not_swallowed.append("caught")
        except BaseException:
            not_swallowed.append(exc.__name__)
    check("6 bare `except:` swallows Ctrl-C and SystemExit; `except Exception` lets them through",
          swallowed == ["KeyboardInterrupt", "SystemExit"] == not_swallowed)


# ---------------------------------------------------------------- 7
class InsufficientFunds(Exception):
    """A domain exception: the program's OWN vocabulary for a refused operation."""


def withdraw(balance: float, amount: float) -> float:
    if amount > balance:
        raise InsufficientFunds(f"asked for {amount}, only {balance} available")
    return balance - amount


def demo_7_raise_your_own() -> None:
    msg = None
    try:
        withdraw(50.0, 80.0)
    except InsufficientFunds as e:
        msg = str(e)
    check("7 raise your own exception class and catch it by name",
          msg == "asked for 80.0, only 50.0 available" and issubclass(InsufficientFunds, Exception))


# ---------------------------------------------------------------- 8
def demo_8_lbyl_hole() -> None:
    """Look-before-you-leap: the check passes, the world changes, the act fails."""
    d = tempfile.mkdtemp()
    path = os.path.join(d, "config.txt")
    open(path, "w").close()
    exists = os.path.exists(path)          # the check ...
    os.remove(path)                        # ... the world moves (another process, a user, a sync client)
    failed_after_check = False
    try:
        open(path).read()                  # ... the act
    except FileNotFoundError:
        failed_after_check = True
    check("8 the exists() check passed and open() still failed — try/except is the only airtight form",
          exists and failed_after_check)


if __name__ == "__main__":
    for fn in (demo_1_unhandled_halts, demo_2_caught_upstairs, demo_3_finally_always_runs,
               demo_4_with_closes_on_error, demo_5_close_outside_try, demo_6_bare_except_swallows_exit,
               demo_7_raise_your_own, demo_8_lbyl_hole):
        fn()
    print("\n".join(results))
    print(f"\n{len(results)} claims checked, all PASS")
