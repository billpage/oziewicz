"""Exact checks for supplement/grassmann_to_clifford.md.

The papers are Z. Oziewicz, "From Grassmann to Clifford" (Reidel 1986) and
"Clifford algebra of multivectors" (Adv. Appl. Clifford Alg. 7 (S), 1997),
A. Jadczyk, arXiv:2103.09767, and G. Sobczyk's null-vector papers.  Equation
numbers are those of the paper named in each check.

Model.  V^1 has basis e_0..e_{n-1}; the Grassmann algebra V has the basis
blades e_S = e_{i1}^...^e_{ik} (i1 < ... < ik), indexed by the bitmask S.  The
multiforms have the dual blades, and the determinant pairing, eq. (3) of 1986,
gives <e^S, e_T> = delta_ST.  Hence, as matrices in these bases,

    e_x on V       : E[x]   (left exterior multiplication)
    i_alpha on V   : transpose of the matrix of e_alpha     (eq. 9)

phi is a generic n x n matrix of independent symbols, with no symmetry, unless
a check says otherwise.  Everything is exact: SymPy polynomial arithmetic.
Part D4 multiplies integer-valued matrices in 64-bit floats; an assertion
bounds the entries so that every product is exact.

Parts
  A  1986: Grassmann multiplications, eqs (6)-(17), (22)
  B  1986: the Clifford product, eqs (23)-(27); idempotents, eqs (30)-(32)
  C  Jadczyk 2021: the antisymmetric part as a gauge, eqs (60)-(72), Prop. 3.12
     (parts A to C are part_1986, run for n = 3 and n = 4)
  S  Sobczyk: global and local duality, idempotents, the observer, the
     triangular phi, and evaluation in the null-vector algebra
  D  1997: Prop. 10.1, the omega-deformed exterior algebra, eqs (6.6)-(6.7),
     and Conjecture 8.2 (the minimum polynomial of gamma^mu (x) gamma_mu)

Run:  PYTHONPATH=src python3 -u src/verify_grassmann_clifford.py
Writes no files.  About 50 s.
"""

from __future__ import annotations

import itertools as it

import numpy as np
import sympy as sp
from sympy.combinatorics import Permutation

COUNT = 0


def check(name, ok):
    global COUNT
    COUNT += 1
    print(f"[{'PASS' if ok else 'FAIL'}] {name}", flush=True)
    assert ok, name


def part_1986(n):
    N = 1 << n
    deg = [bin(S).count("1") for S in range(N)]
    bits = lambda S: [i for i in range(n) if S >> i & 1]

    def isz(M):
        return all(sp.expand(x) == 0 for x in M)


    # ---------------------------------------------------------------- Grassmann part
    E = [sp.zeros(N, N) for _ in range(n)]
    for i in range(n):
        for S in range(N):
            if not S >> i & 1:
                E[i][S | 1 << i, S] = (-1) ** bin(S & ((1 << i) - 1)).count("1")
    I = [M.T for M in E]                      # contraction by the dual covector e^i
    Id = sp.eye(N)
    unit = lambda S: sp.Matrix([1 if T == S else 0 for T in range(N)])

    def prod(ms):
        P = Id
        for M in ms:
            P = P * M
        return P

    EB = [prod([E[i] for i in bits(S)]) for S in range(N)]      # e_{e_S}
    op_e = lambda u: sum((u[S] * EB[S] for S in range(N)), sp.zeros(N, N))
    op_i = lambda u: op_e(u).T                                   # i_u (dual algebra acting)

    check("blade operators: e_{e_S} 1 = e_S", all(EB[S][:, 0] == unit(S) for S in range(N)))
    check("(6)  e_x e_y = (-1)^{deg x deg y} e_y e_x",
          all(EB[S] * EB[T] == (-1) ** (deg[S] * deg[T]) * EB[T] * EB[S] for S in range(N) for T in range(N)))
    check("(7)  e_x e_y = e_{e_x y}",
          all(EB[S] * EB[T] == op_e(EB[S] * unit(T)) for S in range(N) for T in range(N)))
    check("(12) i_x i_y = i_{e_y x}   (order reversed)",
          all(EB[S].T * EB[T].T == op_i(EB[T] * unit(S)) for S in range(N) for T in range(N)))
    check("(13) i_x e_a = e_{i_x a} + (-1)^{deg a} e_a i_x   (deg x = 1, any deg a)",
          all(I[i] * EB[S] == op_e(I[i] * unit(S)) + (-1) ** deg[S] * EB[S] * I[i]
              for i in range(n) for S in range(N)))
    check("(16) {i_x, e_a} = a(x)   (CAR, degrees 1)",
          all(I[i] * E[j] + E[j] * I[i] == (1 if i == j else 0) * Id for i in range(n) for j in range(n)))
    ok = True
    for x, y in it.permutations(range(n), 2):
        ixy = I[y] * I[x]                                        # i_{x^y} = i_y i_x by (12)
        for S in [S for S in range(N) if deg[S] == 2]:
            a = unit(S)
            lhs = ixy * EB[S] - EB[S] * ixy
            rhs = (ixy * a)[0] * Id + op_e(I[y] * a) * I[x] - op_e(I[x] * a) * I[y]
            ok &= lhs == rhs
    check("(17) [i_{x^y}, e_a] = a(x^y) + e_{i_y a} i_x - e_{i_x a} i_y   (deg a = 2)", ok)
    xs, als = sp.symbols(f"x0:{n}"), sp.symbols(f"al0:{n}")
    Q = sum((xs[i] * E[i] + als[i] * I[i] for i in range(n)), sp.zeros(N, N))
    check("(22) (e_x + i_a)^2 = a(x)   (generic vector x, covector a)",
          isz(Q * Q - sum(xs[i] * als[i] for i in range(n)) * Id))

    # ---------------------------------------------------------------- Clifford part
    F = sp.Matrix(n, n, lambda i, j: sp.Symbol(f"F{i}{j}"))     # phi(e_i, e_j), no symmetry assumed
    g, w = (F + F.T) / 2, (F - F.T) / 2
    G = [E[i] + sum((F[i, j] * I[j] for j in range(n)), sp.zeros(N, N)) for i in range(n)]  # (23.2)
    GS = [prod([G[i] for i in bits(S)]).applyfunc(sp.expand) for S in range(N)]
    W = sp.Matrix.hstack(*[GS[S][:, 0] for S in range(N)])      # columns: gamma-words applied to 1
    M = W - Id
    Winv = (Id - M + M * M - M * M * M).applyfunc(sp.expand)     # M lowers degree by >= 2
    check("W = [gamma_{i1}...gamma_{ik} 1] is unipotent; inverse found", isz(W * Winv - Id))
    GAM = [sum((Winv[S, T] * GS[S] for S in range(N)), sp.zeros(N, N)).applyfunc(sp.expand) for T in range(N)]
    gam = lambda u: sum((u[T] * GAM[T] for T in range(N)), sp.zeros(N, N))
    cl = lambda u, v: (gam(u) * v).applyfunc(sp.expand)          # Clifford product on V

    check("(23.1-2) gamma_1 = id, gamma_v = e_v + i_{phi v}", GAM[0] == Id and all(isz(GAM[1 << i] - G[i]) for i in range(n)))
    check("gamma_u 1 = u for all u", all(GAM[T][:, 0] == unit(T) for T in range(N)))
    check("(23.3) gamma_{gamma_u w} = gamma_u gamma_w for ALL basis blades u, w (generic phi)",
          all(isz(gam(GAM[T][:, U]) - GAM[T] * GAM[U]) for T in range(N) for U in range(N)))
    vw = lambda *idx: prod([E[i] for i in idx])[:, 0]            # e_i ^ e_j ^ ... as a column
    check("(24)/(25) gamma_{v^w} = gamma_v gamma_w - phi(v,w)",
          all(isz(gam(vw(i, j)) - G[i] * G[j] + F[i, j] * Id) for i in range(n) for j in range(n)))
    iF = lambda i: sum((F[i, j] * I[j] for j in range(n)), sp.zeros(N, N))
    check("(25') gamma_{v^w} = e_{v^w} + i_{phi v} i_{phi w} + e_v i_{phi w} - e_w i_{phi v}",
          all(isz(gam(vw(i, j)) - (E[i] * E[j] + iF(i) * iF(j) + E[i] * iF(j) - E[j] * iF(i)))
              for i in range(n) for j in range(n)))
    check("{gamma_v, gamma_w} = 2 g(v,w)",
          all(isz(G[i] * G[j] + G[j] * G[i] - 2 * g[i, j] * Id) for i in range(n) for j in range(n)))
    check("gamma_{v^w} = (1/2)[gamma_v, gamma_w] - omega(v,w)",
          all(isz(gam(vw(i, j)) - (G[i] * G[j] - G[j] * G[i]) / 2 + w[i, j] * Id) for i in range(n) for j in range(n)))
    check("(27a) trivector formula",
          all(isz(gam(vw(k, l, m)) - (G[k] * G[l] * G[m] + F[k, m] * G[l] - F[l, m] * G[k] - F[k, l] * G[m]))
              for k, l, m in it.product(range(n), repeat=3)))
    if n >= 4:
        ok = True
        for p, q, r, s in it.product(range(n), repeat=4):
            rhs = (G[p] * G[q] * G[r] * G[s]
                   + F[q, s] * G[p] * G[r] - F[r, s] * G[p] * G[q] - F[q, r] * G[p] * G[s]
                   - F[p, q] * G[r] * G[s] + F[p, r] * G[q] * G[s] - F[p, s] * G[q] * G[r]
                   + (F[p, q] * F[r, s] - F[p, r] * F[q, s] + F[p, s] * F[q, r]) * Id)
            ok &= isz(gam(vw(p, q, r, s)) - rhs)
        check("(27b) 4-vector formula", ok)

    # gauge equivalence (Jadczyk 2021, eqs. 68-72): omega is removed by exp(i_omega)
    Nop = sum((w[i, j] * I[j] * I[i] for i in range(n) for j in range(i + 1, n)), sp.zeros(N, N))  # i_omega
    expN = Id + Nop + Nop * Nop / 2 + Nop ** 3 / 6
    expm = Id - Nop + Nop * Nop / 2 - Nop ** 3 / 6
    check("[i_omega, e_x] = i^omega_x", all(isz(Nop * E[k] - E[k] * Nop - sum((w[k, j] * I[j] for j in range(n)), sp.zeros(N, N))) for k in range(n)))
    sym = {F[i, j]: g[i, j] for i in range(n) for j in range(n)}
    GAMg = [Mx.subs(sym, simultaneous=True) for Mx in GAM]       # the same construction with phi = g
    gamg = lambda u: sum((u[T] * GAMg[T] for T in range(N)), sp.zeros(N, N))
    check("gamma^{g+omega}_u = exp(i_omega) gamma^g_{exp(-i_omega) u} exp(-i_omega) for all blades u",
          all(isz(GAM[T] - expN * gamg(expm[:, T]) * expm) for T in range(N)))

    # idempotents of the form 2p = lam + v + a^b, eqs. (30)-(31)
    lam = sp.Symbol("lam")
    vv, aa, bb = (sp.Matrix(sp.symbols(f"{c}0:{n}")) for c in "vab")
    vec = lambda c: sum((c[i] * unit(1 << i) for i in range(n)), sp.zeros(N, 1))
    B2 = op_e(vec(aa)) * vec(bb)
    P2 = lam * unit(0) + vec(vv) + B2                            # = 2p
    bil = lambda Mx, x, y: (x.T * Mx * y)[0]
    R = cl(P2, P2) - 2 * P2                                      # (2p)^2 - 2(2p) = 4(p.p - p)
    pred = ((lam ** 2 - 2 * lam + bil(g, vv, vv) + bil(g, aa, bb) ** 2 - bil(w, aa, bb) ** 2
             - bil(g, aa, aa) * bil(g, bb, bb)) * unit(0)
            + 2 * ((lam - 1) * vec(vv) + bil(w, vv, aa) * vec(bb) - bil(w, vv, bb) * vec(aa))
            + 2 * (lam - 1 - bil(w, aa, bb)) * B2
            + 2 * op_e(vec(vv)) * B2)
    check("(30)-(31) grade decomposition of 4(p.p - p), generic v,a,b,phi", isz(R - pred))
    tri = op_e(vec(vv)) * B2
    contr = Nop * tri                                            # i_omega (v^a^b)
    third = bil(w, aa, bb) * vec(vv) + bil(w, vv, aa) * vec(bb) - bil(w, vv, bb) * vec(aa)
    check("3rd condition of (31) equals i_omega(v^a^b): implied by v^a^b = 0", isz(contr - third))
    check("exp(i_omega)(v^w) = v^w + omega(v,w)",
          all(isz(expN * vw(i, j) - vw(i, j) - w[i, j] * unit(0)) for i in range(n) for j in range(n)))

    # ---------------------------------------------------------------- comparison with Jadczyk (2021)
    iw = lambda k: sum((w[k, j] * I[j] for j in range(n)), sp.zeros(N, N))          # i_{omega(e_k, .)}
    NJ = sum((w[i, j] * I[i] * I[j] for i in range(n) for j in range(i + 1, n)), sp.zeros(N, N))
    # NJ is Jadczyk's i_{A*}: A* = sum_{i<j} A_ij e^i^e^j, i_{f^g} = i_f i_g (his eqs. 60-63), A = omega
    check("Jadczyk eq. (68) under his own conventions (60)-(63) has the opposite sign: [i_{A*}, e_x] = - i^A_x",
          all(isz(NJ * E[k] - E[k] * NJ + iw(k)) for k in range(n)))
    check("Jadczyk's i_{A*} = - (Oziewicz's i_omega): the two conventions differ by eq. (12)", isz(NJ + Nop))
    check("exp(i_omega) i_alpha exp(-i_omega) = i_alpha  and  exp(i_omega) e_x exp(-i_omega) = e_x + i_{omega x}",
          all(isz(expN * I[k] * expm - I[k]) and isz(expN * E[k] * expm - E[k] - iw(k)) for k in range(n)))
    Gg = [Mx.subs(sym, simultaneous=True) for Mx in G]                              # generators for phi = g

    def antisym(gens, idx):
        tot = sp.zeros(N, N)
        for perm in it.permutations(range(len(idx))):
            sgn = Permutation(list(perm)).signature()
            tot += sgn * prod([gens[idx[q]] for q in perm])
        return tot / sp.factorial(len(idx))

    check("Jadczyk Prop. 3.12 (phi = g): gamma_{y1^..^yk} = antisymmetrised product, k = 2, 3",
          all(isz(gamg(vw(i, j)) - antisym(Gg, (i, j))) for i in range(n) for j in range(n))
          and all(isz(gamg(vw(k, l, m)) - antisym(Gg, (k, l, m))) for k, l, m in it.product(range(n), repeat=3)))
    check("  ... and it fails by exactly -omega(v,w) when omega != 0",
          all(isz(gam(vw(i, j)) - antisym(G, (i, j)) + w[i, j] * Id) for i in range(n) for j in range(n)))
    check("idempotent family (30): exp(i_omega) maps (lam + v + a^b) to (lam + omega(a,b) + v + a^b)",
          isz(expN * P2 - (P2 + bil(w, aa, bb) * unit(0))))

    # concrete idempotents, signature (-,+,+,+) on e_0..e_3
    if n == 4:
        eta = sp.diag(-1, 1, 1, 1)
        num = {F[i, j]: eta[i, j] for i in range(4) for j in range(4)}
        GAMn = [Mx.subs(num) for Mx in GAM]
        gn = lambda u: sum((u[T] * GAMn[T] for T in range(N)), sp.zeros(N, N))
        A = (unit(0) + unit(1 << 1)) / 2                         # (1 + e_1)/2
        B = (unit(0) + vw(0, 2)) / 2                             # (1 + e_0^e_2)/2
        AB, BA = gn(A) * B, gn(B) * A
        right = lambda p: sp.Matrix.hstack(*[gn(unit(T)) * p for T in range(N)])   # delta_p
        check("signature (3,1): A, B idempotent, commute, AB idempotent",
              gn(A) * A == A and gn(B) * B == B and AB == BA and gn(AB) * AB == AB)
        print("     ranks of delta_A, delta_B, delta_AB:", right(A).rank(), right(B).rank(), right(AB).rank())
        check("delta_AB has rank 4 = dim of a minimal left ideal of Cl(3,1) = M_4(R)", right(AB).rank() == 4)



def part_sobczyk():
    n = 4
    N = 1 << n
    bits = lambda S: [i for i in range(n) if S >> i & 1]
    E = [sp.zeros(N, N) for _ in range(n)]
    for i in range(n):
        for S in range(N):
            if not S >> i & 1:
                E[i][S | 1 << i, S] = (-1) ** bin(S & ((1 << i) - 1)).count("1")
    I = [M.T for M in E]
    Id, Z = sp.eye(N), sp.zeros(N, N)
    half = sp.Rational(1, 2)

    def prod(ms):
        P = Id
        for M in ms:
            P = P * M
        return P


    # (a) global duality  a_i b_j + b_j a_i = delta_ij  with  a_i = e_i, b_j = i_j = a_j^T
    a, b = E, I
    check("(a) global duality: a_i = e_{x_i}, b_j = i_{alpha^j} = a_j^T; a_i b_j + b_j a_i = delta_ij; a, b nilpotent, anticommuting",
          all(a[i] * b[j] + b[j] * a[i] == int(i == j) * Id and a[i] * a[j] + a[j] * a[i] == Z
              and b[i] * b[j] + b[j] * b[i] == Z for i in range(n) for j in range(n)))
    ee = [a[i] + b[i] for i in range(n)]
    ff = [a[i] - b[i] for i in range(n)]
    gens = ee + ff
    sq = [1] * n + [-1] * n
    check("    e_i = a_i + b_i, f_i = a_i - b_i are an orthonormal basis of signature (n,n)",
          all(gens[p] * gens[q] + gens[q] * gens[p] == (2 * sq[p] if p == q else 0) * Id
              for p in range(2 * n) for q in range(2 * n)))
    words = [prod([a[i] for i in bits(S)]) * prod([b[i] for i in bits(T)]) for S in range(N) for T in range(N)]
    span = sp.Matrix([list(Wd) for Wd in words])
    check("    the 4^n products a_S b_T span all of End(V): G_{n,n} = M_{2^n}(R)", span.rank() == N * N)

    # (d) observer idempotent kappa = e_T i_tau, tau(T) = 1
    k = a[0] * b[0]
    proj = sp.Matrix(n, n, lambda r, c: k[1 << r, 1 << c])
    check("(d) kappa = a_1 b_1 = e_T i_tau is idempotent and equals T (x) tau on degree 1",
          k * k == k and proj == sp.diag(1, 0, 0, 0))

    # (b) local duality: one Grassmann algebra plus phi = g, g_ij = (1 - delta_ij)/2
    g = sp.Matrix(n, n, lambda i, j: 0 if i == j else half)
    c = [E[i] + sum((g[i, j] * I[j] for j in range(n)), Z) for i in range(n)]      # gamma_{c_i}, eq. (23.2)
    check("(b) local duality: gamma_{c_i} = e_i + i_{g c_i} gives c_i^2 = 0, c_i c_j + c_j c_i = 1",
          all(c[i] * c[j] + c[j] * c[i] == int(i != j) * Id for i in range(n) for j in range(n)))
    print("    eigenvalues of g:", g.eigenvals(), "-> signature (1, n-1)")
    check("    Sobczyk Table 1: c_i c_j c_i = c_i and (c_i c_j)^2 = c_i c_j",
          all(c[i] * c[j] * c[i] == c[i] and (c[i] * c[j]) ** 2 == c[i] * c[j] for i, j in it.permutations(range(n), 2)))
    check("    c_i c_j = (1 + 2 c_i^c_j)/2 applied to 1: Oziewicz idempotent B of (30)-(31) with a = 2c_i, b = c_j",
          all((c[i] * c[j])[:, 0] == half * (Id[:, 0] + 2 * (E[i] * E[j])[:, 0]) for i, j in it.permutations(range(n), 2)))
    # recursive orthogonalization (Theorem 1 of the UNS paper), n = 4 null vectors -> G_{1,3}
    e1, f = c[0] + c[1], [c[0] - c[1]]
    for kk in (2, 3):
        alpha = -sp.sqrt(2) / sp.sqrt(kk * (kk - 1))
        f.append(alpha * (sum(c[:kk], Z) - (kk - 1) * c[kk]))
    basis, sgn = [e1] + f, [1, -1, -1, -1]
    check("    e1 = c1+c2, f1 = c1-c2, f_k = alpha_k(C_k - (k-1)c_{k+1}): orthonormal, signature (1,3)",
          all((basis[p] * basis[q] + basis[q] * basis[p]).applyfunc(sp.simplify) == (2 * sgn[p] if p == q else 0) * Id
              for p in range(4) for q in range(4)))

    # (c) the antisymmetric part: phi = g + omega with phi triangular
    Ftri = sp.Matrix(n, n, lambda i, j: 1 if i > j else 0)                          # phi(c_i, c_j) = 0 for i < j
    check("(c) triangular phi has the same symmetric part g", (Ftri + Ftri.T) / 2 == g)
    ct = [E[i] + sum((Ftri[i, j] * I[j] for j in range(n)), Z) for i in range(n)]
    check("    with it, ordered products c_{i1}...c_{ik} (i1<...<ik) applied to 1 ARE the wedge blades",
          all(prod([ct[i] for i in bits(S)])[:, 0] == Id[:, S] for S in range(N)))
    check("    with phi = g they are not (e.g. c_1 c_2 . 1 = c_1^c_2 + 1/2)",
          (c[0] * c[1])[:, 0] == (E[0] * E[1])[:, 0] + half * Id[:, 0])


    # ---------------------------------------------------------------- evaluation (supplement, concluding section)
    def evaluation_checks(m=3):
        M_ = 1 << m
        Em = [sp.zeros(M_, M_) for _ in range(m)]
        for i in range(m):
            for S in range(M_):
                if not S >> i & 1:
                    Em[i][S | 1 << i, S] = (-1) ** bin(S & ((1 << i) - 1)).count("1")
        am, bm, Idm = Em, [X.T for X in Em], sp.eye(M_)
        def pr(ms):
            P = Idm
            for X in ms:
                P = P * X
            return P
        u = pr([bm[i] * am[i] for i in range(m)])                       # vacuum idempotent
        check("(e) u = b_1 a_1 ... b_n a_n is a primitive idempotent (rank 1) with b_j u = 0",
              u * u == u and u.rank() == 1 and all((bm[j] * u).is_zero_matrix for j in range(m)))
        ok1 = ok2 = True
        for k in range(1, m + 1):
            X = sp.Matrix(k, m, lambda r, c: sp.Symbol(f"x{r}{c}"))
            A = sp.Matrix(k, m, lambda r, c: sp.Symbol(f"al{r}{c}"))
            xs = [sum((X[r, c] * am[c] for c in range(m)), sp.zeros(M_, M_)) for r in range(k)]
            al = [sum((A[r, c] * bm[c] for c in range(m)), sp.zeros(M_, M_)) for r in range(k)]
            det = (A * X.T).det()                                       # det[alpha^i(x_j)], Oziewicz eq. (3)
            op = pr(al[::-1]) * pr(xs)                                  # reverse(B) A
            ok1 &= all(sp.expand(z) == 0 for z in (op * u - det * u))
            ok2 &= sp.expand(op.trace() / M_ - det / 2 ** k) == 0
        check("    evaluation: reverse(B) A u = det[alpha^i(x_j)] u, generic k-vector and k-form, k = 1..3", ok1)
        check("    evaluation: scalar part <reverse(B) A>_0 = 2^-k det[alpha^i(x_j)]", ok2)
        Fm = sp.Matrix(m, m, lambda i, j: sp.Symbol(f"F{i}{j}"))
        vs = sp.symbols(f"v0:{m}")
        gv = (sum((vs[i] * am[i] for i in range(m)), sp.zeros(M_, M_))
              + sum((vs[i] * Fm[i, j] * bm[j] for i in range(m) for j in range(m)), sp.zeros(M_, M_)))
        check("    graph of phi: (v + phi v)^2 = (phi v)(v) = g(v,v)",
              all(sp.expand(z) == 0 for z in (gv * gv - sum(vs[i] * Fm[i, j] * vs[j] for i in range(m) for j in range(m)) * Idm)))
        Nd = sum((am[i] * bm[i] for i in range(m)), sp.zeros(M_, M_))
        check("    sum_i a_i b_i is the degree operator (the bare grading)",
              Nd.is_diagonal() and all(Nd[S, S] == bin(S).count("1") for S in range(M_)))
        cm = [am[i] + sum((half * bm[j] for j in range(m) if j != i), sp.zeros(M_, M_)) for i in range(m)]
        check("    local duality inside the doubled space: c_i = a_i + (1/2) sum_{j != i} b_j",
              all(cm[i] * cm[j] + cm[j] * cm[i] == int(i != j) * Idm for i in range(m) for j in range(m)))

    evaluation_checks()



def part_1997():

    def grassmann(n):
        N = 1 << n
        E = [sp.zeros(N, N) for _ in range(n)]
        for i in range(n):
            for S in range(N):
                if not S >> i & 1:
                    E[i][S | 1 << i, S] = (-1) ** bin(S & ((1 << i) - 1)).count("1")
        return E, [M.T for M in E]

    # ------------------------------------------------------------------ Part A
    n = 4; N = 1 << n
    E, I = grassmann(n)
    Id = sp.eye(N)
    deg = [bin(S).count("1") for S in range(N)]
    bits = lambda S: [i for i in range(n) if S >> i & 1]
    isz = lambda M: all(sp.expand(x) == 0 for x in M)
    def prod(ms):
        P = Id
        for M in ms:
            P = P * M
        return P
    F = sp.Matrix(n, n, lambda i, j: sp.Symbol(f"F{i}{j}"))
    eta, om = (F + F.T) / 2, (F - F.T) / 2

    def clifford(Fm):
        """left-multiplication matrices GAM[T] = gamma_{e_T} for the bilinear form Fm (eq. 23 of 1986)."""
        G = [E[i] + sum((Fm[i, j] * I[j] for j in range(n)), sp.zeros(N, N)) for i in range(n)]
        GS = [prod([G[i] for i in bits(S)]).applyfunc(sp.expand) for S in range(N)]
        W = sp.Matrix.hstack(*[GS[S][:, 0] for S in range(N)])
        M = W - Id
        Winv = (Id - M + M * M - M ** 3).applyfunc(sp.expand)
        return [sum((Winv[S, T] * GS[S] for S in range(N)), sp.zeros(N, N)).applyfunc(sp.expand) for T in range(N)]

    GAM = clifford(F)
    GAMopp = clifford(-F.T)
    check("Prop. 10.1: u .phi w = (-1)^{|u||w|} w .(-phi^T) u for all blades (generic phi)",
          all(isz(GAM[T][:, U] - (-1) ** (deg[T] * deg[U]) * GAMopp[U][:, T]) for T in range(N) for U in range(N)))
    GAMw = clifford(om)                                            # eta = 0: the omega-deformed exterior algebra
    check("Sec. 9.1: the omega-deformed exterior product is Z2-graded commutative",
          all(isz(GAMw[T][:, U] - (-1) ** (deg[T] * deg[U]) * GAMw[U][:, T]) for T in range(N) for U in range(N)))
    Nop = sum((om[i, j] * I[j] * I[i] for i in range(n) for j in range(i + 1, n)), sp.zeros(N, N))
    expN = Id + Nop + Nop * Nop / 2
    EB = [prod([E[i] for i in bits(S)]) for S in range(N)]
    gw = lambda u: sum((u[T] * GAMw[T] for T in range(N)), sp.zeros(N, N))
    check("Sec. 9.1: exp(i_omega) is an algebra isomorphism (wedge) -> (wedge_omega); 'clouded' grade k = exp(i_omega)(bare grade k)",
          all(isz(gw(expN[:, S]) * expN[:, T] - expN * EB[S][:, T]) for S in range(N) for T in range(N)))
    v = sp.Matrix(sp.symbols("v0:4"))
    vec = sum((v[i] * Id[:, 1 << i] for i in range(n)), sp.zeros(N, 1))
    gF = lambda u: sum((u[T] * GAM[T] for T in range(N)), sp.zeros(N, N))
    check("v . v = eta(v,v) (a scalar): for eta != 0 no Z-grading with vectors in degree 1 is preserved",
          isz(gF(vec) * vec - (v.T * eta * v)[0] * Id[:, 0]))

    # ------------------------------------------------------------------ Part B
    # tensors as {word (tuple of letters): coefficient}; h(a,b) stands for the scalar product eta(a,b)
    h = sp.Function("h")
    def add(d, w, c):
        d[w] = sp.expand(d.get(w, 0) + c)
    def mu4(p, q, r, s):
        """eq. (6.7) with sigma = -switch, so that (id (x) sigma^{2,1}) pqrs = p s q r and (id (x) sigma (x) id) pqrs = -p r q s."""
        d = {}
        add(d, (p, q, r, s), 1)
        add(d, (r, s), -h(p, q)); add(d, (p, q), -h(r, s)); add(d, (p, s), -h(q, r))
        add(d, (p, r), +h(q, s))                                   # -(id eta id)(id^2 sigma)
        add(d, (), h(p, q) * h(r, s))
        for sign, (a, b, c, e) in ((-1, (p, r, q, s)), (+1, (p, s, q, r))):   # (eta eta - eta id^2)(...)
            add(d, (), sign * h(a, b) * h(c, e)); add(d, (c, e), -sign * h(a, b))
        return d
    def eq27b(p, q, r, s):
        d = {}
        add(d, (p, q, r, s), 1)
        add(d, (p, r), h(q, s)); add(d, (p, q), -h(r, s)); add(d, (p, s), -h(q, r))
        add(d, (r, s), -h(p, q)); add(d, (q, s), h(p, r)); add(d, (q, r), -h(p, s))
        add(d, (), h(p, q) * h(r, s) - h(p, r) * h(q, s) + h(p, s) * h(q, r))
        return d
    def mu3(k, l, m):                                              # eq. (6.6)
        d = {}
        add(d, (k, l, m), 1); add(d, (m,), -h(k, l)); add(d, (l,), +h(k, m)); add(d, (k,), -h(l, m))
        return d
    def eq27a(k, l, m):
        d = {}
        add(d, (k, l, m), 1); add(d, (l,), h(k, m)); add(d, (k,), -h(l, m)); add(d, (m,), -h(k, l))
        return d
    clean = lambda d: {w: c for w, c in d.items() if c != 0}
    L = sp.symbols("p q r s")
    check("eqs. (6.6), (6.7) of 1997 with sigma = -switch are eqs. (27) of 1986 (trivector, 4-vector)",
          clean(mu3(*L[:3])) == clean(eq27a(*L[:3])) and clean(mu4(*L)) == clean(eq27b(*L)))

    # ------------------------------------------------------------------ Part C
    def gamma_int(etam):
        m = etam.shape[0]
        Em, Im = grassmann(m)
        Em = [np.array(M.tolist(), dtype=np.float64) for M in Em]
        Im = [M.T for M in Em]
        return [Em[i] + sum(float(etam[i, j]) * Im[j] for j in range(m)) for i in range(m)]

    def minpoly_check(phim, etam=None):
        """Gamma = sum xi^{mu nu} gamma_mu (x) gamma_nu with xi = eta^{-1}; test prod_{k=0..n}(x-(n-2k))."""
        etam = phim if etam is None else etam
        m = etam.shape[0]
        xi = np.array(sp.Matrix(etam).inv().tolist(), dtype=np.float64)
        g = gamma_int(np.array(phim.tolist(), dtype=np.float64))
        D = (1 << m) ** 2
        Gam = sum(xi[a, b] * np.kron(g[a], g[b]) for a in range(m) for b in range(m) if xi[a, b] != 0)
        roots = [m - 2 * k for k in range(m + 1)]
        assert (np.abs(Gam).sum(axis=1).max() + m) ** (m + 1) < 2 ** 52      # float64 products stay exact integers
        full = np.eye(D)
        for c in roots:
            full = full @ (Gam - c * np.eye(D))
        annihilated = not full.any()
        minimal = True
        for skip in roots:
            part = np.eye(D)
            for c in roots:
                if c != skip:
                    part = part @ (Gam - c * np.eye(D))
            minimal &= bool(part.any())
        return annihilated, minimal, roots

    for m in range(1, 6):
        a, mn, roots = minpoly_check(sp.eye(m))
        check(f"Conjecture 8.2, dim M = {m}: minimum polynomial of Gamma has exactly the roots {roots}", a and mn)
    for name, em in (("signature (1,3)", sp.diag(1, -1, -1, -1)), ("signature (2,2)", sp.diag(1, 1, -1, -1)),
                     ("non-diagonal eta, det = -1", sp.Matrix([[0, 1, 0, 0], [1, 0, 0, 0], [0, 0, 2, 1], [0, 0, 1, 1]]))):
        a, mn, roots = minpoly_check(em)
        check(f"   independent of the scalar product: {name}, dim 4", a and mn)
    ph = sp.diag(1, -1, -1, -1) + sp.Matrix(4, 4, lambda i, j: 0 if i == j else (1 if i < j else -1) * (i + j + 1))
    a, mn, roots = minpoly_check(ph, sp.diag(1, -1, -1, -1))
    check("   unchanged for non-symmetric phi = eta + omega (xi = eta^{-1}), dim 4", a and mn)



if __name__ == "__main__":
    print("== 1986 and Jadczyk, n = 3"); part_1986(3)
    print("== 1986 and Jadczyk, n = 4"); part_1986(4)
    print("== Sobczyk"); part_sobczyk()
    print("== 1997"); part_1997()
    print(f"all {COUNT} checks passed")
