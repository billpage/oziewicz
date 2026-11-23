# verify_cartan_dg.mpl -- cross-check of supplement/cartan_calculus_in_sympy.md (prefix CT)
# with Maple's DifferentialGeometry package (Anderson and Torre).
#
#   K1  conventions: wedge normalisation, Hook contracts the first slot, wedge sign, bracket sign
#   K2  the identities of CT-C, CT-D, CT-E on generic forms of degree 0..3 and generic vector
#       fields (every coefficient an undefined function of t, x, y, z), with must-fail variants
#   K3  naturality under phi(t,x,y,z) = (t + xy, x + z^2, y + z, z) (CT-I), and what
#       Pushforward returns with two and with three arguments
#   K4  edge cases that raise errors (recorded, expected)
#   K5  eight concrete objects printed as OBJ lines, compared term by term with the SymPy
#       functions of src/verify_cartan_tutorial.py by src/compare_cartan_dg.py
#
# Needs Maple (run on Bill Page's Maple 2022 server); not run by CI. About 5 s.
# Prints CHECKS <n> and FAILURES [...] at the end. Every check, including its set-up, runs
# inside try/catch, so an error is a failure; CHECKS 58 with FAILURES [] means all passed.
with(DifferentialGeometry): with(Tools):
DGsetup([t, x, y, z], M):
printf("Maple: %s\n", convert(kernelopts(version), string));
Om := [dt, dx, dy, dz]:  Vb := [D_t, D_x, D_y, D_z]:
iz := proc(e) local c; if e = 0 then return true end if; c := DGinfo(e, "CoefficientSet"); evalb(map(simplify, c) subset {0}) end proc:
nchecks := 0: fails := []:
chk := proc(lbl, f, want) global nchecks, fails; local e;
  nchecks := nchecks + 1;
  try e := f() catch: fails := [op(fails), cat(lbl, " (error)")]; return end try;
  if iz(e) <> want then fails := [op(fails), lbl] end if
end proc:
chkb := proc(lbl, f) global nchecks, fails; local b;     # f() returns true or false
  nchecks := nchecks + 1;
  try b := f() catch: fails := [op(fails), cat(lbl, " (error)")]; return end try;
  if b <> true then fails := [op(fails), lbl] end if
end proc:
data := w -> op(1, w)[2]:                                 # the list of [indices, coefficient] of a _DG object
gform := proc(nm, k) local S, terms, w, i;
  if k = 0 then return nm(t, x, y, z) end if;
  terms := 0;
  for S in combinat:-choose([1, 2, 3, 4], k) do
    w := Om[S[1]]; for i from 2 to k do w := w &wedge Om[S[i]] end do;
    terms := evalDG(terms + cat(nm, op(S))(t, x, y, z) * w)
  end do;
  terms
end proc:
gvec := proc(nm) local i; evalDG(add(cat(nm, i)(t, x, y, z) * Vb[i], i = 1 .. 4)) end proc:
vec := c -> evalDG(c[1] * D_t + c[2] * D_x + c[3] * D_y + c[4] * D_z):

printf("--- K1 conventions\n");
chkb("K1a wedge without 1/2: dt^dx = dt(x)dx - dx(x)dt",
  () -> evalb(data(convert(dt &wedge dx, DGtensor)) = [[[1, 2], 1], [[2, 1], -1]]));
chkb("K1b Hook(D_x, Hook(D_t, dt^dx)) = 1 (first slot)", () -> evalb(Hook(D_x, Hook(D_t, dt &wedge dx)) = 1));
chk("K1c i_X(dt^dx^dy) = X0 dx^dy - X1 dt^dy + X2 dt^dx (CT-C4)",
  () -> evalDG(Hook(vec([X0, X1, X2, X3]), dt &wedge dx &wedge dy) - (X0 * dx &wedge dy - X1 * dt &wedge dy + X2 * dt &wedge dx)), true);
chk("K1d (dx^dz)^(dt^dy) = -dt^dx^dy^dz (CT-A1)", () -> evalDG((dx &wedge dz) &wedge (dt &wedge dy) + dt &wedge dx &wedge dy &wedge dz), true);
chk("K1e LieBracket(x D_y, D_x) = -D_y", () -> evalDG(LieBracket(evalDG(x * D_y), D_x) + D_y), true);

printf("--- K2 identities on generic fields\n");
XV := gvec(xv): YV := gvec(yv): XY := LieBracket(XV, YV):
for k from 1 to 3 do
  FK := gform(ff, k);
  for q from 1 to 4 - k do
    GQ := gform(gg, q);
    chk(cat("C3 ", k, q), () -> evalDG(Hook(XV, FK &wedge GQ) - Hook(XV, FK) &wedge GQ - (-1)^k * FK &wedge Hook(XV, GQ)), true);
    chk(cat("C3' ", k, q, " must fail"), () -> evalDG(Hook(XV, FK &wedge GQ) - Hook(XV, FK) &wedge GQ + (-1)^k * FK &wedge Hook(XV, GQ)), false);
    if k + q <= 3 then
      chk(cat("D3 ", k, q), () -> evalDG(ExteriorDerivative(FK &wedge GQ) - ExteriorDerivative(FK) &wedge GQ - (-1)^k * FK &wedge ExteriorDerivative(GQ)), true);
    end if;
    chk(cat("E5 ", k, q), () -> evalDG(LieDerivative(XV, FK &wedge GQ) - LieDerivative(XV, FK) &wedge GQ - FK &wedge LieDerivative(XV, GQ)), true);
  end do;
  LF := LieDerivative(XV, FK);
  if k <= 2 then chk(cat("D2 ", k), () -> ExteriorDerivative(ExteriorDerivative(FK)), true) end if;
  chk(cat("E1 ", k), () -> evalDG(LF - Hook(XV, ExteriorDerivative(FK)) - ExteriorDerivative(Hook(XV, FK))), true);
  if k <= 2 then chk(cat("E2 ", k), () -> evalDG(LieDerivative(XV, ExteriorDerivative(FK)) - ExteriorDerivative(LF)), true) end if;
  chk(cat("E3 ", k), () -> evalDG(LieDerivative(XV, Hook(YV, FK)) - Hook(YV, LF) - Hook(XY, FK)), true);
  chk(cat("E3' ", k, " must fail"), () -> evalDG(LieDerivative(XV, Hook(YV, FK)) - Hook(YV, LF) + Hook(XY, FK)), false);
  chk(cat("E4 ", k), () -> evalDG(LieDerivative(XV, LieDerivative(YV, FK)) - LieDerivative(YV, LF) - LieDerivative(XY, FK)), true);
end do:
u := ff(t, x, y, z):
chk("E1 0", () -> LieDerivative(XV, u) - Hook(XV, ExteriorDerivative(u)), true);
chk("D2 0", () -> ExteriorDerivative(ExteriorDerivative(u)), true);
chk("E4 0", () -> simplify(LieDerivative(XV, LieDerivative(YV, u)) - LieDerivative(YV, LieDerivative(XV, u)) - LieDerivative(XY, u)), true);
printf("after K2: %d checks\n", nchecks);

printf("--- K3 naturality\n");
phi := [t + x * y, x + z^2, y + z, z]:
eqs := L -> [t = L[1], x = L[2], y = L[3], z = L[4]]:
at := (e, p) -> subs({t = p[1], x = p[2], y = p[3], z = p[4]}, e):
Phi := Transformation(M, M, eqs(phi)):
PhiInv := InverseTransformation(Phi):
psi := [y*z^2 - z^3 - x*y + x*z + t, -z^2 + x, y - z, z]:
chkb("K3a psi o phi = id (psi is phi^-1)", () -> evalb(map(simplify, at(psi, phi)) = [t, x, y, z]));
Jpsi := DGinfo(PhiInv, "JacobianMatrix"):
Vc := Vector([1 + y, x, 0, t]):  V := vec(Vc):
pullV := vec(map(simplify, at(Jpsi, phi) . at(Vc, phi))):       # phi^* V = (D phi)^-1 (V o phi)
F2 := evalDG((x * z + t) * dt &wedge dx + t * y * dt &wedge dz):
G1 := evalDG(x * dt + y * t * dx + dz):
chk("K3b Pushforward(PhiInv, V, eqs(phi)) = phi^* V", () -> evalDG(Pushforward(PhiInv, V, eqs(phi)) - pullV), true);
chk("K3c Pushforward(PhiInv, V) = Dpsi_p V(p), not composed", () -> evalDG(Pushforward(PhiInv, V) - vec(map(simplify, Jpsi . Vc))), true);
chk("K3d ... and so it is not phi^* V", () -> evalDG(Pushforward(PhiInv, V) - pullV), false);
chk("I1 phi^* d = d phi^*", () -> evalDG(Pullback(Phi, ExteriorDerivative(F2)) - ExteriorDerivative(Pullback(Phi, F2))), true);
chk("I2 phi^*(f ^ g) = phi^* f ^ phi^* g", () -> evalDG(Pullback(Phi, F2 &wedge G1) - Pullback(Phi, F2) &wedge Pullback(Phi, G1)), true);
chk("I3 phi^* i_V = i_{phi^* V} phi^*", () -> evalDG(Pullback(Phi, Hook(V, F2)) - Hook(pullV, Pullback(Phi, F2))), true);
chk("I3 phi^* L_V = L_{phi^* V} phi^*", () -> evalDG(Pullback(Phi, LieDerivative(V, F2)) - LieDerivative(pullV, Pullback(Phi, F2))), true);
chk("I3' with V in place of phi^* V, must fail", () -> evalDG(Pullback(Phi, Hook(V, F2)) - Hook(V, Pullback(Phi, F2))), false);

printf("--- K4 edge cases (an error is the expected outcome)\n");
vol := dt &wedge dx &wedge dy &wedge dz:
for pr in [["ExteriorDerivative of a 4-form on a 4-manifold", () -> ExteriorDerivative(vol)],
           ["Hook of a function", () -> Hook(D_t, ff(t, x, y, z))],
           ["sum of a 1-form and a 2-form", () -> evalDG(dx + dt &wedge dx)]] do
  nchecks := nchecks + 1;
  try pr[2](); fails := [op(fails), cat("K4 no error: ", pr[1])]
  catch: printf("  %s -> error: %s\n", pr[1], StringTools:-FormatMessage(lastexception[2 .. -1])) end try;
end do:
chk("K4 LieDerivative of the volume form works: L_{x D_x} vol = vol", () -> evalDG(LieDerivative(evalDG(x * D_x), vol) - vol), true);

printf("--- K5 objects for src/compare_cartan_dg.py\n");
XC := vec([1 + y, x, t * z, t]):  YC := vec([x^2, 0, z, -y * t]):
P2 := evalDG(x * z * dt &wedge dx + y * dy &wedge dz + t * y * dt &wedge dz + sin(x) * dx &wedge dy):
P3 := evalDG(exp(t) * y * dt &wedge dx &wedge dz + x^3 * dx &wedge dy &wedge dz):
A1 := evalDG(dt + x * dy + t^2 * dz):
for ob in [["d F2", ExteriorDerivative(P2)], ["i_X F2", Hook(XC, P2)], ["i_X F3", Hook(XC, P3)],
           ["L_X F2", LieDerivative(XC, P2)], ["L_X F3", LieDerivative(XC, P3)], ["A1 ^ F2", A1 &wedge P2],
           ["[X,Y]", LieBracket(XC, YC)], ["L_X A1", LieDerivative(XC, A1)]] do
  printf("OBJ|%s|%a\n", ob[1], data(ob[2]));
end do:
printf("CHECKS %d\nFAILURES %a\n", nchecks, fails);
printf("time %.1f s\n", time());
