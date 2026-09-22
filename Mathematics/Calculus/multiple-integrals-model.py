"""Every number quoted in [[Multiple Integrals]], computed.

Run:  python3 multiple-integrals-model.py        (sympy, numpy, scipy)
"""
import math
import numpy as np
import sympy as sp
from scipy import integrate

x, y, z, r, t, u, v, rho, ph = sp.symbols("x y z r theta u v rho phi", real=True)
R, a, b, M, k = sp.symbols("R a b M k", positive=True)


def riemann():
    print("== columns under f = 4 - x^2 - y^2 on the square [0,1] x [0,1] ==")
    f = lambda X, Y: 4 - X**2 - Y**2
    exact = sp.integrate(4 - x**2 - y**2, (y, 0, 1), (x, 0, 1))
    for n in (2, 4, 10, 100, 1000):
        c = (np.arange(n) + 0.5) / n
        X, Y = np.meshgrid(c, c)
        print(f"   {n:5d} x {n:<5d} columns (midpoints): {f(X, Y).sum() / n**2:.6f}")
    print(f"   exact: {exact} = {float(exact):.6f}")
    inner = sp.integrate(4 - x**2 - y**2, (y, 0, 1))
    print(f"   inner integral (the area of the slice at x): {sp.expand(inner)}")


def rectangle_and_triangle():
    print("\n== iterated integrals ==")
    f = x * y**2
    print("   x y^2 over 0<=x<=2, 1<=y<=3:", sp.integrate(f, (y, 1, 3), (x, 0, 2)), "and in the other order:", sp.integrate(f, (x, 0, 2), (y, 1, 3)))
    g = x + 2 * y
    A = sp.integrate(g, (y, 0, 2 - 2 * x), (x, 0, 1))
    B = sp.integrate(g, (x, 0, 1 - y / 2), (y, 0, 2))
    print("   x + 2y over the triangle (0,0),(1,0),(0,2): dy dx =", A, "  dx dy =", B)
    print("   inner integral, dy first:", sp.expand(sp.integrate(g, (y, 0, 2 - 2 * x))))
    print("   area of that triangle as a double integral:", sp.integrate(1, (y, 0, 2 - 2 * x), (x, 0, 1)))
    print("   region between y = x^2 and y = x:  integral of xy =", sp.integrate(x * y, (y, x**2, x), (x, 0, 1)),
          " and dx dy:", sp.integrate(x * y, (x, y, sp.sqrt(y)), (y, 0, 1)))


def change_order():
    print("\n== changing the order ==")
    val = sp.integrate(sp.integrate(sp.exp(y**2), (x, 0, y)), (y, 0, 1))
    print("   int_0^1 int_x^1 e^{y^2} dy dx  =  int_0^1 y e^{y^2} dy =", val, "=", float(val))
    num, err = integrate.dblquad(lambda Y, X: math.exp(Y * Y), 0, 1, lambda X: X, lambda X: 1)
    print(f"   numerical check in the ORIGINAL order: {num:.10f}")
    val2 = sp.integrate(sp.integrate(sp.sin(x) / x, (y, 0, x)), (x, 0, sp.pi))
    print("   int_0^pi int_y^pi sin(x)/x dx dy =", val2)


def polar():
    print("\n== polar ==")
    print("   exact area of a polar patch: (1/2)((r+dr)^2 - r^2) dtheta =", sp.expand(sp.Rational(1, 2) * ((r + u)**2 - r**2)), "times dtheta  (u = dr)")
    print("   area of a disc:", sp.integrate(r, (r, 0, R), (t, 0, 2 * sp.pi)))
    print("   volume under z = 4 - x^2 - y^2 above z = 0:", sp.integrate((4 - r**2) * r, (r, 0, 2), (t, 0, 2 * sp.pi)))
    I2 = sp.integrate(sp.exp(-r**2) * r, (r, 0, sp.oo), (t, 0, 2 * sp.pi))
    print("   int int e^{-(x^2+y^2)} over the plane =", I2, " so int e^{-x^2} dx =", sp.sqrt(I2), "=", float(sp.sqrt(I2)))
    print("   int e^{-z^2/2} dz =", sp.integrate(sp.exp(-z**2 / 2), (z, -sp.oo, sp.oo)))
    print("   forgetting the r: int_0^2pi int_0^R dr dtheta =", sp.integrate(1, (r, 0, R), (t, 0, 2 * sp.pi)), "(a length times an angle, not an area)")
    print("   moment of inertia of a uniform disc, sigma = M/(pi R^2):", sp.simplify(sp.integrate(M / (sp.pi * R**2) * r**2 * r, (r, 0, R), (t, 0, 2 * sp.pi))))
    ybar = sp.integrate(r * sp.sin(t) * r, (r, 0, R), (t, 0, sp.pi)) / (sp.pi * R**2 / 2)
    print("   centre of mass of a semicircular lamina: y-bar =", sp.simplify(ybar), "=", float(ybar.subs(R, 1)), "R")


def jacobians():
    print("\n== Jacobians ==")
    J = sp.Matrix([r * sp.cos(t), r * sp.sin(t)]).jacobian([r, t])
    print("   polar:", J.tolist(), " det =", sp.simplify(J.det()))
    J = sp.Matrix([a * u, b * v]).jacobian([u, v]); print("   x = au, y = bv: det =", J.det(), " so the ellipse has area", J.det() * sp.pi)
    J = sp.Matrix([(u + v) / 2, (u - v) / 2]).jacobian([u, v]); print("   x = (u+v)/2, y = (u-v)/2: det =", J.det(), " |det| =", abs(J.det()))
    val = sp.integrate(sp.integrate(u**2 * sp.exp(v) * sp.Rational(1, 2), (v, -1, 1)), (u, 1, 3))
    print("   int int (x+y)^2 e^{x-y} over the diamond 1<=x+y<=3, -1<=x-y<=1 =", sp.simplify(val), "=", float(val))
    n = 3000                                    # a plain grid of midpoints over a box that contains the diamond
    cx = -0.5 + (np.arange(n) + 0.5) * 3.0 / n; cy = -1.5 + (np.arange(n) + 0.5) * 4.0 / n
    X, Y = np.meshgrid(cx, cy)
    inside = (X + Y >= 1) & (X + Y <= 3) & (X - Y >= -1) & (X - Y <= 1)
    num = ((X + Y)**2 * np.exp(X - Y) * inside).sum() * (3.0 / n) * (4.0 / n)
    print(f"   brute-force grid check in x, y ({n} x {n} midpoints): {num:.3f};  area of the diamond by the same grid: {inside.sum() * 12.0 / n**2:.4f}")
    J = sp.Matrix([rho * sp.sin(ph) * sp.cos(t), rho * sp.sin(ph) * sp.sin(t), rho * sp.cos(ph)]).jacobian([rho, ph, t])
    print("   spherical (rho, phi from the z-axis, theta round it): det =", sp.simplify(J.det()))


def hill():
    print("\n== the hill  h = 400 - 0.001 x^2 - 0.002 y^2 ==")
    A, B = math.sqrt(400 / 0.001), math.sqrt(400 / 0.002)
    print(f"   footprint h >= 0: ellipse with semi-axes {A:.1f} m and {B:.1f} m, area {math.pi * A * B:.0f} m^2 = {math.pi*A*B/1e6:.3f} km^2")
    vol = sp.integrate(400 * (1 - r**2) * r, (r, 0, 1), (t, 0, 2 * sp.pi))
    print("   with x = A u, y = B v the height is 400(1 - u^2 - v^2); integral over the unit disc =", vol, " then times AB:")
    print(f"   volume = {float(vol) * A * B:.4e} m^3;  half of base area x height = {0.5 * math.pi * A * B * 400:.4e}")
    num, err = integrate.dblquad(lambda Y, X: max(0.0, 400 - 0.001 * X * X - 0.002 * Y * Y), -A, A, lambda X: -B, lambda X: B)
    print(f"   numerical check in x, y directly: {num:.4e}")
    print(f"   at 1.8 tonnes per cubic metre: {float(vol) * A * B * 1.8 / 1e6:.0f} million tonnes; mean height {float(vol) / math.pi:.0f} m")


def triple():
    print("\n== triple integrals ==")
    print("   volume of a ball:", sp.integrate(rho**2 * sp.sin(ph), (rho, 0, R), (ph, 0, sp.pi), (t, 0, 2 * sp.pi)))
    dens = M / (sp.Rational(4, 3) * sp.pi * R**3)
    I = sp.integrate(dens * (rho * sp.sin(ph))**2 * rho**2 * sp.sin(ph), (rho, 0, R), (ph, 0, sp.pi), (t, 0, 2 * sp.pi))
    print("   moment of inertia of a uniform solid sphere about a diameter:", sp.simplify(I))
    m = sp.integrate(k * rho * rho**2 * sp.sin(ph), (rho, 0, R), (ph, 0, sp.pi), (t, 0, 2 * sp.pi))
    print("   mass of a ball whose density is k*rho:", m)
    print("   box: int xyz over [0,1]x[0,2]x[0,3] =", sp.integrate(x * y * z, (x, 0, 1), (y, 0, 2), (z, 0, 3)))
    print("   tetrahedron x,y,z>=0, x+y+z<=1: volume =", sp.integrate(1, (z, 0, 1 - x - y), (y, 0, 1 - x), (x, 0, 1)))
    print("   cone z from r to 1 (cylindrical): volume =", sp.integrate(r, (z, r, 1), (r, 0, 1), (t, 0, 2 * sp.pi)))


def probability_and_loops():
    print("\n== probability, and nested loops ==")
    print("   X, Y independent uniform on [0,1]: P(X + Y < 1) =", sp.integrate(1, (y, 0, 1 - x), (x, 0, 1)), "  P(XY < 1/2) =",
          sp.simplify(sp.Rational(1, 2) + sp.integrate(1 / (2 * x), (x, sp.Rational(1, 2), 1))), "=", float(sp.Rational(1, 2) + sp.log(2) / 2))
    print("   dart with independent standard normal x and y errors: P(distance < 1) =", sp.simplify(1 - sp.exp(-sp.Rational(1, 2))), "=", float(1 - sp.exp(-sp.Rational(1, 2))))
    for n in (10, 100, 1000):
        print(f"   triangular loop n = {n}: count {n * (n + 1) // 2}, area of the triangle n^2/2 = {n * n / 2:.0f}, ratio {n * (n + 1) / 2 / (n * n / 2):.4f}")


def monte_carlo_and_balls():
    print("\n== Monte Carlo, and the unit ball in n dimensions ==")
    rng = np.random.default_rng(7)
    for N in (1_000, 100_000, 10_000_000):
        p = rng.random((N, 2)) * 2 - 1
        print(f"   {N:>10,d} random points in the square: pi is about {4 * np.mean((p**2).sum(axis=1) <= 1):.5f}")
    for n in (1, 2, 3, 4, 5, 6, 7, 10, 20):
        vol = math.pi**(n / 2) / math.gamma(n / 2 + 1)
        print(f"   n = {n:2d}: volume of the unit ball {vol:.4f}; fraction of the enclosing cube {vol / 2**n:.3e}")


if __name__ == "__main__":
    riemann(); rectangle_and_triangle(); change_order(); polar(); jacobians(); hill(); triple(); probability_and_loops(); monte_carlo_and_balls()
