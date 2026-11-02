"""Exact checks for supplement/velocity_draft.md.

The draft is Oziewicz's "Why Einstein's addition of velocities is
non-associative?" of 22 November 2004 (velocity.pdf), which is not public.
Equation numbers are the draft's.  Every check is exact (SymPy, rational
vectors in 1+3 dimensions, or symbolic where stated).

Conventions, the draft's: signature (-,+,+,+), c = 1, bodies are unit
time-like.  B(P, v) is the Lorentz P-boost (4.3); b_u P = gamma_u (u + P) is
the Lorentz-group-free boost (6.4); varpi(X, Y) = Y/gamma_XY - X is the
velocity-morphism (11.4); p = P tensor (-gP) is the idempotent of P.

Parts
  A  sections 2, 4, 5: Einstein addition from Lorentz boosts
  B  sections 6, 7: associative addition, Table 4, (7.5) to (7.12), Theorem 7.5
  C  section 8: the inverse, Theorem 8.1; a wedge square is det(a_i.a_j)
  D  section 9: how the two additions are related, (9.1) to (9.6)
  E  sections 10, 11, 12: the idempotents, (10.5), (11.5) to (11.11), (12.2)

Run:  PYTHONPATH=src python3 -u src/verify_velocity_draft.py
Writes no files.
"""

from __future__ import annotations

import itertools

import sympy as sp

from verify_relative_velocity import boost, dot, eta, lift

FAILED: list[str] = []
R = sp.Rational
N = 4
ETA = eta(N)


def check(name: str, ok: bool) -> None:
    print(f"  [{'ok' if ok else 'FAIL'}] {name}")
    if not ok:
        FAILED.append(name)


def zero(e) -> bool:
    """All arithmetic here is in exact rationals, so a zero is literally 0."""
    m = sp.Matrix(e) if hasattr(e, "shape") else sp.Matrix([e])
    return all(sp.nsimplify(x) == 0 for x in m)


def d(a, b):
    return dot(a, b, N)


def g_of(v):
    """The Lorentz factor of a velocity: rational in every case used here."""
    return sp.nsimplify(sp.sqrt(1 / (1 - d(v, v))))


def gam(X, Y):
    return -d(X, Y)


def Boost(P, v):
    """The Lorentz P-boost B^P_v of (4.3), with P.v = 0."""
    g = g_of(v)
    return boost(P, g * v, N, gam=g)


def b(u, P):
    """(6.4): b_u P = gamma_u (u + P), for P.u = 0."""
    return g_of(u) * (u + P)


def varpi(X, Y):
    return (Y / gam(X, Y) - X)


def idem(X):
    return -X * X.T * ETA


def odot(P, Q):
    """p circled-dot q of (10.5): acts on ker q, with image ker p."""
    p, q = idem(P), idem(Q)
    g = gam(P, Q)
    return (sp.eye(N) - p - g / (g + 1) * (q * p / g**2 - p))


def oplus(v, u):
    """Table 4, last line: v (+) u for velocities seen by one observer."""
    gu, vu = g_of(u), d(v, u)
    return (gu * u + v) / (gu * (1 + vu)) + gu / (1 + gu) * vu * u / (1 + vu)


def wedge2(a, b_):
    """The square of a bivector as the Gram determinant of its factors."""
    return d(a, a) * d(b_, b_) - d(a, b_)**2


P0 = sp.Matrix([1, 0, 0, 0])
U0 = sp.Matrix([0, R(3, 5), 0, 0])                 # gamma 5/4
V0 = R(3, 5) * sp.Matrix([0, R(2, 7), R(3, 7), R(6, 7)])     # gamma 5/4
W0 = R(4, 5) * sp.Matrix([0, R(2, 3), R(-1, 3), R(2, 3)])    # gamma 5/3


# -------------------------------------------------------------------- Part A
def part_a():
    print("A. Sections 2, 4, 5: Einstein addition from Lorentz boosts")
    P, u, v, w = P0, U0, V0, W0
    Bu, Bv = Boost(P, u), Boost(P, v)
    gu = g_of(u)

    l = P * (gu * u).T * ETA - gu * u * P.T * ETA     # (4.1)
    check("(4.2): l^3 = (gamma^2 - 1) l", zero(l**3 - (gu**2 - 1) * l))
    check("(4.2): l P = gamma v", zero(l * P - gu * u))
    check("(4.3): B = id + l + l^2/(gamma + 1)",
          zero(Bu - (sp.eye(N) + l + l**2 / (gu + 1))))
    check("(4.5): B P = gamma (v + P)", zero(Bu * P - gu * (u + P)))
    check("Lemma 4.1: B is an isometry", zero(Bu.T * ETA * Bu - ETA))

    vu = d(v, u)
    check("(5.4): B_u v", zero(Bu * v - (v + vu * gu**2 * u / (gu + 1) + gu * vu * P)))
    Q = Bu * Bv * P
    s = oplus(v, u)
    check("Definition 5.1: B_u B_v P = gamma (v (+) u + P)", zero(varpi(P, Q) - s))
    gs = g_of(s)
    check("(5.7): Silberstein identity", sp.nsimplify(gs - g_of(v) * gu * (1 + vu)) == 0)
    check("(7.4)", zero(gs * s - (g_of(v) * v + (gs + g_of(v)) * gu * u / (gu + 1))))
    check("not commutative", not zero(oplus(v, u) - oplus(u, v)))

    a1, a2 = oplus(w, oplus(v, u)), oplus(oplus(w, v), u)
    check("not associative: (2.4), the two results are not parallel",
          not sp.Matrix.hstack(a1, a2).rank() < 2)
    triple = g_of(w) * g_of(v) * g_of(u)
    base = 1 + d(u, v) + d(v, w) + d(w, u)

    def biv(a, b_, c, e):                        # (a^b).(c^e), Gram sign
        return d(a, c) * d(b_, e) - d(a, e) * d(b_, c)

    check("(2.3), first line",
          sp.nsimplify(g_of(a1) / triple
                      - (base + biv(w, u, u, v) / (1 + 1 / gu))) == 0)
    check("(2.3), second line",
          sp.nsimplify(g_of(a2) / triple
                      - (base + biv(w, v, v, u) / (1 + 1 / g_of(v)))) == 0)

    check("(2.2): v (+) u = 0 for v = -u", zero(oplus(-u, u)) and wedge2(-u, u) == 0)
    x = sp.Matrix([0, R(1, 3), 0, 0])
    y = sp.Matrix([0, R(-1, 4), R(1, 5), 0])
    lhs = (x + y).dot(ETA * (x + y)) - wedge2(x, y)
    check("section 2 (i): gamma_(v(+)u) = 1 iff (v+u)^2 = (v^u)^2, with the Gram sign",
          sp.nsimplify((1 - d(x, x)) * (1 - d(y, y)) - (1 + d(x, y))**2 + lhs) == 0)


# -------------------------------------------------------------------- Part B
def chain():
    P = P0
    u = U0
    K = b(u, P)
    v = (Boost(P, u) * V0)
    Lb = b(v, K)
    w = (boost(P, Lb - gam(P, Lb) * P, N, gam=gam(P, Lb)) * W0)
    M = b(w, Lb)
    return P, u, K, v, Lb, w, M


def circ_P(v, u, P):
    """Table 4, first line."""
    gu, vu = g_of(u), d(v, u)
    return (gu * u + v - vu * P) / (gu + vu)


def part_b():
    print("B. Sections 6, 7: associative addition")
    P, u, K, v, Lb, w, M = chain()
    check("composable: K.v = 0, P.v = -v.u",
          d(K, v) == 0 and sp.nsimplify(d(P, v) + d(v, u)) == 0)
    gu, gv, vu = g_of(u), g_of(v), d(v, u)
    s = varpi(P, Lb)
    gs = gam(P, Lb)
    check("(7.3)", zero(s - (gv / gs * (v + gu * u + gu * P) - P)))
    check("Lemma 7.1: gamma_(v o u) = gamma_v (gamma_u + v.u)",
          sp.nsimplify(gs - gv * (gu + vu)) == 0)
    check("Table 4, first line (P)", zero(s - circ_P(v, u, P)))
    check("Table 4, second line (K)",
          zero(s - (u + v / (gu + vu) - vu * K / (gu * (gu + vu)))))
    check("Table 4, third line (L)",
          zero(s - (u + v / gu - vu * Lb / (gv * gu * (gu + vu)))))
    check("Table 4, side conditions on L",
          sp.nsimplify(d(Lb, v) - (gv - 1 / gv)) == 0
          and sp.nsimplify(d(Lb, u) - gv * (gu - 1 / gu + vu)) == 0)
    check("(7.7): P.s = 0", sp.nsimplify(d(P, s)) == 0)
    check("(7.7): K.s", sp.nsimplify(d(K, s) - (gu - gv / gs)) == 0)
    check("(7.7): L.s", sp.nsimplify(d(Lb, s) - (gs - 1 / gs)) == 0)

    v2 = sp.Matrix([0, 0, R(3, 5), 0])
    check("(7.6): for v.u = 0", zero(circ_P(v2, u, P) - oplus(v2, u))
          and zero(oplus(v2, u) - (u + v2 / gu)))

    gw = g_of(w)
    gt = gam(P, M)
    wu, wv = d(w, u), d(w, v)
    check("(7.8)", sp.nsimplify(gt / (gw * gv * gu)
                               - (1 + vu / gu + wu / (gu * gv) + wv / (gu**2 * gv))) == 0)
    check("(7.11): w.(v o u) = w.(u + v/gamma_u)", sp.nsimplify(d(w, s) - (wu + wv / gu)) == 0)
    wv_c = varpi(K, M)
    lhs = d(wv_c, u)
    rhs = (gv * vu - (gu - 1 / gu) * wv + wu) / (gv + wv)
    check("(7.12)", zero(lhs - rhs))
    check("Theorem 7.5, both bracketings are varpi(P, M)",
          zero(circ_P(w, s, P) - varpi(P, M))
          and zero(circ_P(wv_c, u, P) - varpi(P, M)))


# -------------------------------------------------------------------- Part C
def part_c():
    print("C. Section 8: the inverse")
    P, u, K = P0, U0, b(U0, P0)
    g = g_of(u)
    inv = varpi(K, P)
    check("Theorem 8.1 (i): u^-1 = -B_u u", zero(inv + Boost(P, u) * u))
    check("Theorem 8.1 (i): = -gamma u - (gamma - 1/gamma) P",
          zero(inv + g * u + (g - 1 / g) * P))
    check("(iii)", sp.nsimplify(d(inv, u) + d(u, u) * g) == 0)
    check("(iv)", sp.nsimplify(d(inv + u, inv + u) + 2 * (g + 1) * (1 - 1 / g)**2) == 0)
    check("(ii): (u^-1 ^ u)^2 = -(g^2 - 1)^3 / g^4, with the square read as det(a_i.a_j)",
          sp.nsimplify(wedge2(inv, u) + (g**2 - 1)**3 / g**4) == 0)
    check("Exercise 8.2: (B^P_v)^-1 = B^P_(-v)", zero(Boost(P, u).inv() - Boost(P, -u)))


# -------------------------------------------------------------------- Part D
def part_d():
    print("D. Section 9: how the two additions are related")
    P, u, K, v, Lb, _, _ = chain()
    g = g_of(u)
    # (9.1) with gP the form X -> P.X, i.e. the sign printed in the draft
    O_u = (sp.eye(N) + (g * u / (g + 1) + P) * (ETA * P).T)
    O_ui = (sp.eye(N) + (g * u / (g + 1) + P) * (ETA * K).T)
    check("(9.1) is p (.) q of (10.5), P to K", zero(O_u - odot(P, K)))
    check("(9.1), second line, is q (.) p", zero(O_ui - odot(K, P)))
    check("(9.1): the idempotent, and its kernel",
          zero(O_u * O_u - O_u) and zero(O_u * ((g + 1) * P + g * u)))
    check("(9.1): O_u P = -gamma u/(gamma + 1)", zero(O_u * P + g * u / (g + 1)))

    Q = lift([R(6, 35), R(9, 35), R(18, 35)])
    Rr = lift([0, R(4, 5), 0])
    lhs = d(O_u * Q, O_u * Rr)
    gK_ = K
    rhs = d(Q, Rr) + 1 / (g + 1) * (2 / g * d(Rr, gK_) * d(Q, gK_)
                                    - d(Q, u) * d(Rr, gK_) - d(Rr, u) * d(Q, gK_))
    check("(9.2)", zero(lhs - rhs))

    v_P = (O_u * v)
    check("(9.3): B^P_u v0 = (K (.) P) v0", zero(Boost(P, u) * V0 - O_ui * V0))
    check("Theorem 9.1, (9.4): v o u = (O_u v) (+) u", zero(circ_P(v, u, P) - oplus(v_P, u)))
    check("Theorem 9.1, (9.5): v0 (+) u = (B_u v0) o u",
          zero(oplus(V0, u) - circ_P(Boost(P, u) * V0, u, P)))
    B_vP = Boost(P, v_P)
    check("(9.6): B^K_v B^P_u P = L, the composition the text means",
          zero(Boost(K, v) * Boost(P, u) * P - Lb))
    check("(9.6): but B^P_(O_u v) is not B^K_v, and does not carry K to L",
          not zero(B_vP - Boost(K, v)) and not zero(B_vP * K - Lb))


# -------------------------------------------------------------------- Part E
def part_e():
    print("E. Sections 10, 11, 12: the idempotents and the ternary velocity")
    P = lift([R(6, 35), R(9, 35), R(18, 35)])          # gamma 5/4
    A = lift([R(3, 5), 0, 0])                          # gamma 5/4
    Bb = lift([0, R(4, 5), 0])                         # gamma 5/3
    C = lift([0, 0, R(12, 13)])                        # gamma 13/5
    p, a, bb, c = idem(P), idem(A), idem(Bb), idem(C)
    I = sp.eye(N)
    gpa, gpb, gab = gam(P, A), gam(P, Bb), gam(A, Bb)

    Rd, Rd2 = odot(P, A), odot(A, P)
    check("(10.5): idempotent, R(u - p) = u - p, trace d - 1",
          zero(Rd * Rd - Rd) and zero(Rd * (I - p) - (I - p)) and Rd.trace() == 3)
    check("(10.5): P + A in both kernels", zero(Rd * (P + A)) and zero(Rd2 * (P + A)))
    check("(10.6): (p.q)(q.p) = p.q", zero(Rd * Rd2 - Rd))

    x, y = varpi(A, Bb), varpi(A, C)
    check("(11.8): p-independence of the inner product", zero(d(Rd * x, Rd * y) - d(x, y)))
    check("(11.8): = 1 - gamma_bc/(gamma_ab gamma_ac)",
          zero(d(x, y) - (1 - gam(Bb, C) / (gab * gam(A, C)))))
    check("(11.8): (q.p)(p.q) restores the velocity", zero(Rd2 * (Rd * x) - x))

    vel = (bb * a) / (a * bb).trace() - a
    check("(11.6): nilpotent, traceless, a v = 0, and v A = varpi(A, B)",
          zero(vel * vel) and vel.trace() == 0 and zero(a * vel) and zero(vel * A - x))

    U = Rd * x
    check("(11.7): p v^q_p = -varpi^p_q", zero(Rd * varpi(A, P) + varpi(P, A)))
    vPA, vPB = varpi(P, A), varpi(P, Bb)
    check("(11.9), first form",
          zero(U - (gpb / gab * vPB - gpa / (gpa + 1) * (gab + gpb) / gab * vPA)))
    com = (bb * a - a * bb) * P / (a * bb).trace()
    second = com - ((p - a) * (p - a) + ((a * p).trace() - 1) * I) * Bb / (gab * (gpa + 1))
    check("(11.9), second form, with (p-a)^2 + tr(ap) - 1 an operator on B", zero(U - second))
    Z = sp.Matrix([1, 0, 0, 0])
    Ac, Bc = lift([R(3, 5), 0, 0]), lift([R(-4, 5), 0, 0])
    z, ac, bc = idem(Z), idem(Ac), idem(Bc)
    Ua, Ub = odot(Z, Ac) * varpi(Ac, Bc), odot(Z, Bc) * varpi(Bc, Ac)
    check("Theorem 11.5, coplanar: reciprocal", zero(Ua + Ub))
    check("(11.10): = [b,a] P / tr(ab)", zero(Ua - (bc * ac - ac * bc) * Z / (ac * bc).trace()))
    check("Theorem 11.5, not coplanar: not reciprocal", not zero(U + odot(P, Bb) * varpi(Bb, A)))
    check("the condition tr(ab + bp + pa - 2abp) = 1, coplanar",
          (ac * bc + bc * z + z * ac - 2 * ac * bc * z).trace() == 1)
    check("and not otherwise", (a * bb + bb * p + p * a - 2 * a * bb * p).trace() != 1)
    e = (ac - bc) * (ac - bc) * z + (ac * bc).trace() * z - z
    check("(11.11), coplanar triple", zero(e))
    check("(11.11) fails off the plane",
          not zero((a - bb) * (a - bb) * p + (a * bb).trace() * p - p))

    v1, v2, v3 = varpi(A, C), varpi(Bb, C), varpi(A, Bb)
    lhs_m = sp.Matrix.hstack(gam(A, C) * v1, v2, v3)
    rhs_m = sp.Matrix.hstack(A, Bb, C)
    k = -d(varpi(Bb, C), varpi(Bb, A))
    ratios = set()
    for r in itertools.combinations(range(N), 3):
        la = lhs_m.extract(list(r), [0, 1, 2]).det()
        ra = rhs_m.extract(list(r), [0, 1, 2]).det()
        ratios.add(la / ra if ra != 0 else None)
    check("(11.5)", ratios == {k})

    Q2, R2, P2 = lift([R(3, 5), 0, 0]), lift([R(-5, 13), 0, 0]), sp.Matrix([1, 0, 0, 0])
    q2, r2 = idem(Q2), idem(R2)
    lk = (r2 * q2 - q2 * r2) * P2 / (q2 * r2).trace()
    vx = (R(-5, 13) - R(3, 5)) / (1 - R(3, 5) * R(-5, 13))
    check("(12.2): the textbook subtraction", zero(lk[1] - vx))
    check("(12.2): = (gamma_pq R - gamma_pr Q)/gamma_qr",
          zero(lk - (gam(P2, Q2) * R2 - gam(P2, R2) * Q2) / gam(Q2, R2)))

    Q3, R3 = lift([R(3, 5), 0, 0]), lift([R(-3, 5), 0, 0])
    u3 = sp.Matrix([0, 0, 0, R(3, 5)])
    check("(6.5)", zero(d(b(u3, Q3), b(u3, R3)) - d(Q3, R3)
                        + (gam(Q3, R3) - 1) * (R(5, 4)**2 - 1)))


def main():
    part_a()
    part_b()
    part_c()
    part_d()
    part_e()
    if FAILED:
        print(f"\n{len(FAILED)} CHECK(S) FAILED:")
        for name in FAILED:
            print("  -", name)
        raise SystemExit(1)
    print("\nALL CHECKS PASSED")


if __name__ == "__main__":
    main()
