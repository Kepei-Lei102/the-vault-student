#!/usr/bin/env python3
"""Run the Python printed beside the pseudocode in Programming Fundamentals.md.

No packages needed. Run this file to verify the examples and their edge cases.
Use --sales for the interactive example, or --example NAME for another pair.
The code is extracted from the right-hand table cells: checks exercise exactly
what the reader copies, rather than a second implementation that could drift.
"""
from contextlib import redirect_stdout
from html import unescape
from io import StringIO
from itertools import product
from pathlib import Path
import argparse
import builtins
import re

NAMES = (
    'assignment', 'input', 'selection', 'for_loop', 'while_loop',
    'repeat_loop', 'extrema', 'strings', 'function', 'no_parameters',
    'scope', 'nested_selection', 'sales', 'email', 'contacts', 'palindrome',
)


def examples():
    """Read copyable, newline-preserving code from the two-column tables."""
    text = Path(__file__).with_name('Programming Fundamentals.md').read_text()
    rows = re.findall(
        r'^\| <pre[^>]*><code>(.*?)</code></pre> \| <pre[^>]*><code>(.*?)</code></pre> \|$',
        text, re.MULTILINE,
    )
    if len(rows) != len(NAMES):
        raise ValueError('The table roster changed; update NAMES and its fixtures.')
    return {name: unescape(right) for name, (_, right) in zip(NAMES, rows)}


def execute(source, inputs=()):
    """Run an example with supplied keyboard inputs; keep outputs and state."""
    remaining = iter(str(value) for value in inputs)
    consumed = 0

    def fake_input(prompt=''):
        nonlocal consumed
        # Prompts belong to the UI; returned output records print() statements.
        try:
            answer = next(remaining)
        except StopIteration as exc:
            raise AssertionError('The example requested an unexpected input') from exc
        consumed += 1
        return answer

    namespace = {'__builtins__': dict(vars(builtins), input=fake_input)}
    output = StringIO()
    with redirect_stdout(output):
        exec(compile(source, '<displayed Python>', 'exec'), namespace)
    return output.getvalue().splitlines(), namespace, consumed


def verify():
    code = examples()
    fixtures = {
        'assignment': ([], ['13']),
        'input': (['Ada', 3], ['Ada: 750 cents']),
        'selection': ([2], ['Coffee']),
        'for_loop': ([], ['1', '2', '3']),
        'while_loop': ([], ['1', '2', '3']),
        'repeat_loop': ([-1, 101, 75], ['75']),
        'extrema': ([-8, -3, -12], ['-12, -3']),
        'strings': ([], ['5', 'ell', 'HELLO', 'hello']),
        'function': ([], ['750']),
        'no_parameters': ([], ['Sales', '100']),
        'scope': ([], ['99', '10']),
        'nested_selection': (['Ada', 250], ['Accepted']),
        'sales': ([250, -20, 375, 0],
                  ['Rejected', '2 sales; 625', 'Mean cents: 312.5']),
        'email': (['a@b'], ['Valid']),
        'contacts': ([2, 'Ada', 'a@b', '111', 'A',
                     'Grace', 'g@h', '222', 'B'], []),
        'palindrome': ([2, 'RACECAR', 'TREAT'],
                       ['Successful', 'NOT successful']),
    }
    for name, (inputs, expected) in fixtures.items():
        output, _, consumed = execute(code[name], inputs)
        assert output == expected, (name, output, expected)
        assert consumed == len(inputs), (name, consumed)
    print('PASS: all 16 displayed Python examples reproduce their stated results')

    # Do not trust just the happy path: every combination of accepted, rejected
    # and sentinel inputs must preserve the independently calculated summary.
    sales_cases = 0
    for size in range(5):
        for prefix in product([-20, 0, 250, 375], repeat=size):
            stream = list(prefix) + [0]
            first_stop = stream.index(0)
            seen = stream[:first_stop]
            accepted = [x for x in seen if x > 0]
            expected = ['Rejected'] * sum(x < 0 for x in seen)
            if accepted:
                expected += [f'{len(accepted)} sales; {sum(accepted)}',
                             f'Mean cents: {sum(accepted) / len(accepted)}']
            else:
                expected += ['No sales']
            output, state, consumed = execute(code['sales'], stream)
            assert output == expected, (stream, output)
            assert (state['count'], state['total']) == (len(accepted), sum(accepted))
            assert consumed == first_stop + 1  # no reads after the sentinel
            sales_cases += 1
    print(f'PASS: {sales_cases} sales streams, including empty and rejected-only')

    words = [''.join(chars) for n in range(9) for chars in product('AB', repeat=n)]
    output, _, consumed = execute(code['palindrome'], [len(words), *words])
    expected = ['Successful' if word == word[::-1] else 'NOT successful' for word in words]
    assert output == expected
    assert consumed == len(words) + 1
    print(f'PASS: all {len(words)} binary-alphabet words through length 8')

    address_cases = 0
    for n in range(8):
        for chars in product('a@', repeat=n):
            address = ''.join(chars)
            output, _, consumed = execute(code['email'], [address])
            assert output == ['Valid' if '@' in address else 'Invalid']
            assert consumed == 1
            address_cases += 1
    print(f'PASS: {address_cases} @ searches, including empty, first and last position')

    for count in [0, 1, 2, 100]:
        fields = [f'row{r}/field{c}' for r in range(count) for c in range(4)]
        _, state, consumed = execute(code['contacts'], [count, *fields])
        expected = [fields[4*r:4*r+4] for r in range(count)]
        assert state['contacts'][:count] == expected
        assert state['contacts'][count:] == [[''] * 4 for _ in range(100-count)]
        assert consumed == 1 + 4 * count
        assert len({id(row) for row in state['contacts']}) == 100
    for values in product([-12, -3, 0, 8], repeat=3):
        output, _, _ = execute(code['extrema'], values)
        assert output == [f'{min(values)}, {max(values)}']
    for score in [0, 100]:
        assert execute(code['repeat_loop'], [-1, 101, score])[0] == [str(score)]
    for name, amount, expected in [('Ada', 250, 'Accepted'), ('Ada', 0, 'Rejected amount'), ('', 250, 'Missing name')]:
        assert execute(code['nested_selection'], [name, amount])[0] == [expected]
    for choice, expected in [(1, 'Tea'), (2, 'Coffee'), (3, 'Unknown')]:
        assert execute(code['selection'], [choice])[0] == [expected]
    print('PASS: contact capacity/row independence, 64 extrema triples, and boundaries')

    # Independent arithmetic checks, including the exact paper example.
    assert round(86123 / 500, 1) == 172.2
    assert (367 // 60, 367 % 60) == (6, 7)
    assert (-7 // 3, -7 % 3, int(-7 / 3)) == (-3, 2, -2)
    assert (round(2.5), round(3.5), round(2.675, 2)) == (2, 4, 2.67)
    for start in range(1, 6):
        for length in range(1, 7-start):
            # Build by selecting one-based positions, then compare the slice.
            expected = ''.join(ch for i, ch in enumerate('Hello', 1)
                               if start <= i < start + length)
            assert 'Hello'[start-1:start-1+length] == expected
    print('PASS: substring bounds, quotient/remainder and rounding contracts')

    # Deterministic quadrature, not a claimed random sample. Midpoints avoid
    # half-integer ties, so Python's tie policy cannot change these counts.
    sample_count = 60000
    bins = [0] * 7
    for i in range(sample_count):
        u = (i + 0.5) / sample_count
        bins[round(u * 6)] += 1
    assert bins == [5000, 10000, 10000, 10000, 10000, 10000, 5000]
    print('ROUND(6u), 60000 equal-width midpoint samples:', bins)
    print('Endpoint bins have half the width; this construction is not a fair die.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sales', action='store_true', help='run the interactive sales summary')
    parser.add_argument('--example', choices=NAMES, help='run one displayed Python example')
    args = parser.parse_args()
    if args.sales or args.example:
        source = examples()['sales' if args.sales else args.example]
        if args.sales:
            print('Enter sales in integer cents, one per line. 0 stops; negatives are rejected.')
        exec(compile(source, '<displayed Python>', 'exec'), {'__name__': '__main__'})
    else:
        verify()
