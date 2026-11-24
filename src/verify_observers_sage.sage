# verify_observers_sage.sage -- the observer identities MG1 of supplement/magnetismo.md
# (Oziewicz, Magnetismo, (4.7.1) and sections 4.7-4.8), and CT-F4, CT-J1 to CT-J3 of
# supplement/cartan_calculus_in_sympy.md, in ranks n = 2 to 8 and over Z, GF(3) and GF(2),
# with SageMath's own ExteriorAlgebra.
#
# alpha = sum a_i e_i and X = sum X^i e_i have independent symbols as coefficients, and
# s = alpha(X) = sum a_i X^i. On Lambda = ExteriorAlgebra(R, n), R = base[a_i, X^i]:
#   cr x = alpha ^ x,  ev x = i_X x (Sage's interior_product, first slot),
#   D = cr ev,  M = ev cr,  U = ev + cr,  e = (1 + U)/2.
# The supplement says MG1 follows from (4.7.1) and ev^2 = cr^2 = 0 "for a module of any rank"
# and holds over every commutative ring (checked there in rank 4 only). Here:
#   O1  (4.7.1) ev cr + cr ev = s;  ev^2 = 0 = cr^2;  U^2 = s;  D + M = s
#   O2  D^2 = s D, M^2 = s M, D M = 0 = M D;  U D U = s M
#   O3  D is an even derivation; ev is an odd derivation (4.4.9)
#   O4  s M(a ^ b) = M a ^ M b exactly; M(a ^ b) - M a ^ M b lies in the ideal (s - 1)
#   O5  the idempotent e: (1 + U)^2 = 2 (1 + U) + (s - 1) over Z; e^2 - e in (s - 1) over GF(3);
#       GF(2) has no 1/2, so e is not defined there
#   must fail (characteristic not 2): M(a ^ b) = M a ^ M b exactly; D with the odd sign;
#       ev with no sign. In GF(2) the signed and unsigned rules coincide (checked as such).
# Operator identities are checked on every basis blade, product identities on every pair of
# basis blades: by linearity and bilinearity that is exact for symbolic alpha and X.
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


def run(n, base, ideal_pairs=True):
    tag = "n=%d %s" % (n, base)
    names = ['a%d' % i for i in range(n)] + ['X%d' % i for i in range(n)]
    R = PolynomialRing(base, names)
    al, Xs = R.gens()[:n], R.gens()[n:]
    s = sum(al[i] * Xs[i] for i in range(n))
    I = R.ideal(s - 1)
    Lam = ExteriorAlgebra(R, 'e', n)
    e = Lam.gens()
    A = sum(al[i] * e[i] for i in range(n))
    V = sum(Xs[i] * e[i] for i in range(n))
    cr = lambda x: A * x
    ev = lambda x: x.interior_product(V)
    D = lambda x: cr(ev(x))
    M = lambda x: ev(cr(x))
    U = lambda x: ev(x) + cr(x)
    in_I = lambda x: all(I.reduce(c) == 0 for c in x.monomial_coefficients().values())
    B = [Lam.monomial(k) for k in Lam.basis().keys()]
    deg = [len(tuple(k)) for k in Lam.basis().keys()]
    pairs = [(i, j) for i in range(len(B)) for j in range(len(B))]
    char2 = base.characteristic() == 2

    chk(tag + " O1 (4.7.1) ev cr + cr ev = s", lambda: all(ev(cr(b)) + cr(ev(b)) == s * b for b in B))
    chk(tag + " O1 ev^2 = 0 = cr^2", lambda: all(ev(ev(b)) == 0 and cr(cr(b)) == 0 for b in B))
    chk(tag + " O1 U^2 = s, D + M = s", lambda: all(U(U(b)) == s * b and D(b) + M(b) == s * b for b in B))
    chk(tag + " O2 D^2 = s D, M^2 = s M, D M = 0 = M D",
        lambda: all(D(D(b)) == s * D(b) and M(M(b)) == s * M(b) and D(M(b)) == 0 and M(D(b)) == 0 for b in B))
    chk(tag + " O2 U D U = s M", lambda: all(U(D(U(b))) == s * M(b) for b in B))
    DB, MB, EB = [D(b) for b in B], [M(b) for b in B], [ev(b) for b in B]
    chk(tag + " O3 D(a ^ b) = D a ^ b + a ^ D b (even derivation)",
        lambda: all(D(B[i] * B[j]) == DB[i] * B[j] + B[i] * DB[j] for i, j in pairs))
    chk(tag + " O3 ev(a ^ b) = ev a ^ b + (-1)^deg a  a ^ ev b (4.4.9)",
        lambda: all(ev(B[i] * B[j]) == EB[i] * B[j] + (-1) ** deg[i] * B[i] * EB[j] for i, j in pairs))
    chk(tag + " O4 s M(a ^ b) = M a ^ M b", lambda: all(s * M(B[i] * B[j]) == MB[i] * MB[j] for i, j in pairs))
    if ideal_pairs:
        chk(tag + " O4 M(a ^ b) - M a ^ M b in (s - 1)", lambda: all(in_I(M(B[i] * B[j]) - MB[i] * MB[j]) for i, j in pairs))
    if base is ZZ:
        chk(tag + " O5 (1 + U)^2 = 2 (1 + U) + (s - 1)",
            lambda: all(U(U(b)) + 2 * U(b) + b == 2 * (b + U(b)) + (s - 1) * b for b in B))
    elif base.characteristic() == 3:
        half = base(2)                                  # 1/2 = 2 in GF(3)
        E = lambda x: half * (x + U(x))
        chk(tag + " O5 e = (1 + U)/2: e^2 - e in (s - 1)", lambda: all(in_I(E(E(b)) - E(b)) for b in B))
    if not char2:
        chk(tag + " must fail: M(a ^ b) = M a ^ M b exactly",
            lambda: all(M(B[i] * B[j]) == MB[i] * MB[j] for i, j in pairs), False)
        chk(tag + " must fail: D with the odd sign",
            lambda: all(D(B[i] * B[j]) == DB[i] * B[j] + (-1) ** deg[i] * B[i] * DB[j] for i, j in pairs), False)
        chk(tag + " must fail: ev with no sign",
            lambda: all(ev(B[i] * B[j]) == EB[i] * B[j] + B[i] * EB[j] for i, j in pairs), False)
    else:
        chk(tag + " char 2: the signed and unsigned rules for ev coincide",
            lambda: all(ev(B[i] * B[j]) == EB[i] * B[j] + B[i] * EB[j] for i, j in pairs))
    print("%-22s %3d checks so far, %6.1f s" % (tag, NCHECKS, time.time() - t0))


for n in range(2, 9):
    run(n, ZZ, ideal_pairs=(n <= 6))
for n in range(2, 7):
    run(n, GF(3))
    run(n, GF(2))
print("CHECKS %d" % NCHECKS)
print("FAILURES %s" % FAILS)
print("time %.1f s" % (time.time() - t0))
