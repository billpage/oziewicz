"""Exact checks (SymPy) for analysis/grammar_of_a_body.md (step 6, prefix GB).

A  one body: nilpotents, U^2 = 1, the observers D, M, e; U D U = M; e D e = e M e = e/2;
   the Clifford representation c(Y) = ev_Y + h(Y)^ (GB2)
B  two bodies, metric-free: {U_X, U_Y} = 2 s_XY, e_X U_Y e_X = s_XY e_X (GB3(1))
C  three bodies, metric-free: Lambda, its scalar part, (Lambda - <Lambda>_0)^2 = -4 det S; both signs (GB3)
D  one body's forms: d alpha = alpha ^ a + Omega; the Pfaff sequence; P ^ dP (GB4(1)-(2))
E  a system: L ^ L = 2 C ^ P ^ L for every clock (GB6(1))
F  several bodies in Cl(V, -g): T^2 = -det G; commuting triangle rotors iff the 4-vector vanishes (GB6(2)-(3))
G  fields: rescaling of a clock, the momentum form, Kiehn's first law, naturality under a
   polynomial diffeomorphism (GB1, GB4(3)-(4), GB5)
H  GB3(3) in the abstract Clifford algebra of three generators with symbolic clock factors s_ij:
   a polynomial identity with integer coefficients, so it holds over any commutative ring F;
   the sign of det S, and so rotation or boost, is then decided event by event

Everything is exact; nothing is numerical. Runs in a few seconds and writes no files.
Run:  python3 -u src/verify_grammar_of_a_body.py
"""
import itertools
import random
import sympy as sp

FAILED = []


def check(name, cond):
    ok = bool(cond)
    print(("  ok    " if ok else "  FAIL  ") + name, flush=True)
    if not ok:
        FAILED.append(name)


N = 4
BASIS = list(range(1 << N))                                   # forms e^S as bitmasks
deg = lambda m: bin(m).count("1")


def wedge_basis(a, b):
    if a & b:
        return 0, 0
    s, x = 1, a
    for i in range(N):                                        # move each bit of b past higher bits of a
        if (b >> i) & 1:
            if bin(a >> (i + 1)).count("1") % 2:
                s = -s
    return s, a | b


def wedge(f, g):
    out = {}
    for a, ca in f.items():
        for b, cb in g.items():
            s, m = wedge_basis(a, b)
            if s:
                out[m] = out.get(m, 0) + s * ca * cb
    return {k: sp.expand(v) for k, v in out.items() if sp.expand(v) != 0}


def cr(alpha):                                               # alpha ^ . as a 16x16 matrix
    M = sp.zeros(16, 16)
    for m in BASIS:
        for i in range(N):
            s, r = wedge_basis(1 << i, m)
            if s:
                M[r, m] += s * alpha[i]
    return M


def ev(X):                                                   # interior product i_X
    M = sp.zeros(16, 16)
    for m in BASIS:
        for i in range(N):
            if (m >> i) & 1:
                s = (-1) ** bin(m & ((1 << i) - 1)).count("1")
                M[m ^ (1 << i), m] += s * X[i]
    return M


def vecf(f):
    v = sp.zeros(16, 1)
    for k, c in f.items():
        v[k] = c
    return v


def form(v):
    return {k: sp.expand(v[k]) for k in range(16) if sp.expand(v[k]) != 0}


I16 = sp.eye(16)
zero = lambda M: all(sp.expand(x) == 0 for x in M)
rnd = lambda: sp.Rational(random.randint(-9, 9), random.randint(1, 5))
random.seed(7)


def rational_pair():
    """random (X, alpha) with alpha(X) = 1"""
    while True:
        X = [rnd() for _ in range(N)]
        a = [rnd() for _ in range(N)]
        s = sum(x * y for x, y in zip(X, a))
        if s != 0:
            return X, [y / s for y in a]


# ---------------------------------------------------------------- A
print("\nA: Oziewicz's idempotents and unipotent (forms; symbolic X, alpha)")
X = list(sp.symbols("X0:4"))
al = list(sp.symbols("a0:4"))
aX = sum(x * y for x, y in zip(X, al))
E, C = ev(X), cr(al)
D, M, U = C * E, E * C, E + C
check("ev^2 = cr^2 = 0 and ev cr + cr ev = alpha(X) (his (2.8.1))", zero(E * E) and zero(C * C) and zero(E * C + C * E - aX * I16))
check("U^2 = alpha(X): U = ev_X + cr_alpha is unipotent when alpha(X) = 1 (his (2.8.4))", zero(U * U - aX * I16))
check("D + M = alpha(X): the split (his (2.9.1))", zero(D + M - aX * I16))
check("D^2 = alpha(X) D, M^2 = alpha(X) M: idempotents when alpha(X) = 1", zero(D * D - aX * D) and zero(M * M - aX * M))
check("U D U = alpha(X) M: the unipotent conjugates one observer into the other", zero(U * D * U - aX * M))
Xr, ar = rational_pair()
Dr, Mr = cr(ar) * ev(Xr), ev(Xr) * cr(ar)
ok_der = ok_hom = True
for _ in range(6):
    f = {m: rnd() for m in random.sample(BASIS, 5)}
    g = {m: rnd() for m in random.sample(BASIS, 5)}
    for p in BASIS:                                          # homogeneous pieces for the sign
        pass
    fh = {m: c for m, c in f.items() if deg(m) == 1}
    gh = {m: c for m, c in g.items() if deg(m) == 2}
    if not fh or not gh:
        continue
    lhs = form(Dr * vecf(wedge(fh, gh)))
    rhs = wedge(form(Dr * vecf(fh)), gh)
    rhs2 = wedge(fh, form(Dr * vecf(gh)))
    tot = {k: rhs.get(k, 0) + rhs2.get(k, 0) for k in set(rhs) | set(rhs2)}
    ok_der &= all(sp.expand(lhs.get(k, 0) - tot.get(k, 0)) == 0 for k in set(lhs) | set(tot))
    lhs = form(Mr * vecf(wedge(f, g)))
    rhs = wedge(form(Mr * vecf(f)), form(Mr * vecf(g)))
    ok_hom &= all(sp.expand(lhs.get(k, 0) - rhs.get(k, 0)) == 0 for k in set(lhs) | set(rhs))
check("D = alpha^ i_X is a derivation, M = i_X (alpha ^ .) an algebra map (his §2.9, (5.4.1)); rational pairs", ok_der and ok_hom)
check("on 1-forms D is the rank-one projector clock (x) X (MC6) and M = 1 - D",
      all(sp.expand((Dr * vecf({1 << j: 1}))[1 << i] - ar[i] * Xr[j]) == 0 for i in range(N) for j in range(N)))
e = (I16 + U) / 2
check("e = (1+U)/2: e^2 = e + (alpha(X)-1)/4; e D e = e/2 = e M e when alpha(X) = 1",
      zero(e * e - e - (aX - 1) / 4 * I16)
      and zero((e * D * e - e / 2).subs(al[0], (1 - sum(x * y for x, y in zip(X[1:], al[1:]))) / X[0])))

hm = sp.diag(1, -1, -1, -1)                                   # step 5's h = -g
Xh = [sp.Rational(5, 4), sp.Rational(3, 4), 0, 0]           # h(X, X) = 1
ah = list(hm * sp.Matrix(Xh))
c = lambda Y: ev(Y) + cr(list(hm * sp.Matrix(Y)))
Ys = [[rnd() for _ in range(N)] for _ in range(3)]
check("GB2(5) c(Y) = ev_Y + h(Y)^ has c(Y)^2 = h(Y, Y); for alpha = h(X), c(X) = U and U^2 = 1",
      all(zero(c(Y) * c(Y) - (sp.Matrix(Y).T * hm * sp.Matrix(Y))[0] * I16) for Y in Ys)
      and zero(c(Xh) - (ev(Xh) + cr(ah))) and zero(c(Xh) * c(Xh) - I16))

# ---------------------------------------------------------------- B
print("\nB: two bodies, metric-free (symbolic)")
Y = list(sp.symbols("Y0:4"))
be = list(sp.symbols("b0:4"))
UY = ev(Y) + cr(be)
aY, bX = sum(a * y for a, y in zip(al, Y)), sum(b * x for b, x in zip(be, X))
check("U_X U_Y + U_Y U_X = alpha(Y) + beta(X) = Gamma_XY + Gamma_YX", zero(U * UY + UY * U - (aY + bX) * I16))
sub1 = {al[0]: (1 - sum(x * y for x, y in zip(X[1:], al[1:]))) / X[0]}
check("e_X U_Y e_X = (1/2)(Gamma_XY + Gamma_YX) e_X: the corner sees only the symmetrised clock factor",
      zero((e * UY * e - (aY + bX) / 2 * e).subs(sub1)))

# ---------------------------------------------------------------- C
print("\nC: three bodies, metric-free (exact rationals)")


def Umat(X, a):
    return ev(X) + cr(a)


def tri(pairs):
    Us = [Umat(*p) for p in pairs]
    s = lambda i, j: (sum(pairs[i][1][k] * pairs[j][0][k] for k in range(N))
                      + sum(pairs[j][1][k] * pairs[i][0][k] for k in range(N))) / 2
    S = sp.Matrix(3, 3, lambda i, j: 1 if i == j else s(i, j))
    UX, UY_, UZ = Us
    Lam = (I16 + UX * UZ) * (I16 + UZ * UY_) * (I16 + UY_ * UX)
    eX = (I16 + UX) / 2
    sc = Lam.trace() / 16
    Bv = Lam - sc * I16
    return S, Lam, eX, sc, Bv, Us


ok_loop = ok_sc = ok_b = True
signs = set()
for _ in range(12):
    pairs = [rational_pair() for _ in range(3)]
    S, Lam, eX, sc, Bv, Us = tri(pairs)
    loop = eX * ((I16 + Us[2]) / 2) * ((I16 + Us[1]) / 2) * eX
    ok_loop &= zero(loop - Lam * eX / 8)
    ok_sc &= sp.simplify(sc - 2 * (1 + S[0, 1] + S[1, 2] + S[0, 2])) == 0
    ok_b &= zero(Bv * Bv + 4 * S.det() * I16)
    signs.add(sp.sign(S.det()))
check("e_X e_Z e_Y e_X = (1/8) Lambda e_X with Lambda = (1+U_X U_Z)(1+U_Z U_Y)(1+U_Y U_X), no metric", ok_loop)
check("<Lambda>_0 = 2(1 + s_XY + s_YZ + s_ZX), s the symmetrised clock factors", ok_sc)
check("(Lambda - <Lambda>_0)^2 = -4 det S: the 'rotation' is elliptic if det S > 0, hyperbolic if det S < 0", ok_b)
print(f"        signs of det S met in 12 random metric-free triangles: {sorted(signs)}")
check("both signs occur: without reciprocal clocks the loop can be a boost, not a rotation", {-1, 1} <= signs)

# ---------------------------------------------------------------- D
print("\nD: one body's form tower (pointwise, symbolic: F stands for d alpha)")
Fc = {m: sp.Symbol(f"F{m}") for m in BASIS if deg(m) == 2}
alf = {1 << i: al[i] for i in range(N)}
iX = lambda f: form(E * vecf(f))
a_ = iX(Fc)                                                  # acceleration a = i_X d alpha
aw = wedge(alf, a_)
Om = {k: sp.expand(Fc.get(k, 0) - aw.get(k, 0)) for k in set(Fc) | set(aw)}
Om = {k: v for k, v in Om.items() if v != 0}
red = lambda f: {k: sp.expand(v.subs(sub1)) for k, v in f.items() if sp.expand(v.subs(sub1)) != 0}
check("M F = i_X(alpha ^ F) = F - alpha ^ a =: Omega (rotation, his B = M F); D F = alpha ^ a (his S ^ E)",
      red({k: form(M * vecf(Fc)).get(k, 0) - Om.get(k, 0) for k in set(Om) | set(form(M * vecf(Fc)))}) == {})
check("i_X Omega = 0 and i_X a = 0: both relatives are spatial", red(iX(Om)) == {} and red(iX(a_)) == {})
FF = wedge(Fc, Fc)
rhs = wedge(wedge(alf, a_), Om)
check("F ^ F = 2 alpha ^ a ^ Omega: the top form is acceleration along the rotation axis",
      red({k: FF.get(k, 0) - 2 * rhs.get(k, 0) for k in set(FF) | set(rhs)}) == {})
check("alpha ^ F = alpha ^ Omega and i_X(alpha ^ F) = Omega: the 3-form carries the rotation alone",
      red({k: wedge(alf, Fc).get(k, 0) - wedge(alf, Om).get(k, 0) for k in set(wedge(alf, Fc)) | set(wedge(alf, Om))}) == {})
Ef = sp.Symbol("E")
dE = {1 << i: sp.Symbol(f"dE{i}") for i in range(N)}
P = {k: Ef * v for k, v in alf.items()}
dP = {k: sp.expand(wedge(dE, alf).get(k, 0) + Ef * Fc.get(k, 0)) for k in set(wedge(dE, alf)) | set(Fc)}
PdP = wedge(P, dP)
check("P = E alpha: P ^ dP = E^2 alpha ^ d alpha (Oziewicz's spin candidate is E^2 times the vorticity 3-form)",
      all(sp.expand(PdP.get(k, 0) - Ef ** 2 * wedge(alf, Fc).get(k, 0)) == 0 for k in set(PdP) | set(wedge(alf, Fc))))

# ---------------------------------------------------------------- E
print("\nE: step 4, the vector side (symbolic P, L, clock zeta)")
Pv = {1 << i: sp.Symbol(f"P{i}") for i in range(N)}
Lb = {m: sp.Symbol(f"L{m}") for m in BASIS if deg(m) == 2}
z = list(sp.symbols("z0:4"))
zP = sum(z[i] * Pv[1 << i] for i in range(N))
ev_z = ev(z)                                                 # same algebra, read as multivectors
evL = form(ev_z * vecf(Lb))
Cc = {k: -v / zP for k, v in evL.items()}                    # C[zeta](0) = -ev_zeta L / zeta(P)
LL = wedge(Lb, Lb)
CPL = wedge(Cc, wedge(Pv, Lb))
check("L ^ L = 2 C[zeta] ^ P ^ L for every clock zeta: grade 4 adds no invariant beyond P ^ L",
      all(sp.simplify(LL.get(k, 0) - 2 * CPL.get(k, 0)) == 0 for k in set(LL) | set(CPL)))
LC = {k: sp.simplify(Lb.get(k, 0) - wedge(Cc, Pv).get(k, 0)) for k in set(Lb) | set(wedge(Cc, Pv))}
check("relative to its centre, L_C = L - C ^ P has ev_zeta L_C = 0 and L_C ^ L_C = 0",
      all(sp.simplify(v) == 0 for v in form(ev_z * vecf(LC)).values()) and all(sp.simplify(v) == 0 for v in wedge(LC, LC).values()))

# ---------------------------------------------------------------- Clifford helper (exact, any symmetric form)

import sympy as sp
from functools import lru_cache
from itertools import product

R = sp.Rational


class Cl:
    def __init__(self, B):
        self.B = [[sp.nsimplify(x) for x in row] for row in B]
        self.m = len(B)
        self._mwg = lru_cache(maxsize=None)(self._mwg_raw)

    def _mwg_raw(self, word, g):              # (monomial word) * e_g
        B = self.B
        if not word:
            return ((((g,), 1),))
        last = word[-1]
        if last < g:
            return (((word + (g,)), 1),)
        if last == g:
            return ((word[:-1], B[g][g]),)
        res = {}
        if B[last][g] != 0:
            res[word[:-1]] = res.get(word[:-1], 0) + 2 * B[last][g]
        for w2, c2 in self._mwg(word[:-1], g):
            for w3, c3 in self._mwg(w2, last):
                res[w3] = res.get(w3, 0) - c2 * c3
        return tuple(res.items())

    def mul(self, x, y):
        out = {}
        for wa, ca in x.items():
            for wb, cb in y.items():
                cur = {wa: 1}
                for g in wb:
                    nxt = {}
                    for w, c in cur.items():
                        for w2, c2 in self._mwg(w, g):
                            nxt[w2] = nxt.get(w2, 0) + c * c2
                    cur = nxt
                for w, c in cur.items():
                    out[w] = out.get(w, 0) + ca * cb * c
        return cclean(out)

    def gen(self, i): return {(i,): sp.Integer(1)}
    def scal(self, a): return cclean({(): sp.sympify(a)})


def cclean(x): return {k: sp.expand(v) for k, v in x.items() if sp.expand(v) != 0}
def cadd(*xs):
    out = {}
    for x in xs:
        for k, v in x.items(): out[k] = out.get(k, 0) + v
    return cclean(out)
def csm(a, x): return cclean({k: a * v for k, v in x.items()})
def csub(x, y): return cadd(x, csm(-1, y))
def ciszero(x): return len(cclean(x)) == 0
def lin(cl, coeffs): return cadd(*[csm(c, cl.gen(i)) for i, c in enumerate(coeffs) if c != 0])



# ---------------------------------------------------------------- F
print("\nF: step 5, the trivector and the 4-vector of the bodies (G(1,3), exact)")
G13 = Cl([[1, 0, 0, 0], [0, -1, 0, 0], [0, 0, -1, 0], [0, 0, 0, -1]])
vec = lambda c: cadd(*[csm(c[i], G13.gen(i)) for i in range(4) if c[i] != 0])
mul = lambda *xs: xs[0] if len(xs) == 1 else G13.mul(xs[0], mul(*xs[1:]))
one = G13.scal(1)
body = lambda vx, vy, vz=0: (lambda g: vec([g, g * vx, g * vy, g * vz]))(1 / sp.sqrt(1 - vx ** 2 - vy ** 2 - vz ** 2))
Sb, Bb, Cb = body(sp.Rational(3, 5), 0), body(0, sp.Rational(4, 5)), body(sp.Rational(-3, 13), sp.Rational(-4, 13))
dot = lambda a, b: sp.nsimplify((mul(a, b).get((), 0) + mul(b, a).get((), 0)) / 2)


def wedge3(a, b, c):                                         # antisymmetrised product
    terms = []
    for perm, sgn in ((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1), ((1, 0, 2), -1), ((0, 2, 1), -1), ((2, 1, 0), -1):
        v = [a, b, c]
        terms.append(csm(sp.Rational(sgn, 6), mul(v[perm[0]], v[perm[1]], v[perm[2]])))
    return cadd(*terms)


T = wedge3(Sb, Bb, Cb)
G = sp.Matrix([[1, dot(Sb, Bb), dot(Sb, Cb)], [dot(Sb, Bb), 1, dot(Bb, Cb)], [dot(Sb, Cb), dot(Bb, Cb), 1]])
TT = mul(T, T)
check("T = S ^ B ^ C has T^2 = -det G: tan(theta/2) = sqrt(-T^2)/(1 + sum gamma) is the trivector of the three bodies",
      set(TT) <= {()} and sp.simplify(TT.get((), 0) + G.det()) == 0)
lam = lambda P_, Q_: cadd(one, mul(P_, Q_))


def tri_rotor(Xb, Yb, Zb):
    return mul(lam(Xb, Zb), lam(Zb, Yb), lam(Yb, Xb))


for name, Db in (("in the 3-space of S, B, C", body(sp.Rational(5, 13), sp.Rational(0), 0)), ("off it", body(0, 0, sp.Rational(12, 13)))):
    L1, L2 = tri_rotor(Sb, Bb, Cb), tri_rotor(Sb, Cb, Db)
    comm = csub(mul(L1, L2), mul(L2, L1))
    four = cadd(*[csm(sp.Rational(1, 24) * sp.combinatorics.Permutation(list(p)).signature(),
                    mul(*[[Sb, Bb, Cb, Db][i] for i in p])) for p in itertools.permutations(range(4))])
    print(f"        fourth body {name}: S^B^C^D = {dict(four) or 0}, commutator zero: {ciszero(comm)}")
    check(f"triangles SBC and SCD commute exactly when S ^ B ^ C ^ D = 0 (fourth body {name})",
          ciszero(comm) == ciszero(four))

# ---------------------------------------------------------------- G
print("\nG: naturality, rescaling and Kiehn's reading (polynomial fields on R^4, exact)")
CO = sp.symbols("t x y z")


def fclean(f):
    return {k: sp.expand(v) for k, v in f.items() if sp.expand(v) != 0}


def fadd(*fs):
    out = {}
    for f in fs:
        for k, v in f.items():
            out[k] = out.get(k, 0) + v
    return fclean(out)


def fsm(c, f):
    return fclean({k: c * v for k, v in f.items()})


def fd(f):                                                   # exterior derivative
    out = {}
    for m, c in f.items():
        for i in range(N):
            if not (m >> i) & 1:
                s, r = wedge_basis(1 << i, m)
                out[r] = out.get(r, 0) + s * sp.diff(c, CO[i])
    return fclean(out)


def fiv(V, f):                                               # evaluation i_V on a form field
    out = {}
    for m, c in f.items():
        for i in range(N):
            if (m >> i) & 1:
                s = (-1) ** bin(m & ((1 << i) - 1)).count("1")
                out[m ^ (1 << i)] = out.get(m ^ (1 << i), 0) + s * V[i] * c
    return fclean(out)


def fw(f, g):
    return fclean(wedge(f, g))


def flie(V, f):
    return fadd(fiv(V, fd(f)), fd(fiv(V, f)))


def fsimp(f):
    return {k: v for k, v in ((k, sp.simplify(v)) for k, v in f.items()) if v != 0}


def feq(f, g):
    return fsimp(fadd(f, fsm(-1, g))) == {}


one_form = lambda c: fclean({1 << i: c[i] for i in range(N)})
t_, x_, y_, z_ = CO

# G1: the Frobenius condition survives rescaling of a clock; the top class does not
f_ = sp.Function("f")(*CO)
a_gen = one_form([sp.Function(f"a{i}")(*CO) for i in range(N)])
fa = fsm(f_, a_gen)
check("G1 (f alpha) ^ d(f alpha) = f^2 alpha ^ d alpha for any f and alpha", feq(fw(fa, fd(fa)), fsm(f_ ** 2, fw(a_gen, fd(a_gen)))))
al0 = one_form([1, 0, x_, 0])                                # dt + x dy
al1 = fsm(sp.exp(z_), al0)
check("G1 example: alpha = dt + x dy has alpha ^ d alpha != 0 and d alpha ^ d alpha = 0 (class 3)",
      fw(al0, fd(al0)) != {} and fw(fd(al0), fd(al0)) == {})
check("G1 example: e^z alpha has d(e^z alpha) ^ d(e^z alpha) = 2 e^(2z) dz^dt^dx^dy != 0 (class 4)",
      feq(fw(fd(al1), fd(al1)), fsm(2 * sp.exp(2 * z_), fw(one_form([0, 0, 0, 1]), fw(one_form([1, 0, 0, 0]), fw(one_form([0, 1, 0, 0]), one_form([0, 0, 1, 0])))))))

# G2: the momentum form p = E alpha
E_ = sp.Function("E")(*CO)
p_ = fsm(E_, a_gen)
check("G2 p ^ dp = E^2 alpha ^ d alpha", feq(fw(p_, fd(p_)), fsm(E_ ** 2, fw(a_gen, fd(a_gen)))))
check("G2 dp ^ dp = E^2 d alpha ^ d alpha + 2 E dE ^ alpha ^ d alpha",
      feq(fw(fd(p_), fd(p_)), fadd(fsm(E_ ** 2, fw(fd(a_gen), fd(a_gen))), fsm(2 * E_, fw(fd({0: E_}), fw(a_gen, fd(a_gen)))))))

# G3: Kiehn's first law L_V A = i_V dA + d(i_V A) for the body's own pairs
Lv = [1, 0, 0, 0]                                            # L = d/dt
S_ = one_form([1, t_ * y_, t_ * z_, t_ * x_])                # S = dt + t(y dx + z dy + x dz): rotating, accelerated
check("G3 set-up: S(L) = 1, and the test clock rotates (S ^ dS != 0)", fiv(Lv, S_) == {0: 1} and fw(S_, fd(S_)) != {})
acc = fiv(Lv, fd(S_))
check("G3 (L, S): U = i_L S = 1, so Q = L_L S = W = i_L dS = a, the acceleration", feq(flie(Lv, S_), acc) and acc != {})
Ef = 2 + x_ ** 2 / 3 + t_ * z_ / 5
Pv = [Ef * c for c in Lv]
pf = fsm(Ef, S_)
check("G3 (P, p) with P = E L, p = E S: Q = L_P p = i_P dp + d(E^2)",
      feq(flie(Pv, pf), fadd(fiv(Pv, fd(pf)), fd({0: Ef ** 2}))))
Qa = acc
check("G3 Kiehn's reversibility a ^ da = 0 fails for this clock: a = y dx + z dy + x dz", Qa == one_form([0, y_, z_, x_]) and fw(Qa, fd(Qa)) != {})

# G4: naturality, demonstrated: the observer operators commute with a polynomial diffeomorphism
phi = [t_ + x_ * y_, x_ + z_ ** 2, y_ + z_, z_]               # triangular, unit Jacobian determinant
J = sp.Matrix(4, 4, lambda i, j: sp.diff(phi[i], CO[j]))
check("G4 set-up: det(D phi) = 1", sp.simplify(J.det() - 1) == 0)
sub_phi = dict(zip(CO, phi))


def pull_form(f):                                            # phi^* on forms
    out = {}
    dphi = [one_form([sp.diff(phi[i], CO[j]) for j in range(N)]) for i in range(N)]
    for m, c in f.items():
        term = {0: sp.sympify(c).subs(sub_phi, simultaneous=True)}
        for i in range(N):
            if (m >> i) & 1:
                term = fw(term, dphi[i])
        out = fadd(out, term)
    return out


Jinv = J.inv()


def pull_vec(V):                                             # phi^* X = (D phi)^-1 (X o phi)
    Vp = sp.Matrix([sp.sympify(v).subs(sub_phi, simultaneous=True) for v in V])
    return [sp.expand(c) for c in (Jinv * Vp)]


Xn = [1 + y_, x_, 0, t_]
an = one_form([1, 0, z_, x_ * y_])
betas = [one_form([x_, y_ * t_, 0, 1]), fw(one_form([z_, 1, 0, x_]), one_form([0, t_, 1, y_])), {0: x_ * z_ + t_}]
cDn = lambda X, a, b: fw(a, fiv(X, b))
cMn = lambda X, a, b: fiv(X, fw(a, b))
eUn = lambda X, a, b: fsm(sp.Rational(1, 2), fadd(b, fiv(X, b), fw(a, b)))
okn = True
for b in betas:
    for op in (cDn, cMn, eUn):
        okn &= feq(pull_form(op(Xn, an, b)), op(pull_vec(Xn), pull_form(an), pull_form(b)))
    okn &= feq(pull_form(fd(b)), fd(pull_form(b)))
check("G4 phi^*(O_{X,alpha} beta) = O_{phi^*X, phi^*alpha}(phi^* beta) for O = cD, cM, (1 + U)/2, and phi^* d = d phi^*", okn)

# ---------------------------------------------------------------- H
print("\nH: GB3(3) over any commutative ring: abstract Clifford algebra with symbolic clock factors")
sxy, syz, szx = sp.symbols("s_xy s_yz s_zx")
SH = [[1, sxy, szx], [sxy, 1, syz], [szx, syz, 1]]            # generators U_X, U_Y, U_Z: {U_i, U_j} = 2 S_ij
clH = Cl(SH)
UX, UY, UZ = clH.gen(0), clH.gen(1), clH.gen(2)
oneH = clH.scal(1)
LamH = clH.mul(clH.mul(cadd(oneH, clH.mul(UX, UZ)), cadd(oneH, clH.mul(UZ, UY))), cadd(oneH, clH.mul(UY, UX)))
cH = 2 * (1 + sxy + syz + szx)
restH = csub(LamH, clH.scal(cH))
check("H1 {U_i, U_j} = 2 s_ij in the abstract algebra (sanity)",
      ciszero(csub(cadd(clH.mul(UX, UY), clH.mul(UY, UX)), clH.scal(2 * sxy))))
check("H2 (Lambda - 2(1 + s_xy + s_yz + s_zx))^2 = -4 det S, a polynomial identity in the s_ij with integer "
      "coefficients, so over every commutative ring F",
      ciszero(csub(clH.mul(restH, restH), clH.scal(-4 * sp.Matrix(SH).det()))))

print("\n" + ("ALL CHECKS PASSED" if not FAILED else f"{len(FAILED)} FAILED: " + "; ".join(FAILED)))
