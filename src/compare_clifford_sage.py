"""Compare SageMath's Clifford construction with the SymPy functions of verify_cartan_tutorial.py.

Section 13.5 of supplement/cartan_calculus_in_sympy.md. src/verify_clifford_sage.sage
(SageMath) prints, for one fixed integer phi on R^4, the matrix W_phi whose column S is
gamma_{i1} ... gamma_{ik} 1 for the blade e_S = e_{i1} ^ ... ^ e_{ik}, with
gamma_i = e_i ^ . + sum_j phi_ij i_{e_j} (Oziewicz 1986, eq. (23.2)), as lines

    WCOL|<bitmask S>|<list of (bitmask T, entry W[T, S])>

computed with Sage's own ExteriorAlgebra. This script computes W_phi with the functions
wedge and iv of src/verify_cartan_tutorial.py and compares the two entry by entry. It then
changes one entry of Sage's output and checks that the comparison reports it.

With no argument the WCOL lines are those of the run recorded below, so the script runs
without Sage. With a path, it reads the WCOL and PHI lines from that Sage transcript.

Recorded run: SageMath 10.10, 24 November 2026, on Bill Page's server, saved there as
sage-work/host-runs/20261124-095558-verify_clifford_sage.sage; CHECKS 26, FAILURES [].

Run:  PYTHONPATH=src python3 -u src/compare_clifford_sage.py [sage_transcript]
Exact (SymPy rationals). Writes no files.
"""
import ast
import sys

import sympy as sp

# The functions of verify_cartan_tutorial.py, without running its checks (which end in SystemExit):
# execute the part of the file before its test data.
_SRC = open(__file__.replace("compare_clifford_sage.py", "verify_cartan_tutorial.py")).read()
_NS = {}
exec(_SRC.split("# ---------------------------------------------------------------- test data")[0], _NS)
add, bits, iv, sm, wedge = (_NS[k] for k in ("add", "bits", "iv", "sm", "wedge"))

RECORDED = r"""
WCOL|0|[(0, 1)]
WCOL|1|[(1, 1)]
WCOL|2|[(2, 1)]
WCOL|4|[(4, 1)]
WCOL|8|[(8, 1)]
WCOL|3|[(0, 2), (3, 1)]
WCOL|5|[(5, 1)]
WCOL|9|[(0, -1), (9, 1)]
WCOL|6|[(0, 3), (6, 1)]
WCOL|10|[(0, 1), (10, 1)]
WCOL|12|[(12, 1)]
WCOL|7|[(1, 3), (4, 2), (7, 1)]
WCOL|11|[(1, 1), (2, 1), (8, 2), (11, 1)]
WCOL|13|[(4, 1), (13, 1)]
WCOL|14|[(4, -1), (8, 3), (14, 1)]
WCOL|15|[(0, -3), (5, -1), (6, -1), (9, 3), (12, 2), (15, 1)]
PHI|[[1, 2, 0, -1], [0, -1, 3, 1], [2, 1, 1, 0], [1, -2, 0, 2]]
"""
N = 4


def parse(text):
    cols, phi = {}, None
    for line in text.splitlines():
        if line.startswith("WCOL|"):
            _, S, entries = line.split("|", 2)
            cols[int(S)] = {T: sp.Rational(str(c)) for T, c in ast.literal_eval(entries)}
        elif line.startswith("PHI|"):
            phi = sp.Matrix(ast.literal_eval(line.split("|", 1)[1]))
    return cols, phi


def gamma(phi, i, f):
    """gamma_i f = e_i ^ f + sum_j phi_ij i_{e_j} f"""
    return add(wedge({1 << i: 1}, f), *[sm(phi[i, j], iv([int(k == j) for k in range(N)], f)) for j in range(N)])


def w_column(phi, S):
    f = {0: sp.Integer(1)}
    for i in reversed(bits(S)):
        f = gamma(phi, i, f)
    return f


text = open(sys.argv[1]).read() if len(sys.argv) > 1 else RECORDED
sage_cols, PHI = parse(text)
ours = {S: w_column(PHI, S) for S in range(1 << N)}
print("compare_clifford_sage: SageMath W_phi against verify_cartan_tutorial.py (wedge, iv)")
ok = sorted(sage_cols) == list(range(1 << N)) and PHI is not None
print(f"  {'ok  ' if ok else 'FAIL'}  all 16 columns and phi present")
same = all(sage_cols.get(S) == ours[S] for S in range(1 << N))
ok &= same
print(f"  {'ok  ' if same else 'FAIL'}  W_phi agrees entry by entry ({sum(len(c) for c in ours.values())} non-zero entries)")
bad = {S: dict(c) for S, c in sage_cols.items()}
bad[15][0] = bad[15][0] + 1
caught = bad[15] != ours[15]
ok &= caught
print(f"  {'ok  ' if caught else 'FAIL'}  a changed entry of Sage's W is reported as a difference")
print("all checks pass" if ok else "FAILED")
raise SystemExit(0 if ok else 1)
