"""
paradigms-prolog.py — a Prolog in 120 lines, so the declarative paradigm can be *run*.

Companion to [[Programming Paradigms]].  The exam's declarative questions are written in
Prolog, and there is usually no Prolog on a school machine.  This file is a small one:
facts, rules with variables, conjunctions, unification and depth-first search with
backtracking — enough to run every fact-and-rule question the syllabus sets.  Terms are
written as Python tuples: ("parent", "tom", "bob") is the fact  parent(tom, bob).
Variables are strings starting with a capital letter, as in Prolog.

    kb = KB()
    kb.fact("parent", "tom", "bob")
    kb.rule(("grandparent", "X", "Z"), ("parent", "X", "Y"), ("parent", "Y", "Z"))
    for s in kb.query(("grandparent", "tom", "Who")): print(s["Who"])

Run:  python3 paradigms-prolog.py     (runs the worked examples from the card)
"""
import itertools

def is_var(t): return isinstance(t, str) and t[:1].isupper()

def walk(t, s):
    """Follow variable bindings until a value or an unbound variable."""
    while is_var(t) and t in s: t = s[t]
    return t

def unify(a, b, s):
    """Make a and b equal under substitution s; return the extended s, or None."""
    a, b = walk(a, s), walk(b, s)
    if a == b: return s
    if is_var(a): return {**s, a: b}
    if is_var(b): return {**s, b: a}
    if isinstance(a, tuple) and isinstance(b, tuple) and len(a) == len(b):
        for x, y in zip(a, b):
            s = unify(x, y, s)
            if s is None: return None
        return s
    return None

def rename(term, n):
    """Fresh variable names per rule use, so two uses of the same rule do not collide."""
    if is_var(term): return f"{term}_{n}"
    if isinstance(term, tuple): return tuple(rename(t, n) for t in term)
    return term

def resolve(term, s):
    """Substitute bindings into a term for printing."""
    term = walk(term, s)
    return tuple(resolve(t, s) for t in term) if isinstance(term, tuple) else term

class KB:
    def __init__(self): self.clauses = []; self.counter = itertools.count()
    def fact(self, *term): self.clauses.append((tuple(term), ()))
    def rule(self, head, *body): self.clauses.append((tuple(head), tuple(tuple(b) for b in body)))

    def solve(self, goals, s):
        """Depth-first, left-to-right, with backtracking: Prolog's search order."""
        if not goals:
            yield s; return
        goal, rest = goals[0], goals[1:]
        if goal[0] == "not":                                   # negation as failure
            if next(self.solve([goal[1]], s), None) is None:
                yield from self.solve(rest, s)
            return
        if goal[0] in ("<", ">", "=<", ">=", "=\\="):           # arithmetic comparisons on bound values
            x, y = walk(goal[1], s), walk(goal[2], s)
            ok = {"<": x < y, ">": x > y, "=<": x <= y, ">=": x >= y, "=\\=": x != y}[goal[0]]
            if ok: yield from self.solve(rest, s)
            return
        for head, body in self.clauses:
            n = next(self.counter)
            h, b = rename(head, n), rename(body, n)
            s2 = unify(goal, h, s)
            if s2 is not None:
                yield from self.solve(list(b) + rest, s2)

    def query(self, *goals):
        """Yield one binding-dict per solution, with only the query's own variables."""
        seen = set()
        for s in self.solve([tuple(g) for g in goals], {}):
            out = {v: resolve(v, s) for g in goals for v in g if is_var(v)}
            key = tuple(sorted(out.items()))
            if key not in seen:
                seen.add(key); yield out

def ask(kb, *goals):
    sols = list(kb.query(*goals))
    q = ", ".join(f"{g[0]}({', '.join(str(x) for x in g[1:])})" for g in goals)
    if not sols: print(f"?- {q}.\n   false."); return
    if all(not s for s in sols): print(f"?- {q}.\n   true."); return
    print(f"?- {q}.")
    for s in sols: print("   " + "  ".join(f"{k} = {v}" for k, v in s.items()))

if __name__ == "__main__":
    # ---------- a family, and the classic rules ----------
    kb = KB()
    for p, c in (("tom", "bob"), ("tom", "liz"), ("bob", "ann"), ("bob", "pat"), ("pat", "jim")):
        kb.fact("parent", p, c)
    for m in ("tom", "bob", "jim"): kb.fact("male", m)
    for f in ("liz", "ann", "pat"): kb.fact("female", f)
    kb.rule(("father", "X", "Y"), ("parent", "X", "Y"), ("male", "X"))
    kb.rule(("grandparent", "X", "Z"), ("parent", "X", "Y"), ("parent", "Y", "Z"))
    kb.rule(("sibling", "X", "Y"), ("parent", "P", "X"), ("parent", "P", "Y"), ("=\\=", "X", "Y"))
    kb.rule(("ancestor", "X", "Y"), ("parent", "X", "Y"))                           # base case
    kb.rule(("ancestor", "X", "Y"), ("parent", "X", "Z"), ("ancestor", "Z", "Y"))   # recursive case
    print("1. facts and rules — the family:")
    ask(kb, ("father", "Who", "ann"))
    ask(kb, ("grandparent", "tom", "Who"))
    ask(kb, ("sibling", "ann", "Who"))
    ask(kb, ("ancestor", "tom", "jim"))
    ask(kb, ("ancestor", "Who", "jim"))
    ask(kb, ("father", "liz", "Who"))
    # ---------- the exam's shape: a knowledge base about things, and goals that must be satisfied ----------
    print("\n2. the exam's shape — a shop's stock:")
    shop = KB()
    for item, price, kind in (("pen", 2, "stationery"), ("book", 12, "stationery"), ("apple", 1, "food"), ("cheese", 5, "food"), ("lamp", 30, "home")):
        shop.fact("item", item, price, kind)
    shop.rule(("cheap", "I"), ("item", "I", "P", "K"), ("<", "P", 6))
    shop.rule(("cheap_food", "I"), ("cheap", "I"), ("item", "I", "P", "food"))
    ask(shop, ("cheap", "What"))
    ask(shop, ("cheap_food", "What"))
    ask(shop, ("item", "lamp", "Price", "Kind"))
    ask(shop, ("cheap", "lamp"))
    print("\n   — no loop was written for any of these: the engine searched the facts and rules for whatever satisfies the goal")
