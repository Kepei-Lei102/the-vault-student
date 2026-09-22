"""Exact descriptions, lossy summaries, and boundary conditions; stdlib only."""
from cmath import exp, pi
from collections import Counter
from math import cos, sin
from random import Random


def dft(x, inverse=False):
    n = len(x)
    sign = 1 if inverse else -1
    return [sum(v * exp(sign * 2j * pi * k * j / n)
                for j, v in enumerate(x)) / (n if inverse else 1)
            for k in range(n)]


def linear_convolution(x, h):
    y = [0] * (len(x) + len(h) - 1)
    for j, a in enumerate(x):
        for k, b in enumerate(h):
            y[j + k] += a * b
    return y


def transformed_convolution(x, h, n):
    if n < max(len(x), len(h)):
        raise ValueError('Transform length must contain both input sequences')
    X = dft(list(x) + [0] * (n - len(x)))
    H = dft(list(h) + [0] * (n - len(h)))
    return dft([a * b for a, b in zip(X, H)], inverse=True)


def close(a, b, tolerance=1e-9):
    assert len(a) == len(b)
    assert max(abs(x - y) for x, y in zip(a, b)) < tolerance


def main():
    direct = linear_convolution([1, 2], [1, .5])
    transformed = transformed_convolution([1, 2], [1, .5], 4)
    close(direct + [0], transformed)
    print('Echo: direct =', direct, '; transformed =',
          [round(v.real, 8) for v in transformed])
    # Compare two algorithms, with deterministic varied values and lengths.
    rng = Random(73)
    cases = 0
    for L in range(1, 9):
        for M in range(1, 9):
            x = [rng.uniform(-2, 2) for _ in range(L)]
            h = [rng.uniform(-2, 2) for _ in range(M)]
            expected = linear_convolution(x, h)
            for n in (L + M - 1, L + M + 4):
                close(expected + [0] * (n - len(expected)),
                      transformed_convolution(x, h, n))
                cases += 1
    print(f'{cases} padded convolution comparisons PASS')
    x, h = [1, 2, 3], [1, 1, 1]
    linear = linear_convolution(x, h)
    wrapped = [sum(linear[j::3]) for j in range(3)]
    close(wrapped, transformed_convolution(x, h, 3))
    print('No padding: linear', linear, 'wraps to', wrapped)
    a, b = [1, 0, 0, 0], [0, 1, 0, 0]
    A, B = dft(a), dft(b)
    close([abs(z) for z in A], [abs(z) for z in B])
    assert any(abs(u-v) > .1 for u, v in zip(A, B))
    close(a, dft(A, inverse=True)); close(b, dft(B, inverse=True))
    print('Shifted pulses: equal magnitudes, distinct complex spectra; round trips PASS')
    for j in range(101):
        t = j * .13
        qp, qm = .05*cos(t), .05*cos(2*t)
        x1, x2 = qp+qm, qp-qm
        a1, a2 = -qp-4*qm, -qp+4*qm
        close([a1, a2], [-x1+1.5*(x2-x1), -x2-1.5*(x2-x1)])
        close([(x1+x2)/2, (x1-x2)/2], [qp, qm])
    close([.05*(cos(0)+cos(0)), .05*(cos(0)-cos(0)),
           -.05*(sin(0)+2*sin(0)), -.05*(sin(0)-2*sin(0))], [.1, 0, 0, 0])
    print('101 reconstructed oscillator states satisfy both original equations')
    for x in range(-20, 21):
        assert x*x-6*x+5 == (x-1)*(x-5) == (x-3)**2-4
    # Same Counter content AND same insertion order, but different full sequences.
    first = ['original', 'taro', 'original', 'mango']
    second = ['original', 'taro', 'mango', 'original']
    assert list(Counter(first).items()) == list(Counter(second).items())
    assert first[-1] != second[-1]
    print('Identical stored tallies cannot recover which flavour was ordered last')
    assert 60+2*7 > 10*7 and 60+2*8 < 10*8
    print('Polynomial identities and break-even comparison PASS')


if __name__ == '__main__':
    main()
