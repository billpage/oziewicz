"""Exact checks for analysis/ternary_mass_centre.md (ladder step 2).

Conventions: signature (-,+,+,+) and c = 1.  A body is a unit time-like vector.
gamma_AB = -A.B.  The binary velocity is v_AB = B/gamma_AB - A.  w(P, A, B) is
the unique vector with P.w = 0 and L_{P^w} A = B (the boost formula of Concepts
of relative velocity, as in verify_relative_velocity.py), and
v(P, A, B) = w / sqrt(1 + w.w) is (2.2) of Ternary relative velocity (2007).

Parts A to G and I are exact (SymPy).  In Part E the comparison of the rotation with
the area of the triangle, and all of Part H, are numerical and say so.

Parts
  A  TV1: for P in the plane of A and B, P^w = A^B, whichever P
  B  TV2: the ternary velocity at the mass centre is (2.2.10)
  C  TV4: the mass centre leaves the plane of every pair
  D  TV5: gamma_AB - 1 = cosh^2 r (gamma_ternary - 1)
  E  TV6, TV7: the triangle; the three ways out; the Galilean contrast
  F  TV8: alpha, the determinant, the Frobenius form
  G  TV9: Todorov's map
  H  figure (numerical)
  I  TV10: the ternary velocity of velocity.pdf (2004) against the boost-link;
     (11.9), (11.10) and (6.5) of that draft; the commutators of idempotents

Run:  PYTHONPATH=src python3 -u src/verify_ternary_mass_centre.py
Writes ternary_mass_centre_velocity_space.png through ozlib.utils.output_path
(and docs_path when OZ_DOCS is set).
"""

from __future__ import annotations

import itertools
import math

import sympy as sp

from verify_relative_velocity import (boost, dot, gamma_24, lift, ternary_22,
                                      zero)

FAILED: list[str] = []
R = sp.Rational


def check(name: str, ok: bool) -> None:
    print(f"  [{'ok' if ok else 'FAIL'}] {name}")
    if not ok:
        FAILED.append(name)


def gam(X, Y, n):
    return -dot(X, Y, n)


def unit(Q, n):
    return (Q / sp.sqrt(-dot(Q, Q, n))).applyfunc(sp.simplify)


def binary_boost(X, Y, n):
    """L_{X^(gamma v_XY)}: the boost in the plane of X and Y taking X to Y."""
    g = gam(X, Y, n)
    return boost(X, Y - g * X, n, gam=g).applyfunc(sp.simplify)


def ternary_boost(P, A, B, n):
    """L_{P^w} with w = w(P, A, B), from (2.2) and (2.4)."""
    g = gamma_24(P, A, B, n)
    w = (ternary_22(P, A, B, n) * g).applyfunc(sp.simplify)
    return boost(P, w, n, gam=g).applyfunc(sp.simplify)


def wedge3(a, b, c):
    """The 3-by-3 minors of [a b c]: all zero iff a ^ b ^ c = 0."""
    M = sp.Matrix.hstack(a, b, c)
    return [sp.simplify(M.extract(list(r), [0, 1, 2]).det())
            for r in itertools.combinations(range(M.rows), 3)]


def rotation_cos(Q):
    """cos of a 2+1 Lorentz matrix that fixes a time-like vector."""
    return sp.nsimplify(sp.simplify((Q.trace() - 1) / 2))


def degrees(cos_value) -> float:
    return math.degrees(math.acos(float(cos_value)))


# The worked example: masses 4, 3, 12, with the mass centre at rest.
S3, B3, C3 = lift([R(3, 5), 0]), lift([0, R(4, 5)]), lift([R(-3, 13), R(-4, 13)])
Z3 = sp.Matrix([1, 0, 0])


# -------------------------------------------------------------------- Part A
def part_a():
    print("A. TV1: an eagle in the plane")
    a, b, x = sp.symbols("a b x", real=True)

    def ip(u, v):                       # inner product in the basis (A, B)
        return -(u[0] * v[0] + u[1] * v[1] + x * (u[0] * v[1] + u[1] * v[0]))

    A, B = (1, 0), (0, 1)
    P = (a, b)
    w = (ip(P, B), -ip(P, A))           # (P.B) A - (P.A) B
    norm = a**2 + b**2 + 2 * a * b * x  # -P.P
    check("P.w = 0", sp.expand(ip(P, w)) == 0)
    check("P ^ w = (-P.P) A ^ B",
          sp.expand(a * w[1] - b * w[0] - norm) == 0)
    check("w.w = (-P.P)(gamma^2 - 1)",
          sp.expand(ip(w, w) - norm * (x**2 - 1)) == 0)

    r, s, t = sp.symbols("r s t", real=True)
    AA = sp.Matrix([sp.cosh(r), sp.sinh(r), 0])
    BB = sp.Matrix([sp.cosh(s), sp.sinh(s), 0])
    PP = sp.Matrix([sp.cosh(t), sp.sinh(t), 0])
    ww = dot(PP, BB, 3) * AA - dot(PP, AA, 3) * BB
    L = boost(PP, ww, 3, gam=sp.cosh(s - r))
    check("L_{P^w} A = B, symbolic rapidities", zero(L * AA - BB))
    check("the same boost for P = A",
          zero(L - boost(AA, BB - sp.cosh(s - r) * AA, 3, gam=sp.cosh(s - r))))


# -------------------------------------------------------------------- Part B
def part_b():
    print("B. TV2: the ternary velocity at the mass centre")
    m1, m2, x, M = sp.symbols("m_A m_B gamma M", positive=True)
    Q = m1**2 + m2**2 + 2 * m1 * m2 * x

    def ip(u, v):
        return -(u[0] * v[0] + u[1] * v[1] + x * (u[0] * v[1] + u[1] * v[0]))

    def vanishes(e):
        return sp.simplify(sp.simplify(e).subs(M, sp.sqrt(Q))) == 0

    A, B = (1, 0), (0, 1)
    Z = (m1 / M, m2 / M)
    gZA, gZB = -ip(Z, A), -ip(Z, B)
    w = (ip(Z, B), -ip(Z, A))
    pZB = (m2 * (B[0] - gZB * Z[0]), m2 * (B[1] - gZB * Z[1]))
    pZA = (m1 * (A[0] - gZA * Z[0]), m1 * (A[1] - gZA * Z[1]))
    vAB, vBA = (-1, 1 / x), (1 / x, -1)
    vZ = ((m1 * vAB[0] - m2 * vBA[0]) / M, (m1 * vAB[1] - m2 * vBA[1]) / M)
    check("Z.Z = -1", vanishes(ip(Z, Z) + 1))
    check("p_ZB = (m_A m_B / M) w",
          all(vanishes(pZB[i] - m1 * m2 / M * w[i]) for i in (0, 1)))
    check("p_ZA = -p_ZB", all(vanishes(pZA[i] + pZB[i]) for i in (0, 1)))
    check("w = gamma (m_A v_AB - m_B v_BA)/M",
          all(vanishes(w[i] - x * vZ[i]) for i in (0, 1)))
    check("p_ZB = mu_AB v(Z,A,B), mu_AB = gamma m_A m_B / M: (2.2.10)",
          all(vanishes(pZB[i] - x * m1 * m2 / M * vZ[i]) for i in (0, 1)))
    check("v(Z,A,B)^2 = 1 - 1/gamma^2 (the 2012 draft's (3.10))",
          vanishes(ip(vZ, vZ) - (1 - 1 / x**2)))

    n = 3
    A3, B3a = lift([R(3, 5), 0]), lift([0, R(4, 5)])
    ma, mb = 4, 3
    Zp = unit(ma * A3 + mb * B3a, n)
    Mp = sp.sqrt(-dot(ma * A3 + mb * B3a, ma * A3 + mb * B3a, n))
    g = gam(A3, B3a, n)
    v22 = ternary_22(Zp, A3, B3a, n).applyfunc(sp.simplify)
    check("(2.2) at Z equals (m_A v_AB - m_B v_BA)/M (exact case)",
          zero(v22 - (ma * (B3a / g - A3) - mb * (A3 / g - B3a)) / Mp))
    check("(2.3): v(Z,B,A) = -v(Z,A,B), one rest space (exact case)",
          zero(ternary_22(Zp, B3a, A3, n) + ternary_22(Zp, A3, B3a, n)))
    check("(2.4) at Z equals gamma_AB (exact case)",
          sp.simplify(gamma_24(Zp, A3, B3a, n) - g) == 0)
    check("Z ^ A ^ B = 0", all(e == 0 for e in wedge3(Zp, A3, B3a)))
    check("L_{Z^w} is the binary boost (exact case)",
          zero(ternary_boost(Zp, A3, B3a, n) - binary_boost(A3, B3a, n)))

    Zm = unit(ma * A3 + mb * B3a, n)
    Mab = sp.sqrt(-dot(ma * A3 + mb * B3a, ma * A3 + mb * B3a, n))
    check("nesting: Mab Z(A,B) + m_C C = m_A A + m_B B + m_C C",
          zero(Mab * Zm + 12 * C3 - (ma * A3 + mb * B3a + 12 * C3)))


# -------------------------------------------------------------------- Part C
def part_c():
    print("C. TV4: the mass centre of three bodies")
    n = 3
    Q = 4 * S3 + 3 * B3 + 12 * C3
    print("    total 4-momentum:", list(Q))
    check("Z is at rest and M = 23", zero(Q - 23 * Z3))
    check("Z ^ S ^ B != 0", any(e != 0 for e in wedge3(Z3, S3, B3)))
    check("Z ^ S ^ B = (12/23) C ^ S ^ B",
          all(sp.simplify(p - R(12, 23) * q) == 0
              for p, q in zip(wedge3(Z3, S3, B3), wedge3(C3, S3, B3))))
    gt = gamma_24(Z3, S3, B3, n)
    w = (ternary_22(Z3, S3, B3, n) * gt).applyfunc(sp.simplify)
    print("    w(Z,S,B) =", list(w), " gamma_ternary =", gt,
          " gamma_SB =", gam(S3, B3, n))
    check("this is the case of RV3",
          gt == R(781, 444) and zero(w - sp.Matrix([0, R(-105, 148), R(140, 111)])))
    Q2 = binary_boost(S3, B3, n).inv() * ternary_boost(Z3, S3, B3, n)
    c2 = rotation_cos(Q2.applyfunc(sp.simplify))
    print(f"    binary and ternary boosts differ by cos t = {c2}, t = {degrees(c2):.2f} deg")
    check("the rotation of RV3", c2 == R(1081, 1369))
    for mc in (1, 12, 100):
        Zc = unit(4 * S3 + 3 * B3 + mc * C3, n)
        print(f"    m_C = {mc:>3}: gamma_ternary(Z, S, B) = "
              f"{float(gamma_24(Zc, S3, B3, n)):.4f}")

    G = sp.Matrix([1, 1, 0])
    A2, B2 = lift([R(3, 5), 0]), lift([0, R(4, 5)])
    Zr = 4 * A2 + 3 * B2 - G
    check("radiation: Z ^ A ^ B = -G ^ A ^ B / M, which is not zero here",
          dot(G, G, n) == 0
          and all(sp.simplify(p + q) == 0
                  for p, q in zip(wedge3(Zr, A2, B2), wedge3(G, A2, B2)))
          and any(e != 0 for e in wedge3(G, A2, B2)))


# -------------------------------------------------------------------- Part D
def part_d():
    print("D. TV5: how far the ternary gamma falls below the binary one")
    n = 4
    r, s, l = sp.symbols("r s l", positive=True)
    P_, e_, n_ = (sp.Matrix([1, 0, 0]), sp.Matrix([0, 1, 0]), sp.Matrix([0, 0, 1]))
    A = sp.cosh(r) * (sp.cosh(s) * P_ + sp.sinh(s) * e_) + sp.sinh(r) * n_
    TA = sp.cosh(r) * (sp.cosh(s + l) * P_ + sp.sinh(s + l) * e_) + sp.sinh(r) * n_
    lhs = -dot(A, TA, 3) - 1
    check("gamma_AB - 1 = cosh^2 r (cosh l - 1), symbolic",
          zero(lhs - sp.cosh(r)**2 * (sp.cosh(l) - 1)))

    def residual(P, A, B, dim):
        v = ternary_22(P, A, B, dim).applyfunc(sp.simplify)
        sinh2 = dot(A, A, dim) + dot(A, P, dim)**2 - dot(A, v, dim)**2 / dot(v, v, dim)
        return (sp.simplify(gam(A, B, dim) - 1
                            - (1 + sinh2) * (gamma_24(P, A, B, dim) - 1)),
                sp.simplify(sinh2))

    res, sh2 = residual(Z3, S3, B3, 3)
    print("    RV3 case: residual", res, " sinh^2 r =", sh2)
    check("identity on the RV3 case; sinh^2 r = 144/337", res == 0 and sh2 == R(144, 337))
    res, _ = residual(lift([R(1, 7), R(-2, 9), R(1, 5)]), lift([R(2, 5), R(1, 3), 0]),
                      lift([R(-1, 4), R(1, 2), R(2, 7)]), n)
    check("identity on a general 1+3 case", res == 0)

    x, y, z = sp.symbols("x y z", positive=True)
    gt = (y**2 + z**2 + x - 1) / (2 * y * z - x + 1)       # (2.4)
    check("gamma_ternary - 1 = ((y-z)^2 + 2(x-1)) / (2yz - x + 1)",
          sp.simplify(gt - 1 - ((y - z)**2 + 2 * (x - 1)) / (2 * y * z - x + 1)) == 0)
    check("on the bisector y = z, gamma_ternary -> 1 as y -> oo",
          sp.limit(gt.subs(z, y), y, sp.oo) == 1)


# -------------------------------------------------------------------- Part E
def part_e():
    print("E. TV6, TV7: the triangle S -> B -> C -> S (masses 4, 3, 12)")
    n = 3
    Hb = (binary_boost(C3, S3, n) * binary_boost(B3, C3, n)
          * binary_boost(S3, B3, n)).applyfunc(sp.simplify)
    check("binary boosts: the product fixes S", zero(Hb * S3 - S3))
    cb = rotation_cos(Hb)
    print(f"    binary boosts:  cos = {cb}, angle = {degrees(cb):.2f} deg")
    check("binary boosts do not compose", not zero(Hb - sp.eye(3)))

    Ht = (ternary_boost(Z3, C3, S3, n) * ternary_boost(Z3, B3, C3, n)
          * ternary_boost(Z3, S3, B3, n)).applyfunc(sp.simplify)
    check("ternary boosts at Z: the product fixes S", zero(Ht * S3 - S3))
    ct = rotation_cos(Ht)
    print(f"    ternary at Z:   cos = {ct}, angle = {degrees(ct):.2f} deg")
    check("ternary boosts at one eagle do not compose", not zero(Ht - sp.eye(3)))

    sec = {k: binary_boost(Z3, X, n) for k, X in (("S", S3), ("B", B3), ("C", C3))}

    def lifted(x, y):
        return (sec[y] * sec[x].inv()).applyfunc(sp.simplify)

    check("based lift: g_BC g_SB = g_SC", zero(lifted("B", "C") * lifted("S", "B") - lifted("S", "C")))
    check("based lift: g_SB S = B", zero(lifted("S", "B") * S3 - B3))
    check("based lift is not the binary boost", not zero(lifted("S", "B") - binary_boost(S3, B3, n)))
    check("based lift is not the ternary boost at Z", not zero(lifted("S", "B") - ternary_boost(Z3, S3, B3, n)))

    Zo = unit(4 * S3 + 3 * B3 + 1 * C3, n)
    other = (binary_boost(Zo, B3, n) * binary_boost(Zo, S3, n).inv()).applyfunc(sp.simplify)
    check("based lift depends on the bystander's mass", not zero(lifted("S", "B") - other))

    Lam = binary_boost(sp.Matrix([1, 0, 0]), lift([R(5, 13), R(0)]), n)
    moved = (binary_boost(Lam * Z3, Lam * B3, n)
             * binary_boost(Lam * Z3, Lam * S3, n).inv()).applyfunc(sp.simplify)
    check("based lift is covariant when the whole system is carried along",
          zero(moved - (Lam * lifted("S", "B") * Lam.inv())))

    A1, B1, C1 = lift([R(3, 5), 0]), lift([R(-1, 2), 0]), lift([R(1, 3), 0])
    P1 = unit(2 * A1 + B1 + 3 * C1, n)
    H1 = (binary_boost(C1, A1, n) * binary_boost(B1, C1, n)
          * binary_boost(A1, B1, n)).applyfunc(sp.simplify)
    check("collinear bodies: binary boosts compose", zero(H1 - sp.eye(3)))
    check("collinear bodies: the mass centre sees the binary boost",
          zero(ternary_boost(P1, A1, B1, n) - binary_boost(A1, B1, n)))

    # Galilean contrast: velocities in the plane, G = rotations and translations.
    th, ph = sp.symbols("theta phi", real=True)
    a1, a2, b1, b2, u1, u2, v1, v2 = sp.symbols("a1 a2 b1 b2 u1 u2 v1 v2", real=True)

    def rot(t):
        return sp.Matrix([[sp.cos(t), -sp.sin(t)], [sp.sin(t), sp.cos(t)]])

    def mul(p, q):                      # (R, a) acts as u -> R u + a
        return (p[0] * q[0], p[0] * q[1] + p[1])

    def inv(p):
        return (p[0].T, -p[0].T * p[1])

    def act(p, u):
        return p[0] * u + p[1]

    def glink(A, B):
        return (sp.eye(2), B - A)

    o = sp.Matrix([0, 0])
    L1, L2 = (rot(th), sp.Matrix([a1, a2])), (rot(ph), sp.Matrix([b1, b2]))
    Uu, Vv = sp.Matrix([u1, u2]), sp.Matrix([v1, v2])

    def phi(L):
        return mul(glink(act(L, o), o), L)

    gl = glink(act(L1, Uu), act(L1, Vv))
    conj = mul(mul(L1, glink(Uu, Vv)), inv(L1))
    check("Galilei: (a) covariance", zero(gl[0] - conj[0]) and zero(gl[1] - conj[1]))
    check("Galilei: phi is the homomorphism (R, a) -> R",
          zero(phi(mul(L1, L2))[0] - phi(L1)[0] * phi(L2)[0])
          and zero(phi(L1)[1]) and zero(phi(L1)[0] - L1[0]))


def hyperbolic_area(A, B, C, n) -> float:
    """Numerical: the angle defect of the geodesic triangle ABC."""
    def angle(P, Q, R_):
        gq, gr = float(gam(P, Q, n)), float(gam(P, R_, n))
        gqr = float(gam(Q, R_, n))
        return math.acos((gq * gr - gqr)
                         / (math.sqrt(gq**2 - 1) * math.sqrt(gr**2 - 1)))
    return math.pi - angle(A, B, C) - angle(B, C, A) - angle(C, A, B)


def part_e_area():
    print("E'. The rotation is the area of the triangle (numerical)")
    area = math.degrees(hyperbolic_area(S3, B3, C3, 3))
    print(f"    area (angle defect) of S, B, C = {area:.4f} deg")
    Hb = (binary_boost(C3, S3, 3) * binary_boost(B3, C3, 3)
          * binary_boost(S3, B3, 3)).applyfunc(sp.simplify)
    check("binary holonomy = area, to 1e-9 deg",
          abs(area - degrees(rotation_cos(Hb))) < 1e-9)


# -------------------------------------------------------------------- Part F
def part_f():
    print("F. TV8: alpha, the determinant, Frobenius")
    n = 3
    x, y, z = sp.symbols("x y z", positive=True)
    num = (x - y * z)**2 - (y**2 - 1) * (z**2 - 1)
    alpha = num / (x - 2 * y * z - 1)
    G3 = sp.Matrix([[1, x, y], [x, 1, z], [y, z, 1]])
    check("numerator of alpha = -det[gamma]", sp.expand(num + G3.det()) == 0)
    check("polynomial (5) of 16 Nov 2004 = -det[gamma]",
          sp.expand(-1 + x**2 + y**2 - 2 * y * z * x + z**2 + G3.det()) == 0)
    check("(2.4): gamma_ternary = x - alpha",
          sp.simplify((y**2 + z**2 + x - 1) / (2 * y * z - x + 1) - (x - alpha)) == 0)
    xv, yv, zv = gam(S3, B3, n), gam(Z3, S3, n), gam(Z3, B3, n)
    a_v = alpha.subs({x: xv, y: yv, z: zv})
    print(f"    example: alpha = {a_v}, gamma_SB - alpha = {xv - a_v}")
    check("example: gamma_SB - alpha = 781/444", xv - a_v == R(781, 444))
    a_first = -2 * G3.det() / (-(2 * x - 2) + 4 * y * z)
    check("slide 8, first form, with (P^R^S)^2 = det[gamma] (Clifford): gamma_t = x + alpha",
          sp.simplify((y**2 + z**2 + x - 1) / (2 * y * z - x + 1) - (x + a_first)) == 0)
    check("slide 8, explicit form: minus the first form", sp.simplify(alpha + a_first) == 0)
    g_c = xv + a_first.subs({x: xv, y: yv, z: zv})
    v2 = 1 - 1 / xv**2
    lv2 = 1 + (v2 - 1) / (1 + a_first.subs({x: xv, y: yv, z: zv}) * sp.sqrt(1 - v2))**2
    check("slide 9 with the first form: Lv^2 = 1 - 1/gamma_t^2",
          sp.simplify(lv2 - (1 - 1 / g_c**2)) == 0)

    def form_det(G):
        m = G.rows
        idx = list(itertools.product(range(m), range(m)))
        F = sp.zeros(len(idx), len(idx))
        for a, (i, j) in enumerate(idx):
            for b, (k, l) in enumerate(idx):
                F[a, b] = G[j, k] * G[l, i]     # tr(e_ij G e_kl G)
        # F is (G tensor G) times the swap of the two factors, whose determinant
        # is (-1)^(m(m-1)/2); so det F = (-1)^(m(m-1)/2) (det G)^(2m).
        return F.det()

    G5 = sp.Matrix([[1, 2, 2], [2, 1, 2], [2, 2, 1]])
    G0 = sp.Matrix([[1, 2, 2], [2, 1, 7], [2, 7, 1]])
    print("    det G for (2,2,2) and (2,2,7):", G5.det(), G0.det())
    check("Frobenius form: det = -(det G)^6 for n = 3 (pq=qr=pr=2)", form_det(G5) == -G5.det()**6)
    check("Frobenius form degenerate for pq=2, qr=2, pr=7 (collinear)", form_det(G0) == 0)
    G2 = sp.Matrix([[1, R(5, 4)], [R(5, 4), 1]])
    check("n = 2: det = -(det G)^4", form_det(G2) == -G2.det()**4)

    Zp = unit(4 * S3 + 3 * B3, n)
    gm = sp.Matrix([[1, xv, sp.simplify(gam(Zp, S3, n))],
                    [xv, 1, sp.simplify(gam(Zp, B3, n))],
                    [sp.simplify(gam(Zp, S3, n)), sp.simplify(gam(Zp, B3, n)), 1]])
    check("a pair with its own mass centre: det[gamma] = 0", sp.simplify(gm.det()) == 0)
    bodies = [S3, B3, C3, Z3]
    gm4 = sp.Matrix(4, 4, lambda i, j: gam(bodies[i], bodies[j], n))
    check("three bodies with their mass centre: det[gamma] = 0", sp.simplify(gm4.det()) == 0)
    gm3 = sp.Matrix(3, 3, lambda i, j: gam(bodies[i], bodies[j], n))
    check("the three bodies alone: det[gamma] != 0", gm3.det() != 0)


# -------------------------------------------------------------------- Part G
def part_g():
    print("G. TV9: Todorov's map")
    m1, m2, x = sp.symbols("m1 m2 gamma", positive=True)
    M2 = m1**2 + m2**2 + 2 * m1 * m2 * x
    M = sp.sqrt(M2)
    eps = (M2 - m1**2 - m2**2) / (2 * M)
    mw = m1 * m2 / M
    p2 = mw**2 * (x**2 - 1)
    check("epsilon_w = mu_12 = gamma m1 m2 / M", sp.simplify(eps - x * m1 * m2 / M) == 0)
    check("kappa^2 = epsilon_w^2 - m_w^2 is p_ZB^2", sp.simplify(p2 - (eps**2 - mw**2)) == 0)
    check("kappa/epsilon_w is the binary speed",
          sp.simplify(p2 / eps**2 - (1 - 1 / x**2)) == 0)
    check("gamma_effective = epsilon_w/m_w = gamma", sp.simplify(eps / mw - x) == 0)


# -------------------------------------------------------------------- Part I
def idem(X, n=3):
    """The idempotent X tensor (-gX) of a unit time-like vector."""
    from verify_relative_velocity import eta
    return -X * X.T * eta(n)


def transported(P, A, B, n=3):
    """U(P, A, B): the binary velocity v_AB carried to the rest space of P."""
    g = gam(A, B, n)
    return (binary_boost(A, P, n) * (B / g - A)).applyfunc(sp.simplify)


def part_i():
    print("I. TV10: the two ternary velocities; velocity.pdf (22 Nov 2004)")
    n = 3
    S, B = S3, B3
    g = gam(S, B, n)
    p, q = idem(Z3), idem(S)
    y = gam(Z3, S, n)
    Rd = sp.eye(3) - p - y / (y + 1) * (q * p / y**2 - p)      # (10.5)
    vSB = B / g - S
    check("(10.5) on the rest space of S is the binary boost S -> Z",
          zero(Rd * vSB - transported(Z3, S, B)))
    U1, U2 = transported(Z3, S, B), transported(Z3, B, S)
    check("U is orthogonal to the eagle", sp.simplify(dot(U1, Z3, n)) == 0)
    check("U keeps the binary speed", sp.simplify(dot(U1, U1, n) - (1 - 1 / g**2)) == 0)
    diff = (U1 + U2).applyfunc(sp.simplify)
    print("    U(Z,S,B) =", list(U1))
    print("    U(Z,B,S) =", list(U2))
    print("    (U(Z,S,B) + U(Z,B,S))^2 =", sp.simplify(dot(diff, diff, n)))
    check("off the plane U is not reciprocal (Theorem 11.5)", not zero(diff))
    print("    v(Z,S,B)^2 =", sp.nsimplify(sp.simplify(
        dot(ternary_22(Z3, S, B, n), ternary_22(Z3, S, B, n), n))),
        " binary v^2 =", 1 - 1 / g**2)

    Zp = unit(4 * S + 3 * B, n)
    a, b = idem(S), idem(B)
    U3, U4 = transported(Zp, S, B), transported(Zp, B, S)
    check("in the plane U is reciprocal (Theorem 11.5)", zero(U3 + U4))
    check("in the plane U = v(P, A, B)",
          zero(U3 - ternary_22(Zp, S, B, n)))
    check("(11.10): v(Z,S,B) = [b,a] Z / tr(ab), pair mass centre",
          zero(ternary_22(Zp, S, B, n) - (b * a - a * b) * Zp / (a * b).trace()))
    check("tr(ab) = gamma^2", sp.simplify((a * b).trace() - g**2) == 0)

    P, A1, B1 = Z3, S, B
    gPA, gPB, gAB = gam(P, A1, n), gam(P, B1, n), gam(A1, B1, n)
    vPA, vPB = A1 / gPA - P, B1 / gPB - P
    check("(11.9): U as a subtraction of binary velocities",
          zero(transported(P, A1, B1)
               - (gPB / gAB * vPB
                  - gPA / (gPA + 1) * (gAB + gPB) / gAB * vPA)))

    c = idem(C3)
    k1, k2 = a * b - b * a, b * c - c * b
    check("tr([a,b]^2) = 2 gamma^2 (gamma^2 - 1) > 0: a boost generator",
          sp.simplify((k1 * k1).trace() - 2 * g**2 * (g**2 - 1)) == 0)
    rot_gen = (k1 * k2 - k2 * k1).applyfunc(sp.simplify)
    check("[[a,b],[b,c]] annihilates B", zero(rot_gen * B))
    t2 = sp.simplify((rot_gen * rot_gen).trace())
    print("    tr([[a,b],[b,c]]^2) =", t2)
    check("[[a,b],[b,c]] generates a rotation about B", t2 < 0)

    Q, Rr, u = lift([R(3, 5), 0, 0]), lift([R(-3, 5), 0, 0]), sp.Matrix([0, 0, 0, R(3, 5)])
    gu = R(5, 4)
    bQ, bR = gu * (u + Q), gu * (u + Rr)
    check("(6.5): the boost b_u of velocity.pdf is not an isometry",
          dot(bQ, bR, 4) - dot(Q, Rr, 4) == -(gam(Q, Rr, 4) - 1) * (gu**2 - 1))


# -------------------------------------------------------------------- Part H
def part_h():
    import numpy as np
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    from ozlib.utils import docs_path, output_path

    def num(X):
        return np.array([float(c) for c in X])

    def ip(a, b):
        return -a[0] * b[0] + a[1:] @ b[1:]

    def disk(X):
        return X[1:] / (1 + X[0])

    def geodesic(A, B, k=120):
        e = np.arccosh(-ip(A, B))
        t = np.linspace(0, 1, k)[:, None]
        return np.array([disk(x) for x in
                         (np.sinh((1 - t) * e) * A[None, :]
                          + np.sinh(t * e) * B[None, :]) / np.sinh(e)])

    S, B, C = num(S3), num(B3), num(C3)
    Zpair = 4 * S + 3 * B
    Zpair = Zpair / np.sqrt(-ip(Zpair, Zpair))
    v = num(ternary_22(Z3, S3, B3, 3).applyfunc(sp.simplify))
    e = v[1:] / np.linalg.norm(v[1:])

    ink, muted, teal, coral = "#222222", "#888780", "#0F6E56", "#D85A30"
    fig, ax = plt.subplots(figsize=(6.4, 7.1))
    ax.add_patch(plt.Circle((0, 0), 1, fill=False, color=muted, lw=0.8))
    ax.plot([-e[0], e[0]], [-e[1], e[1]], color=coral, lw=1.6, ls=(0, (5, 4)),
            label="axis of the ternary boost at Z")
    for a, b in ((B, C), (C, S)):
        p = geodesic(a, b)
        ax.plot(p[:, 0], p[:, 1], color=muted, lw=1.2)
    p = geodesic(S, B)
    ax.plot(p[:, 0], p[:, 1], color=teal, lw=2.2,
            label="geodesic S to B: the binary boost")
    for X, name, off in ((S, "S (m = 4)", (0.03, -0.055)), (B, "B (m = 3)", (0.03, 0.03)),
                         (C, "C (m = 12)", (-0.27, -0.03))):
        q = disk(X)
        ax.plot(*q, "o", color=ink, ms=6)
        ax.annotate(name, q + np.array(off), color=ink, fontsize=10)
    q = disk(Zpair)
    ax.plot(*q, "o", mfc="white", mec=coral, mew=1.8, ms=8, ls="none",
            label="mass centre of S and B: on the geodesic")
    ax.plot(0, 0, "o", color=coral, ms=8, ls="none",
            label="mass centre of all three: on no side")
    ax.set_aspect("equal")
    ax.set_xlim(-1.03, 1.03)
    ax.set_ylim(-1.03, 1.03)
    ax.set_axis_off()
    ax.set_title("Bodies as points of velocity space (Poincaré disk), in the rest frame of Z",
                 fontsize=10, color=ink)
    ax.legend(fontsize=8, loc="upper center", bbox_to_anchor=(0.5, 0.0), ncol=2,
              frameon=False)
    fig.tight_layout()
    name = "ternary_mass_centre_velocity_space.png"
    fig.savefig(output_path(name), dpi=150)
    dp = docs_path(name)
    if dp:
        fig.savefig(dp, dpi=150)
    print(f"H. figure written: {output_path(name)}" + (f" and {dp}" if dp else ""))


def main():
    part_a()
    part_b()
    part_c()
    part_d()
    part_e()
    part_e_area()
    part_f()
    part_g()
    part_i()
    part_h()
    if FAILED:
        print(f"\n{len(FAILED)} CHECK(S) FAILED:")
        for name in FAILED:
            print("  -", name)
        raise SystemExit(1)
    print("\nALL CHECKS PASSED")


if __name__ == "__main__":
    main()
