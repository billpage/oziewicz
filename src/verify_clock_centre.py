"""Exact checks for analysis/clock_centre.md (ladder step 4).

No metric is used except where a part says so.  P = sum p_k, and L is the bivector
L^{ab} = sum (a^a p^b - a^b p^a) about a chosen origin.  zeta is any covector with
zeta(P) != 0.  c = 1 unless a check says otherwise.

All parts are exact (SymPy).

Parts
  A  CS1: the centre of a clock; origin shift; a collision
  B  CS2: spin as P ^ L; the displacement of two centres; spin zero
  C  CS3: Pryce (2.8), (2.11), Moller (26)-(28) on step 1's example
  D  CS4: a common clock adds, own clocks do not
  E  CS5: the second moment of d pi; two smeared bodies; the rotor
  F  CS6: circulation of the clock, Sagnac, Moller's radius

Run:  PYTHONPATH=src python3 -u src/verify_clock_centre.py
"""

from __future__ import annotations

import itertools

import sympy as sp
from sympy import Matrix, Rational as R, symbols, zeros

FAILED: list[str] = []


def check(name: str, condition) -> None:
    good = bool(condition)
    print(("  ok    " if good else "  FAIL  ") + name, flush=True)
    if not good:
        FAILED.append(name)


def biv(pairs, n):
    return sum(((a * p.T - p * a.T) for a, p in pairs), zeros(n, n))


def centre(z, level, P, L):
    """CS1: (level P - ev_z L) / z(P)"""
    return (level * P - (z.T * L).T) / (z.T * P)[0]


def part_a():
    print("\nPart A: CS1, the centre of a clock")
    n, N = 4, 3
    a = [Matrix(symbols(f"a{k}_0:{n}")) for k in range(N)]
    p = [Matrix(symbols(f"p{k}_0:{n}")) for k in range(N)]
    z = Matrix(symbols(f"z0:{n}"))
    tau = symbols("tau")
    P = sum(p, zeros(n, 1))
    L = biv(zip(a, p), n)
    num = zeros(n, 1)
    for k in range(N):
        s = (tau - (z.T * a[k])[0]) / (z.T * p[k])[0]
        num += (z.T * p[k])[0] * (a[k] + s * p[k])
    c = num / (z.T * P)[0]
    check("the z(p_k)-weighted mean on z = tau is (tau P - ev_z L) / z(P), n = 4, 3 bodies, symbolic",
          sp.simplify(c - centre(z, tau, P, L)) == zeros(n, 1))
    s_ = Matrix(symbols(f"s0:{n}"))
    L2 = biv([(a[k] + s_, p[k]) for k in range(N)], n)
    check("origin shift: L -> L + s ^ P",
          (L2 - L - (s_ * P.T - P * s_.T)).applyfunc(sp.expand) == zeros(n, n))
    # A collision: two bodies meet at e and scatter, P conserved.  The centre is unchanged.
    e = Matrix([2, 1, -1])
    pa, pb = Matrix([5, 3, 0]), Matrix([5, -3, 0])
    qa, qb = Matrix([5, 0, 3]), Matrix([5, 0, -3])
    zz = Matrix([1, R(1, 3), R(-1, 5)])
    Lbefore, Lafter = biv([(e, pa), (e, pb)], 3), biv([(e, qa), (e, qb)], 3)
    check("a collision at one event: P and L, so the centre of every clock, are unchanged",
          pa + pb == qa + qb and Lbefore == Lafter
          and centre(zz, 7, pa + pb, Lbefore) == centre(zz, 7, qa + qb, Lafter))


def wedge3(P, L, n):
    t = {}
    for i, j, k in itertools.combinations(range(n), 3):
        v = P[i] * L[j, k] - P[j] * L[i, k] + P[k] * L[i, j]
        for perm, sg in (((i, j, k), 1), ((j, k, i), 1), ((k, i, j), 1), ((j, i, k), -1), ((i, k, j), -1), ((k, j, i), -1)):
            t[perm] = sg * v
    return t


def part_b():
    print("\nPart B: CS2, the spin")
    n, N = 4, 3
    a = [Matrix(symbols(f"a{k}_0:{n}")) for k in range(N)]
    p = [Matrix(symbols(f"p{k}_0:{n}")) for k in range(N)]
    z1, z2 = Matrix(symbols(f"z0:{n}")), Matrix(symbols(f"w0:{n}"))
    tau = symbols("tau")
    P = sum(p, zeros(n, 1))
    L = biv(zip(a, p), n)
    s_ = Matrix(symbols(f"s0:{n}"))
    L2 = L + s_ * P.T - P * s_.T
    t1, t2 = wedge3(P, L, n), wedge3(P, L2, n)
    check("P ^ L does not depend on the origin", all(sp.expand(t1[k] - t2[k]) == 0 for k in t1))
    F = Matrix([sum(z1[i] * z2[j] * t1.get((i, j, b), 0) for i in range(n) for j in range(n)) for b in range(n)])
    zp1, zp2 = (z1.T * P)[0], (z2.T * P)[0]
    d = (centre(z1, tau, P, L) - centre(z2, tau, P, L)) * zp1 * zp2 - F
    check("C[z1] - C[z2] = (P ^ L)(z1, z2, .) / (z1(P) z2(P)), modulo P",
          all(sp.expand(sp.simplify(d[i] * P[j] - d[j] * P[i])) == 0 for i, j in [(0, 1), (0, 2), (0, 3), (1, 3)]))
    c = centre(z1, tau, P, s_ * P.T - P * s_.T)
    v = c - s_
    check("spin zero, L = s ^ P: every clock gives the line through s parallel to P",
          all(sp.simplify(v[i] * P[j] - v[j] * P[i]) == 0 for i, j in [(0, 1), (1, 2), (2, 3)]))
    # A clock that is no observer's, on a case with spin
    pa, pb = Matrix([20, 12, 0]), Matrix([15, -12, 0])
    La = biv([(Matrix([0, 0, R(6, 7)]), pa), (Matrix([0, 0, R(-8, 7)]), pb)], 3)
    zz = Matrix([1, 7, -3])
    print("        an arbitrary covector, zeta(P) = 35, centre at level 0:", list(centre(zz, 0, pa + pb, La)))
    check("the centre needs only zeta(P) != 0", (zz.T * (pa + pb))[0] == 35)


def part_c():
    print("\nPart C: CS3, Pryce and Moller (metric diag(1, -1, -1), c = 1)")
    pa, pb = Matrix([20, 12, 0]), Matrix([15, -12, 0])
    ya, yb = R(6, 7), R(-8, 7)
    P = pa + pb
    L = biv([(Matrix([0, 0, ya]), pa), (Matrix([0, 0, yb]), pb)], 3)
    S = -(ya * 12 + yb * (-12))
    M = 35
    print("        P =", list(P), " S =", S)
    check("step 1's example: masses 16, 9; M = 35; S = -24", P == Matrix([35, 0, 0]) and S == -24)
    good = True
    for bx, by in [(R(3, 5), 0), (0, R(4, 5)), (R(1, 3), R(2, 3)), (R(-12, 13), 0), (R(5, 13), R(12, 13) / 2)]:
        z = Matrix([1, -bx, -by])
        disp = centre(z, 0, P, L) - centre(Matrix([1, 0, 0]), 0, P, L)
        disp = disp - P * disp[0] / P[0]
        pred = Matrix([0, -S * by / M, S * bx / M])
        print("        beta", (bx, by), " displacement", list(disp[1:, 0]), " (S x beta)/M", list(pred[1:, 0]))
        good &= disp == pred
    check("the clock formula gives Moller's displacement (26), (27) on five observers", good)
    # Pryce (2.11): X = tP/P0 + M n / ... with n = P/m; here his M has the opposite sign to L
    g = sp.diag(1, -1, -1)
    p1, p2 = Matrix([13, 5, 0]), Matrix([5, 0, 3])
    a1, a2 = Matrix([0, 1, 2]), Matrix([0, -1, 3])
    Pg, Lg = p1 + p2, biv([(a1, p1), (a2, p2)], 3)
    m2 = (Pg.T * g * Pg)[0]
    M_ = Lg                                                 # Pryce's M^{mu nu}, (2.5), is L^{mu nu}
    Plow = g * Pg
    t = R(3)
    xp = t * Pg / Pg[0] + M_ * Plow / m2 + Pg * (Plow.T * M_[:, 0])[0] / (m2 * Pg[0])
    z_own = g * Pg
    mine = centre(z_own, (z_own.T * xp)[0], Pg, Lg)
    print("        Pryce (2.11) at t = 3:", list(xp), " own clock:", list(mine))
    check("Pryce (2.11) as printed is the centre of the clock b(P, .), on a boosted example",
          xp == mine and xp[0] == t)
    n_ = Matrix([R(5, 3), R(4, 3), 0])
    nlow = g * n_
    check("Pryce (2.8), (s P + M n)/(P.n), is CS1 with zeta = n lowered",
          (R(2) * Pg + M_ * nlow) / (Pg.T * nlow)[0] == centre(nlow, R(2), Pg, Lg))


def part_d():
    print("\nPart D: CS4, adding subsystems")
    g = sp.diag(1, -1, -1)
    A = [(Matrix([0, 1, 0]), Matrix([5, 3, 0])), (Matrix([0, -1, 0]), Matrix([5, 0, 4]))]
    B = [(Matrix([0, 2, 3]), Matrix([13, 0, 5]))]
    PA, PB = sum((p for _, p in A), zeros(3, 1)), sum((p for _, p in B), zeros(3, 1))
    LA, LB = biv(A, 3), biv(B, 3)
    PT, LT = PA + PB, LA + LB
    z = Matrix([1, R(1, 4), R(-1, 3)])
    lhs = centre(z, 2, PT, LT) * (z.T * PT)[0]
    rhs = centre(z, 2, PA, LA) * (z.T * PA)[0] + centre(z, 2, PB, LB) * (z.T * PB)[0]
    check("one clock: z(P) C[z] adds over subsystems", lhs == rhs)
    zT, zA, zB = g * PT, g * PA, g * PB
    cT = centre(zT, 0, PT, LT)
    # own-clock centres of the parts, at the total's level 0
    lvA = (zT.T * centre(zA, 0, PA, LA))[0]
    lvB = (zT.T * centre(zB, 0, PB, LB))[0]
    cA = centre(zA, 0, PA, LA) - PA * lvA / (zT.T * PA)[0]
    cB = centre(zB, 0, PB, LB) - PB * lvB / (zT.T * PB)[0]
    mean = (cA * (zT.T * PA)[0] + cB * (zT.T * PB)[0]) / (zT.T * PT)[0]
    diff = cT - mean
    print("        own-clock centre of the whole minus the weighted mean of its parts' own centres:", list(diff))
    check("own clocks: the centre of the whole is not the weighted mean of the parts' centres",
          all(v.is_rational for v in diff) and diff != zeros(3, 1))
    wA = wedge3(PA, LA, 3)
    check("the failure comes from the spin of a part (P_A ^ L_A != 0)", any(v != 0 for v in wA.values()))


def part_e():
    print("\nPart E: CS5, the second moment of d pi")
    x, y = symbols("x y", real=True)
    w = symbols("w", positive=True)
    ya, yb = R(6, 7), R(-8, 7)
    g = lambda y0: sp.exp(-(x**2 + (y - y0) ** 2) / (2 * w**2)) / (2 * sp.pi * w**2)
    pix = g(ya) * 12 + g(yb) * (-12)
    oo = sp.oo
    integ = lambda f: sp.integrate(sp.integrate(f, (x, -oo, oo)), (y, -oo, oo))
    fix = lambda e: sp.simplify(e.replace(sp.erfc, lambda t: 1 - sp.erf(t)))
    S_d = fix(integ(-y * pix))
    S_c = fix(-integ((x**2 + y**2) * (-sp.diff(pix, y))) / 2)
    print("        S directly:", S_d, "  -(1/2) int r^2 (d pi)_xy:", S_c)
    check("two smeared free bodies, each d alpha = 0: S = -24 from the second moment of d pi", S_d == -24 == S_c)
    Om, r = symbols("Omega r", positive=True)
    rho = sp.exp(-(r**2))
    I_ = sp.integrate(rho * r**2 * 2 * sp.pi * r, (r, 0, oo))
    vort = sp.integrate(r**2 * rho * 2 * Om * 2 * sp.pi * r, (r, 0, oo))
    grad = sp.integrate(r**2 * sp.diff(rho, r) * Om * r * 2 * sp.pi * r, (r, 0, oo))
    print("        I =", I_, "  vorticity term:", -vort / 2, "  gradient term:", -grad / 2)
    check("Gaussian rotor: S = I Omega = -I Omega + 2 I Omega",
          sp.simplify(-vort / 2 + I_ * Om) == 0 and sp.simplify(-grad / 2 - 2 * I_ * Om) == 0)


def part_f():
    print("\nPart F: CS6, circulation and Sagnac")
    om, c, m, Rr = symbols("omega c m R", positive=True)
    t, r, ph = symbols("t r phi", positive=True)
    gam = 1 / sp.sqrt(1 - om**2 * r**2)
    g = sp.diag(-1, 1, r**2)
    u = Matrix([gam, 0, gam * om])
    alpha = -(g * u)
    circ = sp.integrate(alpha[2], (ph, 0, 2 * sp.pi))
    check("circulation round the axis of the clock -u: -2 pi u_phi, u_phi = gamma omega r^2",
          sp.simplify(circ + 2 * sp.pi * gam * om * r**2) == 0)
    d_alpha = sp.diff(alpha[2], r)                      # (d alpha)_{r phi}
    flux = sp.integrate(sp.simplify(d_alpha), (r, 0, Rr)) * 2 * sp.pi
    check("Stokes: the flux of d alpha through the disk of radius R is that circulation",
          sp.simplify(flux - circ.subs(r, Rr)) == 0)
    gamc = 1 / sp.sqrt(1 - om**2 * Rr**2 / c**2)
    dtau = 4 * sp.pi * Rr**2 * om * gamc / c**2         # (30) of Rizzi et al.
    check("ring: S = gamma m R^2 omega = (c^2 / 4 pi) m Delta tau",
          sp.simplify(m * gamc * om * Rr**2 - c**2 / (4 * sp.pi) * m * dtau) == 0)
    rM = m * gamc * om * Rr**2 / (gamc * m * c)
    check("ring: Moller's (28) S/(Mc) = R v/c = c Delta tau / (4 pi gamma)",
          sp.simplify(rM - Rr * (om * Rr) / c) == 0 and sp.simplify(rM - c * dtau / (4 * sp.pi * gamc)) == 0)
    Sm = sp.integrate(gam**2 * om * r**2 * 2 * sp.pi * r, (r, 0, Rr))
    dm = gam * 2 * sp.pi * r
    Ss = sp.integrate(sp.simplify(gam * om * r**2 * dm), (r, 0, Rr))
    check("uniform-proper-density disk, c = 1: S from T^{t phi} = (1/4 pi) int Delta tau dm",
          sp.simplify(Sm - Ss) == 0)


if __name__ == "__main__":
    part_a()
    part_b()
    part_c()
    part_d()
    part_e()
    part_f()
    print()
    if FAILED:
        print(f"{len(FAILED)} CHECKS FAILED:")
        for name_ in FAILED:
            print("  " + name_)
        raise SystemExit(1)
    print("ALL CHECKS PASSED")
