"""Exact checks for supplement/magnetismo.md (Oziewicz, Magnetismo e Electricidad, 2020).

All parts are exact (SymPy); nothing here is numerical. Equation numbers are those of the
version of 18 July 2020 (chapters 4 and 7); labels MG1-MG5 are the supplement's.

Forms on R^4 with coordinates (t, x, y, z) are dicts {bitmask: coefficient}; bit i is
d(coordinate i). A body is a vector field L with a clock 1-form S, S(L) = 1; on forms
cD = cr_S ev_L (derivation) and cM = ev_L cr_S (algebra map), U = ev_L + cr_S.

Parts
  Chapter 4  (MG1) nilpotents, (4.7.1), U^2 = 1, the four idempotents, derivation and
             algebra-map properties, U cD U = cM: first spot-checked with random rationals,
             then symbolically, with generic X, alpha and generic forms, as polynomial
             identities with integer coefficients (and 1/2 for e) modulo alpha X - 1; so they
             hold over every commutative ring F (with 2 invertible for e), F-linearly, in a free
             module of rank 4. For any module they follow from (4.7.1) by the hand proofs cited
             in the supplement.
  Chapter 7  (MG2) places and simultaneity, (7.4.7) against (7.4.2)/(7.4.5);
             (MG3) cM d cD beta = (cM dS) ^ ev_L beta, so the private differential exists iff
             S ^ dS = 0; (MG4) the split of F and dF = 0 for a rotating, accelerated clock;
             (MG5) the metric intertwining (7.11.4) needs alpha = gX

Run:  PYTHONPATH=src python3 -u src/verify_magnetismo.py
Writes no files.
"""

import itertools
import random
import sympy as sp

random.seed(11)
t, x, y, z = X4 = sp.symbols("t x y z")
N = 4
FAILED = []


def check(name, cond):
    ok = bool(cond)
    print(("  ok    " if ok else "  FAIL  ") + name, flush=True)
    if not ok:
        FAILED.append(name)


def clean(f):
    out = {}
    for k, v in f.items():
        v = sp.expand(v)
        if v != 0:
            out[k] = v
    return out


def add(*fs):
    out = {}
    for f in fs:
        for k, v in f.items():
            out[k] = out.get(k, 0) + v
    return clean(out)


def sm(c, f):
    return clean({k: c * v for k, v in f.items()})


def sign_merge(a, b):
    s = 1
    for i in range(N):
        if (b >> i) & 1 and bin(a >> (i + 1)).count("1") % 2:
            s = -s
    return s


def wedge(f, g):
    out = {}
    for a, ca in f.items():
        for b, cb in g.items():
            if a & b == 0:
                m = a | b
                out[m] = out.get(m, 0) + sign_merge(a, b) * ca * cb
    return clean(out)


def iv(V, f):
    """interior product (evaluation) ev_V with a vector field V = [V^t, V^x, V^y, V^z]"""
    out = {}
    for m, c in f.items():
        for i in range(N):
            if (m >> i) & 1:
                s = (-1) ** bin(m & ((1 << i) - 1)).count("1")
                out[m ^ (1 << i)] = out.get(m ^ (1 << i), 0) + s * V[i] * c
    return clean(out)


def d(f):
    out = {}
    for m, c in f.items():
        for i in range(N):
            if not (m >> i) & 1:
                dc = sp.diff(c, X4[i])
                if dc != 0:
                    s = sign_merge(1 << i, m)
                    out[m | (1 << i)] = out.get(m | (1 << i), 0) + s * dc
    return clean(out)


def form1(c):
    return clean({1 << i: c[i] for i in range(N)})


def lie(V, f):
    return add(iv(V, d(f)), d(iv(V, f)))


def eq(f, g):
    return add(f, sm(-1, g)) == {}


def deg(m):
    return bin(m).count("1")


def homog(f, k):
    return {m: c for m, c in f.items() if deg(m) == k}


rnd = lambda: sp.Rational(random.randint(-9, 9), random.randint(1, 4))


def rform(k=None, poly=False):
    def coeff():
        if not poly:
            return rnd()
        return sum(rnd() * mono for mono in (1, t, x, y * z, t * x, z ** 2))
    ms = [m for m in range(16) if k is None or deg(m) == k]
    return clean({m: coeff() for m in random.sample(ms, min(len(ms), 5))})


# ---------------------------------------------------------------------------------------------- chapter 4
print("\nChapter 4: nilpotents, unipotents, idempotents (constant coefficients, exact rationals)")
Xv = [rnd() for _ in range(N)]
al = [rnd() for _ in range(N)]
s0 = sum(a * b for a, b in zip(al, Xv))
al = [a / s0 for a in al]                                     # alpha X = 1
A1 = form1(al)
cr = lambda f: wedge(A1, f)
ev = lambda f: iv(Xv, f)
cD = lambda f: cr(ev(f))
cM = lambda f: ev(cr(f))
U = lambda f: add(ev(f), cr(f))
tests = [rform() for _ in range(6)]
check("(4.6.1) ev_X^2 = cr_alpha^2 = 0", all(ev(ev(f)) == {} and cr(cr(f)) == {} for f in tests))
ok = True
for r in (1, 2, 3):
    for _ in range(3):
        b = rform(r); f = rform()
        lhs = ev(wedge(b, f))
        rhs = add(wedge(ev(b), f), sm((-1) ** r, wedge(b, ev(f))))
        ok &= eq(lhs, rhs)
check("(4.7.1) ev_X o cr_beta = cr_(ev_X beta) + (-1)^r cr_beta o ev_X, r = 1, 2, 3", ok)
check("(4.7.5), (4.7.7) U^2 = (alpha X) id with U = ev_X + cr_alpha", all(eq(U(U(f)), f) for f in tests))
check("(4.7.8), (4.7.10) ev cr ev = ev, cr ev cr = cr (alpha X = 1)",
      all(eq(ev(cr(ev(f))), ev(f)) and eq(cr(ev(cr(f))), cr(f)) for f in tests))
check("(4.8) cD^2 = cD, cM^2 = cM, cD + cM = id", all(eq(cD(cD(f)), cD(f)) and eq(cM(cM(f)), cM(f)) and eq(add(cD(f), cM(f)), f) for f in tests))
ok_der = ok_hom = True
for _ in range(8):
    f, g = rform(random.randint(0, 3)), rform(random.randint(0, 3))
    ok_der &= eq(cD(wedge(f, g)), add(wedge(cD(f), g), wedge(f, cD(g))))
    ok_hom &= eq(cM(wedge(f, g)), wedge(cM(f), cM(g)))
check("(4.8), (7.4.1) cD = cr_alpha ev_X is an (even) derivation, cM = ev_X cr_alpha an algebra map", ok_der and ok_hom)
ok5 = all(cM(cr(f)) == {} and eq(cr(cM(f)), cr(f)) and eq(cD(cr(f)), cr(f)) and eq(ev(cD(f)), ev(f)) and eq(cM(ev(f)), ev(f))
          and cD(ev(f)) == {} and ev(cM(f)) == {} for f in tests)
check("(5.2.9)-(5.2.10) on forms, composed in the reverse of the printed order: cM cr = 0, cr cM = cD cr = cr, ev cD = cM ev = ev", ok5)
e = lambda f: sm(sp.Rational(1, 2), add(f, U(f)))
check("e = (1 + U)/2 (not in the text): e^2 = e and e cD e = e cM e = e/2",
      all(eq(e(e(f)), e(f)) and eq(e(cD(e(f))), sm(sp.Rational(1, 2), e(f))) and eq(e(cM(e(f))), sm(sp.Rational(1, 2), e(f))) for f in tests))
check("UDU = M: the unipotent conjugates one idempotent into the other (not stated in the text)",
      all(eq(U(cD(U(f))), cM(f)) for f in tests))
# the vector side is the same algebra with the roles of vectors and covectors exchanged: nothing new to check.

# ------------------------------------------------------------------------- chapter 4, over any commutative ring
print("\nChapter 4 again, symbolically: generic X, alpha and generic forms; identities modulo alpha X - 1")
Xs = list(sp.symbols("X0:4"))
As = list(sp.symbols("a0:4"))
sX = sum(a * b for a, b in zip(As, Xs))                       # alpha X, kept as a symbol-polynomial
GENS = As + Xs


def gform(name, k=None):
    return {m: sp.Symbol(f"{name}{m}") for m in range(16) if k is None or deg(m) == k}


def zero_mod(f):
    """every coefficient lies in the ideal (alpha X - 1) of Z[1/2][X, alpha, form coefficients]"""
    for c in f.values():
        q, r = sp.reduced(sp.expand(c), [sX - 1], *GENS, order="lex")
        if sp.expand(r) != 0:
            return False
    return True


crS = lambda f: wedge(form1(As), f)
evS = lambda f: iv(Xs, f)
DS = lambda f: crS(evS(f))
MS = lambda f: evS(crS(f))
US = lambda f: add(evS(f), crS(f))
eS = lambda f: sm(sp.Rational(1, 2), add(f, US(f)))
fg, gg = gform("f"), gform("g")
check("symbolic (4.6.1) ev_X^2 = cr_alpha^2 = 0", evS(evS(fg)) == {} and crS(crS(fg)) == {})
check("symbolic (4.7.1) ev_X cr_alpha + cr_alpha ev_X = (alpha X) id, exactly",
      eq(add(evS(crS(fg)), crS(evS(fg))), sm(sX, fg)))
ok = all(eq(evS(wedge(gform("b", r), fg)), add(wedge(evS(gform("b", r)), fg), sm((-1) ** r, wedge(gform("b", r), evS(fg)))))
         for r in (1, 2, 3))
check("symbolic (4.7.1) ev_X o cr_beta = cr_(ev_X beta) + (-1)^r cr_beta o ev_X, generic beta of degree 1, 2, 3", ok)
check("symbolic U^2 = (alpha X) id, D^2 = (alpha X) D, M^2 = (alpha X) M, D + M = (alpha X) id, exactly",
      eq(US(US(fg)), sm(sX, fg)) and eq(DS(DS(fg)), sm(sX, DS(fg))) and eq(MS(MS(fg)), sm(sX, MS(fg)))
      and eq(add(DS(fg), MS(fg)), sm(sX, fg)))
check("symbolic D is an even derivation, exactly; M is an algebra map modulo alpha X - 1",
      eq(DS(wedge(fg, gg)), add(wedge(DS(fg), gg), wedge(fg, DS(gg))))
      and zero_mod(add(MS(wedge(fg, gg)), sm(-1, wedge(MS(fg), MS(gg))))))
check("symbolic (5.2.9)-(5.2.10) reversed, modulo alpha X - 1",
      MS(crS(fg)) == {} and zero_mod(add(crS(MS(fg)), sm(-1, crS(fg)))) and zero_mod(add(DS(crS(fg)), sm(-1, crS(fg))))
      and zero_mod(add(evS(DS(fg)), sm(-1, evS(fg)))) and zero_mod(add(MS(evS(fg)), sm(-1, evS(fg))))
      and DS(evS(fg)) == {} and evS(MS(fg)) == {})
check("symbolic U D U = M and e^2 = e, e D e = e M e = e/2, modulo alpha X - 1",
      zero_mod(add(US(DS(US(fg))), sm(-1, MS(fg)))) and zero_mod(add(eS(eS(fg)), sm(-1, eS(fg))))
      and zero_mod(add(eS(DS(eS(fg))), sm(sp.Rational(-1, 2), eS(fg))))
      and zero_mod(add(eS(MS(eS(fg))), sm(sp.Rational(-1, 2), eS(fg)))))

# ---------------------------------------------------------------------------------------------- chapter 7
print("\nChapter 7: a body with a clock field S and its Length L, S(L) = 1 (polynomial fields)")
# Length L and clock S, deliberately non-inertial: S is neither closed nor Frobenius.
L = [1 + x * y / 7, y / 3, -t / 5, x / 2]
S0 = [1, t * z / 2, x - y, 3 * z * t / 4]
norm = sum(a * b for a, b in zip(S0, L))
S = form1([sp.simplify(c / norm) for c in S0])
check("set-up: S(L) = 1", sp.simplify(iv(L, S).get(0, 0) - 1) == 0)
crS = lambda f: wedge(S, f)
evL = lambda f: iv(L, f)
DD = lambda f: crS(evL(f))
MM = lambda f: evL(crS(f))


def simp(f):
    return clean({k: sp.simplify(v) for k, v in f.items()})


def seq(f, g):
    return simp(add(f, sm(-1, g))) == {}


fields = [rform(k, poly=True) for k in (0, 1, 2, 3)]
dx = {1 << 1: 1}
check("(7.3.5) cM(dx) = dx for L = d/dt, clock dt (adapted coordinates)",
      eq(iv([1, 0, 0, 0], wedge({1: 1}, dx)), dx))
check("(7.6.1, item 7.6.1) cM o ev_L = ev_L", all(seq(MM(evL(f)), evL(f)) for f in fields))
# (7.4.2) and (7.4.5) against (7.4.7)
ok747 = all(seq(DD(f), {}) == seq(evL(f), {}) for f in fields) and all(seq(MM(crS(f)), {}) for f in fields)
check("(7.4.7) ev_L beta = 0 <=> cD beta = 0, and cM kills every S ^ gamma", ok747)
dxL = {1 << 1: 1}
Ls = [1, 0, 0, 0]
cMa = lambda f: iv(Ls, wedge({1: 1}, f))
check("(7.4.2) as printed fails: alpha = dx has ev_L alpha = 0 but cM alpha = dx != 0 (clock dt, L = d/dt)",
      iv(Ls, dxL) == {} and cMa(dxL) == dxL)
check("(7.4.5) as printed fails: beta = dx has cD beta = 0 but dt ^ beta != 0",
      wedge({1: 1}, iv(Ls, dxL)) == {} and wedge({1: 1}, dxL) != {})
# the private differential: M d D beta = (M dS) ^ ev_L beta for every beta
ok = all(seq(MM(d(DD(f))), wedge(MM(d(S)), evL(f))) for f in fields)
check("cM d cD beta = (cM dS) ^ ev_L beta: d_M exists iff cM dS = ev_L(S ^ dS) = 0", ok)
check("(7.8.5) (cM d cD) S = ev_L(S ^ dS) = dS - S ^ L_L S",
      seq(MM(d(DD(S))), evL(wedge(S, d(S)))) and seq(evL(wedge(S, d(S))), add(d(S), sm(-1, wedge(S, lie(L, S))))))
check("cM dS = 0 <=> S ^ dS = 0 (Frobenius): checked on the identity S ^ cM dS = S ^ dS",
      seq(wedge(S, MM(d(S))), wedge(S, d(S))))
check("the test body is rotating: cM dS != 0", not seq(MM(d(S)), {}))
# Maxwell split with a general clock
Apot = rform(1, poly=True)
F = d(Apot)
E = evL(F)
B = MM(F)
check("(7.9.2) F = cM F + cD F, cD F = S ^ E_L", seq(F, add(B, crS(E))) and seq(DD(F), crS(E)))
check("(7.9.7)-(7.9.8) cD E = cD B = 0, ev_L E = ev_L B = 0",
      all(seq(g, {}) for g in (DD(E), DD(B), evL(E), evL(B))))
check("(7.9.9)-(7.9.10) L_L B = ev_L dB, L_L E = ev_L dE", seq(lie(L, B), evL(d(B))) and seq(lie(L, E), evL(d(E))))
check("(7.9.11) cM E_L = E_L", seq(MM(E), E))
check("(7.6.2) dF = 0 splits: cM dF = 0 and ev_L dF = 0", seq(MM(d(F)), {}) and seq(evL(d(F)), {}))
r774 = add(lie(L, B), sm(-1, MM(d(E))), wedge(lie(L, S), E))
check("(7.7.4) L_L B - cM dE + (L_L S) ^ E = 0 for any clock (Faraday, with the acceleration term)", seq(r774, {}))
r768 = add(lie(L, B), sm(-1, MM(d(E))))
check("(7.6.8) without the (L_L S) ^ E term fails for this accelerated clock", not seq(r768, {}))
Om = MM(d(S))
check("MG4 magnetic Gauss for any clock: cM dB + (cM dS) ^ E_L = 0 (so d_M B = 0 needs cM dS = 0)",
      seq(add(MM(d(B)), wedge(Om, E)), {}) and not seq(MM(d(B)), {}))
check("(7.12.7) L_V = ev_V d + d ev_V = (d + ev_V)^2 (Cartan)",
      all(seq(lie(L, f), add(d(d(f)), d(evL(f)), evL(d(f)), evL(evL(f)))) for f in fields))

# (7.11.4): g o U = cU o g needs the clock to be the metric dual of X with g(X, X) = 1
print("\n(7.11.4) intertwining by the metric (constant coefficients)")
g = sp.diag(-1, 1, 1, 1)
Xc = [sp.Rational(5, 4), sp.Rational(3, 4), 0, 0]              # g(X, X) = -1
gX = list(g * sp.Matrix(Xc))


def lam_g(V):                                                  # Lambda g on a multivector {mask: coeff} -> form
    out = {}
    for m, c in V.items():
        idx = [i for i in range(N) if (m >> i) & 1]
        for perm_idx in itertools.product(range(N), repeat=len(idx)):
            if len(set(perm_idx)) < len(idx):
                continue
            coeff = c
            for a, b in zip(idx, perm_idx):
                coeff *= g[a, b]
            if coeff == 0:
                continue
            mask = 0
            for b in perm_idx:
                mask |= 1 << b
            order = sorted(perm_idx)
            sgn = sp.combinatorics.Permutation([order.index(b) for b in perm_idx]).signature()
            out[mask] = out.get(mask, 0) + sgn * coeff
    return clean(out)


Vs = [rform() for _ in range(4)]                               # same dict format read as multivectors
for name, clk in (("clock = gX/(gX)X (Oziewicz's (7.11.2))", [c / sum(a * b for a, b in zip(gX, Xc)) for c in gX]),
                  ("clock = gX", gX)):
    # vector side U = ev_alpha + cr_X with alpha = clk; form side cU = ev_X + cr_alpha
    U_vec = lambda V: add(iv(clk, V), wedge(form1(Xc), V))
    U_form = lambda f: add(iv(Xc, f), wedge(form1(clk), f))
    ok = all(eq(lam_g(U_vec(V)), U_form(lam_g(V))) for V in Vs)
    print(f"        {name}: g o U = cU o g holds: {ok}")
    if name.startswith("clock = gX/"):
        check("(7.11.4) g o U = cU o g needs alpha = gX, i.e. g(X,X) = 1; with g(X,X) = -1 it fails under (7.11.2)", not ok)

print("\n" + ("ALL CHECKS PASSED" if not FAILED else f"{len(FAILED)} FAILED: " + "; ".join(FAILED)))
