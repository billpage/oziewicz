"""Companion script for supplement/cartan_calculus_in_sympy.md (prefix CT).

A minimal version of the exterior-calculus machinery that the other verify_*.py scripts
each re-implement, with exact checks of the identities the tutorial states. The tutorial
quotes the functions below; the section letters match its sections.

  A  two key encodings of a form (sorted tuples, bitmasks) give the same wedge product
  B  the Grassmann algebra: associativity, graded commutativity, alpha ^ alpha = 0
  C  the interior product: i_X i_X = 0, the antiderivation rule (Oziewicz (4.7.1))
  D  the exterior derivative: d^2 = 0, Leibniz rule, df = f_i dx^i
  E  Cartan's calculus: L_X = i_X d + d i_X, [L_X, d] = 0, [L_X, i_Y] = i_[X,Y],
     [L_X, L_Y] = L_[X,Y], L_X a derivation
  F  operators as 2^n x 2^n matrices: CAR, ev = transpose of cr, U^2 = alpha(X), D, M
  G  the Clifford product on the same space: {gamma_i, gamma_j} = phi_ij + phi_ji; the blade table
  H  a body in flow-box coordinates: a, Omega, i_X Omega = 0; a class-3 clock
  I  naturality under a polynomial diffeomorphism
  J  identities that need alpha(X) = 1: exactly with s = alpha(X), and modulo s - 1

Everything is exact (SymPy); nothing is numerical. Writes no files. A few seconds.
Run:  PYTHONPATH=src python3 -u src/verify_cartan_tutorial.py
"""
import random

import sympy as sp

FAILED = []


def check(name, cond):
    ok = bool(cond)
    print(("  ok    " if ok else "  FAIL  ") + name, flush=True)
    if not ok:
        FAILED.append(name)


# ---------------------------------------------------------------- forms as {bitmask: coefficient}
def bits(m):
    """indices i with bit i set in m, increasing"""
    return [i for i in range(m.bit_length()) if m >> i & 1]


def clean(f):
    """canonical form: expanded coefficients, zeros dropped"""
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


def eq(f, g):
    return add(f, sm(-1, g)) == {}


def sign_merge(a, b):
    """sign of dx^a ^ dx^b = sign * dx^(a|b), a & b == 0: (-1)^(pairs i in a, j in b, i > j)"""
    s = 1
    for j in bits(b):
        if bin(a >> (j + 1)).count("1") % 2:
            s = -s
    return s


def wedge(f, g):
    out = {}
    for a, ca in f.items():
        for b, cb in g.items():
            if a & b == 0:
                out[a | b] = out.get(a | b, 0) + sign_merge(a, b) * ca * cb
    return clean(out)


def iv(V, f):
    """interior product i_V: contracts the first slot, sign (-1)^(position of i)"""
    out = {}
    for m, c in f.items():
        for i in bits(m):
            s = (-1) ** bin(m & ((1 << i) - 1)).count("1")
            out[m ^ 1 << i] = out.get(m ^ 1 << i, 0) + s * V[i] * c
    return clean(out)


def d(f, xs):
    """exterior derivative: d(c dx^m) = sum_i (d_i c) dx^i ^ dx^m"""
    out = {}
    for m, c in f.items():
        for i, x in enumerate(xs):
            if not m >> i & 1:
                s = sign_merge(1 << i, m)
                out[m | 1 << i] = out.get(m | 1 << i, 0) + s * sp.diff(c, x)
    return clean(out)


def lie(V, f, xs):
    """Cartan's formula L_V = i_V d + d i_V"""
    return add(iv(V, d(f, xs)), d(iv(V, f), xs))


def bracket(U, V, xs):
    """[U, V]^i = U^j d_j V^i - V^j d_j U^i"""
    n = len(xs)
    return [sp.expand(sum(U[j] * sp.diff(V[i], xs[j]) - V[j] * sp.diff(U[i], xs[j])
                          for j in range(n))) for i in range(n)]


def form1(c):
    return clean({1 << i: ci for i, ci in enumerate(c)})


def deg(m):
    return bin(m).count("1")


# ---------------------------------------------------------------- forms as {sorted tuple: coefficient}
def perm_sign(seq):
    s, seq = 1, list(seq)
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]:
                s = -s
    return s


def wedge_t(f, g):
    out = {}
    for a, ca in f.items():
        for b, cb in g.items():
            if set(a) & set(b):
                continue
            k = tuple(sorted(a + b))
            out[k] = out.get(k, 0) + perm_sign(a + b) * ca * cb
    return clean(out)


to_tuple = lambda f: {tuple(bits(m)): c for m, c in f.items()}
to_mask = lambda f: {sum(1 << i for i in k): c for k, c in f.items()}

# ---------------------------------------------------------------- test data
random.seed(5)
rnd = lambda: sp.Rational(random.randint(-9, 9), random.randint(1, 4))
t, x, y, z = XS = sp.symbols("t x y z")
N = 4


def rform(k=None, n=N):
    ms = [m for m in range(1 << n) if k is None or deg(m) == k]
    return clean({m: rnd() for m in random.sample(ms, min(len(ms), 5))})


def gform(name, k=None, n=N, args=None):
    """generic form: one independent symbol (or undefined function of args) per basis element"""
    mk = (lambda s: sp.Function(s)(*args)) if args else sp.Symbol
    return {m: mk(f"{name}{m}") for m in range(1 << n) if k is None or deg(m) == k}


# ---------------------------------------------------------------- A
print("A  two key encodings")
check("A1 dx^1 ^ dx^3 times dx^0 ^ dx^2 = -dx^0 ^ dx^1 ^ dx^2 ^ dx^3 (three inversions)",
      wedge({0b1010: 1}, {0b0101: 1}) == {0b1111: -1} and wedge_t({(1, 3): 1}, {(0, 2): 1}) == {(0, 1, 2, 3): -1})
okA = all(to_mask(wedge_t(to_tuple(f), to_tuple(g))) == wedge(f, g)
          for f, g in ((rform(), rform()) for _ in range(20)))
check("A2 the tuple and bitmask wedge agree on 20 random pairs of forms on R^4", okA)
okA3 = all(to_mask(wedge_t(to_tuple(gform("f", p)), to_tuple(gform("g", q)))) == wedge(gform("f", p), gform("g", q))
           for p in range(5) for q in range(5))
check("A3 ... and on generic forms of every pair of degrees (symbolic coefficients)", okA3)

# ---------------------------------------------------------------- B
print("B  the Grassmann algebra")
f, g, h = gform("f"), gform("g"), gform("h")
check("B1 associativity (f ^ g) ^ h = f ^ (g ^ h), generic inhomogeneous forms", eq(wedge(wedge(f, g), h), wedge(f, wedge(g, h))))
check("B2 graded commutativity f ^ g = (-1)^(pq) g ^ f, generic homogeneous forms, all p, q",
      all(eq(wedge(gform("f", p), gform("g", q)), sm((-1) ** (p * q), wedge(gform("g", q), gform("f", p))))
          for p in range(5) for q in range(5)))
a1 = gform("a", 1)
check("B3 alpha ^ alpha = 0 for a generic 1-form; dimension of Lambda(R^4) is 16 = 2^4",
      wedge(a1, a1) == {} and len(gform("f")) == 16)

# ---------------------------------------------------------------- C
print("C  the interior product")
Xs = list(sp.symbols("X0:4"))
Ys = list(sp.symbols("Y0:4"))
check("C1 i_X alpha = alpha(X) = sum alpha_i X^i", iv(Xs, a1) == clean({0: sum(a1[1 << i] * Xs[i] for i in range(4))}))
check("C2 i_X i_X = 0 and i_X i_Y = -i_Y i_X on a generic form", iv(Xs, iv(Xs, f)) == {}
      and eq(iv(Xs, iv(Ys, f)), sm(-1, iv(Ys, iv(Xs, f)))))
check("C3 i_X (b ^ f) = (i_X b) ^ f + (-1)^r b ^ i_X f, b of degree r = 0..4 (Oziewicz (4.7.1))",
      all(eq(iv(Xs, wedge(gform("b", r), f)), add(wedge(iv(Xs, gform("b", r)), f), sm((-1) ** r, wedge(gform("b", r), iv(Xs, f)))))
          for r in range(5)))


def iv_last(V, f_):
    """the other convention: contract the last slot, sign (-1)^(k - 1 - position)"""
    out = {}
    for m, c in f_.items():
        bs = bits(m)
        for p, i in enumerate(bs):
            out[m ^ 1 << i] = out.get(m ^ 1 << i, 0) + (-1) ** (len(bs) - 1 - p) * V[i] * c
    return clean(out)


b1 = gform("b", 1)
check("C3' C3 can fail: with last-slot contraction the rule of C3 is false already for deg b = 1",
      not eq(iv_last(Xs, wedge(b1, f)), add(wedge(iv_last(Xs, b1), f), sm(-1, wedge(b1, iv_last(Xs, f))))))
check("C4 i_{dx^i} on the bitmask basis: i_X dt ^ dx ^ dy = X^0 dx^dy - X^1 dt^dy + X^2 dt^dx",
      iv(Xs, {0b0111: 1}) == {0b0110: Xs[0], 0b0101: -Xs[1], 0b0011: Xs[2]})

# ---------------------------------------------------------------- D
print("D  the exterior derivative (coefficients are undefined functions of t, x, y, z)")
F = gform("F", args=XS)
Fp = {p: gform("P", p, args=XS) for p in range(5)}
Gq = gform("G", args=XS)
fun = sp.Function("u")(*XS)
check("D1 df = sum_i (d_i f) dx^i", d({0: fun}, XS) == form1([sp.diff(fun, c) for c in XS]))
check("D2 d d = 0 on a generic form (equality of mixed partials)", d(d(F, XS), XS) == {})
check("D3 d(b ^ g) = db ^ g + (-1)^p b ^ dg, b generic of degree p = 0..4",
      all(eq(d(wedge(Fp[p], Gq), XS), add(wedge(d(Fp[p], XS), Gq), sm((-1) ** p, wedge(Fp[p], d(Gq, XS)))))
          for p in range(5)))

# ---------------------------------------------------------------- E
print("E  Cartan's calculus (generic vector fields X, Y; generic form F)")
Xf = [sp.Function(f"X{i}")(*XS) for i in range(4)]
Yf = [sp.Function(f"Y{i}")(*XS) for i in range(4)]
XY = bracket(Xf, Yf, XS)
check("E1 L_X u = X(u) = X^i d_i u for a function u", lie(Xf, {0: fun}, XS) == clean({0: sum(Xf[i] * sp.diff(fun, XS[i]) for i in range(4))}))
check("E2 L_X d = d L_X", eq(lie(Xf, d(F, XS), XS), d(lie(Xf, F, XS), XS)))
check("E3 L_X i_Y - i_Y L_X = i_[X,Y]", eq(add(lie(Xf, iv(Yf, F), XS), sm(-1, iv(Yf, lie(Xf, F, XS)))), iv(XY, F)))
check("E3' E3 can fail: it is false with -[X,Y] in place of [X,Y]",
      not eq(add(lie(Xf, iv(Yf, F), XS), sm(-1, iv(Yf, lie(Xf, F, XS)))), iv([-c for c in XY], F)))
check("E4 L_X L_Y - L_Y L_X = L_[X,Y]",
      eq(add(lie(Xf, lie(Yf, F, XS), XS), sm(-1, lie(Yf, lie(Xf, F, XS), XS))), lie(XY, F, XS)))
check("E5 L_X (F ^ G) = L_X F ^ G + F ^ L_X G (a derivation of degree 0)",
      eq(lie(Xf, wedge(F, Gq), XS), add(wedge(lie(Xf, F, XS), Gq), wedge(F, lie(Xf, Gq, XS)))))
check("E6 i_X L_X = L_X i_X", eq(iv(Xf, lie(Xf, F, XS)), lie(Xf, iv(Xf, F), XS)))

# ---------------------------------------------------------------- F
print("F  operators as 2^n x 2^n matrices (pointwise: constant coefficients)")


def op_matrix(op, n=N):
    """the matrix of a linear operator on forms in the bitmask basis: column m is op(dx^m)"""
    M = sp.zeros(1 << n, 1 << n)
    for m in range(1 << n):
        for k, c in op({m: sp.Integer(1)}).items():
            M[k, m] = c
    return M


unit = lambda i: [int(j == i) for j in range(N)]                         # d_i as a list
cre = [op_matrix(lambda f_, i=i: wedge({1 << i: 1}, f_)) for i in range(N)]   # cr_{dx^i}
ann = [op_matrix(lambda f_, i=i: iv(unit(i), f_)) for i in range(N)]         # ev_{d_i}
I16, Z16 = sp.eye(16), sp.zeros(16, 16)
ac = lambda A, B: A * B + B * A
check("F1 ev_{d_i} is the transpose of cr_{dx^i} (1986 eq. (9): the determinant pairing)",
      all(ann[i] == cre[i].T for i in range(N)))
check("F2 CAR: {a_i, c_j} = delta_ij, {c_i, c_j} = 0 = {a_i, a_j}",
      all(ac(ann[i], cre[j]) == (I16 if i == j else Z16) and ac(cre[i], cre[j]) == Z16 and ac(ann[i], ann[j]) == Z16
          for i in range(N) for j in range(N)))
As = list(sp.symbols("al0:4"))
CR = sum((As[i] * cre[i] for i in range(N)), Z16)
EV = sum((Xs[i] * ann[i] for i in range(N)), Z16)
s = sum(As[i] * Xs[i] for i in range(N))
fv = sp.Matrix([f[m] for m in range(16)])
check("F3 the matrices act as the dict functions: CR f = alpha ^ f, EV f = i_X f",
      clean(dict(enumerate(CR * fv))) == wedge(form1(As), f) and clean(dict(enumerate(EV * fv))) == iv(Xs, f))
U, D_, M_ = EV + CR, CR * EV, EV * CR
check("F4 U = ev_X + cr_alpha has U^2 = alpha(X) 1; D = cr ev, M = ev cr have D + M = alpha(X) 1, D M = 0",
      (U * U - s * I16).expand() == Z16 and (D_ + M_ - s * I16).expand() == Z16 and (D_ * M_).expand() == Z16)

# ---------------------------------------------------------------- G
print("G  the Clifford product on the same space (n = 3, generic phi, no symmetry)")
n3 = 3
cre3 = [op_matrix(lambda f_, i=i: wedge({1 << i: 1}, f_), n3) for i in range(n3)]
ann3 = [c.T for c in cre3]
phi = sp.Matrix(n3, n3, lambda i, j: sp.Symbol(f"phi{i}{j}"))
gam = [cre3[i] + sum((phi[i, j] * ann3[j] for j in range(n3)), sp.zeros(8, 8)) for i in range(n3)]
check("G1 gamma_i = e_i + i_{phi e_i}: {gamma_i, gamma_j} = (phi_ij + phi_ji) 1, only the symmetric part",
      all((ac(gam[i], gam[j]) - (phi[i, j] + phi[j, i]) * sp.eye(8)).expand() == sp.zeros(8, 8)
          for i in range(n3) for j in range(n3)))
check("G2 gamma_i gamma_j 1 = e_i ^ e_j + phi_ij (columns: the Clifford product of two vectors on V)",
      all(((gam[i] * gam[j])[:, 0] - op_matrix(lambda f_: wedge({1 << i: 1}, wedge({1 << j: 1}, f_)), n3)[:, 0]
           - phi[i, j] * sp.eye(8)[:, 0]).expand() == sp.zeros(8, 1) for i in range(n3) for j in range(n3)))

SIGS = sp.symbols("sig0:4")


def blade(a, b, sig):
    """e_a e_b = sign * e_(a xor b) for an orthogonal basis with e_i^2 = sig[i]"""
    s, x = 1, a >> 1
    while x:                                      # reordering: pairs (i in a, j in b) with i > j
        if bin(x & b).count("1") % 2:
            s = -s
        x >>= 1
    for i in bits(a & b):                         # repeated generators square to sig[i]
        s *= sig[i]
    return s, a ^ b


gamN = [cre[i] + SIGS[i] * ann[i] for i in range(N)]            # phi = diag(sig)
okG3 = True
for a in range(16):
    Ga = sp.eye(16)
    for i in reversed(bits(a)):
        Ga = gamN[i] * Ga                                        # gamma_{i1} ... gamma_{ik}
    for b in range(16):
        sg, m = blade(a, b, SIGS)
        okG3 &= (Ga[:, b] - sg * sp.eye(16)[:, m]).expand() == sp.zeros(16, 1)
check("G3 the blade table of verify_observer_idempotents.py (sign by bit counting, e_i^2 = sig_i) is the"
      " Chevalley product for phi = diag(sig), all 16 x 16 pairs of blades", okG3)
check("G4 with sig = 0 the blade table is the wedge product: sign_merge is the same bit count",
      all(blade(a, b, [0] * 4) == ((sign_merge(a, b), a | b) if a & b == 0 else (0, a ^ b))
          for a in range(16) for b in range(16)))

# ---------------------------------------------------------------- H
print("H  a body in flow-box coordinates: X = d_t, alpha = dt + A(t, x)")
Af = form1([0] + [sp.Function(f"A{i}")(*XS) for i in (1, 2, 3)])
alpha = add({1: 1}, Af)
Xb = [1, 0, 0, 0]
dal = d(alpha, XS)
acc = iv(Xb, dal)
Om = add(dal, sm(-1, wedge(alpha, acc)))
check("H1 alpha(X) = 1, and a = i_X d alpha = d_t A (the acceleration)",
      iv(Xb, alpha) == {0: 1} and eq(acc, {k: sp.diff(v, t) for k, v in Af.items()}))
check("H2 i_X a = 0 and i_X Omega = 0 for Omega = d alpha - alpha ^ a (both are spatial)",
      iv(Xb, acc) == {} and iv(Xb, Om) == {})
check("H3 L_X alpha = a (Cartan: i_X d alpha + d(alpha(X)) = a + 0)", eq(lie(Xb, alpha, XS), acc))
al0 = form1([1, 0, x, 0])
check("H4 alpha = dt + x dy: alpha ^ d alpha = dt^dx^dy != 0, d alpha ^ d alpha = 0 (class 3)",
      wedge(al0, d(al0, XS)) == {0b0111: 1} and wedge(d(al0, XS), d(al0, XS)) == {})

# ---------------------------------------------------------------- I
print("I  naturality under phi(t,x,y,z) = (t + xy, x + z^2, y + z, z)")
phimap = [t + x * y, x + z ** 2, y + z, z]
J = sp.Matrix(4, 4, lambda i, j: sp.diff(phimap[i], XS[j]))
sub = dict(zip(XS, phimap))


def pull_form(f_):
    """phi^* f = sum_m (c o phi) dphi^(i1) ^ ... ^ dphi^(ik)"""
    dphi = [form1([sp.diff(phimap[i], c) for c in XS]) for i in range(4)]
    out = {}
    for m, c in f_.items():
        term = {0: sp.sympify(c).subs(sub, simultaneous=True)}
        for i in bits(m):
            term = wedge(term, dphi[i])
        out = add(out, term)
    return out


def pull_vec(V):
    """phi^* V = (D phi)^-1 (V o phi)"""
    Vp = sp.Matrix([sp.sympify(v).subs(sub, simultaneous=True) for v in V])
    return [sp.expand(c) for c in J.inv() * Vp]


Vn = [1 + y, x, 0, t]
fn = {0b0011: x * z + t, 0b0100: y, 0b1001: t * y}
gn = form1([x, y * t, 0, 1])
check("I0 set-up: det(D phi) = 1, so (D phi)^-1 is polynomial", sp.expand(J.det()) == 1)
check("I1 phi^* d = d phi^*", eq(pull_form(d(fn, XS)), d(pull_form(fn), XS)))
check("I2 phi^*(f ^ g) = phi^* f ^ phi^* g", eq(pull_form(wedge(fn, gn)), wedge(pull_form(fn), pull_form(gn))))
check("I3 phi^*(i_V f) = i_{phi^* V} phi^* f, and so phi^* L_V = L_{phi^* V} phi^*",
      eq(pull_form(iv(Vn, fn)), iv(pull_vec(Vn), pull_form(fn)))
      and eq(pull_form(lie(Vn, fn, XS)), lie(pull_vec(Vn), pull_form(fn), XS)))
swap = {t: x, x: t}
check("I4 pitfall: (t + x^2).subs({t: x, x: t}) substitutes one key after the other and gives t + t^2;"
      " with simultaneous=True it gives x + t^2",
      (t + x ** 2).subs(swap) == t + t ** 2 and (t + x ** 2).subs(swap, simultaneous=True) == x + t ** 2)

# ---------------------------------------------------------------- J
print("J  identities that need alpha(X) = 1")
cr = lambda f_: wedge(form1(As), f_)
ev = lambda f_: iv(Xs, f_)
DD = lambda f_: cr(ev(f_))
MM = lambda f_: ev(cr(f_))
GENS = As + Xs


def zero_mod(f_):
    """each coefficient lies in the ideal (s - 1), s = alpha(X): remainder 0 on division"""
    rem = lambda c: sp.reduced(sp.expand(c), [s - 1], *GENS, order="lex")[1]
    return all(sp.expand(rem(c)) == 0 for c in f_.values())


check("J1 exactly: D^2 = s D, M^2 = s M; D is a derivation of ^", eq(DD(DD(f)), sm(s, DD(f))) and eq(MM(MM(f)), sm(s, MM(f)))
      and eq(DD(wedge(f, g)), add(wedge(DD(f), g), wedge(f, DD(g)))))
Mdiff = add(MM(wedge(f, g)), sm(-1, wedge(MM(f), MM(g))))
check("J2 M(f ^ g) - M f ^ M g is not zero, but it is zero modulo s - 1 (M is an algebra map when alpha(X) = 1)",
      Mdiff != {} and zero_mod(Mdiff))
check("J3 ... and exactly: s M(f ^ g) = M f ^ M g", eq(sm(s, MM(wedge(f, g))), wedge(MM(f), MM(g))))
Xr = [rnd() for _ in range(4)]
ar = [rnd() for _ in range(4)]
sr = sum(p * q for p, q in zip(ar, Xr))
ar = [p / sr for p in ar]
fr, gr = rform(), rform()
Mr = lambda f_: iv(Xr, wedge(form1(ar), f_))
check("J4 spot check with random rationals normalised to alpha(X) = 1: M(f ^ g) = M f ^ M g",
      eq(Mr(wedge(fr, gr)), wedge(Mr(fr), Mr(gr))))

print()
print(f"{'FAILED: ' + str(FAILED) if FAILED else 'all checks pass'}")
raise SystemExit(1 if FAILED else 0)
