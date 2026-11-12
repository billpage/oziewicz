"""Exact checks for supplement/matolcsi_spacetime.md.

The book is T. Matolcsi, "Spacetime Without Reference Frames" (Akademiai
Kiado, Budapest 1993), Part One, chapter II (special relativistic spacetime
models).  Section numbers are the book's, written II.x.y.z.  Every check is
exact (SymPy): rational vectors in 1+3 dimensions, or symbolic where stated.

Conventions, the book's: signature (-,+,+,+), light speed 1, V(1) is the set
of future-directed unit time-like vectors ("velocity values"), E_u is the
g-orthogonal complement of u, and (a (x) b) . x = a (b . x).

  v(u', u) = u'/(-u.u') - u                               (II.1.3.7, II.4.2.2)
  L(u', u) = g + (u'+u)(x)(u'+u)/(1 - u'.u) - 2 u'(x)u    (II.1.3.8)

Parts
  A  II.1.3.7, II.4.2: the relative velocity; it is Oziewicz's binary velocity
  B  II.1.3.8: the Lorentz boost from u to u'
  C  II.1.3.9, II.5.1.2, II.10.1.5: boosts compose only for coplanar velocity
     values; the defect is a rotation of E_u (Thomas-Wigner)
  D  II.4.3: the addition formula of relative velocities
  E  II.4.7: light, and the aberration formula
  F  II.5.2, II.5.3: observed vectors and the Lorentz contraction
  G  II.7.1: the vector transformation rule and the Lorentz transformation
  H  II.6.2.4, II.6.7, II.6.8: the two uniformly rotating observers are not
     regular (alpha ^ d alpha != 0), symbolic
  I  the second edition (2018), II.4.3.2 and II.4.8, and Matolcsi and Goher
     (2001), eqs (35), (42), (46): the boosted addition formula, the angle of
     the Thomas rotation, and velocities in a nonstandard synchronization
  J  Oziewicz's observer p = T (x) tau is an inertial reference frame
     (synchronization, observer) of the 2018 edition; a shared clock form
     gives additive velocities in one vector space

Run:  PYTHONPATH=src python3 -u src/verify_matolcsi.py
Writes no files.
"""

from __future__ import annotations

import sympy as sp

from verify_relative_velocity import binary, dot, eta

FAILED: list[str] = []
R = sp.Rational
N = 4
ETA = eta(N)
ID = sp.eye(N)


def check(name: str, ok: bool) -> None:
    print(f"  [{'ok' if ok else 'FAIL'}] {name}")
    if not ok:
        FAILED.append(name)


def zero(e) -> bool:
    m = sp.Matrix(e) if hasattr(e, "shape") else sp.Matrix([e])
    return all(sp.simplify(x) == 0 for x in m)


def d(a, b):
    return dot(a, b, N)


def vv(*c):
    return sp.Matrix(c)


def unit(*c):
    """Future-directed unit time-like vector with the given spatial part."""
    s = sp.Matrix(c)
    g = sp.sqrt(1 + s.dot(s))
    assert g.is_rational, "choose a spatial part with rational gamma"
    return sp.Matrix([g, *s])


def v(up, u):
    """Relative velocity of u' with respect to u, II.4.2.2."""
    return up / (-d(u, up)) - u


def tens(a, b):
    """Matrix of a (x) b acting by (a (x) b) . x = a (b . x)."""
    return a * (ETA * b).T


def L(up, u):
    """Lorentz boost from u to u', Definition in II.1.3.8."""
    return ID + tens(up + u, up + u) / (1 - d(up, u)) - 2 * tens(up, u)


# Velocity values used throughout: all Lorentz factors are rational.
U0 = unit(0, 0, 0)                      # (1, 0, 0, 0)
U1 = unit(R(3, 4), 0, 0)                # gamma 5/4, speed 3/5 along x
U2 = unit(0, R(4, 3), 0)                # gamma 5/3, speed 4/5 along y
U3 = unit(R(4, 3), 0, 0)                # coplanar with U0, U1
U4 = unit(1, 1, 1)                      # gamma 2, generic direction
PAIRS = [(U0, U1), (U1, U2), (U2, U4), (U4, U1), (U0, U4)]


def part_a():
    print("Part A  II.1.3.7, II.4.2: relative velocity")
    ok1 = ok2 = ok3 = ok4 = ok5 = True
    for a, b in PAIRS:
        g = -d(a, b)
        ok1 &= zero(d(v(b, a), a))
        ok2 &= zero(d(v(b, a), v(b, a)) - (1 - 1 / g**2))
        ok2 &= zero(d(v(a, b), v(a, b)) - (1 - 1 / g**2))
        ok3 &= zero(v(b, a) + v(a, b) - (a + b) * (1 / g - 1))
        ok3 &= not zero(v(b, a) + v(a, b))
        s = sp.sqrt(1 - d(v(b, a), v(b, a)))
        ok4 &= zero(g - 1 / s) and zero(b - (a + v(b, a)) / s)
        ok5 &= zero(v(b, a) - binary(a, b, N))
    check("4.2.2 (i): v(u',u) is g-orthogonal to u", ok1)
    check("4.2.2 (iii): |v(u',u)|^2 = |v(u,u')|^2 = 1 - 1/(u.u')^2", ok2)
    check("4.2.2 (ii): v(u',u) + v(u,u') = (u+u')(1/gamma - 1), not 0", ok3)
    check("4.2.4: -u.u' = 1/sqrt(1-|v|^2), u' = (u+v)/sqrt(1-|v|^2)", ok4)
    check("v(u',u) equals the binary velocity v_{u u'} of this repository (MC1)", ok5)
    # 1.3.7 Proposition: E_u ^ E_u' is orthogonal to both relative velocities
    q = vv(0, 0, 1, 0)
    check("1.3.7: q in E_u ^ E_u' is orthogonal to v(u',u) and v(u,u')",
          zero(d(q, U0)) and zero(d(q, U1)) and zero(d(q, v(U1, U0))) and zero(d(q, v(U0, U1))))


def part_b():
    print("Part B  II.1.3.8: the Lorentz boost L(u',u)")
    ok = [True] * 5
    for a, b in PAIRS:
        M = L(b, a)
        ok[0] &= zero(M.T * ETA * M - ETA)
        ok[1] &= zero(M * a - b)
        ok[2] &= zero(M * v(b, a) + v(a, b))
        ok[3] &= zero(M * L(a, b) - ID) and zero(L(a, a) - ID)
        ok[4] &= M.det() == 1
    check("(i) L(u',u) is g-orthogonal", ok[0])
    check("(ii) L(u',u) u = u'", ok[1])
    check("(iii) L(u',u) v(u',u) = -v(u,u')", ok[2])
    check("(iv) L(u,u) = g, L(u',u)^-1 = L(u,u')", ok[3])
    check("det L(u',u) = 1", ok[4])
    M = L(U1, U0)
    check("(iii) L(u',u) q = q for q in E_u ^ E_u'",
          zero(M * vv(0, 0, 1, 0) - vv(0, 0, 1, 0)) and zero(M * vv(0, 0, 0, 1) - vv(0, 0, 0, 1)))


def part_c():
    print("Part C  II.1.3.9, II.5.1.2, II.10.1.5: composition of boosts")
    check("coplanar u, u', u'': L(u'',u') L(u',u) = L(u'',u)",
          zero(L(U3, U1) * L(U1, U0) - L(U3, U0)))
    check("not coplanar: L(u'',u') L(u',u) != L(u'',u)",
          not zero(L(U2, U1) * L(U1, U0) - L(U2, U0)))
    # the defect, read in E_u: W = L(u,u'') L(u'',u') L(u',u)
    W = L(U0, U2) * L(U2, U1) * L(U1, U0)
    check("W = L(u,u'') L(u'',u') L(u',u) fixes u and is g-orthogonal",
          zero(W * U0 - U0) and zero(W.T * ETA * W - ETA))
    rot = W[1:3, 1:3]
    c = rot[0, 0]
    check("W is a rotation of E_u about the normal of the plane of the velocities",
          zero(rot.T * rot - sp.eye(2)) and rot.det() == 1 and W[3, 3] == 1)
    g1, g2, g12 = -d(U0, U1), -d(U0, U2), -d(U1, U2)
    wig = (1 + g1 + g2 + g12) ** 2 / ((1 + g1) * (1 + g2) * (1 + g12)) - 1
    print(f"         cos(angle) = {c}  (speeds 3/5 and 4/5 at right angles)")
    check("its angle is the Thomas-Wigner angle (standard closed formula)",
          zero(c - wig) and c == R(35, 37))
    # 5.1.2: 'physically equal' is not transitive
    q = vv(0, 1, 0, 0)
    q2 = L(U2, U1) * L(U1, U0) * q
    direct = L(U2, U0) * q
    cross = sp.Matrix([[q2[i] * direct[j] - q2[j] * direct[i] for j in range(N)] for i in range(N)])
    check("5.1.2: L(u'',u')L(u',u) q is not parallel to L(u'',u) q", not zero(cross))
    # 10.1.5: R(L,u) = L(u, L u) L is in O(b_u), for L a product of two boosts
    Lg = L(U4, U2) * L(U1, U0)
    Rm = L(U0, Lg * U0) * Lg
    check("10.1.5: R(L,u) = L(u, L u) L fixes u (L orthochronous)",
          zero(Rm * U0 - U0) and zero(Rm.T * ETA * Rm - ETA))


def add_432(v_pp_p, v_p_u, v_u_p):
    """Proposition II.4.3.2: v(u'',u) from v(u'',u'), v(u',u) and v(u,u')."""
    n2 = d(v_u_p, v_u_p)
    k = d(v_pp_p, v_u_p)
    num = (v_pp_p - k / n2 * v_u_p) * sp.sqrt(1 - n2) + (1 - k / n2) * v_p_u
    return num / (1 - k)


def part_d():
    print("Part D  II.4.3: addition of relative velocities")
    ok = ok_naive = ok_g = True
    for a, b, c in [(U0, U1, U2), (U1, U2, U4), (U4, U0, U2), (U2, U4, U1)]:
        lhs = v(c, a)
        ok &= zero(lhs - add_432(v(c, b), v(b, a), v(a, b)))
        ok_naive &= not zero(lhs - v(c, b) - v(b, a))
        s = lambda x: sp.sqrt(1 - d(x, x))
        ok_g &= zero(1 / s(v(c, a)) - (1 - d(v(c, b), v(a, b))) / (s(v(c, b)) * s(v(a, b))))
    check("4.3.2 Proposition: the addition formula (4 triples)", ok)
    check("4.3.1: v(u'',u) != v(u'',u') + v(u',u)", ok_naive)
    check("4.3.2 auxiliary: 1/sqrt(1-|v(u'',u)|^2) in terms of v(u'',u').v(u,u')", ok_g)
    # 4.3.1: the boosted sum can be longer than 1
    Ua = unit(R(4, 3), 0, 0)             # speed 4/5 relative to U0
    Ub = L(Ua, U0) * Ua                  # speed 4/5 relative to Ua, same direction
    w = L(U0, Ua) * v(Ub, Ua) + v(Ua, U0)
    check("4.3.1: |L(u,u') v(u'',u') + v(u',u)| can exceed 1", d(w, w) > 1)
    # 4.3.3: collinear case, v(u'',u') = -alpha v(u,u')
    al = sp.Symbol("alpha", positive=True)
    a, b = U0, U1
    vpp = -al * v(a, b)
    lhs = add_432(vpp, v(b, a), v(a, b))
    n2 = d(v(b, a), v(b, a))
    check("4.3.3: collinear case gives (v + alpha v)/(1 + alpha |v|^2), symbolic alpha",
          zero(lhs - (v(b, a) + al * v(b, a)) / (1 + al * n2)))
    # associativity is that of the pair groupoid: three steps, either bracketing
    a, b, c, e = U0, U1, U2, U4
    left = add_432(v(e, c), add_432(v(c, b), v(b, a), v(a, b)), v(a, c))
    right = add_432(add_432(v(e, c), v(c, b), v(b, c)), v(b, a), v(a, b))
    check("three steps: both bracketings give v(u''',u) (pair groupoid, MC2)",
          zero(left - v(e, a)) and zero(right - v(e, a)))


def part_e():
    print("Part E  II.4.7: light")
    w = vv(1, R(2, 3), R(2, 3), R(1, 3))
    check("w is light-like", zero(d(w, w)))
    ok = True
    for a in (U0, U1, U2, U4):
        x = v(w, a)
        ok &= zero(d(x, a)) and zero(d(x, x) - 1)
    check("4.7.2: v(w,u) is in E_u and |v(w,u)| = 1 for every u", ok)
    check("v(alpha w, u) = v(w, u)", zero(v(3 * w, U1) - v(w, U1)))
    okab = True
    for a, b in [(U0, U1), (U1, U0), (U0, U3)]:
        n = sp.sqrt(d(v(b, a), v(b, a)))
        assert n.is_rational
        cos = d(v(w, a), v(b, a)) / n
        cosp = d(v(w, b), -v(a, b)) / n
        okab &= zero(cos - (cosp + n) / (1 + n * cosp))
    check("4.7.3: aberration, with theta' measured from -v(u,u')", okab)


def part_f():
    print("Part F  II.5.2, II.5.3: observed vectors, Lorentz contraction")
    ok1 = ok2 = ok3 = True
    for u0, u in [(U0, U1), (U1, U2), (U4, U2)]:
        P = ID + tens(u0, u) / (-d(u0, u))      # projection onto E_u along u0
        check_proj = zero(P * u0) and zero(P * P - P)
        s = sp.sqrt(1 - d(v(u, u0), v(u, u0)))
        ok1 &= check_proj and zero(P * v(u, u0) + s * v(u0, u))
        for e0 in (v(u, u0), v(U3, u0) if u0 is not U3 else v(U2, u0), v(U0, u0) + v(u, u0)):
            e = P * e0
            ok2 &= zero(d(e, u))
            ok3 &= zero(d(e, e) - (d(e0, e0) - d(v(u, u0), e0) ** 2))
            ok3 &= zero(d(e, e) - (d(e0, e0) - d(u, e0) ** 2 / d(u, u0) ** 2))
    check("5.2.2: A v(u,u0) = -sqrt(1-|v|^2) v(u0,u)", ok1)
    check("5.2.1: the observed vector lies in E_u", ok2)
    check("5.3.1: |e|^2 = |e0|^2 - (v(u,u0).e0)^2", ok3)


def part_g():
    print("Part G  II.7.1: transformation rule and Lorentz transformation")
    t = sp.Symbol("t", real=True)
    ok1 = ok2 = True
    for a, b in [(U0, U1), (U1, U2), (U2, U4)]:
        vba = v(b, a)
        kap = 1 / sp.sqrt(1 - d(vba, vba))
        for q in (vba * R(2, 7), v(U3 if a is not U3 else U0, a), v(U4 if a is not U4 else U0, a)):
            x = a * t + q                       # h_u^-1 (t, q)
            y = L(a, b) * x                     # H_{u'u} = h_u L(u,u') h_u^-1
            tp = -d(a, y)
            qp = y + a * d(a, y)
            D = (ID + tens(vba, vba) * kap**2 / (kap + 1)) / kap
            ok1 &= zero(tp - kap * (t - d(vba, q)))
            ok1 &= zero(qp - kap * (-vba * t + D * q))
            # the same numbers are the u'-components, boosted back to E_u
            ok2 &= zero(tp + d(b, x)) and zero(qp - L(a, b) * (x + b * d(b, x)))
    check("7.1.7: H = kappa [[1, -v], [-v, D(v)]], v = v(u',u)", ok1)
    check("7.1.4: t' is the u'-time component; q' is the boosted u'-space component", ok2)
    a, b = U0, U1
    vba = v(b, a)
    kap = 1 / sp.sqrt(1 - d(vba, vba))
    lam = sp.Symbol("lambda", real=True)
    y = L(a, b) * (a * t + lam * vba)
    check("7.1.6: for q parallel to v: t' = kappa(t - v.q), q' = kappa(-v t + q)",
          zero(-d(a, y) - kap * (t - lam * d(vba, vba))) and
          zero(y + a * d(a, y) - kap * (-vba * t + lam * vba)))


def part_h():
    print("Part H  II.6.2.4, II.6.7, II.6.8: regular observers (symbolic)")
    t, x, y, z, w = sp.symbols("t x y z omega", real=True, positive=True)
    X = (t, x, y, z)

    def a_da(Uvec):
        """Component (t,x,y) ... of alpha ^ d alpha for alpha = g(U, .)."""
        al = [-Uvec[0], Uvec[1], Uvec[2], Uvec[3]]
        dal = [[sp.diff(al[j], X[i]) - sp.diff(al[i], X[j]) for j in range(4)] for i in range(4)]
        out = []
        for (i, j, k) in [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]:
            out.append(sp.simplify(al[i] * dal[j][k] + al[j] * dal[k][i] + al[k] * dal[i][j]))
        return out

    # Omega = omega (rotation in the x-y plane of E_{u0}), u0 = (1,0,0,0), o = 0
    Oq = sp.Matrix([-w * y, w * x, 0])
    n2 = Oq.dot(Oq)
    U_I = sp.Matrix([sp.sqrt(1 + n2), *Oq])
    U_II = sp.Matrix([1, *Oq]) / sp.sqrt(1 - n2)
    for name, Uv in (("6.7.1 uniformly rotating observer I", U_I),
                     ("6.8.1 uniformly rotating observer II", U_II)):
        unitlen = sp.simplify(-Uv[0] ** 2 + Uv[1] ** 2 + Uv[2] ** 2 + Uv[3] ** 2 + 1) == 0
        comp = a_da(Uv)
        print(f"         {name}: (alpha^d alpha)_txy = {sp.factor(comp[0])}")
        check(f"{name}: unit time-like, and alpha ^ d alpha != 0 (not regular)",
              unitlen and comp[0] != 0)
    U_in = sp.Matrix([R(5, 4), R(3, 4), 0, 0])
    check("an inertial observer has alpha ^ d alpha = 0 (regular)", all(c == 0 for c in a_da(U_in)))
    # II.6.7.5 / 6.8: observer II is rigid (Born), observer I is not
    def expansion_shear(Uv):
        al = sp.Matrix([-Uv[0], Uv[1], Uv[2], Uv[3]])
        grad = sp.Matrix(4, 4, lambda i, j: sp.diff(al[j], X[i]))       # d_i alpha_j
        acc = sp.Matrix([sum(Uv[i] * grad[i, j] for i in range(4)) for j in range(4)])
        h = sp.Matrix(4, 4, lambda i, j: grad[i, j] + al[i] * acc[j])   # project the first slot
        return (h + h.T).applyfunc(sp.simplify)
    check("6.8: observer II is Born rigid (projected symmetric gradient = 0)",
          expansion_shear(U_II) == sp.zeros(4, 4))
    check("6.7.5: observer I is not rigid", expansion_shear(U_I) != sp.zeros(4, 4))


def part_i():
    print("Part I  2018 edition II.4.3.2, II.4.8; Matolcsi-Goher 2001")
    ok = ok35 = ok42 = True
    printed = []
    for a, b, c in [(U0, U1, U2), (U1, U2, U4), (U4, U0, U2), (U2, U4, U1)]:
        vp = L(a, b) * v(c, b)            # v' = L(u,u') v(u'',u'), boosted into E_u
        vv_ = v(b, a)
        al, be, ga = -d(b, a), -d(c, b), -d(c, a)
        ok35 &= zero(ga - al * be * (1 + d(vv_, vp)))
        ok &= zero(v(c, a) - (al * (be + ga) / (ga * (1 + al)) * vv_ + be / ga * vp))
        printed.append(zero(v(c, a) - (be / ga * vv_ + al * (be + ga) / (ga * (1 + al)) * vp)))
        W = L(a, c) * L(c, b) * L(b, a)   # R_u(u',u'') of Goher (32)
        cos = (W.trace() - 2) / 2         # W fixes u and an axis: trace = 2 + 2 cos
        ok42 &= zero(cos - (1 - (1 + 2 * al * be * ga - (al**2 + be**2 + ga**2))
                            / ((1 + al) * (1 + be) * (1 + ga))))
    check("Goher (46): v'' = a(b+c)/(c(1+a)) v + (b/c) v', v' boosted into E_u (4 triples)", ok)
    check("... so 2018 II.4.3.2 as printed, with the two coefficients exchanged, is a misprint",
          not all(printed))
    print(f"         as printed it holds for {sum(printed)} of {len(printed)} triples")
    check("Goher (35): c = a b (1 + v.v')", ok35)
    check("Goher (42): cos of the Thomas rotation angle, from the trace (4 triples)", ok42)
    # 2018 II.4.8: observer u with the synchronization of u_s
    ok48 = okdir = True
    changed = False
    for u, us, up in [(U0, U1, U2), (U1, U4, U2), (U2, U0, U4)]:
        y_x = up                           # y - x is parallel to u'
        vel = (y_x + u * d(u, y_x)) / (-d(us, y_x)) * (-d(us, u))
        fac = (-d(u, up)) * (-d(us, u)) / (-d(us, up))
        ok48 &= zero(vel - v(up, u) * fac)
        okdir &= fac > 0
        changed = changed or fac != 1
    check("2018 II.4.8.1: v(u'; u_s, u) = v(u',u) (-u.u')(-u_s.u)/(-u_s.u')", ok48)
    check("so a synchronization changes the size of a relative velocity, not its direction",
          okdir and changed)
    vs, c_ = sp.symbols("v_s c", real=True)   # c = n_s . n_w
    u = U0
    ns, nperp = vv(0, 1, 0, 0), vv(0, 0, 1, 0)
    us = (u + vs * ns) / sp.sqrt(1 - vs**2)
    w = u + c_ * ns + sp.sqrt(1 - c_**2) * nperp
    fac = sp.simplify((-d(u, w)) * (-d(us, u)) / (-d(us, w)))
    check("2018 II.4.8.2: one-way light speed is 1/(1 - v_s n_s.n_w), symbolic",
          zero(fac - 1 / (1 - vs * c_)))
    check("... so the last display of II.4.8.2, (1 - v_s n_s.n_w)/sqrt(1 - v_s^2), is a misprint",
          not zero(fac - (1 - vs * c_) / sp.sqrt(1 - vs**2)))
    check("... while its stated extremes 1/(1 + v_s), 1/(1 - v_s) are right",
          zero(fac.subs(c_, -1) - 1 / (1 + vs)) and zero(fac.subs(c_, 1) - 1 / (1 - vs)))


def part_j():
    print("Part J  an observer T (x) tau is a reference frame (u_s, u)")
    tau = lambda us, u: (lambda x: (-d(us, x)) / (-d(us, u)))     # tau(u) = 1, ker tau = E_{u_s}
    ok1 = ok2 = ok3 = True
    for u, us, up in [(U0, U1, U2), (U1, U4, U2), (U2, U0, U4), (U4, U4, U1)]:
        t = tau(us, u)
        voz = up / t(up) - u                       # Oziewicz: T_q/tau_p(T_q) - T_p
        vm = (up + u * d(u, up)) / (-d(us, up)) * (-d(us, u))    # Matolcsi 2018 II.4.8.1
        ok1 &= zero(t(voz)) and zero(d(vm, u))     # in ker tau, resp. in E_u
        diff = voz - vm
        ok2 &= zero(diff - u * (-d(u, diff)))      # they differ by a multiple of u
        if us is u:
            ok3 &= zero(voz - v(up, u)) and zero(vm - v(up, u))
    check("T_q/tau_p(T_q) - T_p is in ker tau_p; II.4.8.1 is in E_u", ok1)
    check("the two are the same element of M/<u>: they differ by a multiple of u", ok2)
    check("for u_s = u (tau = -g(u, .)) both are the standard v(u',u)", ok3)
    # one clock form for all observers: tau = -g(u_s, .), T_i = u_i / tau(u_i)
    us = U4
    T = [x / (-d(us, x)) for x in (U0, U1, U2, U3)]
    vel = lambda i, j: T[j] / (-d(us, T[j])) - T[i]          # = T_j - T_i
    ok4 = all(zero(vel(i, j) + vel(j, k) - vel(i, k)) and zero(d(us, vel(i, j)))
              for i in range(4) for j in range(4) for k in range(4))
    ok5 = all(zero(vel(i, j) + vel(j, i)) for i in range(4) for j in range(4))
    check("shared clock: all velocities lie in E_{u_s} and add, v_ij + v_jk = v_ik", ok4)
    check("shared clock: velocities are reciprocal, v_ji = -v_ij", ok5)
    G = sp.Matrix(4, 4, lambda i, j: -d(us, T[j]) / 1)       # tau_i(T_j) = 1 for all i, j
    check("shared clock: Gamma_ij = tau(T_j) = 1 for all pairs (MF6, Gamma = 1)",
          all(x == 1 for x in G))


def main():
    for part in (part_a, part_b, part_c, part_d, part_e, part_f, part_g, part_h, part_i, part_j):
        part()
    n = len(FAILED)
    print(f"\n{'ALL CHECKS PASSED' if n == 0 else f'{n} FAILED: ' + '; '.join(FAILED)}")
    raise SystemExit(1 if n else 0)


if __name__ == "__main__":
    main()
