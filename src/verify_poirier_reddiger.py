"""Exact checks for supplement/poirier_reddiger.md.

All parts are exact (SymPy); nothing here is numerical.

Conventions: c = 1, signature (-,+,+) in 2+1 dimensions.  A congruence is a nowhere
zero vector field X; J = rho X is a current; varpi = i_J vol is the flux form.  The
clock of a unit timelike field V is alpha = -eta(V, .), so alpha(V) = 1.

Parts
  A  PR1 in general: d(i_J vol) = (div J) vol in 2+1 (generic functions); i_X varpi = 0
  B  PR2, Poirier's coordinate in 1+1: with x(t, C) and rho = f(C) / x_C, the flux form
     rho dx - rho v dt equals f(C) dC.  The free Gaussian packet: continuity holds and
     rho dx - rho v dt = dP, P the probability to the left of the path
  C  PR3, Reddiger-Poirier Example 3.1 (V^0 = sqrt(1 + w^2 r^2), V^i = w (-y, x)):
     V is a unit timelike field; J = rho(r) V has zero divergence; the flux form is
     rho gamma r dr ^ dphi0 with phi0 = phi - w t / gamma (basic, so a measure on the
     leaf space); alpha ^ d alpha = -w r (2 + w^2 r^2) / gamma dt ^ dr ^ dphi != 0 (no
     orthogonal simultaneity surfaces, so Poirier's Eq. (8) does not apply); the
     flowout of t = 0 stops being spacelike exactly when w tau > 1
  D  PR4, the two means: for a discrete ensemble on the leaf space the centre of a clock
     (weights zeta(p), CS1 of analysis/clock_centre.md) and the Born mean (weights mu)
     differ by Cov_mu(zeta(p), sigma) / E_mu[zeta(p)]; they agree when zeta(p) is constant

Run:  PYTHONPATH=src python3 -u src/verify_poirier_reddiger.py
Writes no files.
"""

from __future__ import annotations

import sympy as sp
from sympy import Function, Matrix, Rational as R, symbols

FAILED: list[str] = []


def check(name: str, condition) -> None:
    good = bool(condition)
    print(("  ok    " if good else "  FAIL  ") + name, flush=True)
    if not good:
        FAILED.append(name)


def part_a():
    print("\nPart A: PR1, the flux form of a current (generic functions, 2+1)")
    t, x, y = symbols("t x y")
    X = (t, x, y)
    J = [Function(f"J{k}")(*X) for k in range(3)]
    # varpi = i_J (dt ^ dx ^ dy): components varpi_{mu nu} = eps_{mu nu lam} J^lam
    eps = sp.LeviCivita
    om = Matrix(3, 3, lambda m, n: sum(eps(m, n, l) * J[l] for l in range(3)))
    # (d varpi)_{012} = d_0 om_12 + d_1 om_20 + d_2 om_01
    d_om = sp.diff(om[1, 2], t) + sp.diff(om[2, 0], x) + sp.diff(om[0, 1], y)
    div = sum(sp.diff(J[k], X[k]) for k in range(3))
    check("d(i_J vol) = (div J) vol", sp.simplify(d_om - div) == 0)
    # i_J varpi = 0 because J^mu eps_{mu nu lam} J^lam = 0 (antisymmetry)
    contr = [sum(J[m] * om[m, n] for m in range(3)) for n in range(3)]
    check("i_J (i_J vol) = 0, so varpi is horizontal for the flow of J",
          all(sp.simplify(c) == 0 for c in contr))


def part_b():
    print("\nPart B: PR2, Poirier's C in 1+1")
    t, C = symbols("t C")
    xs = Function("x")(t, C)
    f = Function("f")(C)
    rho = f / sp.diff(xs, C)
    v = sp.diff(xs, t)
    # varpi = rho dx - rho v dt, pulled back to (t, C): dx = x_t dt + x_C dC
    w_t = rho * sp.diff(xs, t) - rho * v
    w_C = rho * sp.diff(xs, C)
    check("generic x(t, C): varpi = f(C) dC, no dt component (basic)",
          sp.simplify(w_t) == 0 and sp.simplify(w_C - f) == 0)

    # the free Gaussian packet (Galilean, so no light-cone claim): sigma(t) = s0 sqrt(1 + (hbar t / 2 m s0^2)^2)
    x = symbols("x", real=True)
    s0, hb, m = symbols("s0 hbar m", positive=True)
    tt = symbols("t", real=True)
    sig = s0 * sp.sqrt(1 + (hb * tt / (2 * m * s0**2)) ** 2)
    rho_g = sp.exp(-(x**2) / (2 * sig**2)) / (sig * sp.sqrt(2 * sp.pi))
    v_g = x * sp.diff(sig, tt) / sig
    cont = sp.diff(rho_g, tt) + sp.diff(rho_g * v_g, x)
    check("Gaussian packet: rho_t + (rho v)_x = 0, v = x sigma'/sigma", sp.simplify(cont) == 0)
    P = (1 + sp.erf(x / (sp.sqrt(2) * sig))) / 2
    check("P = probability to the left of x: dP/dx = rho", sp.simplify(sp.diff(P, x) - rho_g) == 0)
    check("dP/dt = -rho v, so rho dx - rho v dt = dP (varpi = dP)",
          sp.simplify(sp.diff(P, tt) + rho_g * v_g) == 0)
    check("the path through P0 is x = sqrt(2) sigma(t) erfinv(2 P0 - 1): it solves dx/dt = v",
          sp.simplify(sp.diff(sp.sqrt(2) * sig * sp.erfinv(2 * symbols("P0") - 1), tt)
                      - v_g.subs(x, sp.sqrt(2) * sig * sp.erfinv(2 * symbols("P0") - 1))) == 0)


def part_c():
    print("\nPart C: PR3, Reddiger-Poirier Example 3.1 (2+1, signature -++)")
    t, r, ph = symbols("t r phi", real=True)
    w = symbols("omega", positive=True)
    g = sp.sqrt(1 + w**2 * r**2)
    rho = Function("rho")(r)
    # polar coordinates: metric -dt^2 + dr^2 + r^2 dphi^2, vol = r dt ^ dr ^ dphi
    V = [g, 0, w]  # (V^t, V^r, V^phi)
    norm = -V[0] ** 2 + V[1] ** 2 + r**2 * V[2] ** 2
    check("V is a unit timelike field: eta(V, V) = -1", sp.simplify(norm + 1) == 0)
    J = [rho * V[0], 0, rho * V[2]]
    div = sp.diff(r * J[0], t) / r + sp.diff(r * J[1], r) / r + sp.diff(r * J[2], ph) / r
    check("div(rho(r) V) = 0 for every rho(r)", sp.simplify(div) == 0)

    # varpi = i_J (r dt^dr^dphi) = r [J^t dr^dphi - J^r dt^dphi + J^phi dt^dr]
    # components in the basis (dr^dphi, dt^dphi, dt^dr):
    c_rph, c_tph, c_tr = r * J[0], -r * J[1], r * J[2]
    # phi0 = phi - w t / g: dr ^ dphi0 = dr^dphi - (w/g) dr^dt = dr^dphi + (w/g) dt^dr
    mu_density = rho * g * r
    check("varpi = rho gamma r dr ^ dphi0, phi0 = phi - w t / gamma (a measure on the leaf space)",
          sp.simplify(c_rph - mu_density) == 0 and sp.simplify(c_tr - mu_density * w / g) == 0
          and c_tph == 0)

    # alpha = -eta(V, .) = gamma dt - w r^2 dphi
    a = [g, 0, -w * r**2]
    # d alpha: (d alpha)_{mu nu} = d_mu a_nu - d_nu a_mu, coordinates (t, r, phi)
    coords = (t, r, ph)
    da = Matrix(3, 3, lambda i, j: sp.diff(a[j], coords[i]) - sp.diff(a[i], coords[j]))
    # alpha ^ d alpha, the (t, r, phi) component: a_t da_{r phi} - a_r da_{t phi} + a_phi da_{t r}
    aa = a[0] * da[1, 2] - a[1] * da[0, 2] + a[2] * da[0, 1]
    check("alpha ^ d alpha = -w r (2 + w^2 r^2) / gamma  dt ^ dr ^ dphi",
          sp.simplify(aa + w * r * (2 + w**2 * r**2) / g) == 0)
    check("alpha ^ d alpha != 0 for every r > 0 and w > 0 (no time function, MF11)",
          sp.simplify(aa / r).is_negative)

    # the flowout of t = 0 along V by proper time tau: t = gamma(r) tau, phi = phi0 + w tau
    tau = symbols("tau", positive=True)
    tang = Matrix([sp.diff(g, r) * tau, 1, 0])  # d/dr of (t, r, phi)
    n2 = -tang[0] ** 2 + tang[1] ** 2 + r**2 * tang[2] ** 2
    check("norm of the radial tangent of the flowout: 1 - (gamma' tau)^2, gamma' = w^2 r / gamma",
          sp.simplify(n2 - (1 - (w**2 * r / g) ** 2 * tau**2)) == 0)
    # lost somewhere iff w tau > 1: solve n2 < 0, i.e. r^2 w^2 (w^2 tau^2 - 1) > 1
    cond = sp.simplify(sp.expand((w**4 * r**2 * tau**2) - (1 + w**2 * r**2)) - r**2 * w**2 * (w**2 * tau**2 - 1) + 1)
    check("n2 < 0  <=>  r^2 w^2 (w^2 tau^2 - 1) > 1, possible for some r iff w tau > 1", cond == 0)


def part_d():
    print("\nPart D: PR4, centre of a clock against the Born mean (two paths, symbolic)")
    w1, w2, E1, E2, s1, s2 = symbols("w1 w2 E1 E2 s1 s2", positive=True)
    # mu-weights w_i on two points of the leaf space; zeta(p_i) = E_i; sigma_i = position on zeta = tau
    Wt = w1 + w2
    born = (w1 * s1 + w2 * s2) / Wt
    cs1 = (w1 * E1 * s1 + w2 * E2 * s2) / (w1 * E1 + w2 * E2)
    Em = (w1 * E1 + w2 * E2) / Wt
    cov = (w1 * E1 * s1 + w2 * E2 * s2) / Wt - Em * born
    check("CS1 centre - Born mean = Cov_mu(zeta(p), sigma) / E_mu[zeta(p)]",
          sp.simplify(cs1 - born - cov / Em) == 0)
    check("equal zeta(p) on the ensemble: the two means coincide",
          sp.simplify((cs1 - born).subs(E2, E1)) == 0)
    # free paths x_i = x0_i + v_i t, p_i = m gamma_i (1, v_i); zeta = dt, so zeta(p_i) = m gamma_i
    x1, x2, v1, v2, tau, m = symbols("x1 x2 v1 v2 tau m", real=True)
    g1, g2 = 1 / sp.sqrt(1 - v1**2), 1 / sp.sqrt(1 - v2**2)
    c_cs1 = (w1 * m * g1 * (x1 + v1 * tau) + w2 * m * g2 * (x2 + v2 * tau)) / (w1 * m * g1 + w2 * m * g2)
    c_born = (w1 * (x1 + v1 * tau) + w2 * (x2 + v2 * tau)) / Wt
    sym = (c_cs1 - c_born).subs({v2: -v1, x2: x1})
    check("lab clock, mirror velocities from one point: the two means coincide at every tau",
          sp.simplify(sym.subs({w2: w1})) == 0)
    asym = sp.simplify((c_cs1 - c_born).subs({v1: R(3, 5), v2: R(-4, 5), x1: 0, x2: 0, w1: 1, w2: 1, m: 1, tau: 1}))
    check("lab clock, v = 3/5 and -4/5 from one point (gamma = 5/4 and 5/3): the means differ, by -1/10 at tau = 1",
          asym == R(-1, 10))


if __name__ == "__main__":
    part_a()
    part_b()
    part_c()
    part_d()
    print()
    if FAILED:
        print(f"{len(FAILED)} CHECKS FAILED:")
        for name_ in FAILED:
            print("  " + name_)
        raise SystemExit(1)
    print("ALL CHECKS PASSED")
