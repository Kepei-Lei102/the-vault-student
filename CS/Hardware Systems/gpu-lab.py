"""CPU reference models for GPU ideas, not GPU implementations or benchmarks.
Run: python3 gpu-lab.py [--output /tmp/triangle.svg]
No external dependencies. Counts exclude caches and output traffic.
"""
import argparse
import math
import random
from pathlib import Path


def weights(x, y):
    """Barycentric coordinates in A=(1,1), B=(7,1), C=(1,7)."""
    b, c = (x - 1) / 6, (y - 1) / 6
    return 1 - b - c, b, c


def samples():
    # Inclusive edges are sufficient for ONE triangle, not shared-edge rasterisation.
    return [(x+.5, y+.5, weights(x+.5, y+.5))
            for y in range(8) for x in range(8)
            if min(weights(x+.5, y+.5)) >= -1e-12]


def raster_svg(path):
    parts = ['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 400" width="100%">']
    for x, y, w in samples():
        rgb = ','.join(str(round(255 * max(0, q))) for q in w)
        parts.append(f'<rect x="{(x-.5)*50}" y="{(7.5-y)*50}" width="50" height="50" fill="rgb({rgb})" fill-opacity="0.7"/>')
    parts.append('</svg>')
    path.write_text('\n'.join(parts) + '\n')


def shape(a):
    if not a or not a[0] or any(len(row) != len(a[0]) for row in a):
        raise ValueError('Expected a nonempty rectangular matrix')
    return len(a), len(a[0])


def scalar(a, b):
    m, k = shape(a)
    kb, n = shape(b)
    if k != kb:
        raise ValueError('Inner dimensions must match')
    out = [[sum(a[i][r]*b[r][j] for r in range(k)) for j in range(n)] for i in range(m)]
    return out, 2*m*n*k


def tiled(a, b, tile):
    m, k = shape(a)
    kb, n = shape(b)
    if k != kb or not isinstance(tile, int) or tile < 1:
        raise ValueError('Matching inner dimensions and a positive integer tile required')
    out = [[0 for _ in range(n)] for _ in range(m)]
    loads = 0
    for ii in range(0, m, tile):
        for jj in range(0, n, tile):
            for kk in range(0, k, tile):
                rows, cols, inner = min(tile, m-ii), min(tile, n-jj), min(tile, k-kk)
                aa = [[a[ii+i][kk+r] for r in range(inner)] for i in range(rows)]
                bb = [[b[kk+r][jj+j] for j in range(cols)] for r in range(inner)]
                loads += rows*inner + inner*cols
                for i in range(rows):
                    for j in range(cols):
                        for r in range(inner):
                            out[ii+i][jj+j] += aa[i][r]*bb[r][j]
    return out, loads


def verify():
    assert weights(2.5, 2.5) == (.5, .25, .25)
    assert len(samples()) == 21
    for x, y, w in samples():
        assert math.isclose(sum(w), 1)
        assert math.isclose(w[0]+7*w[1]+w[2], x)
        assert math.isclose(w[0]+w[1]+7*w[2], y)
    rng = random.Random(20260922)
    cases = 0
    # Rectangles and partial edge tiles, with an independently structured reference.
    for m in range(1, 8):
        for k in range(1, 8):
            for n in range(1, 8):
                a = [[rng.randrange(-4, 5) for _ in range(k)] for _ in range(m)]
                b = [[rng.randrange(-4, 5) for _ in range(n)] for _ in range(k)]
                expected, naive = scalar(a, b)
                for t in (1, 2, 3, 4, 8):
                    result, loads = tiled(a, b, t)
                    assert result == expected
                    assert loads == m*k*math.ceil(n/t) + k*n*math.ceil(m/t)
                    assert loads <= naive
                    cases += 1
    return cases


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('gpu-lab-output.svg'))
    args = parser.parse_args()
    print(f'PASS: {verify()} rectangular / partial-tile comparisons; 21 covered samples.')
    a = [[i+j for j in range(8)] for i in range(8)]
    b = [[i-j for j in range(8)] for i in range(8)]
    print('8x8 matrix: scalar input loads =', scalar(a, b)[1])
    for t in (1, 2, 4, 8):
        print(f'Tile {t}: input loads = {tiled(a, b, t)[1]}; multiply-adds = 512')
    values = [-4, -3, -2, -1, 0, 1, 2, 3]
    print('Square mask:', [int(x >= 0) for x in values])
    print('Negate mask:', [int(x < 0) for x in values])
    print('Results:', [x*x if x >= 0 else -x for x in values])
    print('Equal-cost toy paths: 8 useful lane-operations / 16 issued slots = 50%')
    raster_svg(args.output)
    print('Triangle written to', args.output)


if __name__ == '__main__':
    main()
