"""
paradigms-four-ways.py — one problem, four paradigms, one answer.

Companion to [[Programming Paradigms]].  The problem: a shop's stock list — five items with
prices — and the question "what is the total price of the items that cost less than 6?"
Answer: pen 2 + apple 1 + cheese 5 = 8.  Solved four times, once per syllabus paradigm:

  1. LOW-LEVEL  — on a tiny register machine written here, in an assembly language with
                  the five addressing modes the syllabus names (immediate, direct, indirect,
                  indexed, relative); the program is a list of instructions, the data is
                  numbers in memory cells, and the loop is a conditional jump.
  2. IMPERATIVE (procedural) — Python with a variable, a loop and an if: HOW, step by step.
  3. OBJECT-ORIENTED — the same logic with the data and its behaviour bundled into classes.
  4. DECLARATIVE — SQL (SQLite, no loop written) and Prolog (paradigms-prolog.py): WHAT,
                  and the engine finds how.
  +  FUNCTIONAL — one line of map/filter/reduce, beyond the syllabus, for comparison.

Run:  python3 paradigms-four-ways.py
"""
import sqlite3
from functools import reduce
from paradigms_prolog_import import KB   # see the shim below

ITEMS = [("pen", 2), ("book", 12), ("apple", 1), ("cheese", 5), ("lamp", 30)]

# ------------------------------------------------------------------ 1. low-level
class Machine:
    """A one-accumulator machine with an index register. Memory is a list of integers.
    Operands name their addressing mode, in the syllabus's five kinds:
       #n  immediate (the number itself) · n  direct (the cell) · (n)  indirect (the cell holds the address)
       n,IX  indexed (base + index register) · a jump label is relative to the program, not to memory."""
    def __init__(self, memory, program):
        self.mem = list(memory); self.prog = program; self.acc = 0; self.ix = 0; self.pc = 0; self.steps = 0; self.flag = False
    def value(self, operand):
        if operand.startswith("#"): return int(operand[1:])                        # immediate
        if operand.startswith("("): return self.mem[self.mem[int(operand[1:-1])]]   # indirect
        if operand.endswith(",IX"): return self.mem[int(operand[:-3]) + self.ix]    # indexed
        return self.mem[int(operand)]                                             # direct
    def run(self):
        labels = {lab: i for i, (lab, _, _) in enumerate(self.prog) if lab}
        while self.pc < len(self.prog):
            _, op, arg = self.prog[self.pc]; self.pc += 1; self.steps += 1
            if op == "LDM": self.acc = int(arg[1:])
            elif op in ("LDD", "LDI", "LDX"): self.acc = self.value(arg)
            elif op == "LDR": self.ix = int(arg[1:])
            elif op == "STO": self.mem[int(arg)] = self.acc
            elif op == "ADD": self.acc += self.value(arg)
            elif op == "SUB": self.acc -= self.value(arg)
            elif op == "INC": self.ix += (arg == "IX"); self.acc += (arg == "ACC")
            elif op == "CMP": self.flag = (self.acc == self.value(arg))
            elif op == "JPE": self.pc = labels[arg] if self.flag else self.pc
            elif op == "JPN": self.pc = labels[arg] if not self.flag else self.pc
            elif op == "JLT": self.pc = labels[arg] if self.acc < 0 else self.pc      # jump if the last result was negative
            elif op == "JMP": self.pc = labels[arg] if arg in labels else self.pc + int(arg)   # relative: +n / −n
            elif op == "END": break
        return self.acc

def low_level():
    # memory map: cells 0–4 the five prices; 5 scratch; 10 counter (5 items); 11 running total;
    # 12 a pointer holding the ADDRESS of the limit; 13 the limit itself (6)
    memory = [2, 12, 1, 5, 30, 0, 0, 0, 0, 0, 5, 0, 13, 6]
    program = [
        (None,    "LDM", "#0"),      # immediate: acc ← 0
        (None,    "STO", "11"),      # direct: total ← 0
        (None,    "LDR", "#0"),      # ix ← 0
        ("LOOP",  "LDX", "0,IX"),    # indexed: acc ← price[ix]
        (None,    "STO", "5"),       # scratch ← price
        (None,    "SUB", "(12)"),    # indirect: acc ← price − limit, the limit found via the pointer in cell 12
        (None,    "JLT", "ADDIT"),   # price < limit → add it
        (None,    "JMP", "NEXT"),
        ("ADDIT", "LDD", "11"),      # total ← total + price
        (None,    "ADD", "5"),
        (None,    "STO", "11"),
        ("NEXT",  "INC", "IX"),      # next item
        (None,    "LDD", "10"),      # counter ← counter − 1
        (None,    "SUB", "#1"),
        (None,    "STO", "10"),
        (None,    "CMP", "#0"),
        (None,    "JPN", "LOOP"),    # not zero → loop again
        (None,    "LDD", "11"),      # answer in the accumulator
        (None,    "END", None),
    ]
    m = Machine(memory, program)
    total = m.run()
    print(f"1. low-level: {total}   ({m.steps} instructions executed for five items; addressing modes: immediate #0, direct 11, indirect (12), indexed 0,IX, and jumps relative to the program — every step is HOW)")
    return total

# ------------------------------------------------------------------ 2. imperative
def imperative():
    total = 0
    for name, price in ITEMS:
        if price < 6:
            total = total + price
    print(f"2. imperative: {total}   (a variable, a loop, an if — the state changes line by line, in the order written)")
    return total

# ------------------------------------------------------------------ 3. object-oriented
class Item:
    def __init__(self, name, price): self.__name = name; self.__price = price
    def get_price(self): return self.__price
    def is_cheap(self, limit=6): return self.__price < limit

class Stock:
    def __init__(self): self.__items = []
    def add(self, item): self.__items.append(item)
    def total_cheap(self): return sum(i.get_price() for i in self.__items if i.is_cheap())

def object_oriented():
    stock = Stock()
    for n, p in ITEMS: stock.add(Item(n, p))
    total = stock.total_cheap()
    print(f"3. object-oriented: {total}   (Item knows its own price and whether it is cheap; Stock contains Items; nobody outside touches __price)")
    return total

# ------------------------------------------------------------------ 4. declarative
def declarative():
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE item (name TEXT, price INTEGER)")
    db.executemany("INSERT INTO item VALUES (?, ?)", ITEMS)
    (total,) = db.execute("SELECT SUM(price) FROM item WHERE price < 6").fetchone()
    print(f"4a. declarative, SQL: {total}   (SELECT SUM(price) FROM item WHERE price < 6 — what, not how; no loop written)")
    kb = KB()
    for n, p in ITEMS: kb.fact("item", n, p)
    kb.rule(("cheap", "N", "P"), ("item", "N", "P"), ("<", "P", 6))
    cheap = list(kb.query(("cheap", "N", "P")))
    total2 = sum(s["P"] for s in cheap)
    found = ", ".join(f"{sol['N']}={sol['P']}" for sol in cheap)
    print(f"4b. declarative, Prolog: cheap(N, P) gives {found} → {total2}   (a fact per item, one rule, one goal; the engine did the searching)")
    return total

# ------------------------------------------------------------------ +. functional
def functional():
    total = reduce(lambda a, b: a + b, map(lambda i: i[1], filter(lambda i: i[1] < 6, ITEMS)), 0)
    print(f"+. functional: {total}   (filter → map → reduce; no variable is ever reassigned)")
    return total

if __name__ == "__main__":
    results = {low_level(), imperative(), object_oriented(), declarative(), functional()}
    print(f"\nsame answer every way: {results}")
