"""Compare Maple DifferentialGeometry with the SymPy functions of verify_cartan_tutorial.py.

Section 13.4 of supplement/cartan_calculus_in_sympy.md. src/verify_cartan_dg.mpl (Maple)
prints eight objects as lines

    OBJ|<label>|<list of [indices, coefficient]>

with Maple's indices 1..4 for t, x, y, z. This script computes the same eight objects with
the functions d, iv, lie, wedge and bracket of src/verify_cartan_tutorial.py and compares
them term by term (sp.simplify of each difference). It then changes one sign in Maple's
first object and checks that the comparison reports the difference.

With no argument the OBJ lines are those of the run recorded below, so the script runs
without Maple. With a path, it reads the OBJ lines from that Maple transcript.

Recorded run: Maple 2022.2 (X86 64 LINUX, build 1657361), 23 November 2026, on Bill Page's
server, saved there as maple-work/runs/20261123-165819-verify_cartan_dg.mpl and .out;
CHECKS 58, FAILURES [].

Run:  PYTHONPATH=src python3 -u src/compare_cartan_dg.py [maple_transcript.out]
Exact (SymPy). Writes no files.
"""
import sys

import sympy as sp

# The functions of verify_cartan_tutorial.py, without running its checks (which end in SystemExit):
# execute the part of the file before its test data.
_SRC = open(__file__.replace("compare_cartan_dg.py", "verify_cartan_tutorial.py")).read()
_NS = {}
exec(_SRC.split("# ---------------------------------------------------------------- test data")[0], _NS)
add, bracket, d, form1, iv, lie, wedge = (_NS[k] for k in ("add", "bracket", "d", "form1", "iv", "lie", "wedge"))

RECORDED = r"""
OBJ|d F2|[[[1, 2, 4], x], [[1, 3, 4], -t]]
OBJ|i_X F2|[[[1], -t^2*y-x^2*z], [[2], -z*(sin(x)*t-x*y-x)], [[3], -t*y+sin(x)*x], [[4], t*y^2+t*y*z+t*y]]
OBJ|i_X F3|[[[1, 2], exp(t)*y*t], [[1, 4], -exp(t)*y*x], [[2, 3], x^3*t], [[2, 4], -x^3*t*z+exp(t)*y^2+exp(t)*y], [[3, 4], x^4]]
OBJ|L_X F2|[[[1, 2], -z*sin(x)+t*x+2*x*z], [[1, 3], -y], [[1, 4], t^2*z+y^2+y*z+y], [[2, 3], sin(x)+x*(cos(x)-z)], [[2, 4], sin(x)*t], [[3, 4], t*y+t*z]]
OBJ|L_X F3|[[[1, 2, 3], x^3], [[1, 2, 4], -x^3*z+t*z*exp(t)+exp(t)*y^2+2*exp(t)*y], [[2, 3, 4], 4*x^3-exp(t)*y]]
OBJ|A1 ^ F2|[[[1, 2, 3], x^2*z+sin(x)], [[1, 2, 4], t^2*x*z], [[1, 3, 4], -t*x*y+y], [[2, 3, 4], t^2*sin(x)]]
OBJ|[X,Y]|[[[1], 2*x^2-z], [[3], t^2*y-x^2*z+t], [[4], -t^2*z-x^2-y^2-y]]
OBJ|L_X A1|[[[1], t^2+x*z], [[3], 1+x], [[4], t*x+2*t*y+2*t]]
"""

t, x, y, z = XS = sp.symbols("t x y z")
LOC = dict(t=t, x=x, y=y, z=z, sin=sp.sin, cos=sp.cos, exp=sp.exp)

# the same objects as section K5 of verify_cartan_dg.mpl
X = [1 + y, x, t * z, t]
Y = [x ** 2, 0, z, -y * t]
F2 = {0b0011: x * z, 0b1100: y, 0b1001: t * y, 0b0110: sp.sin(x)}
F3 = {0b1011: sp.exp(t) * y, 0b1110: x ** 3}
A1 = form1([1, 0, x, t ** 2])
SYMPY = {"d F2": d(F2, XS), "i_X F2": iv(X, F2), "i_X F3": iv(X, F3), "L_X F2": lie(X, F2, XS),
         "L_X F3": lie(X, F3, XS), "A1 ^ F2": wedge(A1, F2), "[X,Y]": bracket(X, Y, XS),
         "L_X A1": lie(X, A1, XS)}


def parse(text):
    out = {}
    for line in text.splitlines():
        if line.startswith("OBJ|"):
            _, lbl, body = line.split("|", 2)
            out[lbl] = sp.sympify(body.replace("^", "**"), locals=LOC)
    return out


def agrees(lbl, terms):
    if lbl == "[X,Y]":
        mv = [0] * 4
        for idx, c in terms:
            mv[idx[0] - 1] = c
        return all(sp.simplify(a - b) == 0 for a, b in zip(mv, SYMPY[lbl]))
    mf = {sum(1 << (i - 1) for i in idx): c for idx, c in terms}       # Maple index i -> bit i - 1
    diff = add(mf, {k: -v for k, v in SYMPY[lbl].items()})
    return all(sp.simplify(v) == 0 for v in diff.values())


text = open(sys.argv[1]).read() if len(sys.argv) > 1 else RECORDED
maple = parse(text)
print()
print("compare_cartan_dg: Maple DifferentialGeometry against verify_cartan_tutorial.py")
ok = sorted(maple) == sorted(SYMPY)
print(f"  {'ok  ' if ok else 'FAIL'}  all eight objects present ({len(maple)} OBJ lines)")
for lbl in SYMPY:
    same = lbl in maple and agrees(lbl, maple[lbl])
    ok &= same
    print(f"  {'ok  ' if same else 'FAIL'}  {lbl}")
first = maple.get("d F2", [])
flipped = [[idx, -c] if k == 0 else [idx, c] for k, (idx, c) in enumerate(first)]
caught = bool(first) and not agrees("d F2", flipped)
ok &= caught
print(f"  {'ok  ' if caught else 'FAIL'}  a sign changed in Maple's d F2 is reported as a difference")
print("all checks pass" if ok else "FAILED")
raise SystemExit(0 if ok else 1)
