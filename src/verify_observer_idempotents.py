"""Checks for analysis/observer_idempotents.md (ladder step 5).

The algebra is A = Cl(V, -g), the spacetime algebra G(1,3), with g of signature
(-, +, +, +) as in MC0.  In A a body X has X^2 = -g(X, X) = 1 and X.Y = gamma_XY.
The observer idempotent of X is e_X = (1 + X)/2.  Orthonormal basis gamma_0..gamma_3
with gamma_0^2 = 1, gamma_k^2 = -1.  Elements are dicts {bitmask: coefficient}.

Parts A to F and H are exact (SymPy).  Part G is numerical (NumPy).

Parts
  A  OI1: e_X Y e_X = gamma_XY e_X; the corner e_X A e_X is a quaternion algebra
  B  OI2: e_Y e_X = (1/2)(1 + YX) e_X; the boost intertwines e_X and e_Y
  C  OI3: e_X e_Z e_Y e_X = (1/8) Lambda e_X; Lambda = (1+XZ)(1+ZY)(1+YX) fixes X;
         its scalar, bivector and norm; the open product
  D  OI3 on step 2's example: cos = 25109/29341 (TV7); OI3 equals Aravind's eq. (2)
  E  OI4: corners are 4-dimensional; inverses; the boost section fails to compose by H;
         OI3 (6): a non-planar quadrilateral, triangulation, non-commuting rotations
  F  OI5: rank-one projectors have 1-dimensional corners; Cl(V, g) has no e_X
  G  numerical: 500 random triples, angle of H = area; 200 random pentagons;
         the boost is parallel transport on rest spaces
  H  the dictionary with Baylis and Sobczyk (2004): L^2 = u_B u_A, the space-time split,
         the observer's conjugation, the polar decomposition L = B R

Run:  PYTHONPATH=src python3 -u src/verify_observer_idempotents.py
"""

from __future__ import annotations

import itertools

import numpy as np
import sympy as sp
from sympy import Rational as R

FAILED: list[str] = []


def check(name: str, condition) -> None:
    good = bool(condition)
    print(("  ok    " if good else "  FAIL  ") + name, flush=True)
    if not good:
        FAILED.append(name)


# ---------------------------------------------------------------- G(1,3), exact
SIG = (1, -1, -1, -1)


def _blade(a: int, b: int):
    """product of basis blades a, b (bitmasks): (sign, mask)"""
    s, x = 1, a >> 1
    while x:                                   # reordering sign
        if bin(x & b).count("1") % 2:
            s = -s
        x >>= 1
    for i in range(4):                         # metric on repeated generators
        if (a & b) >> i & 1:
            s *= SIG[i]
    return s, a ^ b


TABLE = {(a, b): _blade(a, b) for a in range(16) for b in range(16)}


def clean(x):
    return {k: v for k, v in ((k, sp.expand(v)) for k, v in x.items()) if v != 0}


def mul(*xs):
    out = xs[0]
    for y in xs[1:]:
        r: dict = {}
        for a, ca in out.items():
            for b, cb in y.items():
                s, m = TABLE[a, b]
                r[m] = r.get(m, 0) + s * ca * cb
        out = clean(r)
    return out


def add(*xs):
    r: dict = {}
    for x in xs:
        for k, v in x.items():
            r[k] = r.get(k, 0) + v
    return clean(r)


def sm(c, x):
    return clean({k: c * v for k, v in x.items()})


def sub(x, y):
    return add(x, sm(-1, y))


def one():
    return {0: sp.Integer(1)}


def vec(c):
    return clean({1 << i: sp.sympify(c[i]) for i in range(4)})


def grade(x, k):
    return {m: v for m, v in x.items() if bin(m).count("1") == k}


def rev(x):
    return {m: (v if bin(m).count("1") % 4 in (0, 1) else -v) for m, v in x.items()}


def e(X):
    return sm(R(1, 2), add(one(), X))


def dot(X, Y):
    return sp.expand(sum(SIG[i] * X.get(1 << i, 0) * Y.get(1 << i, 0) for i in range(4)))


def is_zero(x, red=lambda v: v):
    return all(sp.expand(red(v)) == 0 for v in x.values())


# symbolic bodies on the hyperboloid: X0^2 = 1 + X1^2 + X2^2 + X3^2
Xs, Ys, Zs = (sp.symbols(f"{n}0:4") for n in "XYZ")
HYP = {s[0]: 1 + s[1] ** 2 + s[2] ** 2 + s[3] ** 2 for s in (Xs, Ys, Zs)}


def red(v):
    """reduce a polynomial modulo X0^2 = 1 + |X|^2 and the same for Y0, Z0"""
    v = sp.expand(v)
    if v == 0:
        return v
    lead = [s[0] for s in (Xs, Ys, Zs)]
    P = sp.Poly(v, *lead)
    out = 0
    for (a, b, c), coeff in P.terms():
        t = coeff
        for s, k in zip(lead, (a, b, c)):
            t *= s ** (k % 2) * HYP[s] ** (k // 2)
        out += t
    return sp.expand(out)


def rational_body(vx, vy, vz=0):
    v2 = R(vx) ** 2 + R(vy) ** 2 + R(vz) ** 2
    gam = 1 / sp.sqrt(1 - v2)
    assert gam.is_rational, "choose velocities with rational gamma"
    return vec([gam, gam * R(vx), gam * R(vy), gam * R(vz)])


def span_rank(elems):
    M = sp.Matrix([[x.get(m, 0) for m in range(16)] for x in elems])
    return M.rank()


BASIS = [{m: sp.Integer(1)} for m in range(16)]


# ---------------------------------------------------------------- parts
def part_a():
    print("\nPart A: OI1, the lemma and the corner of one body")
    X, Y = vec(sp.symbols("x0:4")), vec(sp.symbols("y0:4"))
    lhs = mul(e(X), Y, e(X))
    rem = sm(R(1, 4), mul(Y, sub(one(), mul(X, X))))
    check("e_X Y e_X = (X.Y) e_X + (1/4) Y (1 - X^2), symbolic, no constraint",
          is_zero(sub(lhs, add(sm(dot(X, Y), e(X)), rem))))
    check("e_X^2 = e_X + (1/4)(X^2 - 1), so e_X is idempotent exactly when X^2 = 1",
          is_zero(sub(mul(e(X), e(X)), add(e(X), sm(R(1, 4), sub(mul(X, X), one()))))))
    g0 = vec([1, 0, 0, 0])
    e0 = e(g0)
    corner = [mul(e0, b, e0) for b in BASIS]
    check("dim e_X A e_X = 4 for X = gamma_0", span_rank(corner) == 4)
    i, j, k = (mul({m: sp.Integer(1)}, e0) for m in (0b1100, 0b1010, 0b0110))   # g23, g13, g12
    check("its basis e, g23 e, g31 e, g12 e multiplies as the quaternions (i^2 = j^2 = k^2 = ijk = -e)",
          all(is_zero(add(mul(q, q), e0)) for q in (i, j, k))
          and is_zero(add(mul(i, sm(-1, j), k), e0)))
    X = rational_body(R(3, 5), 0)
    eX = e(X)
    check("dim e_X A e_X = 4 for the rational body X = (5/4)(1, 3/5, 0, 0)",
          span_rank([mul(eX, b, eX) for b in BASIS]) == 4)
    check("e_X is primitive: dim A e_X = 8 = 16/2 (minimal left ideal of M2(H))",
          span_rank([mul(b, eX) for b in BASIS]) == 8)


def part_b():
    print("\nPart B: OI2, two bodies")
    X, Y = vec(sp.symbols("x0:4")), vec(sp.symbols("y0:4"))
    rem = sm(R(1, 4), mul(Y, sub(one(), mul(X, X))))
    check("e_Y e_X = (1/2)(1 + YX) e_X + (1/4) Y (1 - X^2), symbolic",
          is_zero(sub(mul(e(Y), e(X)), add(sm(R(1, 2), mul(add(one(), mul(Y, X)), e(X))), rem))))
    lhs = sub(mul(add(one(), mul(Y, X)), e(X)), mul(e(Y), add(one(), mul(Y, X))))
    rhs = sm(R(1, 2), sub(mul(Y, sub(mul(X, X), one())), mul(sub(mul(Y, Y), one()), X)))
    check("(1 + YX) e_X - e_Y (1 + YX) = (1/2)[Y (X^2 - 1) - (Y^2 - 1) X]: intertwining on the hyperboloid",
          is_zero(sub(lhs, rhs)))
    X, Y = vec(Xs), vec(Ys)
    nrm = mul(add(one(), mul(Y, X)), add(one(), mul(X, Y)))
    check("(1 + YX)(1 + XY) = 2 (1 + gamma_XY) on the hyperboloid",
          is_zero(sub(nrm, sm(2 * (1 + dot(X, Y)), one())), red))
    check("e_Y e_X = (1/2)(X + Y) e_X: the bisector, Urbantke's second reflection (on the hyperboloid)",
          is_zero(sub(mul(e(Y), e(X)), sm(R(1, 2), mul(add(X, Y), e(X)))), red))
    check("1 + YX = (X + Y) X on the hyperboloid: the boost as the product of two reflections",
          is_zero(sub(add(one(), mul(Y, X)), mul(add(X, Y), X)), red))
    v = sub(sm(1, Y), sm(dot(X, Y), X))                    # gamma v_XY = Y - gamma X
    check("gamma v_XY = Y - gamma X is orthogonal to X; e_Y e_X = (1/2)(1 + gamma) e_X + (1/2) gamma v_XY e_X",
          red(dot(v, X)) == 0
          and is_zero(sub(mul(e(Y), e(X)), add(sm(R(1, 2) * (1 + dot(X, Y)), e(X)), sm(R(1, 2), mul(v, e(X))))), red))


def part_c():
    print("\nPart C: OI3, three bodies (symbolic, on the hyperboloid)")
    X, Y, Z = vec(Xs), vec(Ys), vec(Zs)
    x, y, z = dot(X, Y), dot(Y, Z), dot(Z, X)
    Lam = mul(add(one(), mul(X, Z)), add(one(), mul(Z, Y)), add(one(), mul(Y, X)))
    loop = mul(e(X), e(Z), e(Y), e(X))
    check("e_X e_Z e_Y e_X = (1/8) Lambda e_X", is_zero(sub(loop, sm(R(1, 8), mul(Lam, e(X)))), red))
    check("Lambda X = X Lambda (the loop fixes X)", is_zero(sub(mul(Lam, X), mul(X, Lam)), red))
    check("Lambda has grades 0 and 2 only",
          all(is_zero(grade(Lam, k), red) for k in (1, 3, 4)))
    check("<Lambda>_0 = 2 (1 + gamma_XY + gamma_YZ + gamma_ZX)",
          red(Lam.get(0, 0) - 2 * (1 + x + y + z)) == 0)
    G = sp.Matrix([[1, x, z], [x, 1, y], [z, y, 1]])
    B2 = grade(Lam, 2)
    check("<Lambda>_2^2 = -4 det G, G = [gamma_ij] (TV8's polynomial)",
          is_zero(sub(mul(B2, B2), sm(-4 * G.det(), one())), red))
    check("<Lambda>_2 is a rotation of X's rest space: it commutes with X",
          is_zero(sub(mul(B2, X), mul(X, B2)), red))
    ZwY = grade(mul(Z, Y), 2)
    check("<Lambda>_2 = Z^Y + X (Z^Y) X: twice the rest-space part of Z^Y relative to X",
          is_zero(sub(B2, add(ZwY, mul(X, ZwY, X))), red))
    check("Lambda rev(Lambda) = 8 (1 + gamma_XY)(1 + gamma_YZ)(1 + gamma_ZX)",
          is_zero(sub(mul(Lam, rev(Lam)), sm(8 * (1 + x) * (1 + y) * (1 + z), one())), red))
    opn = mul(e(Z), e(Y), e(X))
    check("open product: 8 (1 + gamma_ZX) e_Z e_Y e_X = (1 + ZX) Lambda e_X",
          is_zero(sub(sm(8 * (1 + z), opn), mul(add(one(), mul(Z, X)), Lam, e(X))), red))
    rloop = mul(e(X), e(Y), e(Z), e(X))
    check("reverse loop: e_X e_Y e_Z e_X = (1/8) rev(Lambda) e_X; same scalar part",
          is_zero(sub(rloop, sm(R(1, 8), mul(rev(Lam), e(X)))), red))


def part_d():
    print("\nPart D: OI3 on step 2's example (S, B, C of TV7)")
    S, B, C = rational_body(R(3, 5), 0), rational_body(0, R(4, 5)), rational_body(R(-3, 13), R(-4, 13))
    x, y, z = dot(S, B), dot(B, C), dot(C, S)
    print(f"        gamma_SB = {x}, gamma_BC = {y}, gamma_CS = {z}")
    loop = mul(e(S), e(C), e(B), e(S))           # round S -> B -> C -> S
    s0 = loop.get(0, 0)
    k2 = (1 + x) * (1 + y) * (1 + z) / 8         # (product of cosh(r/2))^2
    cos_half = 2 * s0 / sp.sqrt(k2)
    cos_full = sp.nsimplify(2 * cos_half ** 2 - 1)
    print(f"        <e_S e_C e_B e_S>_0 = {s0}, cos(theta) = {cos_full}, theta = {float(sp.acos(cos_full)) * 180 / np.pi:.2f} deg")
    check("<loop>_0 = (1 + x + y + z)/8 = 55/64", s0 == R(55, 64))
    check("cos(theta) = 25109/29341, TV7's binary-boost rotation", cos_full == R(25109, 29341))
    G = sp.Matrix([[1, x, z], [x, 1, y], [z, y, 1]])
    tan_half = sp.sqrt(G.det()) / (1 + x + y + z)
    check("tan(theta/2) = sqrt(det G)/(1 + x + y + z) gives the same angle",
          sp.simplify((1 - tan_half ** 2) / (1 + tan_half ** 2) - cos_full) == 0)

    # Aravind (1997): sides eta = r_XY, lambda = r_YZ, angle at Y = pi - phi; his eqs. (2), (3).
    # c_i, s_i = cosh, sinh of the half rapidities; reduce with s^2 = c^2 - 1, sin^2 = 1 - cos^2.
    c1, s1, c2, s2, cp, sn = sp.symbols("c1 s1 c2 s2 cphi sphi")

    def red2(v):
        P = sp.Poly(sp.expand(v), s1, s2, sn)
        out = 0
        for (i, j, k), co in P.terms():
            out += (co * s1 ** (i % 2) * (c1 ** 2 - 1) ** (i // 2) * s2 ** (j % 2) * (c2 ** 2 - 1) ** (j // 2)
                    * sn ** (k % 2) * (1 - cp ** 2) ** (k // 2))
        return sp.expand(out)

    x, y = c1 ** 2 + s1 ** 2, c2 ** 2 + s2 ** 2                        # cosh eta, cosh lambda
    she, shl = 2 * s1 * c1, 2 * s2 * c2
    z = x * y + cp * shl * she                                          # Aravind (3), the cosh rule
    detG = 1 + 2 * x * y * z - x ** 2 - y ** 2 - z ** 2
    den = c1 * c2 + cp * s1 * s2
    check("1 + x + y + z = 4 cosh(eta/2) cosh(lambda/2) [cosh cosh + cos(phi) sinh sinh] (exact)",
          red2(1 + x + y + z - 4 * c1 * c2 * den) == 0)
    check("det G = (sinh eta sinh lambda sin phi)^2 (exact)", red2(detG - (she * shl * sn) ** 2) == 0)
    check("OI3's tan(theta/2) = |Aravind (2)| = sin(phi) sinh sinh/(cosh cosh + cos(phi) sinh sinh) (exact)",
          red2(detG * den ** 2 - (sn * s1 * s2) ** 2 * (1 + x + y + z) ** 2) == 0)


def part_e():
    print("\nPart E: OI4, corners and the orientation groupoid")
    X, Y, Z = rational_body(R(3, 5), 0), rational_body(0, R(4, 5)), rational_body(R(-3, 13), R(-4, 13))
    eX, eY = e(X), e(Y)
    hom = [mul(eY, b, eX) for b in BASIS]
    check("dim e_Y A e_X = 4, so Oziewicz's postulate (8) (every corner spanned by qp) fails in A",
          span_rank(hom) == 4)
    gen = [mul(eY, eX, mul(eX, b, eX)) for b in BASIS]
    check("e_Y A e_X = e_Y e_X (e_X A e_X): free of rank 1 over the quaternions of X",
          span_rank(gen) == 4 and span_rank(hom + gen) == 4)
    # inverse of L_YX Q e_X, X = gamma_0, Q a rational quaternion of X's rest space
    g0 = vec([1, 0, 0, 0])
    a, b_, c, d = R(1), R(2), R(-1), R(3)
    Q = add(sm(a, one()), sm(b_, {0b1100: 1}), sm(c, {0b1010: 1}), sm(d, {0b0110: 1}))
    QQ = mul(rev(Q), Q).get(0, 0)
    u = mul(add(one(), mul(Y, g0)), Q, e(g0))                  # unnormalised arrow X -> Y
    ubar = mul(rev(Q), add(one(), mul(g0, Y)), eY)             # candidate inverse Y -> X
    check("Q commutes with e_X", is_zero(sub(mul(Q, e(g0)), mul(e(g0), Q))))
    check("(rev Q (1 + XY) e_Y)(L Q e_X) = 2 (1 + gamma) |Q|^2 e_X: every arrow has an inverse",
          is_zero(sub(mul(ubar, u), sm(2 * (1 + dot(g0, Y)) * QQ, e(g0)))))
    check("and it lies in e_X A e_Y", is_zero(sub(mul(e(g0), ubar, eY), ubar)))
    # the boost section s(Y<-X) = (1 + YX) e_X fails to compose by Lambda (exact, rational)
    lhs = mul(add(one(), mul(Z, Y)), add(one(), mul(Y, X)), eX)
    Lam = mul(add(one(), mul(X, Z)), add(one(), mul(Z, Y)), add(one(), mul(Y, X)))
    rhs = sm(1 / (2 * (1 + dot(X, Z))), mul(add(one(), mul(Z, X)), Lam, eX))
    check("s(Z<-Y) s(Y<-X) = s(Z<-X) Lambda / (2 (1 + gamma_XZ)): the defect is the Wigner rotation",
          is_zero(sub(lhs, rhs)))
    check("Lambda is not a scalar for this triangle (the rotation is not trivial)", grade(Lam, 2) != {})

    # OI3 (6): a non-planar quadrilateral S -> B -> C -> D -> S
    S, B, C, D = X, Y, Z, rational_body(0, 0, R(12, 13))
    lam = lambda P, Q: add(one(), mul(P, Q))                    # unnormalised boost Q -> P
    Lam4 = mul(lam(S, D), lam(D, C), lam(C, B), lam(B, S))
    loop4 = mul(e(S), e(D), e(C), e(B), e(S))
    check("quadrilateral: e_S e_D e_C e_B e_S = (1/16) Lambda_4 e_S, Lambda_4 the path-ordered product",
          is_zero(sub(loop4, sm(R(1, 16), mul(Lam4, e(S))))))
    check("Lambda_4 commutes with S (a rotation of S's rest space)", is_zero(sub(mul(Lam4, S), mul(S, Lam4))))
    gSC = dot(S, C)
    check("a diagonal costs a scalar: e_C e_S e_C = (1/2)(1 + gamma_SC) e_C", is_zero(sub(mul(e(C), e(S), e(C)), sm((1 + gSC) / 2, e(C)))))
    check("so (e_S e_D e_C e_S)(e_S e_C e_B e_S) = (1/2)(1 + gamma_SC) e_S e_D e_C e_B e_S",
          is_zero(sub(mul(e(S), e(D), e(C), e(S), e(C), e(B), e(S)), sm((1 + gSC) / 2, loop4))))
    LSCD = mul(lam(S, D), lam(D, C), lam(C, S))
    LSBC = mul(lam(S, C), lam(C, B), lam(B, S))
    check("Lambda_SCD Lambda_SBC = 2 (1 + gamma_SC) Lambda_4: the quadrilateral's rotation is the product of its triangles'",
          is_zero(sub(mul(LSCD, LSBC), sm(2 * (1 + gSC), Lam4))))
    check("the two triangle rotations do not commute (non-planar: they add as rotations, not as areas)",
          not is_zero(sub(mul(LSCD, LSBC), mul(LSBC, LSCD))))


def part_f():
    print("\nPart F: OI5, the contrast")
    eta = sp.diag(-1, 1, 1, 1)
    bodies = [sp.Matrix([R(5, 4), R(3, 4), 0, 0]), sp.Matrix([R(5, 3), 0, R(4, 3), 0]),
              sp.Matrix([R(13, 12), R(-1, 4), R(-1, 3), 0])]
    proj = [Xv * (-(eta * Xv)).T for Xv in bodies]           # p = X (x) clock_X, clock_X = -g(X, .)
    check("each p = X (x) clock_X is a rank-one idempotent of End(V)",
          all(p * p == p and p.rank() == 1 for p in proj))
    units = [sp.Matrix(4, 4, lambda r, s: 1 if (r, s) == (i, j) else 0) for i in range(4) for j in range(4)]
    corner = sp.Matrix([list(proj[1] * u * proj[0]) for u in units])
    check("dim p_Y End(V) p_X = 1: only a scalar per pair, no room for a rotation", corner.rank() == 1)
    t1 = (proj[0] * proj[1] * proj[2]).trace()
    t2 = (proj[0] * proj[2] * proj[1]).trace()
    check("tr(pqr) = tr(qpr) = gamma_12 gamma_23 gamma_31 for metric observers: the loop is a real number",
          t1 == t2 and t1 == R(25, 12) * R(9, 4) * R(37, 24))
    # Cl(V, g): a body squares to -1
    global SIG
    saved = SIG
    SIG = (-1, 1, 1, 1)
    TABLE.clear()
    TABLE.update({(a, b): _blade(a, b) for a in range(16) for b in range(16)})
    X = vec([R(5, 4), R(3, 4), 0, 0])
    check("in Cl(V, g) = G(3,1), X^2 = -1, so (1 + X)/2 is not idempotent",
          mul(X, X) == {0: -1} and not is_zero(sub(mul(e(X), e(X)), e(X))))
    SIG = saved
    TABLE.clear()
    TABLE.update({(a, b): _blade(a, b) for a in range(16) for b in range(16)})


def part_g():
    print("\nPart G: numerical, 500 random triples (NumPy, Dirac matrices)")
    rng = np.random.default_rng(1)
    I2, Z2 = np.eye(2), np.zeros((2, 2))
    sig = [np.array([[0, 1], [1, 0]]), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]])]
    gm = [np.block([[I2, Z2], [Z2, -I2]]).astype(complex)] + [np.block([[Z2, s], [-s, Z2]]) for s in sig]
    I4 = np.eye(4)

    def v_(x):
        return sum(x[m] * gm[m] for m in range(4))

    def sp0(M):
        return np.trace(M).real / 4

    def body():
        u = rng.normal(size=3)
        u *= 0.95 * rng.random() / np.linalg.norm(u)
        gam = 1 / np.sqrt(1 - u @ u)
        return v_(np.r_[gam, gam * u])

    def boost(b, a):
        return (I4 + b @ a) / np.sqrt(2 * (1 + sp0(a @ b)))

    def ang(a, b, c):
        tb, tc = b - sp0(b @ a) * a, c - sp0(c @ a) * a
        return np.arccos(np.clip(-sp0(tb @ tc) / np.sqrt(sp0(tb @ tb) * sp0(tc @ tc)), -1, 1))

    E = lambda X: (I4 + X) / 2
    e1 = e2 = 0.0
    for _ in range(500):
        p, q, r = body(), body(), body()
        H = boost(p, r) @ boost(r, q) @ boost(q, p)
        k = np.sqrt((1 + sp0(p @ q)) * (1 + sp0(q @ r)) * (1 + sp0(r @ p)) / 8)
        e1 = max(e1, np.abs(E(p) @ E(r) @ E(q) @ E(p) - k * H @ E(p)).max())
        theta = 2 * np.arccos(np.clip(sp0(H), -1, 1))
        e2 = max(e2, abs(theta - (np.pi - ang(p, q, r) - ang(q, r, p) - ang(r, p, q))))
    print(f"        max |loop - k H e_p| = {e1:.1e};  max |angle(H) - area| = {e2:.1e}")
    check("loop = (prod cosh) H e_p with H the boost holonomy (numerical, 1e-12)", e1 < 1e-12)
    check("angle of H = pi - (A + B + C), the area of the triangle (numerical, 1e-10)", e2 < 1e-10)

    e3 = 0.0
    for _ in range(200):                                        # random skew pentagons
        P = [body() for _ in range(5)]
        Hp, k, M = I4, 1.0, E(P[0])
        for a, b in zip(P, P[1:] + P[:1]):                      # P0 -> P1 -> ... -> P4 -> P0
            Hp = boost(b, a) @ Hp
            k *= np.sqrt((1 + sp0(a @ b)) / 2)
        for Q in P[1:] + P[:1]:
            M = E(Q) @ M
        e3 = max(e3, np.abs(M - k * Hp @ E(P[0])).max())
    print(f"        pentagons: max |loop - k H e_p| = {e3:.1e}")
    check("polygon loops: product of idempotents = weights times path-ordered boost holonomy (numerical, 1e-12)", e3 < 1e-12)

    # section 6.1: on rest spaces the boost is Levi-Civita transport along the geodesic of H
    eta = np.diag([1.0, -1, -1, -1])
    dt = lambda a, b: a @ eta @ b

    rng2 = np.random.default_rng(3)                             # own generator: independent of the checks above

    def b4():
        u = rng2.normal(size=3)
        u *= 0.9 * rng.random() / np.linalg.norm(u)
        gam = 1 / np.sqrt(1 - u @ u)
        return np.r_[gam, gam * u]

    X, Y = b4(), b4()
    gXY = dt(X, Y)
    Lm = np.eye(4) - np.outer(X + Y, X + Y) @ eta / (1 + gXY) + 2 * np.outer(Y, X) @ eta
    r = np.arccosh(gXY)
    U = (Y - gXY * X) / np.sinh(r)
    w = rng2.normal(size=4)
    w -= dt(w, X) * X
    errs = []
    for N in (1000, 10000):
        v = w.copy()
        for k in range(1, N + 1):
            P = np.cosh(r * k / N) * X + np.sinh(r * k / N) * U
            v = v - dt(v, P) * P
        errs.append(np.abs(v - Lm @ w).max())
    print(f"        transport by projection: error {errs[0]:.1e} (N = 1000), {errs[1]:.1e} (N = 10000)")
    check("the boost L_YX on rest spaces is parallel transport along the geodesic (numerical, error ~ 1/N)",
          np.allclose(Lm @ X, Y) and np.allclose(Lm.T @ eta @ Lm, eta)
          and errs[1] < 1e-4 and 8 < errs[0] / errs[1] < 12)


def part_h():
    print("\nPart H: the dictionary with Baylis and Sobczyk (2004)")
    X, Y = vec(Xs), vec(Ys)
    YX, gXY = mul(Y, X), dot(X, Y)
    check("(1 + YX)^2 = 2 (1 + gamma) YX, so L_YX^2 = YX = u_Y u_X (BS eq. (24))",
          is_zero(sub(mul(add(one(), YX), add(one(), YX)), sm(2 * (1 + gXY), YX)), red))
    check("e_X (Y ^ X) e_X = 0: the sandwich keeps the time part of the space-time split (BS eqs. (26)-(27))",
          is_zero(mul(e(X), grade(YX, 2), e(X)), red))

    def dag(K, P):                                              # BS eq. (22): K^{dagger P} = P rev(K) P
        return mul(P, rev(K), P)

    ks = sp.symbols("k0:8")
    even = [m for m in range(16) if bin(m).count("1") % 2 == 0]
    K = clean({m: ks[i] for i, m in enumerate(even)})
    comm = sm(R(1, 2), add(K, mul(X, K, X)))                    # part of K commuting with X
    check("even K: e_X K e_X = (1/2)(K + X K X) e_X, the part of K that commutes with X",
          is_zero(sub(mul(e(X), K, e(X)), mul(comm, e(X))), red))
    check("that part has no pseudoscalar, and its real part for X is the scalar alone (scalar + rest bivectors)",
          is_zero(grade(comm, 4), red)
          and is_zero(sub(sm(R(1, 2), add(comm, dag(comm, X))), {0: ks[0]}), red))
    # polar decomposition relative to S (BS section II and eq. (23)), exact rationals
    S, Bb, C = rational_body(R(3, 5), 0), rational_body(0, R(4, 5)), rational_body(R(-3, 13), R(-4, 13))
    lam = lambda P, Q: add(one(), mul(P, Q))
    L = mul(lam(C, Bb), lam(Bb, S))                             # unnormalised L_CB L_BS
    Bm = lam(C, S)                                              # unnormalised boost S -> C
    Lam = mul(lam(S, C), lam(C, Bb), lam(Bb, S))                # unnormalised Wigner rotor at S
    nL = 4 * (1 + dot(C, Bb)) * (1 + dot(Bb, S))
    check("L L^{dagger S} = |L|^2 C S: BS eq. (23), L L^{dagger A} = u_B u_A", is_zero(sub(mul(L, dag(L, S)), sm(nL, mul(C, S)))))
    check("the boost factor is hermitian for S: (1 + CS)^{dagger S} = 1 + CS", is_zero(sub(dag(Bm, S), Bm)))
    check("the rotation factor is unitary for S: Lambda^{dagger S} = rev(Lambda), Lambda^{dagger S} Lambda a scalar",
          is_zero(sub(dag(Lam, S), rev(Lam))) and set(mul(dag(Lam, S), Lam)) <= {0})
    check("2 (1 + gamma_SC) L = (1 + CS) Lambda: OI3 (5) is the polar decomposition L = B R relative to S",
          is_zero(sub(sm(2 * (1 + dot(S, C)), L), mul(Bm, Lam))))


if __name__ == "__main__":
    for part in (part_a, part_b, part_c, part_d, part_e, part_f, part_g, part_h):
        part()
    if FAILED:
        print(f"\n{len(FAILED)} CHECK(S) FAILED")
        raise SystemExit(1)
    print("\nALL CHECKS PASSED")
