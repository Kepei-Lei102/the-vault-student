"""Modern, finite checks for the Sophie Germain Story; no search proves FLT."""
from math import isqrt


def is_prime(n):
    return n > 1 and all(n % d for d in range(2, isqrt(n) + 1))


def residues(p, q):
    if not is_prime(q):
        raise ValueError('q must be prime: the proof divides by nonzero residues')
    return {pow(a, p, q) for a in range(1, q)}


def consecutive_pairs(p, q):
    values = residues(p, q)
    return sorted((r, (r + 1) % q) for r in values if (r + 1) % q in values)


def verify():
    # Gauss's explicit counterexample, letter of 30 April 1807.
    assert 15**11 + 8**11 == 1595826**2 + 11 * 745391**2 == 8658345793967
    assert not [(x, y) for x in range(5) for y in range(2) if x*x + 11*y*y == 23]
    assert residues(5, 11) == {1, 10}
    assert not consecutive_pairs(5, 11)
    assert consecutive_pairs(5, 7)  # Changing the modulus destroys the obstruction.
    for p in (3, 5, 7):
        for q in (q for q in range(3, 60) if is_prime(q)):
            # Check a complete residue system; equivalent to every integer modulo q.
            values = residues(p, q)
            direct = any((a + b) % q in values for a in values for b in values)
            assert direct == bool(consecutive_pairs(p, q))
            if not direct:
                assert all((pow(x,p,q) + pow(y,p,q) - pow(z,p,q)) % q
                           for x in range(1,q) for y in range(1,q) for z in range(1,q))
    # The exact in-card code is a runnable part of the artifact.
    from pathlib import Path
    import re
    card = Path(__file__).with_name('Sophie Germain and the Borrowed Name.md')
    if card.exists():
        table_row = next(line for line in card.read_text().splitlines() if line.startswith('| Remainder of $a^5$'))
        displayed = [int(cell.strip()) for cell in table_row.split('|')[2:-1]]
        assert displayed == [pow(a, 5, 11) for a in range(1, 11)]
        for block in re.findall(r'```python\n(.*?)```', card.read_text(), re.S):
            exec(compile(block, str(card), 'exec'), {})
    print('PASS: Gauss counterexample; residue sets; changed moduli; normalized/direct checks.')


if __name__ == '__main__':
    verify()
    for p, q in ((3,7),(3,13),(3,19),(5,11),(5,7),(5,31)):
        print(f'p={p}, q={q}: residues={sorted(residues(p,q))}, consecutive pairs={consecutive_pairs(p,q)}')
    print('Finite residue checks establish local obstructions; they do not prove Fermat’s Last Theorem.')
