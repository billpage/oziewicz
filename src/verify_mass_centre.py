"""Exact checks for analysis/mass_centre.md (ladder step 1).

Every statement checked here is checked exactly with SymPy; the figure in
Part F is numerical (NumPy) and only illustrates Part E.

Conventions (Oziewicz 2014/2017, long version; the public 2015 long version
on Academia.edu is checked where its printed forms differ):
  g is the metric, det g = -c^2 in vacuum, and a material body is a time-like
  vector X with g(X, X) = det g.  gamma_XY = g(X, Y)/det g.  The binary
  velocity is v_XY = Y/gamma_XY - X (eq. 1.4.7 / 1.7.14).  E_kk = m_k c^2,
  E_lk = gamma_lk E_kk.  Radiation G is null, g(G, G) = 0, and
  E_iG = g(X_i, G)/det g (Def. 2.1.2).

Most checks use a Gram model: a vector is a column of coefficients over the
basis (X_1, ..., X_n, G) and g is the Gram matrix of that basis.  This needs
no coordinates and keeps every gamma symbolic.

Parts
  A  binary velocity: eqs (1.7.15), (1.7.19)-(1.7.23); reciprocity by the boost
  B  mass centre with null radiation: (2.1.5)-(2.1.7), (2.1.14), (2.1.15)
  C  reduced momentum: (2.2.4)-(2.2.5), the missing factor c^2, (2.2.8),
     (2.2.10), (2.2.11)
  D  the mass centre as an idempotent of the observer algebra
  E  what the mass centre leaves open: observer-dependent centroids (Moller)
  F  figure for Part E (numerical)
  W  size of gamma - 1 for wide binary stars

Run:  PYTHONPATH=src python3 -u src/verify_mass_centre.py
Writes mass_centre_moller_disk.png through ozlib.utils.output_path (and
docs_path when OZ_DOCS is set).
"""

from __future__ import annotations

import itertools

import sympy as sp

c = sp.symbols("c", positive=True)
DETG = -c**2
FAILED: list[str] = []


def check(name: str, ok: bool) -> None:
    print(f"  [{'ok' if ok else 'FAIL'}] {name}")
    if not ok:
        FAILED.append(name)


def zero(expr) -> bool:
    return sp.simplify(sp.together(expr)) == 0


# ---------------------------------------------------------------- Gram model
class Gram:
    """Bodies X_1..X_n (and optionally a null vector G) with symbolic gammas."""

    def __init__(self, n: int, radiation: bool):
        self.n = n
        self.m = sp.symbols(f"m1:{n + 1}", positive=True)
        self.gam = {}
        for i, j in itertools.combinations(range(n), 2):
            s = sp.Symbol(f"gamma{i + 1}{j + 1}", positive=True)
            self.gam[(i, j)] = self.gam[(j, i)] = s
        for i in range(n):
            self.gam[(i, i)] = sp.Integer(1)
        self.EG = (sp.symbols(" ".join(f"E{i + 1}G" for i in range(n)))
                   if radiation else (0,) * n)
        dim = n + (1 if radiation else 0)
        K = sp.zeros(dim, dim)
        for i in range(n):
            for j in range(n):
                K[i, j] = DETG * self.gam[(i, j)]
            if radiation:
                K[i, n] = K[n, i] = DETG * self.EG[i]
        self.K = K
        self.dim = dim
        self.radiation = radiation

    def X(self, i):
        v = sp.zeros(self.dim, 1)
        v[i] = 1
        return v

    def G(self):
        v = sp.zeros(self.dim, 1)
        v[self.n] = 1
        return v

    def dot(self, a, b):
        return sp.expand((a.T * self.K * b)[0, 0])


def binary_velocity(gm: Gram, i, j):
    """v_ij = X_j/gamma_ij - X_i, the velocity of body j relative to body i."""
    if i == j:
        return sp.zeros(gm.dim, 1)
    return gm.X(j) / gm.gam[(i, j)] - gm.X(i)


# -------------------------------------------------------------------- Part A
def part_a():
    print("A. Binary velocity (1.7.14)-(1.7.23)")
    gm = Gram(2, radiation=False)
    g = gm.gam[(0, 1)]
    X, Y = gm.X(0), gm.X(1)
    vXY, vYX = binary_velocity(gm, 0, 1), binary_velocity(gm, 1, 0)
    check("v_XY is g-orthogonal to X (lies in X's rest space)", zero(gm.dot(X, vXY)))
    check("(1.7.15) v^2 = -det g (1 - 1/gamma^2), same for v_YX",
          zero(gm.dot(vXY, vXY) - c**2 * (1 - 1 / g**2))
          and zero(gm.dot(vYX, vYX) - gm.dot(vXY, vXY)))
    check("(1.7.19) v_YX = -gamma v_XY - (gamma - 1/gamma) X",
          zero(sp.Matrix(vYX + g * vXY + (g - 1 / g) * X).norm()))
    check("(1.7.19) v_YX = -v_XY/gamma - (1 - 1/gamma^2) Y",
          zero(sp.Matrix(vYX + vXY / g + (1 - 1 / g**2) * Y).norm()))
    # (1.7.20): v_YX ^ v_XY = (v^2/c^2) Y ^ X. A bivector a^b in the plane
    # span{X, Y} is fixed by the 2x2 determinant of the coefficients.
    wedge = lambda a, b: sp.Matrix([[a[0], b[0]], [a[1], b[1]]]).det()
    v2c2 = 1 - 1 / g**2
    check("(1.7.20) v_YX ^ v_XY = (v^2/c^2) Y ^ X",
          zero(wedge(vYX, vXY) - v2c2 * wedge(Y, X)))
    s = vYX + vXY
    check("(1.7.22) v_YX + v_XY = -(1 - 1/gamma)(X + Y)",
          zero(sp.Matrix(s + (1 - 1 / g) * (X + Y)).norm()))
    check("(1.7.23) (v_YX + v_XY)^2 = -2 (gamma - 1) v^2",
          zero(gm.dot(s, s) + 2 * (g - 1) * gm.dot(vXY, vXY)))
    check("2015 version (7.19): (v_YX + v_XY)^2 = 2 det g (1 + gamma)(1 - 1/gamma)^2",
          zero(gm.dot(s, s) - 2 * DETG * (1 + g) * (1 - 1 / g)**2))
    # The boost B in the plane span{X, Y} with B X = Y is B Y = 2 gamma Y - X
    # (and the identity on the g-orthogonal complement).
    B = sp.Matrix([[0, -1], [1, 2 * g]])  # columns: images of X and Y
    iso = all(zero(gm.dot(B * a, B * b) - gm.dot(a, b))
              for a in (X, Y) for b in (X, Y))
    check("B (B X = Y, B Y = 2 gamma Y - X) is a g-isometry", iso)
    check("reciprocity after transport: B v_XY = -v_YX",
          zero(sp.Matrix(B * vXY + vYX).norm()))
    print("    v_YX != -v_XY because the two vectors lie in different rest spaces;")
    print("    the boost that carries X's rest space to Y's carries v_XY to -v_YX.")


# -------------------------------------------------------------------- Part B
def mass_centre(gm: Gram):
    """Z from (2.1.4): G + E_ZZ Z = sum E_ii X_i, with E_ZZ = M c^2."""
    M = sp.Symbol("M", positive=True)
    rhs = sum((gm.m[i] * c**2 * gm.X(i) for i in range(gm.n)), sp.zeros(gm.dim, 1))
    if gm.radiation:
        rhs = rhs - gm.G()
    Z = rhs / (M * c**2)
    Q = sum(gm.m[i] * gm.m[j] * gm.gam[(i, j)] for i in range(gm.n) for j in range(gm.n))
    Q -= 2 * sum(gm.m[i] * gm.EG[i] for i in range(gm.n)) / c**2
    return M, Z, sp.expand(Q)


def mod_norm(expr, M, Q) -> bool:
    """True if expr vanishes once M^2 = Q (the normalisation g(Z, Z) = det g)."""
    num = sp.numer(sp.together(sp.expand(expr)))
    r = sp.rem(sp.expand(num), M**2 - Q, M)
    return sp.simplify(r) == 0


def part_b():
    print("B. Many-body mass centre with null radiation (2.1.4)-(2.1.15)")
    for n in (2, 3):
        gm = Gram(n, radiation=True)
        M, Z, Q = mass_centre(gm)
        EZZ = M * c**2
        gZ = [gm.dot(gm.X(i), Z) / DETG for i in range(n)]       # gamma_iZ
        EZG = gm.dot(Z, gm.G()) / DETG
        print(f"  n = {n}:")
        check("g(Z, Z) = det g  <=>  M^2 = sum m_i m_j gamma_ij - 2 sum m_i E_iG / c^2  (2.1.6)",
              mod_norm(gm.dot(Z, Z) - DETG, M, Q))
        check("(2.1.5) E_ZZ = sum E_Zi - E_ZG",
              mod_norm(EZZ - (sum(gm.m[i] * c**2 * gZ[i] for i in range(n)) - EZG), M, Q))
        check("(2.1.13b) M E_ZG = sum m_i E_iG",
              zero(M * EZG - sum(gm.m[i] * gm.EG[i] for i in range(n))))
        lhs = (EZG / DETG) ** 2
        rhs = sum(gm.m[i] * gm.m[j] * (gZ[i] * gZ[j] - gm.gam[(i, j)])
                  for i in range(n) for j in range(n))
        check("(2.1.7) (E_ZG/det g)^2 = sum m_i m_j (gamma_i gamma_j - gamma_ij)",
              mod_norm(lhs - rhs, M, Q))
        # The public 2015 version (Academia.edu) prints (8.5) and (8.6) without
        # the factors of det g that the 2017 version has in (2.1.6), (2.1.7).
        Q15 = sp.expand(sum(gm.m[i] * gm.m[j] * gm.gam[(i, j)] for i in range(n) for j in range(n))
                        - 2 * sum(gm.m[i] * gm.EG[i] for i in range(n)))
        check("2015 (8.5) M^2 = sum m_i m_j gamma_ij - 2 sum m_i E_iG holds only with c = 1",
              zero((Q - Q15).subs(c, 1)) and not zero(Q - Q15))
        check("2015 (8.6) E_ZG^2 = sum m_i m_j (gamma_i gamma_j - gamma_ij) holds with c = 1",
              mod_norm(sp.sympify(EZG**2 - rhs).subs(c, 1), M, Q.subs(c, 1)))
        if n == 2:
            q = (M**2 - 2 * M * (gm.m[0] * gZ[0] + gm.m[1] * gZ[1])
                 + gm.m[0]**2 + 2 * gm.m[0] * gm.m[1] * gm.gam[(0, 1)] + gm.m[1]**2)
            check("(2.1.14) M^2 - 2M(m_x g_ZX + m_y g_ZY) + m_x^2 + 2 m_x m_y g_XY + m_y^2 = 0",
                  mod_norm(q, M, Q))
    # (2.1.15) is the root of the quadratic (2.1.14) in M, with the gammas as
    # parameters.  Pure algebra:
    mx, my, a, b, gxy = sp.symbols("m_x m_y gamma_ZX gamma_ZY gamma_XY", positive=True)
    S = mx * a + my * b
    disc = sp.expand(S**2 - (mx**2 + 2 * mx * my * gxy + my**2))
    correct = mx**2 * (a**2 - 1) + 2 * mx * my * (a * b - gxy) + my**2 * (b**2 - 1)
    printed = mx**2 * (a - 1) + 2 * mx * my * (a * b - gxy) + my**2 * (b - 1)
    check("(2.1.15) radicand as printed is NOT S^2 - (m_x^2 + 2 m_x m_y g_XY + m_y^2)",
          not zero(disc - printed))
    check("(2.1.15) corrected radicand m_x^2(g_ZX^2 - 1) + ... + m_y^2(g_ZY^2 - 1)",
          zero(disc - correct))
    print("    printed - corrected =", sp.factor(printed - correct))
    # Without radiation, Z lies in span{X, Y} and the radicand vanishes.
    gm = Gram(2, radiation=False)
    M, Z, Q = mass_centre(gm)
    gZ = [gm.dot(gm.X(i), Z) / DETG for i in range(2)]
    rad = sp.expand(gm.m[0]**2 * (gZ[0]**2 - 1) + 2 * gm.m[0] * gm.m[1] * (gZ[0] * gZ[1] - gm.gam[(0, 1)])
                    + gm.m[1]**2 * (gZ[1]**2 - 1))
    check("G = 0: the corrected radicand vanishes, M = m_x g_ZX + m_y g_ZY",
          mod_norm(rad, M, Q))


# -------------------------------------------------------------------- Part C
def part_c():
    print("C. Reduced momentum and reduced mass (2.2.1)-(2.2.14)")
    gm = Gram(3, radiation=True)
    M, Z, Q = mass_centre(gm)
    n = gm.n
    gZ = [gm.dot(gm.X(i), Z) / DETG for i in range(n)]
    E = [gm.m[i] * c**2 for i in range(n)]
    pZ = [E[k] * (gm.X(k) - gZ[k] * Z) for k in range(n)]          # (2.2.4)
    EZG = gm.dot(Z, gm.G()) / DETG
    pZG = gm.G() - EZG * Z
    check("(2.2.4) p_Zk is g-orthogonal to Z", all(mod_norm(gm.dot(p, Z), M, Q) for p in pZ))
    tot = sum(pZ, sp.zeros(gm.dim, 1)) - pZG
    check("(2.2.5) sum_k p_Zk - p_ZG = 0  (n = 3, null G)",
          all(mod_norm(tot[r], M, Q) for r in range(gm.dim)))
    # Magnitude: Planck's momentum p = gamma m v has p^2 = m^2 c^2 (gamma^2 - 1).
    k = 0
    ratio = gm.dot(pZ[k], pZ[k]) / (gm.m[k]**2 * c**2 * (gZ[k]**2 - 1))
    check("p_Zk as printed = c^2 x (Planck momentum): g(p,p)/p_Planck^2 = c^4",
          mod_norm(sp.numer(sp.together(ratio - c**4)), M, Q))

    for n in (2, 3):
        gm = Gram(n, radiation=False)
        M, Z, Q = mass_centre(gm)
        gZ = [gm.dot(gm.X(i), Z) / DETG for i in range(n)]
        Ekk = [gm.m[i] * c**2 for i in range(n)]
        Elk = lambda l, kk: gm.gam[(l, kk)] * Ekk[kk]
        EZZ = M * c**2
        v = lambda l, kk: binary_velocity(gm, l, kk)
        mu = lambda kk, l: gm.gam[(kk, l)] * Ekk[kk] * Ekk[l] / EZZ          # (2.2.9)
        pZ = [Ekk[kk] * (gm.X(kk) - gZ[kk] * Z) for kk in range(n)]
        print(f"  n = {n}, G = 0:")
        # (2.2.8) without radiation terms
        ok = True
        for i in range(n):
            rhs = sum((Elk(i, l) * Elk(l, kk) * (v(l, i) - v(l, kk))
                       for l in range(n) for kk in range(n)), sp.zeros(gm.dim, 1))
            rhs = Ekk[i] / EZZ**2 * rhs
            ok &= all(mod_norm(pZ[i][r] - rhs[r], M, Q) for r in range(gm.dim))
        check("(2.2.8) p_Zi = E_ii/E_ZZ^2 sum_lk E_il E_lk (v_li - v_lk)", ok)
        if n == 2:
            rhs = mu(0, 1) * (Ekk[1] * v(1, 0) - Ekk[0] * v(0, 1)) / EZZ
            check("(2.2.10) p_Z1 = mu_12 (E_22 v_21 - E_11 v_12)/E_ZZ",
                  all(mod_norm(pZ[0][r] - rhs[r], M, Q) for r in range(gm.dim)))
        if n == 3:
            E = lambda a, b: Elk(a, b)
            r1 = (mu(0, 1) * ((Ekk[1] + E(1, 2)) * v(1, 0) - Ekk[0] * v(0, 1)) / EZZ
                  + mu(2, 0) * ((Ekk[2] + E(2, 1)) * v(2, 0) - Ekk[0] * v(0, 2)) / EZZ
                  - Ekk[0] / EZZ * (E(0, 1) * E(1, 2) * v(1, 2) + E(0, 2) * E(2, 1) * v(2, 1)) / EZZ)
            check("(2.2.11) three-body p_Z1 as printed",
                  all(mod_norm(pZ[0][r] - r1[r], M, Q) for r in range(gm.dim)))


# -------------------------------------------------------------------- Part D
def part_d():
    print("D. The mass centre as an idempotent of the observer algebra")
    for n in (2, 3):
        m = sp.Matrix(sp.symbols(f"m1:{n + 1}", positive=True))
        Gm = sp.eye(n)
        for i, j in itertools.combinations(range(n), 2):
            s = sp.Symbol(f"gamma{i + 1}{j + 1}", positive=True)
            Gm[i, j] = Gm[j, i] = s
        mul = lambda A, B: A * Gm * B          # e_ij e_kl = gamma_jk e_il
        tr = lambda A: (A * Gm).trace()        # tr e_ij = gamma_ij
        unit = lambda i: sp.Matrix(n, n, lambda r, s: 1 if (r, s) == (i, i) else 0)
        p = [unit(i) for i in range(n)]
        P = sp.zeros(n, n)
        for i in range(n):
            for j in range(n):
                P += m[i] * m[j] * mul(p[i], p[j]) / Gm[i, j]
        M2 = sp.expand((m.T * Gm * m)[0, 0])
        cc = P / M2
        print(f"  n = {n}:")
        check("p_i p_j p_i = gamma_ij^2 p_i", all(zero(sp.Matrix(mul(mul(p[i], p[j]), p[i]) - Gm[i, j]**2 * p[i]).norm())
                                                    for i in range(n) for j in range(n)))
        check("P = sum m_i m_j p_i p_j / gamma_ij = m m^T", zero((P - m * m.T).norm()))
        check("P P = M^2 P and tr P = M^2 (M^2 = m^T G m)",
              zero(sp.Matrix(mul(P, P) - M2 * P).norm()) and zero(tr(P) - M2))
        check("c = P/M^2: c c = c, tr c = 1", zero(sp.Matrix(mul(cc, cc) - cc).norm()) and zero(tr(cc) - 1))
        gZ = (Gm * m) / sp.sqrt(M2)
        check("c p_i c = gamma_iZ^2 c with gamma_iZ = (G m)_i / M",
              all(zero(sp.Matrix(mul(mul(cc, p[i]), cc) - gZ[i]**2 * cc).norm()) for i in range(n)))
        check("c is not central (c p_1 != p_1 c)", not zero(sp.Matrix(mul(cc, p[0]) - mul(p[0], cc)).norm()))
        if n == 2:
            x = sp.Matrix(2, 2, sp.symbols("x11 x12 x21 x22"))
            eqs = list(mul(x, P) - P) + list(mul(P, x) - P) + list(mul(x, x) - x) + [tr(x) - 1]
            sol = sp.solve(eqs, list(x), dict=True)
            check("uniqueness: c is the only idempotent of trace 1 with cP = P = Pc (n = 2, solved)",
                  len(sol) == 1 and zero(sp.Matrix(x.subs(sol[0]) - cc).norm()))


# -------------------------------------------------------------------- Part E
def centroid_rest_position(particles, beta):
    """Observer-n energy centroid of free particles, in the centre-of-momentum
    frame (c = 1).  particles: list of (m, w, a) with w the velocity and a the
    position at t = 0, all in the CM frame.  Returns (spatial position, d/dtau)."""
    tau = sp.Symbol("tau")
    bx, by = beta
    pts, wts = [], []
    for m, w, a in particles:
        gam = 1 / sp.sqrt(1 - w[0]**2 - w[1]**2)
        E, p = m * gam, (m * gam * w[0], m * gam * w[1])
        t = (tau + bx * a[0] + by * a[1]) / (1 - bx * w[0] - by * w[1])   # t - beta.x = tau
        pts.append((a[0] + w[0] * t, a[1] + w[1] * t))
        wts.append(E - bx * p[0] - by * p[1])                             # energy seen by n (up to gamma_n)
    W = sum(wts)
    X = [sp.simplify(sum(wt * pt[i] for wt, pt in zip(wts, pts)) / W) for i in range(2)]
    return X, [sp.diff(Xi, tau) for Xi in X]


def part_e():
    print("E. What Z does not fix: the centroid depends on the observer (c = 1, exact rationals)")
    R = sp.Rational
    # CM frame: p1 = (12, 0), p2 = (-12, 0); E1 = 20, E2 = 15; M = 35; S = -24.
    parts = [(16, (R(3, 5), 0), (0, 1)), (9, (R(-4, 5), 0), (0, -1))]
    M = sum(m / sp.sqrt(1 - w[0]**2 - w[1]**2) for m, w, a in parts)
    S = sum(a[0] * m * w[1] / sp.sqrt(1 - w[0]**2 - w[1]**2) - a[1] * m * w[0] / sp.sqrt(1 - w[0]**2 - w[1]**2)
            for m, w, a in parts)
    X0, _ = centroid_rest_position(parts, (0, 0))
    print(f"  M = {M}, S = {S}, rest-frame centroid = {X0}, disk radius |S|/M = {abs(S) / M}")
    betas = [(R(3, 5), 0), (0, R(3, 5)), (R(-3, 5), 0), (R(12, 25), R(9, 25)),
             (R(5, 13), 0), (R(12, 13), 0), (0, R(-20, 29)), (R(-63, 65), 0)]
    ok_rest, ok_formula = True, True
    for b in betas:
        X, V = centroid_rest_position(parts, b)
        ok_rest &= all(zero(Vi) for Vi in V)
        d = (X[0] - X0[0], X[1] - X0[1])
        pred = (-b[1] * S / M, b[0] * S / M)       # Delta = (S x beta)/M, S along e_z
        ok_formula &= zero(d[0] - pred[0]) and zero(d[1] - pred[1])
        print(f"    beta = ({b[0]}, {b[1]}):  Delta = ({sp.nsimplify(d[0])}, {sp.nsimplify(d[1])})")
    check("each observer's centroid is at rest in the CM frame (moves parallel to Z)", ok_rest)
    check("Moller: Delta = (S x beta)/(M c), so |Delta| < |S|/(M c)", ok_formula)


# -------------------------------------------------------------------- Part F
def part_f():
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from ozlib.utils import docs_path, output_path

    M, S, y0 = 35.0, -24.0, 1.0 / 7.0
    R = abs(S) / M
    fig, ax = plt.subplots(figsize=(8, 4.2))
    th = np.linspace(0, 2 * np.pi, 400)
    ax.fill(R * np.cos(th), y0 + R * np.sin(th), color="0.9", zorder=0,
            label=r"Møller disk, radius $|S|/(Mc)$")
    for speed, mk in ((0.3, "o"), (0.6, "s"), (0.9, "^")):
        phi = np.linspace(0, 2 * np.pi, 13)[:-1]
        bx, by = speed * np.cos(phi), speed * np.sin(phi)
        ax.plot(-by * S / M, y0 + bx * S / M, mk, ms=4, ls="none",
                label=fr"centroid for observer at $|\beta| = {speed}$")
    ax.plot([0], [y0], "k+", ms=10, label="centroid in the CM frame")
    ax.axhline(1, color="C3", lw=1)
    ax.axhline(-1, color="C0", lw=1)
    ax.annotate(r"body 1: $m=16$, $w=(3/5,0)$", (-1.5, 1.05), color="C3", fontsize=8)
    ax.annotate(r"body 2: $m=9$, $w=(-4/5,0)$", (-1.5, -0.95), color="C0", fontsize=8)
    ax.set_aspect("equal")
    ax.set_xlim(-1.6, 1.6)
    ax.set_ylim(-1.2, 1.3)
    ax.set_xlabel("x (rest space of Z)")
    ax.set_ylabel("y")
    ax.set_title("All centroids move with Z; where they sit depends on the observer", fontsize=9)
    ax.legend(fontsize=7, loc="center left", bbox_to_anchor=(1.02, 0.5))
    fig.tight_layout()
    name = "mass_centre_moller_disk.png"
    fig.savefig(output_path(name), dpi=150)
    dp = docs_path(name)
    if dp:
        fig.savefig(dp, dpi=150)
    print(f"F. figure written: {output_path(name)}" + (f" and {dp}" if dp else ""))


# -------------------------------------------------------------------- Part W
def part_w():
    print("W. Wide binary stars: how large is gamma - 1?")
    cc = sp.Integer(299792458)
    for v_kms in (sp.Rational(1, 2), 1, 2):
        v = v_kms * 1000
        gm1 = 1 / sp.sqrt(1 - (v / cc) ** 2) - 1
        print(f"  v = {v_kms} km/s: gamma - 1 = {sp.N(gm1, 3)}")


if __name__ == "__main__":
    part_a()
    part_b()
    part_c()
    part_d()
    part_e()
    part_f()
    part_w()
    print()
    print("ALL CHECKS PASSED" if not FAILED else f"{len(FAILED)} FAILED: {FAILED}")
