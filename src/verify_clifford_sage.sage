# verify_clifford_sage.sage -- cross-check of the Clifford construction of
# supplement/cartan_calculus_in_sympy.md section 8 and src/verify_grassmann_clifford.py
# (Oziewicz 1986, eq. (23.2); the gauge statement after Jadczyk 2021, eqs. (68)-(72))
# against SageMath's own CliffordAlgebra and ExteriorAlgebra.
#
# phi = g + w, g symmetric, w antisymmetric, all entries independent symbols; n = 3 and 4.
# Lambda = ExteriorAlgebra(R, n), gamma^phi_i x = e_i ^ x + sum_j phi_ij i_{e_j} x (Sage's
# interior_product, first slot). Phi_phi : Cl(Q) -> Lambda, Phi_phi(a) = gamma^phi(a) 1,
# where Cl(Q) is Sage's CliffordAlgebra of the quadratic form with Gram matrix g.
#
#   L0  conventions: Q.Gram_matrix() = g, and Sage's f_i f_j + f_j f_i = 2 g_ij
#   L1  phi = g:     Phi_g(a b) = gamma^g(a) Phi_g(b) for all basis a, b, and Phi_g is unipotent
#   L2  phi = g + w: the same with gamma^phi and the same Cl(Q) (w does not change the algebra)
#   L3  Phi_{g+w} = exp(i_w) Phi_g, i_w x = sum_{i<j} w_ij i_{e_j} i_{e_i} x (the 1986 order);
#       must fail: exp(-i_w), the reversed order i_{e_i} i_{e_j} (Jadczyk's convention), exp(i_{w/2})
#   L4  the statement of verify_grassmann_clifford.py, as matrices on Lambda:
#       gamma^{g+w}_u = exp(i_w) gamma^g_{exp(-i_w) u} exp(-i_w) for every basis blade u,
#       where gamma^phi_u = W_phi L(W_phi^-1 u) W_phi^-1 and L(a) is Sage's left multiplication
#   L5  W_phi (columns Phi_phi(e_S)) for a fixed integer phi, n = 4, printed as WCOL lines in the
#       bitmask basis, compared with src/verify_cartan_tutorial.py by src/compare_clifford_sage.py
#
# Needs SageMath (run on Bill Page's server); not run by CI. Every check runs inside
# try/except, so an error is a failure. Ends with CHECKS n and FAILURES [...].
import time
t0 = time.time()
from sage.version import version as sage_version
print("SageMath", sage_version)

NCHECKS = 0
FAILS = []


def chk(lbl, f, want=True):
    global NCHECKS
    NCHECKS += 1
    try:
        ok = bool(f()) == want
    except Exception as ex:
        FAILS.append(lbl + " (error: %s)" % ex)
        return
    if not ok:
        FAILS.append(lbl)


def setup(n):
    gn = ['g%d%d' % (i, j) for i in range(n) for j in range(i, n)]
    wn = ['w%d%d' % (i, j) for i in range(n) for j in range(i + 1, n)]
    R = PolynomialRing(QQ, gn + wn)
    g = matrix(R, n, n, lambda i, j: R('g%d%d' % (min(i, j), max(i, j))))
    w = matrix(R, n, n, lambda i, j: 0 if i == j else (R('w%d%d' % (i, j)) if i < j else -R('w%d%d' % (j, i))))
    Q = QuadraticForm(R, n, [g[i, i] if i == j else 2 * g[i, j] for i in range(n) for j in range(i, n)])
    return R, g, w, Q


def machinery(R, n, Q):
    Cl = CliffordAlgebra(Q, names='f')
    Lam = ExteriorAlgebra(R, 'e', n)
    e = Lam.gens()
    LK = list(Lam.basis().keys())
    CK = list(Cl.basis().keys())
    lam_key = dict((tuple(k), k) for k in LK)
    cl_key = dict((tuple(k), k) for k in CK)
    tuples = [tuple(k) for k in LK]                     # grade, then lexicographic
    ip = lambda x, j: x.interior_product(e[j])

    def gamma(phi, i, x):
        return e[i] * x + sum(phi[i, j] * ip(x, j) for j in range(n))

    def act_word(phi, S, x):                            # gamma_{i1} ... gamma_{ik} x
        for i in reversed(S):
            x = gamma(phi, i, x)
        return x

    def act(phi, a, x):                                 # gamma^phi(a) x, a in Cl
        return sum((c * act_word(phi, tuple(k), x) for k, c in a.monomial_coefficients().items()), Lam.zero())

    def Phi(phi, a):
        return act(phi, a, Lam.one())

    def vec(x):                                         # coordinates in the order of `tuples`
        mc = x.monomial_coefficients()
        return vector(R, [mc.get(lam_key[s], 0) for s in tuples])

    def lam_from(v):
        return sum((v[k] * Lam.monomial(lam_key[s]) for k, s in enumerate(tuples)), Lam.zero())

    def cl_from(v):
        return sum((v[k] * Cl.monomial(cl_key[s]) for k, s in enumerate(tuples)), Cl.zero())

    def cvec(a):
        mc = a.monomial_coefficients()
        return vector(R, [mc.get(cl_key[s], 0) for s in tuples])

    clb = [Cl.monomial(cl_key[s]) for s in tuples]
    lamb = [Lam.monomial(lam_key[s]) for s in tuples]
    return dict(Cl=Cl, Lam=Lam, e=e, ip=ip, gamma=gamma, act=act, Phi=Phi, vec=vec, lam_from=lam_from,
                cl_from=cl_from, cvec=cvec, clb=clb, lamb=lamb, tuples=tuples)


def iw_op(m, w, n, order=1, scale=1):
    """i_w x = sum_{i<j} w_ij i_{e_j} i_{e_i} x (order=1, 1986); order=-1 applies i_{e_i} last"""
    ip = m['ip']

    def f(x):
        if order == 1:
            return sum((scale * w[i, j] * ip(ip(x, i), j) for i in range(n) for j in range(i + 1, n)), m['Lam'].zero())
        return sum((scale * w[i, j] * ip(ip(x, j), i) for i in range(n) for j in range(i + 1, n)), m['Lam'].zero())
    return f


def expo(op, n):
    def f(x):
        tot, term = x, x
        for k in range(1, n // 2 + 1):
            term = op(term) / k
            tot += term
        return tot
    return f


for n in (3, 4):
    print("--- n = %d" % n)
    R, g, w, Q = setup(n)
    m = machinery(R, n, Q)
    Cl, Lam, Phi, act, vec, clb, lamb, tuples = (m[k] for k in ('Cl', 'Lam', 'Phi', 'act', 'vec', 'clb', 'lamb', 'tuples'))
    f = Cl.gens()
    N = len(tuples)
    phi = g + w
    chk("L0 n=%d Q.Gram_matrix() = g" % n, lambda: Q.Gram_matrix() == g)
    chk("L0 n=%d Sage: f_i f_j + f_j f_i = 2 g_ij" % n,
        lambda: all(f[i] * f[j] + f[j] * f[i] == 2 * g[i, j] * Cl.one() for i in range(n) for j in range(n)))
    for lbl, ph in (("L1 n=%d phi = g" % n, g), ("L2 n=%d phi = g + w" % n, phi)):
        PB = [Phi(ph, b) for b in clb]
        chk(lbl + ": Phi(a b) = gamma(a) Phi(b) for all basis a, b",
            lambda: all(Phi(ph, a * b) == act(ph, a, PB[k]) for a in clb for k, b in enumerate(clb)))
        chk(lbl + ": Phi(e_S) = e_S + terms of lower degree",
            lambda: all(all(len(key) < len(tuples[k]) for key in (PB[k] - lamb[k]).monomial_coefficients())
                        for k in range(N)))
    Pg = [Phi(g, b) for b in clb]
    Pp = [Phi(phi, b) for b in clb]
    for lbl, op, want in (("L3 n=%d Phi_{g+w} = exp(i_w) Phi_g, i_w in the 1986 order" % n, iw_op(m, w, n), True),
                          ("L3 n=%d must fail: exp(-i_w)" % n, iw_op(m, w, n, scale=-1), False),
                          ("L3 n=%d must fail: i_w in the reversed (Jadczyk) order" % n, iw_op(m, w, n, order=-1), False),
                          ("L3 n=%d must fail: exp(i_{w/2})" % n, iw_op(m, w, n, scale=1/2), False)):
        E = expo(op, n)
        chk(lbl, lambda: all(Pp[k] == E(Pg[k]) for k in range(N)), want)
    # L4: the gauge statement as matrices on Lambda
    Wg = matrix(R, N, N, lambda r, c: vec(Pg[c])[r])
    Wp = matrix(R, N, N, lambda r, c: vec(Pp[c])[r])
    cvec, cl_from, lam_from = m['cvec'], m['cl_from'], m['lam_from']
    Lmat = lambda a: matrix(R, N, N, lambda r, c: cvec(a * clb[c])[r])      # left multiplication on Cl
    Lb = [Lmat(b) for b in clb]
    Lof = lambda v: sum((v[k] * Lb[k] for k in range(N)), zero_matrix(R, N))
    Wgi, Wpi = Wg.inverse(), Wp.inverse()
    gam = lambda W, Wi, u: W * Lof(Wi * u) * Wi                              # gamma_u on Lambda
    Ew = matrix(R, N, N, lambda r, c: vec(expo(iw_op(m, w, n), n)(lamb[c]))[r])
    Emw = matrix(R, N, N, lambda r, c: vec(expo(iw_op(m, w, n, scale=-1), n)(lamb[c]))[r])
    chk("L4 n=%d exp(i_w) exp(-i_w) = 1" % n, lambda: Ew * Emw == identity_matrix(R, N))
    unit = lambda k: vector(R, [1 if r == k else 0 for r in range(N)])
    chk("L4 n=%d gamma^{g+w}_u = exp(i_w) gamma^g_{exp(-i_w) u} exp(-i_w), all blades u" % n,
        lambda: all(gam(Wp, Wpi, unit(k)) == Ew * gam(Wg, Wgi, Emw * unit(k)) * Emw for k in range(N)))
    chk("L4 n=%d must fail: the same with exp(i_w) and exp(-i_w) exchanged" % n,
        lambda: all(gam(Wp, Wpi, unit(k)) == Emw * gam(Wg, Wgi, Ew * unit(k)) * Ew for k in range(N)), False)
    print("after n = %d: %d checks, %.1f s" % (n, NCHECKS, time.time() - t0))

# L5: W for a fixed integer phi, n = 4, in the bitmask basis
print("--- L5 W for a fixed phi, n = 4")
n = 4
R, g, w, Q = setup(n)
m = machinery(R, n, Q)
PHI = matrix(QQ, [[1, 2, 0, -1], [0, -1, 3, 1], [2, 1, 1, 0], [1, -2, 0, 2]])
gnum, wnum = (PHI + PHI.transpose()) / 2, (PHI - PHI.transpose()) / 2
sub = dict()
for i in range(n):
    for j in range(i, n):
        sub[R('g%d%d' % (i, j))] = gnum[i, j]
        if j > i:
            sub[R('w%d%d' % (i, j))] = wnum[i, j]
phi = g + w
mask = lambda s: sum(1 << i for i in s)
for k, b in enumerate(m['clb']):
    col = m['Phi'](phi, b)
    entries = sorted((mask(tuple(key)), QQ(c.subs(sub))) for key, c in col.monomial_coefficients().items())
    entries = [(T, c) for T, c in entries if c != 0]
    print("WCOL|%d|%s" % (mask(m['tuples'][k]), entries))
print("PHI|%s" % [list(r) for r in PHI.rows()])
print("CHECKS %d" % NCHECKS)
print("FAILURES %s" % FAILS)
print("time %.1f s" % (time.time() - t0))
