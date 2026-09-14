"""The four user-defined types, built and used in real Python — the bubble-tea slip from the card.

Run:  python3 udt-demo.py

An enumerated type refuses values off the menu; a record pins different types under one name
and copies whole; a set ignores duplicates and order; a pointer is an address you follow.
"""
from enum import Enum
from dataclasses import dataclass, replace, field

# ---- enumerated: the sweetness menu. Fixed, ordered, no repeats, nothing off-menu.
class Sweetness(Enum):
    NONE = 0; THIRTY = 30; FIFTY = 50; SEVENTY = 70; FULL = 100
print("enumerated:", [m.name for m in Sweetness], "-> values", [m.value for m in Sweetness])
try:
    Sweetness["SIXTYFIVE"]
except KeyError as e:
    print("  off-menu value refused at once:", e)
print("  ordered:", Sweetness.THIRTY.value < Sweetness.FULL.value, " | Sweetness(50) looks up by value ->", Sweetness(50).name)

# ---- set: the toppings. Membership only; a second tick of 'pearls' changes nothing; order is meaningless.
toppings = {"pearls", "coconut jelly"}
toppings.add("pearls")
print("set:", toppings, "| 'pearls' in toppings ->", "pearls" in toppings, "| ticked twice still", len(toppings), "items")
print("  {pearls, jelly} == {jelly, pearls} ->", {"pearls", "coconut jelly"} == {"coconut jelly", "pearls"})

# ---- record: the slip. Different types under one identity; dot access; copies whole.
@dataclass
class Order:
    drink: str
    sweetness: Sweetness            # a UDT inside a UDT
    toppings: set = field(default_factory=set)
    pickup: int = 0
slip = Order("jasmine milk tea", Sweetness.FIFTY, toppings, pickup=47)
copy_ = replace(slip)               # one statement copies every field
copy_.sweetness = Sweetness.FULL
print("record:", slip)
print("  copy changed to FULL; the original still", slip.sweetness.name, "-> records assign whole, they do not share")
orders = [slip, copy_]              # the array-of-records shape
print("  orders[1].sweetness ->", orders[1].sweetness.name, " (index picks the record, dot picks the field)")

# ---- pointer: the pickup number. Its VALUE is an address; following it is dereferencing.
counter = [None] * 100              # the shop's counter: numbered slots
counter[47] = slip                  # the drink lives at slot 47
p = 47                              # p is a pointer: it holds an address, not a drink
print("pointer: p =", p, "| counter[p].drink ->", counter[p].drink, " (dereferenced)")
q = p                               # copying a pointer copies the ADDRESS; both point at the same slot
counter[q].drink = "oolong milk tea"
print("  changed through q; seen through p ->", counter[p].drink, " (two pointers, one drink)")
null = None
print("  a null pointer points at nothing:", null, "-> following it is the classic crash: ", end="")
try:
    counter[null]
except TypeError as e:
    print(type(e).__name__)
