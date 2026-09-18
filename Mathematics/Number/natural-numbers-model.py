"""Two finite models of naturals. Teaching representations, not fast arithmetic."""
ZERO = ()


def succ(n):
    return (n,)


def unary(n):
    if type(n) is not int or n < 0:
        raise ValueError('Expected a nonnegative integer')
    result = ZERO
    for _ in range(n):
        result = succ(result)
    return result


def decode(n):
    result = 0
    while n != ZERO:
        if not isinstance(n, tuple) or len(n) != 1:
            raise ValueError('Malformed unary natural')
        result += 1
        n = n[0]
    return result


def add(a, b):
    return a if b == ZERO else succ(add(a, b[0]))


def mul(a, b):
    return ZERO if b == ZERO else add(mul(a, b[0]), a)


def von_neumann(n):
    if type(n) is not int or n < 0:
        raise ValueError('Expected a nonnegative integer')
    result = frozenset()
    for _ in range(n):
        result = result | frozenset([result])
    return result


def drain(jobs):
    pending = list(jobs)
    completed = []
    while pending:
        completed.append(pending.pop())
    return completed


def verify():
    ns = [unary(i) for i in range(12)]
    for i, a in enumerate(ns):
        assert decode(a) == i
        for j, b in enumerate(ns):
            assert decode(add(a, b)) == i + j
            assert decode(mul(a, b)) == i * j
            assert add(a, b) == add(b, a)
            for c in ns[:5]:
                assert add(add(a, b), c) == add(a, add(b, c))
    vs = [von_neumann(i) for i in range(8)]
    for i, a in enumerate(vs):
        assert len(a) == i
        assert a == frozenset(vs[:i])
        for j, b in enumerate(vs):
            assert (a in b) == (i < j)
            assert (a <= b) == (i <= j)
    assert len(succ(succ(ZERO))) == 1
    assert len(vs[2]) == 2
    assert drain([]) == []
    assert drain(['a', 'b', 'a']) == ['a', 'b', 'a']
    assert drain(range(20)) == list(reversed(range(20)))
    assert (255 + 1) % 256 == 0  # finite counter violates no-return axiom
    for bad in [-1, 1.5, True]:
        for factory in [unary, von_neumann]:
            try:
                factory(bad)
            except ValueError:
                pass
            else:
                raise AssertionError('Invalid input accepted')
    print('144 addition/multiplication pairs and 720 associativity cases pass.')
    print('Eight finite ordinals: cardinality, membership/order and subset/order pass.')
    print('Unary 2 has one outer element; von Neumann 2 has two. Encodings differ.')
    print('2 + 3 =', decode(add(unary(2), unary(3))))
    print('2 * 3 =', decode(mul(unary(2), unary(3))))
    print('Termination examples, input guards and finite-wrap counterexample pass.')


if __name__ == '__main__':
    verify()
