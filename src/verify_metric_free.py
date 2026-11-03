"""Exact checks for analysis/metric_free_body.md (ladder step 3).

A body is a pair (X, alpha) with alpha X = 1, and Gamma_XY = alpha_X(Y).  No
metric is used except where a part says so.  Equation numbers are those of
Oziewicz, Many-body mass-centre, long version revised 11 April 2017.

Parts A to H are exact (SymPy).  Part I draws the figure (NumPy, numerical).

Parts
  A  MF1: creation and evaluation, the split, the Koszul homotopy
  B  MF2: velocity without a metric; the misprint in (1.4.11)
  C  MF3: the mass centre and radiation
  D  MF4, MF5: reciprocity of clocks gives b; counting; (16) of the 2007 paper
  E  MF6: the signature from the sign of Gamma - 1
  F  MF7: the surface of unit processes; a surface that is not a quadric
  G  MF8: the two mass centres
  H  MF9 to MF11: the rotating disk, position, the clock as a connection
  I  figure

Run:  PYTHONPATH=src python3 -u src/verify_metric_free.py
Writes metric_free_unit_surfaces.png through ozlib.utils.output_path (and
docs_path when OZ_DOCS is set).
"""

from __future__ import annotations

import itertools

import sympy as sp
from sympy import Matrix, Rational as R, eye, symbols, zeros
from sympy.polys.matrices import DomainMatrix

FAILED: list[str] = []


def check(name: str, condition) -> None:
    good = bool(condition)
    print(("  ok    " if good else "  FAIL  ") + name, flush=True)
    if not good:
        FAILED.append(name)


def dual(a, x):
    return sum(p * q for p, q in zip(a, x))


# --------------------------------------------------------------------------
# Grassmann algebra of a space of dimension n, as matrices on the 2^n basis
# --------------------------------------------------------------------------
class Grassmann:
    def __init__(self, n: int):
        self.n, self.N = n, 2**n
        self.subs = sorted(range(self.N), key=lambda s: (bin(s).count("1"), s))
        self.idx = {s: i for i, s in enumerate(self.subs)}
        self.cre = [self._cre(i) for i in range(n)]
        self.ann = [c.T for c in self.cre]

    def _cre(self, i):
        c = zeros(self.N, self.N)
        for s in self.subs:
            if not s >> i & 1:
                c[self.idx[s | 1 << i], self.idx[s]] = (-1) ** bin(s & ((1 << i) - 1)).count("1")
        return c

    def wedge(self, a):
        return sum((a[i] * self.cre[i] for i in range(self.n)), zeros(self.N, self.N))

    def ev(self, x):
        return sum((x[i] * self.ann[i] for i in range(self.n)), zeros(self.N, self.N))

    def lmul(self, v):
        out = zeros(self.N, self.N)
        for s in self.subs:
            if v[self.idx[s]] != 0:
                m = eye(self.N)
                for i in reversed([i for i in range(self.n) if s >> i & 1]):
                    m = self.cre[i] * m
                out += v[self.idx[s]] * m
        return out


def acomm(a, b):
    return a * b + b * a


def part_a():
    print("\nPart A: MF1, the split")
    g4 = Grassmann(4)
    z16 = zeros(16, 16)
    # The fermion relations are integer identities; bilinearity then gives
    # {ev_X, wedge_a} = aX for all X, a.
    fermion = all(
        acomm(g4.ann[i], g4.cre[j]) == (eye(16) if i == j else z16)
        and acomm(g4.ann[i], g4.ann[j]) == z16
        and acomm(g4.cre[i], g4.cre[j]) == z16
        for i in range(4) for j in range(4))
    check("{a_i, c_j} = delta_ij, {a,a} = {c,c} = 0: so {ev_X, wedge_a} = aX, and neutral Clifford", fermion)

    # Symbolic in n = 3: Pi is the algebra map, D the derivation
    g3 = Grassmann(3)
    xs, a_s = symbols("x0:3"), symbols("a0:3")
    s = dual(a_s, xs)
    ev3, we3 = g3.ev(xs), g3.wedge(a_s)
    pi3, d3 = ev3 * we3, we3 * ev3
    check("n=3 symbolic: Pi + D = s id, Pi D = 0, Pi^2 = s Pi",
          (pi3 + d3 - s * eye(8)).expand() == zeros(8, 8)
          and (pi3 * d3).expand() == zeros(8, 8)
          and (pi3 * pi3 - s * pi3).expand() == zeros(8, 8))
    good_map = good_der = True
    basis = [Matrix([1 if i == k else 0 for i in range(8)]) for k in range(8)]
    for b, c in itertools.product(basis, basis):
        p = g3.lmul(b) * c
        # s Pi(b ^ c) = Pi b ^ Pi c, cleared of denominators (Pi here is unnormalised)
        if (s * pi3 * p - g3.lmul(pi3 * b) * (pi3 * c)).expand() != zeros(8, 1):
            good_map = False
        if (d3 * p - g3.lmul(d3 * b) * c - g3.lmul(b) * (d3 * c)).expand() != zeros(8, 1):
            good_der = False
    check("n=3 symbolic, all basis pairs: Pi is multiplicative, D is a grade-0 derivation", good_map and good_der)

    # Rational case in n = 4
    x = [R(2), R(-1), R(3), R(1, 2)]
    a = [R(1), R(5, 3), R(-2), R(4)]
    sc = dual(a, x)
    a = [p / sc for p in a]
    ev, we = g4.ev(x), g4.wedge(a)
    pi, d = ev * we, we * ev
    check("n=4: Pi, D idempotent, Pi D = 0, Pi + D = id, ranks 8, 8",
          pi**2 == pi and d**2 == d and pi * d == z16 and pi + d == eye(16)
          and pi.rank() == 8 and d.rank() == 8)
    check("n=4: rank ev_X = 8, so ker ev_X = im ev_X: the Koszul complex is exact, with the clock as homotopy",
          ev.rank() == 8 and ev * ev == z16)
    check("(1.3.21): ev wedge ev = (aX) ev, wedge ev wedge = (aX) wedge",
          ev * we * ev == ev and we * ev * we == we)
    same_span = lambda p, q: p.rank() == q.rank() == p.row_join(q).rank()
    x2 = [R(1), R(4), R(-1), R(2)]
    a2 = [R(3), R(1), R(1), R(-1)]
    s1, s2 = dual(a, x2), dual(a2, x)
    d12 = g4.wedge(a) * g4.ev(x2) / s1
    pi21 = g4.ev(x) * g4.wedge(a2) / s2
    check("(alpha), the kernel of Pi, depends on the clock only", same_span(d, d12))
    check("ker ev_X, the image of Pi, depends on the process only", same_span(pi, pi21))
    f = R(7, 3)
    check("the gauge (X, a) -> (fX, a/f) leaves Pi and D unchanged",
          g4.ev([f * p for p in x]) * g4.wedge([p / f for p in a]) == pi)
    # X, a and -X, -a give one idempotent
    check("(X, a) and (-X, -a) give the same p = X tensor a",
          Matrix(x) * Matrix([a]) == Matrix([-p for p in x]) * Matrix([[-p for p in a]]))
    return g4


def part_b():
    print("\nPart B: MF2, velocity")
    A, B = symbols("A B", positive=True)  # A = alpha(Y), B = beta(X)
    X, Y = symbols("X Y", commutative=True)
    v_xy, v_yx = Y / A - X, X / B - Y
    check("(1.7.19) general: v_YX = -A v_XY - (A - 1/B) X",
          sp.simplify(v_yx - (-A * v_xy - (A - 1 / B) * X)) == 0)
    check("(1.7.22) general: v_XY + v_YX = (1/A - 1) Y + (1/B - 1) X",
          sp.simplify(v_xy + v_yx - ((1 / A - 1) * Y + (1 / B - 1) * X)) == 0)
    # (1.7.20): v_YX ^ v_XY on the basis X, Y: coefficient of Y ^ X
    m = Matrix([[1 / B, -1], [-1, 1 / A]])  # rows: v_YX, v_XY on (X, Y)
    check("(1.7.20) general: v_YX ^ v_XY = (1 - 1/(A B)) Y ^ X, using only tr(pq) = A B",
          sp.simplify(m.det() + (1 - 1 / (A * B))) == 0)
    # Change of clock: a' = a + b with b X = 0
    a, b, y = symbols("a:4"), symbols("b:4"), symbols("y:4")
    a = (1, a[1], a[2], a[3])         # adopted coordinates: X = d/dt, so a X = 1, and b X = 0
    bb = (0, b[1], b[2], b[3])
    ap = tuple(p + q for p, q in zip(a, bb))
    v = [y[i] / dual(a, y) for i in (1, 2, 3)]
    vp = [y[i] / dual(ap, y) for i in (1, 2, 3)]
    check("a -> a + b, b X = 0: the components v x^i = Y x^i / a(Y) change by one common factor",
          all(sp.simplify(p / q - dual(a, y) / dual(ap, y)) == 0 for p, q in zip(vp, v)))
    # (1.4.11) against (1.4.7): X = d/dt, Y = gamma (d/dt + u d/dx), metric clock dt
    u = R(3, 5)
    g = 1 / sp.sqrt(1 - u**2)
    yt, yx = g, g * u                 # Y t, Y x
    vx = yx / yt - 0                  # (1.4.7): v x = (Y/clock_X Y - X) x, with X x = 0
    check("(1.4.7) gives v x = Yx/gamma = 3/5, while line 1 of (1.4.11) gives Yx = 3/4: off by gamma",
          vx == u and yx == R(3, 4) and vx == yx / g != yx)
    # (1.4.12), (1.4.13), (1.6.6): Minkowski g = diag(-c^2, 1), det g = -c^2, X = d/dt, Y as above
    c = symbols("c", positive=True)
    gm = sp.diag(-(c**2), 1)
    Xv, Yv = Matrix([1, 0]), Matrix([g, g * u * c])     # Y with speed u c
    detg = gm.det()
    gX = gm * Xv
    clock_y = (gX.T * Yv)[0] / (gX.T * Xv)[0]
    check("(1.6.6): clock_X X = 1 and clock_X Y = gamma, not (det g) gamma; (gX)Y = (det g) gamma as in (1.7.12)",
          (gX.T * Xv)[0] == detg and clock_y == g and (gX.T * Yv)[0] == detg * g != clock_y)


def part_c(g4):
    print("\nPart C: MF3, the mass centre and radiation")
    m = symbols("m1:4", positive=True)
    X = [[symbols(f"x{i}{j}") for j in range(4)] for i in range(3)]
    A = [[symbols(f"a{i}{j}") for j in range(4)] for i in range(3)]
    P = [sum(m[i] * X[i][k] for i in range(3)) for k in range(4)]
    th = [sum(m[i] * A[i][k] for i in range(3)) for k in range(4)]
    M2 = dual(th, P)
    G = [[dual(A[i], X[j]) for j in range(3)] for i in range(3)]
    check("M^2 = theta(P) = sum m_i m_j Gamma_ij, for non-symmetric Gamma",
          sp.expand(M2 - sum(m[i] * m[j] * G[i][j] for i in range(3) for j in range(3))) == 0)
    c = Matrix(P) * Matrix([th]) / M2
    tm = symbols("t0:4"), symbols("u0:4")
    p_ = Matrix(tm[0]); t_ = Matrix([tm[1]]); s = (t_ * p_)[0]
    c = p_ * t_ / s
    check("c = P tensor theta / theta(P) is an idempotent of trace 1 (P, theta symbolic)",
          sp.simplify(c * c - c) == zeros(4, 4) and sp.simplify(c.trace() - 1) == 0)
    g12, g21 = symbols("g12 g21", positive=True)
    m1, m2 = m[0], m[1]
    q2 = m1**2 + m2**2 + m1 * m2 * (g12 + g21)
    check("M^2 - (sum m)^2 = sum m_i m_j (Gamma_ij - 1), Gamma_ii = 1",
          sp.expand(q2 - (m1 + m2) ** 2 - m1 * m2 * (g12 - 1) - m1 * m2 * (g21 - 1)) == 0)
    # common clock
    s0, s1, t = symbols("s0 s1 t")
    tau = (1, 0)
    x1, x2 = (1, s0), (1, s1)
    Z = [(m1 * p + m2 * q) / (m1 + m2) for p, q in zip(x1, x2)]
    check("common clock: Gamma = 1, M = m1 + m2, Z is the barycentric velocity",
          dual(tau, x1) == 1 == dual(tau, x2) and sp.simplify(dual(tau, Z) - 1) == 0)
    # radiation
    pp, tt, gg, ga = [Matrix(symbols(f"{n}0:4")) for n in ("p", "q", "g", "h")]
    M2r = ((tt - ga).T * (pp - gg))[0]
    check("with radiation M^2 = theta(P) - theta(G) - gamma(P) + gamma(G)",
          sp.expand(M2r - ((tt.T * pp)[0] - (tt.T * gg)[0] - (ga.T * pp)[0] + (ga.T * gg)[0])) == 0)
    G_, gam = [1, 2, 0, 0], [2, -1, 3, 5]
    check("radiation: gamma G = 0 gives a square-zero rank-one operator and anticommuting operators, so no split",
          dual(gam, G_) == 0 and (Matrix(G_) * Matrix([gam])) ** 2 == zeros(4, 4)
          and acomm(g4.ev(G_), g4.wedge(gam)) == zeros(16, 16))


def part_d():
    print("\nPart D: MF4, reciprocity of clocks gives b")
    # Symbolic n = 3: a basis of bodies, symmetric Gamma, and a further body Y
    A = Matrix(3, 3, symbols("x0:9"))            # columns are X_1, X_2, X_3
    g = symbols("g12 g13 g23")
    G = Matrix([[1, g[0], g[1]], [g[0], 1, g[2]], [g[1], g[2], 1]])
    Ainv = A.adjugate()                          # A^-1 times det A
    d = A.det()
    b = Ainv.T * G * Ainv                        # d^2 b, where b(X_i, X_j) = G_ij
    check("b(X_i, X_j) = Gamma_ij reproduces each clock, b(X_i, .) = alpha_i",
          (A.T * b * A - d**2 * G).applyfunc(sp.expand) == zeros(3, 3))
    y = Matrix(symbols("y0:3"))
    # A clock beta of Y with beta(X_i) = alpha_i(Y) for each i is forced:
    ai = G * Ainv                                # rows: d * alpha_i
    beta = Matrix(symbols("b0:3"))
    eqs = [(beta.T * A[:, i])[0] * d - (ai[i, :] * y)[0] for i in range(3)]
    sol = sp.solve(eqs, list(beta), dict=True)[0]
    forced = Matrix([sol[b_] for b_ in beta])
    check("reciprocity with X_1, X_2, X_3 forces the clock of any Y to be b(Y, .)",
          sp.simplify(forced * d**2 - b * y) == zeros(3, 1))

    def solve_clocks(xs):
        rows, rhs = [], []
        n_ = len(xs)
        for i in range(n_):
            r = [0] * (4 * n_)
            r[4 * i:4 * i + 4] = xs[i]
            rows.append(r); rhs.append(1)
        for i, j in itertools.combinations(range(n_), 2):
            r = [0] * (4 * n_)
            r[4 * i:4 * i + 4] = xs[j]
            for k in range(4):
                r[4 * j + k] -= xs[i][k]
            rows.append(r); rhs.append(0)
        dm = lambda m: DomainMatrix([[sp.QQ(int(v)) for v in r] for r in m], (len(m), len(m[0])), sp.QQ)
        ra, rb = dm(rows).rank(), dm([r + [c] for r, c in zip(rows, rhs)]).rank()
        return ra == rb, 4 * n_ - ra

    xs = [[(i * j + i + 2 * j + 1) ** 2 % 23 - 11 + (i == j) * 7 for j in range(4)] for i in range(11)]
    counts = {n_: solve_clocks(xs[:n_]) for n_ in (4, 5, 8, 10, 11)}
    print("        bodies: (symmetric clocks exist, dimension) =", counts)
    check("one fixed set of bodies in 4D: dimension 10 - N for N <= 10, none for N = 11",
          all(counts[n_] == (True, 10 - n_) for n_ in (4, 5, 8, 10)) and not counts[11][0])

    # (16) of Relativity groupoid: p* g = g p holds iff alpha is proportional to gP
    P = Matrix(symbols("P0:4"))
    a = Matrix(symbols("a0:4"))
    gm = Matrix(4, 4, lambda i, j: symbols(f"g{min(i, j)}{max(i, j)}"))
    p = P * a.T
    lhs = p.T * gm - gm * p
    # With a = gP/(P.gP) the difference vanishes
    gp = gm * P
    check("(16) of the 2007 paper: p* g - g p = a (gP)^T - (gP) a^T, zero iff a is parallel to gP",
          (lhs - (a * gp.T - gp * a.T)).applyfunc(sp.expand) == zeros(4, 4))

    # Scale gauge: cycle ratios
    Gr = Matrix([[1, 2, 3], [R(3, 2), 1, 4], [2, 5, 1]])
    lam = [R(2), R(5), R(7)]
    Gg = Matrix(3, 3, lambda i, j: Gr[i, j] * lam[j] / lam[i])
    ratio = lambda m: m[0, 1] * m[1, 2] * m[2, 0] / (m[0, 2] * m[2, 1] * m[1, 0])
    check("the cycle ratio Gamma_12 Gamma_23 Gamma_31 / Gamma_13 Gamma_32 Gamma_21 is gauge invariant",
          ratio(Gg) == ratio(Gr) != 1)
    sym = Matrix([[1, 2, 3], [2, 1, 4], [3, 4, 1]])
    Gs = Matrix(3, 3, lambda i, j: sym[i, j] * (i + 1) / sp.Integer(j + 1))  # a gauge of a symmetric matrix
    r12, r13 = Gs[1, 0] / Gs[0, 1], Gs[2, 0] / Gs[0, 2]
    lams = [sp.Integer(1), sp.sqrt(r12), sp.sqrt(r13)]
    Gt = Matrix(3, 3, lambda i, j: Gs[i, j] * lams[j] / lams[i])
    check("cycle ratio 1 and positive ratios: lambda_j^2 = Gamma_j1/Gamma_1j symmetrises",
          ratio(Gs) == 1 and sp.simplify(Gt - Gt.T) == zeros(3, 3))


def part_e():
    print("\nPart E: MF6, the signature")
    eps, s = symbols("epsilon s", real=True)
    Gam = 1 / sp.sqrt(1 + eps**2 * s)
    ser = sp.series(Gam, eps, 0, 4).removeO()
    check("Gamma(X, Y) = 1/sqrt(1 + e^2 b(w,w)) = 1 - e^2 b(w,w)/2 + ...",
          sp.simplify(ser - (1 - eps**2 * s / 2)) == 0)
    # Rank one from Gamma = 1 on a neighbourhood
    w = symbols("w1:4")
    b = sp.diag(1, 0, 0, 0)
    tau = Matrix([[1, 0, 0, 0]])
    y = Matrix([1, *w])
    check("b = tau tensor tau: the clock of every Y with tau Y = 1 is tau",
          (b * y).T == tau)
    # three bodies with all Gamma >= 1 and the wrong signature
    G3 = Matrix([[1, R(11, 10), R(11, 10)], [R(11, 10), 1, 3], [R(11, 10), 3, 1]])
    cp = sp.Poly(G3.charpoly().as_expr())
    roots = sorted(sp.N(r) for r in cp.all_roots())
    print("        eigenvalues:", roots, " det:", G3.det())
    check("three bodies, every Gamma >= 1, two positive eigenvalues", sum(1 for r in roots if r > 0) == 2)
    # rapidity triangle fails there
    check("there arccosh 3 > 2 arccosh(11/10), so the triangle inequality of rapidities fails",
          sp.acosh(3).evalf() > 2 * sp.acosh(R(11, 10)).evalf())
    # A Lorentz example
    X = Matrix([R(5, 3), R(4, 3)]); Y = Matrix([R(13, 12), R(5, 12)])
    bl = sp.diag(1, -1)
    check("Lorentz example: Gamma >= 1 and b negative on the rest space of X",
          (X.T * bl * Y)[0] >= 1 and (Matrix([R(4, 3), R(5, 3)]).T * bl * Matrix([R(4, 3), R(5, 3)]))[0] < 0
          and (Matrix([R(4, 3), R(5, 3)]).T * bl * X)[0] == 0)


def part_f():
    print("\nPart F: MF7, the surface of unit processes")
    t, x, e, u = symbols("t x e u", real=True)
    # A quadric: L^2 = t^2 - x^2
    L = sp.sqrt(t**2 - x**2)
    dL = Matrix([sp.diff(L, t), sp.diff(L, x)])
    check("quadric: dL at (t, x) is (t, -x)/L, so the tangent clock is b(X, .)/L",
          sp.simplify(dL - Matrix([t, -x]) / L) == zeros(2, 1))
    check("Euler: dL(X) = L(X)", sp.simplify(dL.dot(Matrix([t, x])) - L) == 0)
    # Not a quadric: L^4 = t^4 - x^4
    L4 = lambda a, b: (a**4 - b**4) ** R(1, 4)
    dL4 = lambda a, b: Matrix([a**3, -(b**3)]) / L4(a, b) ** 3
    check("L^4 = t^4 - x^4: Euler holds at (2, 1)",
          sp.simplify(dL4(2, 1).dot(Matrix([2, 1])) - L4(2, 1)) == 0)
    X = Matrix([1, 0])                            # unit, with clock dt
    Y = Matrix([2, 1]) / L4(2, 1)                 # unit
    gxy = dL4(1, 0).dot(Y)
    gyx = dL4(2, 1).dot(X)
    print("        Gamma_XY =", sp.nsimplify(gxy), "=", sp.N(gxy, 8), " Gamma_YX =", sp.nsimplify(gyx), "=", sp.N(gyx, 8))
    check("L^4 = t^4 - x^4: Gamma_XY = 2/15^(1/4), Gamma_YX = 8/15^(3/4), not equal",
          sp.simplify(gxy - 2 / sp.Integer(15) ** R(1, 4)) == 0
          and sp.simplify(gyx - 8 / sp.Integer(15) ** R(3, 4)) == 0 and sp.N(gxy - gyx) != 0)
    # Concavity
    s = symbols("s", positive=True)
    f = (1 - s**4) ** R(1, 4)
    fpp = sp.simplify(sp.diff(f, s, 2))
    print("        L = t f(x/t), f'' =", fpp)
    check("f'' < 0 on 0 < s < 1, so L is concave (value at s = 1/2)", fpp.subs(s, R(1, 2)).evalf() < 0)
    # kappa = -Hess L on the rest space: exact Taylor at (2, 1) for L^4
    a0, b0 = sp.Integer(2), sp.Integer(1)
    ll = L4(t, x)
    H = Matrix(2, 2, lambda i, j: sp.diff(ll, [t, x][i], [t, x][j])).subs({t: a0, x: b0})
    al = dL4(a0, b0)
    w = Matrix([al[1], -al[0]])                  # in ker alpha
    lam = L4(a0, b0)
    X0 = Matrix([a0, b0]) / lam
    # Gamma(e) along Y(e) = (X0 + e w) / L(X0 + e w)
    pt = X0 + e * w
    lp = (pt[0] ** 4 - pt[1] ** 4) ** R(1, 4)
    gam = (al.dot(pt)) / lp
    c2 = sp.diff(gam, e, 2).subs(e, 0) / 2
    hess = lam * (w.T * H * w)[0]                # Hess L at X0 = lam * Hess L at (2, 1)
    check("Gamma(e) = 1 - (e^2/2) Hess L(w, w) + ..., exact at (2, 1) on L^4",
          sp.simplify(c2 + hess / 2) == 0 and sp.simplify(sp.diff(gam, e).subs(e, 0)) == 0)
    # A hyperplane: H = {tau = 1} has tangent plane ker tau at every point
    s0 = symbols("s0")
    pt0 = Matrix([1, s0])
    tang = Matrix([0, 1])
    tau = Matrix([[1, 0]])
    check("hyperplane tau = 1: the tangent clock at every point is tau", (tau * tang)[0] == 0 and (tau * pt0)[0] == 1)
    # (1.7.15) from b: with c = 1, kappa = -b on the rest space and v^2 = 1 - 1/Gamma^2
    y = symbols("y", positive=True)
    bl = sp.diag(1, -1)
    X_, e_ = Matrix([1, 0]), Matrix([0, 1])
    Y_ = sp.cosh(y) * X_ + sp.sinh(y) * e_
    G_ = (X_.T * bl * Y_)[0]
    v_ = Y_ / G_ - X_
    check("(1.7.15) with c = 1: kappa(v, v) = -b(v, v) = 1 - 1/Gamma^2, and Gamma = cosh y",
          sp.simplify(-(v_.T * bl * v_)[0] - (1 - 1 / G_**2)) == 0 and G_ == sp.cosh(y))


def part_g():
    print("\nPart G: MF8, the two mass centres")
    L4 = lambda a, b: (a**4 - b**4) ** R(1, 4)
    dL4 = lambda a, b: Matrix([a**3, -(b**3)]) / L4(a, b) ** 3
    # Momentum vectors (1, 0) and (2, 1): masses 1 and L(2, 1)
    m2 = L4(2, 1)
    th = dL4(1, 0) + m2 * dL4(2, 1)              # sum of momentum forms
    P = Matrix([3, 1])
    cl = dL4(3, 1)                               # tangent clock of the vector mean
    cross = sp.simplify(th[0] * cl[1] - th[1] * cl[0])
    print("        cross product of theta with the clock of P:", cross, "=", sp.N(cross, 8))
    check("L^4: the clock of the vector mean is not parallel to the sum of the clocks", sp.N(cross) != 0)
    # Numerical check of the velocity values, marked as such
    import numpy as np
    from scipy.optimize import brentq
    ln = lambda v: (v[0] ** 4 - v[1] ** 4) ** 0.25
    dn = lambda v: np.array([v[0] ** 3, -(v[1] ** 3)]) / ln(v) ** 3
    un = lambda s: np.array([1.0, s]) / ln(np.array([1.0, s]))
    x_, y_ = un(0.3), un(0.7)
    pn = x_ + 2 * y_
    tn = dn(x_) + 2 * dn(y_)
    s_form = brentq(lambda s: dn(un(s))[1] / dn(un(s))[0] - tn[1] / tn[0], 0.0, 0.99)
    print(f"        NUMERICAL, velocities 0.3 and 0.7, masses 1 and 2: vector mean {pn[1] / pn[0]:.6f}, "
          f"form mean {s_form:.6f}")
    print(f"        NUMERICAL Gamma_XY {dn(x_) @ y_:.6f}, Gamma_YX {dn(y_) @ x_:.6f}")
    grid = np.linspace(-0.95, 0.95, 41)
    gm = np.array([[dn(un(p)) @ un(q) for q in grid] for p in grid])
    print(f"        NUMERICAL min Gamma on the grid {gm.min():.6f}")
    check("NUMERICAL: on the grid every Gamma >= 1 to rounding", gm.min() > 1 - 1e-12)


class Form:
    """Differential forms on coordinates c: dict sorted-index-tuple -> expression."""

    def __init__(self, c, d=None):
        self.c = c
        self.d = {}
        for k, v in (d or {}).items():
            w = sp.simplify(v)
            if w != 0:
                self.d[k] = w

    def __add__(self, o):
        d = dict(self.d)
        for k, v in o.d.items():
            d[k] = d.get(k, 0) + v
        return Form(self.c, d)

    def __rmul__(self, f):
        return Form(self.c, {k: f * v for k, v in self.d.items()})

    def __sub__(self, o):
        return self + (-1) * o

    def zero(self):
        return not self.d


def perm_sign(t):
    sign = 1
    for i in range(len(t)):
        for j in range(i + 1, len(t)):
            if t[i] > t[j]:
                sign = -sign
    return sign


def wed(p, q):
    d = {}
    for k1, v1 in p.d.items():
        for k2, v2 in q.d.items():
            if not set(k1) & set(k2):
                t = k1 + k2
                k = tuple(sorted(t))
                d[k] = d.get(k, 0) + perm_sign(t) * v1 * v2
    return Form(p.c, d)


def ext(p):
    d = {}
    for k, v in p.d.items():
        for i, x in enumerate(p.c):
            if i not in k:
                t = (i,) + k
                kk = tuple(sorted(t))
                d[kk] = d.get(kk, 0) + perm_sign(t) * sp.diff(v, x)
    return Form(p.c, d)


def iv(x, p):
    d = {}
    for k, v in p.d.items():
        for pos, i in enumerate(k):
            kk = k[:pos] + k[pos + 1:]
            d[kk] = d.get(kk, 0) + (-1) ** pos * x[i] * v
    return Form(p.c, d)


def lie(x, p):
    return iv(x, ext(p)) + ext(iv(x, p))


def dfun(c, f):
    return ext(Form(c, {(): f}))


def part_h():
    print("\nPart H: MF9 to MF11, the rotating disk (c = 1)")
    t, r, ph, z = symbols("t r phi z", positive=True)
    w = symbols("omega", positive=True)
    c4 = (t, r, ph, z)
    g = sp.diag(-1, 1, r**2, 1)
    X = [1, 0, w, 0]
    gx = g * Matrix(X)
    s = (Matrix(X).T * gx)[0]
    al = Form(c4, {(i,): gx[i] / s for i in range(4)})
    Pi = lambda p: p - wed(al, iv(X, p))
    dal = ext(al)
    check("alpha X = 1 for the metric clock", sp.simplify(iv(X, al).d.get((), 0) - 1) == 0)
    print("        alpha ^ d alpha =", {k: sp.factor(v) for k, v in wed(al, dal).d.items()})
    check("MF9: alpha ^ d alpha != 0, so no factor differential (3.1.12)", not wed(al, dal).zero())
    psi = ph - w * t
    check("r, z, psi = phi - omega t are conserved", all(iv(X, dfun(c4, q)).zero() for q in (r, z, psi)))
    beta = (r**2 * sp.sin(psi) * sp.exp(z)) * dfun(c4, psi)
    check("a basic form: ev_X = 0, ev_X d = 0, and d of it is basic, with no clock used",
          iv(X, beta).zero() and iv(X, ext(beta)).zero() and iv(X, ext(ext(beta))).zero())
    check("t lies in ker ev_X at grade 0, by (3.1.7), and X t = 1, so t is not conserved",
          iv(X, Form(c4, {(): t})).zero() and sp.simplify(iv(X, dfun(c4, t)).d[()] - 1) == 0)
    f = sp.Function("f")(t, r, ph, z)
    df = dfun(c4, f)
    xf = iv(X, df).d[()]
    check("MF10: (Pi d)^2 f = -(Xf) Pi d alpha", (Pi(ext(Pi(df))) + xf * Pi(dal)).zero())
    check("MF10: d alpha = Pi d alpha + alpha ^ L_X alpha", (dal - Pi(dal) - wed(al, lie(X, al))).zero())
    alt = dfun(c4, t) - (w * r**2 / (1 - w**2 * r**2)) * dfun(c4, psi)
    check("MF10: alpha = dt - w r^2/(1 - w^2 r^2) dpsi, holonomy 2 pi w r^2/(1 - w^2 r^2)", (al - alt).zero())

    # Unit vector, its clock; the Sagnac value
    gam = 1 / sp.sqrt(1 - w**2 * r**2)
    u = [gam, 0, gam * w, 0]
    gu = g * Matrix(u)
    alu = Form(c4, {(i,): -gu[i] for i in range(4)})
    # On a circle of constant r the proper-time connection is d tau - gamma w r^2 dpsi
    coeff = sp.simplify(alu.d[(2,)])
    print("        alpha_u component on dphi =", coeff)
    hol_u = 2 * sp.pi * gam * w * r**2
    check("twice the proper-time holonomy is the Sagnac value 4 pi r^2 w gamma",
          sp.simplify(2 * hol_u - 4 * sp.pi * r**2 * w * gam) == 0
          and sp.simplify(coeff + gam * w * r**2) == 0)

    # One-body acceleration without Christoffel
    ginv = g.inv()
    gamma = lambda a, b, c: sum(ginv[a, d] * (sp.diff(g[d, b], c4[c]) + sp.diff(g[d, c], c4[b]) - sp.diff(g[b, c], c4[d]))
                                for d in range(4)) / 2
    acc = [sum(u[b] * sp.diff(u[a], c4[b]) for b in range(4))
           + sum(gamma(a, b, c) * u[b] * u[c] for b in range(4) for c in range(4)) for a in range(4)]
    low = g * Matrix(acc)
    la = lie(u, alu)
    check("MF10: L_u alpha = -a, with a = nabla_u u computed from Christoffel symbols",
          all(sp.simplify(la.d.get((i,), 0) + low[i]) == 0 for i in range(4)))
    print("        a_r =", sp.simplify(acc[1]))
    check("MF10: on the disk L_X alpha = 0 for the Killing X, and L_u alpha_u = Pi d ln gamma for the unit u",
          lie(X, al).zero() and (la - Pi(dfun(c4, sp.log(gam)))).zero())

    # The clock dt on the disk
    dt = dfun(c4, t)
    check("MF11: dt is a clock of X (X t = 1) and is closed", sp.simplify(iv(X, dt).d[()] - 1) == 0 and ext(dt).zero())
    clk = (1 / gam) * dt
    check("MF11: (u, dt/gamma) is a body, integrable, alpha ^ d alpha = 0",
          sp.simplify(iv(u, clk).d[()] - 1) == 0 and wed(clk, ext(clk)).zero())
    T = [1, 0, 0, 0]
    g_ut, g_tu = iv(T, clk).d[()], iv(u, dt).d[()]
    check("MF11: with T = d/dt and clock dt, Gamma_uT = 1/gamma, Gamma_Tu = gamma: not reciprocal",
          sp.simplify(g_ut - 1 / gam) == 0 and sp.simplify(g_tu - gam) == 0)
    # Time scalars of the metric clock
    k = sp.simplify(al.d[(2,)] / al.d[(0,)])
    print("        d f ^ alpha = 0 needs f_r = f_z = 0, f_phi = k f_t, k =", k)
    check("MF11: dk/dr != 0, so f_t = 0, and only constants have df ^ alpha = 0", sp.simplify(sp.diff(k, r)) != 0)

    # General pair, adopted coordinates
    c0 = symbols("t x y z")
    a = [sp.Function(f"a{i}")(*c0) for i in (1, 2, 3)]
    Xg = [1, 0, 0, 0]
    ag = Form(c0, {(0,): 1, (1,): a[0], (2,): a[1], (3,): a[2]})
    ff = sp.Function("f", positive=True)(*c0)
    fX = [ff, 0, 0, 0]
    ag2 = (1 / ff) * ag
    pig = lambda p: p - wed(ag, iv(Xg, p))
    check("MF10: L_{fX}(alpha/f) = L_X alpha + Pi d ln f",
          (lie(fX, ag2) - lie(Xg, ag) - pig(dfun(c0, sp.log(ff)))).zero())
    check("MF10: Pi d(alpha/f) = (1/f) Pi d alpha, and alpha ^ d alpha only scales",
          (pig(ext(ag2)) - (1 / ff) * pig(ext(ag))).zero()
          and (wed(ag2, ext(ag2)) - (1 / ff**2) * wed(ag, ext(ag))).zero())

    # Relative acceleration
    ta, xi, y1, z1 = symbols("tau xi y z", positive=True)
    c1 = (ta, xi, y1, z1)
    X1 = [1 / xi, 0, 0, 0]
    a1 = Form(c1, {(0,): xi})
    sf = sp.Function("s")(ta, xi)
    v1 = [0, sf, 0, 0]
    br = [sum(X1[j] * sp.diff(v1[i], c1[j]) - v1[j] * sp.diff(X1[i], c1[j]) for j in range(4)) for i in range(4)]
    val = sum(a1.d.get((i,), 0) * br[i] for i in range(4))
    da1 = ext(a1)
    rhs = -sum(da1.d.get(kk, 0) * (X1[kk[0]] * v1[kk[1]] - X1[kk[1]] * v1[kk[0]]) for kk in da1.d)
    check("MF10: alpha(L_X v) = -d alpha(X, v) for v in ker alpha", sp.simplify(val - rhs) == 0)
    print("        on Rindler, alpha(L_X v) =", sp.simplify(val), "for v = s d/dxi")

    # The identity quoted in MF-SP1
    x, y, Om = symbols("x y Omega", real=True)
    rho = sp.exp(-(x**2 + y**2))
    px, py = -Om * y * rho, Om * x * rho
    S = sp.integrate(sp.integrate(x * py - y * px, (x, -sp.oo, sp.oo)), (y, -sp.oo, sp.oo))
    cu = sp.diff(py, x) - sp.diff(px, y)
    Q = sp.integrate(sp.integrate((x**2 + y**2) * cu, (x, -sp.oo, sp.oo)), (y, -sp.oo, sp.oo))
    print("        Gaussian rotor: S =", sp.simplify(S), " -(1/2) int r^2 curl p =", sp.simplify(-Q / 2))
    check("MF-SP1 pointer: S = -(1/2) int r^2 curl p on a Gaussian rotor", sp.simplify(S + Q / 2) == 0)


def part_i():
    print("\nPart I: figure (numerical)")
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    import numpy as np

    from ozlib.utils import docs_path, output_path

    teal, coral, ink = "#0F6E56", "#D85A30", "#3D3D3A"
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.8), sharex=True, sharey=True)
    s = np.linspace(-1.25, 1.25, 241)
    surfaces = [
        ("Galilei: flat", "every $\\Gamma=1$", lambda p: np.array([p, 1.0 + 0 * p]), lambda p: (1.0, 0.0)),
        ("Lorentz: curves away", "$\\Gamma\\geq 1$", lambda p: np.array([np.sinh(p), np.cosh(p)]),
         lambda p: (np.cosh(p), np.sinh(p))),
        ("Euclid: curves towards", "$\\Gamma\\leq 1$", lambda p: np.array([np.sin(p), np.cos(p)]),
         lambda p: (np.cos(p), -np.sin(p))),
    ]
    px, py = 0.55, 0.0
    bils = [lambda a, b: a[1] * b[1], lambda a, b: a[1] * b[1] - a[0] * b[0], lambda a, b: a[1] * b[1] + a[0] * b[0]]
    for ax, (title, sub, curve, tang), bil in zip(axes, surfaces, bils):
        c = curve(s)
        ax.plot(c[0], c[1], color=teal, lw=2)
        xp, yp = curve(np.array(px)), curve(np.array(py))
        gam = bil(xp, yp)
        print(f"        {title}: Gamma_XY = {float(gam):.6f}")
        dx, dy = tang(px)
        ax.plot([xp[0] - 1.1 * dx, xp[0] + 0.9 * dx], [xp[1] - 1.1 * dy, xp[1] + 0.9 * dy], color=coral, lw=1.5, ls="--")
        for pt, lab in ((xp, "$X$"), (yp, "$Y$")):
            ax.annotate("", xy=pt, xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=ink, lw=1.2))
            off = (-14, -14) if (lab == "$Y$" and title.startswith("Euclid")) else (4, 6)
            ax.annotate(lab, xy=pt, xytext=off, textcoords="offset points", color=ink)
        ax.plot([0], [0], "o", color=ink, ms=3)
        ax.set_title(title, fontsize=12)
        ax.set_xlabel(sub, fontsize=11)
        ax.set_xlim(-1.7, 1.9)
        ax.set_ylim(-0.1, 2.0)
        ax.set_aspect("equal")
        ax.set_xticks([])
        ax.set_yticks([])
        for sp_ in ax.spines.values():
            sp_.set_visible(False)
    fig.tight_layout()
    fig.savefig(output_path("metric_free_unit_surfaces.png"), dpi=150, bbox_inches="tight")
    dp = docs_path("metric_free_unit_surfaces.png")
    if dp:
        fig.savefig(dp, dpi=150, bbox_inches="tight")


if __name__ == "__main__":
    g4_ = part_a()
    part_b()
    part_c(g4_)
    part_d()
    part_e()
    part_f()
    part_g()
    part_h()
    part_i()
    print()
    if FAILED:
        print(f"{len(FAILED)} CHECKS FAILED:")
        for name_ in FAILED:
            print("  " + name_)
        raise SystemExit(1)
    print("ALL CHECKS PASSED")
