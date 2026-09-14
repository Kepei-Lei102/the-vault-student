"""
ethics-licence-audit.py — what licences is THIS Python already bound by?

Companion to [[Ethics and Ownership]].

Every installed package carries a licence in its metadata. This script reads
them all (no network, standard library only), classifies each into the card's
spectrum — permissive, weak copyleft, strong copyleft, other — and prints the
tally plus the obligations each class puts on anyone who ships code built on
it.  Run it on any machine:   python3 ethics-licence-audit.py
"""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from importlib import metadata

STRONG = ["GPL-3", "GPL-2", "GPLv3", "GPLv2", "GNU General Public", "AGPL", "GNU GPL"]
WEAK = ["LGPL", "MPL", "Mozilla Public", "EPL", "Eclipse Public", "CDDL"]
PERMISSIVE = ["MIT", "BSD", "Apache", "ISC", "PSF", "Python Software Foundation", "Unlicense", "CC0", "Zlib", "zlib", "HPND", "0BSD", "BSL-1", "Boost", "MIT-CMU"]

OBLIGATION = {
    "permissive":     "keep the copyright notice and licence text; otherwise do as you like, closed source included",
    "weak copyleft":  "changes to the library itself must be released under the same licence; your own program may stay closed",
    "strong copyleft":"any program that includes or links this must be released under the same licence, source and all",
    "other/unclear":  "read it — 'other' is where the surprises live",
}


def licence_of(dist) -> str:
    md = dist.metadata
    # Preferred modern field, then classifiers, then the free-text field
    for key in ("License-Expression", "License"):
        v = md.get(key)
        if v and v.strip() and v.strip().upper() != "UNKNOWN" and len(v) < 120:
            return v.strip()
    for c in md.get_all("Classifier") or []:
        if c.startswith("License ::"):
            return c.split("::")[-1].strip()
    v = md.get("License") or ""
    return (v.splitlines()[0][:60] + "…") if v.strip() else "not declared"


def classify(lic: str) -> str:
    if lic == "not declared": return "other/unclear"
    if any(k in lic for k in STRONG) and not any(k in lic for k in WEAK): return "strong copyleft"
    if any(k in lic for k in WEAK): return "weak copyleft"
    if any(k in lic for k in PERMISSIVE) or re.search(r"\bBSD\b|\bMIT\b", lic): return "permissive"
    return "other/unclear"


def main():
    dists = sorted(metadata.distributions(), key=lambda d: d.metadata["Name"].lower())
    seen = set(); tally = Counter(); by_class = defaultdict(list)
    for d in dists:
        name = d.metadata["Name"]
        if name.lower() in seen: continue
        seen.add(name.lower())
        lic = licence_of(d); cls = classify(lic)
        tally[cls] += 1; by_class[cls].append((name, lic))
    print(f"{len(seen)} installed packages\n")
    for cls in ("permissive", "weak copyleft", "strong copyleft", "other/unclear"):
        print(f"{cls:<16} {tally[cls]:>4}   obligation: {OBLIGATION[cls]}")
    print()
    for cls in ("strong copyleft", "weak copyleft"):
        if by_class[cls]:
            print(f"{cls} packages on this machine:")
            for name, lic in by_class[cls][:12]:
                print(f"   {name:<28} {lic}")
            if len(by_class[cls]) > 12: print(f"   … and {len(by_class[cls]) - 12} more")
            print()
    sample = [(n, l) for n, l in by_class["permissive"][:6]]
    print("a few permissive ones, for the flavour of the metadata:")
    for name, lic in sample:
        print(f"   {name:<28} {lic}")
    unclear = by_class["other/unclear"][:8]
    if unclear:
        print("\nunclear — the ones a real audit would have to open by hand:")
        for name, lic in unclear:
            print(f"   {name:<28} {lic}")


if __name__ == "__main__":
    main()
