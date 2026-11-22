# Heat and helicity of a body: Kiehn's irreversibility, spin as a period

> Step 6 left four open items on the grammar of a body (GB-SP1, GB-SP3 to GB-SP5); this note takes them up. **Lemma HH1**: near any point a body is $`X = \partial_t`$, $`\alpha = dt + A(t, x)`$, a time-dependent connection on its worldlines, with acceleration $`a = \dot A`$ and rotation $`\Omega = d_x A - A \wedge \dot A`$. **Proposition HH2**: every body obeys the vorticity identity $`da = \alpha \wedge L_X a + L_X \Omega`$. **Proposition HH3**: so Kiehn's irreversibility splits, $`a \wedge da = -\alpha \wedge a \wedge L_X a + a \wedge L_X \Omega`$, so either the acceleration turns or the rotation changes about the acceleration. The rotation itself does not enter: a rigidly rotating body in Minkowski space is reversible, with $`a = d \ln \gamma`$, and a non-rotating Fermi frame whose acceleration $`g`$ turns is not, with $`a \wedge da \propto dt \wedge g \wedge \dot g`$; this answers GB-SP4. **Proposition HH4**: for dust $`\int_\Sigma p \wedge dp`$ is a conserved scalar, the helicity, and it is independent of the spin $`P \wedge L`$: circular flows have spin and no helicity, and a counter-helical flow has helicity and no spin; so GB-SP1 is answered no. **Proposition HH5**: for axisymmetric circular flow $`\alpha \wedge d\alpha = u_t^2\, dt \wedge d\phi \wedge d\ell`$, which vanishes exactly when the specific angular momentum $`\ell`$ is constant; a body that contains its axis then cannot rotate, but a ring can, as the potential vortex $`v = \ell/r`$, $`r > |\ell|`$. CS6's link between spin and the clock is the circulation, of grades 1 and 2, not grade 3. **Proposition HH6**: on such a ring with a closed momentum form, $`S = N \oint p/2\pi`$: the spin is a period, and Bohr–Sommerfeld gives the quantized vortex. **Proposition HH7**: pointwise the operators $`\mathrm{ev}`$, $`\mathrm{cr}`$ of several bodies generate the Clifford algebra of their span, of dimension $`2^{\dim W}`$; with $`d`$ the algebra is infinite; $`\mathcal D = \iota_\Phi`$ for the connection $`\Phi = X \otimes \alpha`$, whose curvature is $`-\Omega \otimes X`$. Checked exactly with SymPy. No new prediction.

*Ladder abstract — see the [full list](README.md#the-ladder).*

**Status.** Analysis note, step 7 of the ladder. Theorem prefix **HH**. Companion
script: [`src/verify_heat_and_helicity.py`](../src/verify_heat_and_helicity.py) (Parts A
to I; §8). Prompted by Bill Page, 22 November 2026: take up GB-SP1 and GB-SP4, with
Kiehn's link between $`a \wedge da = 0`$, period integrals and quantization, and the
spin of Pauli and Lubański; then judge from the shortened version of Kolář, Michor and
Slovák (1993) whether that book bears on GB-SP3 and GB-SP5. Derivation and checks were
drafted with Claude (Anthropic) and are subject to review, and no separate reader has
checked them; every claim about what a paper says is a reading of the cited page, and
references marked *from memory* were not checked against the paper.
[PDF](https://github.com/billpage/oziewicz/releases/latest/download/heat_and_helicity.pdf)

---

## 0. What this note asks, inherits and retracts

**Question.** Kiehn reads $`a \wedge da \neq 0`$ as irreversibility and $`p \wedge dp`$ as a
candidate for spin. For one body, what do these grade-3 words measure, and is either of
them the spin $`P \wedge L`$?

**Inherits.** From step 4: CS5 ($`S_{ij} = -\tfrac12 \int r^2 (d\pi)_{ij}`$) and CS6 (the circulation of
the clock). From step 3: MF10 (the clock is a connection) and MF11 (time functions). From
step 5: OI3 (the Wigner angle as an area). From step 6: GB0, GB4 ($`d\alpha = \alpha \wedge a + \Omega`$,
the Pfaff sequence), GB5 ($`Q = a`$), GB6 and the open items GB-SP1, GB-SP3 to GB-SP5.

**Retracts or corrects.** Nothing is retracted.

| Earlier statement | What happens to it |
|---|---|
| `grammar_of_a_body.md` §6: "Step 4 (CS6) has already identified the first two entries for axisymmetric dust" | Refined (HH5): CS6 links $`P \wedge L`$ to the circulation $`\oint \alpha`$, not to $`\alpha \wedge d\alpha`$; on a ring the spin can be nonzero with $`\alpha \wedge d\alpha = 0`$ |
| `grammar_of_a_body.md` GB-SP1 | Answered, no (HH4, HH5) |
| `grammar_of_a_body.md` GB-SP4 | Answered (HH3) |
| `grammar_of_a_body.md` GB-SP3 | Answered in part (HH7): finite pointwise, infinite with $`d`$ |
| `grammar_of_a_body.md` GB-SP5 | Not answered; restated and a route given (§7) |

Sentences in earlier notes were not rewritten; the places are marked.

---

## 1. The flow box

A body is $`(X, \alpha)`$ with $`\alpha X = 1`$ on a 4-manifold (GB0). Its acceleration is $`a = \iota_X d\alpha = L_X \alpha`$,
its rotation is $`\Omega = \mathcal M\, d\alpha`$, and $`d\alpha = \alpha \wedge a + \Omega`$ with $`\iota_X a = \iota_X \Omega = 0`$ (GB4). A form $`\beta`$ is
*spatial* if $`\iota_X \beta = 0`$. On spatial forms $`\alpha \wedge`$ is injective, since $`\iota_X(\alpha \wedge \beta) = \beta`$, so a form
splits uniquely as $`\alpha \wedge \beta + \gamma`$ with $`\beta, \gamma`$ spatial.

**Lemma HH1 (flow box).** Near any point there are coordinates $`(t, x)`$ with $`X = \partial_t`$, and then

```math
\alpha = dt + A,\qquad A = A_i(t, x)\,dx^i,\qquad a = \dot A,\qquad \Omega = d_x A - A \wedge \dot A ,
```

where the dot is $`\partial_t = L_X`$ and $`d_x`$ is the exterior derivative in $`x`$ alone; $`A`$ is an arbitrary
time-dependent spatial 1-form.

*Proof.* $`X`$ is nowhere zero, so it can be straightened; $`\alpha(\partial_t) = 1`$ leaves $`\alpha = dt + A`$. Then
$`d\alpha = dt \wedge \dot A + d_x A`$, $`a = \iota_{\partial_t} d\alpha = \dot A`$, and $`\Omega = d\alpha - \alpha \wedge a`$. *Checked*: Part A, with $`A`$
three arbitrary functions of $`(t, x, y, z)`$. $`\square`$

*Reading.* The body is a time-dependent connection $`A`$ on its space of worldlines, and its
acceleration is the "electric field" of that connection in temporal gauge. Every natural
statement about one body can be checked in this form, since every body is locally of it.

---

## 2. Kiehn's irreversibility of one body

**Proposition HH2 (vorticity identity).** For every body

```math
da = \alpha \wedge L_X a + L_X \Omega ,\qquad\text{so}\qquad \iota_X\, da = L_X a,\quad \mathcal M\, da = L_X \Omega .
```

*Proof.* $`d^2\alpha = 0`$ applied to $`d\alpha = \alpha \wedge a + \Omega`$ gives $`0 = \Omega \wedge a - \alpha \wedge da + d\Omega`$, so
$`\alpha \wedge da = d\Omega + \Omega \wedge a`$. Apply $`\iota_X`$: the left side gives $`da - \alpha \wedge \iota_X da`$, the right side
$`\iota_X d\Omega = L_X \Omega`$, because $`\iota_X \Omega = \iota_X a = 0`$. Finally $`\iota_X da = L_X a - d\iota_X a = L_X a`$. *Checked*: Part A. $`\square`$

The spatial half is the vorticity equation: rotation changes along the process by the curl
of the acceleration. For dust, $`a = 0`$, so $`L_X \Omega = 0`$ and the rotation is carried with the flow
(Helmholtz).

**Proposition HH3 (two kinds of irreversibility).**

```math
a \wedge da = -\,\alpha \wedge \bigl(a \wedge L_X a\bigr) + a \wedge L_X \Omega ,
```

with both brackets spatial. So $`a \wedge da = 0`$ exactly when

1. $`a \wedge L_X a = 0`$: the acceleration keeps its direction along the process, and
2. $`a \wedge L_X \Omega = 0`$: the rate of change of the rotation has no component along the acceleration.

In the flow box, $`a \wedge da = -\,dt \wedge \dot A \wedge \ddot A + \dot A \wedge d_x \dot A`$; in 3-vector words, $`\mathbf a \times \dot{\mathbf a}`$ and
$`\mathbf a \cdot (\nabla \times \mathbf a)`$. The rotation $`\Omega`$ itself does not enter, only its rate $`L_X \Omega`$. Examples:

| body | $`\Omega`$ | $`a \wedge da`$ |
|---|---|---|
| geodesic dust | any | $`0`$, since $`a = 0`$ |
| rigid rotation in Minkowski space, $`\alpha = \gamma(dt - W r^2\, d\phi)`$ | $`\neq 0`$ | $`0`$; $`a = d \ln\gamma`$ exactly |
| non-rotating Fermi frame, $`ds^2 = -N^2 dt^2 + dx^2`$, $`N = 1 + g(t) \cdot x`$ | $`0`$ | $`-N^{-2}\, dt \wedge g \wedge \dot g`$ |
| thrust $`g`$ along an axis and angular acceleration $`k`$ about it, $`A = t g\, dz + \tfrac12 (w_0 + k t)(x\, dy - y\, dx)`$ | $`\neq 0`$ | $`g k\, dx \wedge dy \wedge dz`$ |

*Proof.* Wedge HH2 with $`a`$. $`\iota_X(a \wedge L_X a) = -a \wedge L_X \iota_X a = 0`$, and $`a \wedge L_X \Omega`$ is spatial since both factors
are; the splitting of §1 is unique. *Checked*: Part A for the identity; Parts B, C, D for the
examples. In Part C the Riemann tensor of the Fermi-frame metric vanishes for every $`g(t)`$, so
that row is an observer in Minkowski space with $`g`$ its acceleration in its own Fermi–Walker
axes. $`\square`$

The last row is a metric-free body; a rifle bullet in the barrel is the picture. It is in
Pfaff class 4 already with steady spin ($`d\alpha \wedge d\alpha = 2 g w\, dt \wedge dx \wedge dy \wedge dz + \dots`$, GB4: acceleration along
the rotation axis), but it is irreversible only when the angular velocity also changes:
acceleration along the axis of the *angular acceleration*. Thrust with steady spin, and
spin-up without thrust, are each reversible.

**Readings.** These are interpretations, not results.

- *Floors.* By Frobenius (Carathéodory's form of it in thermodynamics), $`a \wedge da = 0`$ means
  $`a = f\, d\Phi`$ locally. Since $`a(X) = 0`$, each level set $`\Phi = \text{const}`$ is a hypersurface made of whole
  worldlines. A reversible body can be stacked into floors that persist; in the Fermi frame
  the would-be floors $`g(t) \cdot x = \text{const}`$ turn with $`g`$ and contain no whole worldline.
- *Tolman.* For rigid stationary motion along a Killing field $`\xi`$, $`X = \xi/N`$ with $`N = |\xi|`$ and $`a = d \ln N`$
  (row 2). With Tolman and Ehrenfest's $`TN = \text{const}`$, Kiehn's heat 1-form of the body (GB5) is
  $`Q = a = -d \ln T`$. Reversibility in Kiehn's sense extends the existence of a Tolman temperature
  field; this is a place where the dictionary of GB5 reads correctly.
- *Thomas.* For a non-rotating Born-rigid body, condition 1 fails exactly when $`g \times \dot g \neq 0`$, that is,
  when the body's velocity curve on the hyperboloid is not a geodesic. A closed velocity
  loop then encloses area, and the Fermi–Walker axes return rotated by it: Thomas precession,
  the Wigner rotation of OI3 for infinitesimal triangles. So the irreversibility of a
  non-rotating body is the local source of Thomas precession. Only the condition $`g \times \dot g`$ is
  checked (HH-SP1).

**Answer to GB-SP4.** $`a \wedge da \neq 0`$ means that the body cannot be layered into persistent floors:
either its acceleration turns along the process, or its rotation changes about the
direction of its acceleration. It is not related to $`\Omega`$ itself, but to $`L_X \Omega`$ through condition 2.

---

## 3. Helicity is not spin

**Proposition HH4.** Let $`p = m\alpha`$ be the momentum form of dust, $`a = 0`$.

1. $`dp \wedge dp = 0`$, so the 3-form $`p \wedge dp`$ is closed, and $`H = \int_\Sigma p \wedge dp = m^2 \int_\Sigma \mathbf w \cdot (\nabla \times \mathbf w)\, d^3x`$, with $`\mathbf w`$
   the pull-back of $`\alpha`$ to the slice $`\Sigma`$, is the same on every slice (given decay): a Lorentz scalar.
2. $`H`$ and $`P \wedge L`$ are independent. On the slice $`t = \text{const}`$, every stationary axisymmetric circular flow
   has $`H = 0`$, while $`S = \int u_\phi\, dm`$ need not vanish. The flow
   $`\mathbf w = e^{-|x|^2}\bigl[(1 - \rho^2)(-y, x, 0) + (1 - 2\rho^2)(0, 0, 1)\bigr]`$, with $`\rho^2 = x^2 + y^2`$ and rest mass
   $`e^{-|x|^2}`$ per unit volume, has $`P = 0`$, $`L = 0`$ and $`H/m^2 = \sqrt2\,\pi^{3/2}/2 \approx 3.937`$.

*Proof.* (1) $`dp \wedge dp = 2m^2\, \alpha \wedge a \wedge \Omega = 0`$ (GB4), and pull-back commutes with $`d`$ and $`\wedge`$. (2) For
circular flow every term of $`\alpha \wedge d\alpha`$ contains $`dt`$ (HH5), so its pull-back to $`t = \text{const}`$ vanishes. The
example is an inner core and an outer sheath turning in opposite senses and moving in
opposite directions, helices of the same hand; the coefficients 1 and 2 were solved for
$`L_z = P_z = 0`$, and the other components vanish by symmetry. *Checked*: Parts B and F, exact. $`\square`$

$`H`$ is the relativistic fluid helicity (Moffatt 1969, *from memory*; Bekenstein 1987), which
counts the linking of vortex lines. $`P \wedge L`$ is a trivector, four numbers, and a slice integral of
$`p \wedge dp`$ is one number. Dimensions say the same: $`\oint p`$ is an action, $`H`$ an action squared. In
Kiehn's vocabulary $`A \wedge F`$ is *topological torsion*, with period quantum $`(h/e)^2`$, and *topological
spin* is the different 3-form $`A \wedge G`$, which needs an excitation 2-form $`G`$ (Kiehn,
arXiv:gr-qc/0603072, §9.2). Read this way, $`P \wedge dP`$ in Oziewicz's letters is Kiehn's torsion, not
his spin. Pauli–Lubański's $`W`$ is the dual of $`P \wedge L`$ by the volume form alone, a covector; the dual
of $`p \wedge dp`$ is the vorticity vector; comparing them needs the metric as well.

**Spin one half.** The Belinfante momentum density of a spin-up state is $`\pmb\pi_s = \tfrac12 \nabla \times \mathbf s`$, with
spin density $`\mathbf s = \tfrac{\hbar}{2} \rho\, \mathbf e_z`$ (Belinfante 1940; Ohanian 1986; both *from memory*). For every
axisymmetric $`\rho`$ its helicity density is zero, and for a normalised Gaussian
$`\int \mathbf r \times \pmb\pi_s\, d^3x = \hbar/2`$ (Part G). Spin one half is the second moment of $`d\pi`$, as CS5 says, and is
invisible to $`p \wedge dp`$, like the rigid rotor.

---

## 4. What grade 3 says: the axis and the ring

**Proposition HH5.** For a stationary axisymmetric circular flow, $`\alpha = u_t\, dt + u_\phi\, d\phi`$ with $`u_t, u_\phi`$
functions of $`(r, z)`$, and $`\ell = -u_\phi/u_t`$ (the specific angular momentum of the literature on
relativistic tori),

```math
\alpha \wedge d\alpha = u_t^{\,2}\; dt \wedge d\phi \wedge d\ell .
```

So $`\alpha \wedge d\alpha = 0`$ exactly when $`\ell`$ is constant on the body, and

1. if the body contains its axis, where $`u_\phi = 0`$, then $`\alpha \wedge d\alpha = 0`$ forces $`\ell = 0`$: no rotation. For such a
   body $`S \neq 0`$ implies $`\alpha \wedge d\alpha \neq 0`$, an implication, not an integral;
2. on a ring, constant $`\ell \neq 0`$ is allowed. In Minkowski space it is the potential vortex $`v = \ell/r`$,
   which is a unit flow only for $`r > |\ell|`$, so the hole is forced. Then $`\alpha = u_t\, dT`$ with $`T = t - \ell \phi`$:
   Frobenius holds, $`\Omega = 0`$, yet $`T`$ has period $`-2\pi\ell`$ round the ring. For dust, kinematically,
   $`S = \ell \int \gamma\, dm \neq 0`$ (CS6(2) with $`u_\phi = \ell\gamma`$).

*Proof.* Expanding, $`\alpha \wedge d\alpha = dt \wedge (u_t\, du_\phi - u_\phi\, du_t) \wedge d\phi`$, and $`u_t\, du_\phi - u_\phi\, du_t = -u_t^2\, d\ell`$.
On the axis $`u_\phi = g_{\phi\phi} u^\phi = 0`$. For constant $`\ell`$, $`-u_t^2 + u_\phi^2/r^2 = -1`$ gives $`u_t = -(1 - \ell^2/r^2)^{-1/2}`$, and
$`v = r\, d\phi/dt = \ell/r`$. *Checked*: Part E. $`\square`$

So CS6's link between spin and the failure of the clocks to close runs through the
circulation $`\oint \alpha`$, that is through $`d\alpha`$ on a disk (grade 2) or a period on a ring (grade 1), and
not through $`\alpha \wedge d\alpha`$. On the ring there is a Sagnac gap with no rotation $`\Omega`$: the gap is
topological. Holding dust on circles needs forces, as in CS6; the next proposition uses a
fluid, which supplies them.

**Proposition HH6 (spin as a period).** Let a perfect fluid, with particle density $`n`$, enthalpy
per particle $`h`$ and momentum form $`p = h\, u^\flat`$ ($`E = h`$ in GB4(4)), occupy a ring with constant $`\ell`$ and
$`h u_t = -\mu`$ constant. Then $`p = -\mu\, dT`$ is closed, so $`dp = 0`$ and $`p \wedge dp = 0`$, and

```math
S = \int T^t{}_\phi\, d^3x = \int n h\, u^t u_\phi\, d^3x = \mu \ell\, N = N\,\frac{1}{2\pi} \oint p ,\qquad N = \int n u^t\, d^3x .
```

*Proof.* $`T^t{}_\phi = (e + P) u^t u_\phi`$ with $`e + P = nh`$, and $`h u_\phi = -\ell h u_t = \mu \ell`$; $`\oint p = 2\pi \mu \ell`$. $`\square`$

All of the spin is a de Rham period of the closed momentum form. Imposing Bohr–Sommerfeld,
$`\oint p = 2\pi n \hbar`$, gives $`S = N n \hbar`$: the quantized vortex of Onsager (1949) and Feynman (1955) (*from
memory*), and the one-dimensional periods of Kiehn (1977). The same holds for Schrödinger's
equation in Madelung form, where $`p = \hbar\, dS`$ is closed: in a hydrogen state with $`m \neq 0`$ the
density vanishes on the $`z`$-axis, the flow lives on a ring, and $`L_z = m\hbar`$ is a period. A quantum
state evades part 1 of HH5 by a node on its axis.

**Answer to GB-SP1.** No, for dust or anything else checked here. The local grade-3 word
integrates to the helicity, independent of $`P \wedge L`$ (HH4). Spin is reached locally through grade
2 (the second moment of $`d\pi`$, CS5; the circulation, CS6) and, on a ring, globally through a
period of $`p`$ (HH6). The three grade-3 rows of GB6 are three different quantities; the one-body
row has its own invariant, $`H`$, which GB6 did not list.

---

## 5. The algebra of evaluation, creation and $`d`$

**Proposition HH7.**

1. Pointwise, the operators $`\mathrm{ev}_{X_i}`$, $`\mathrm{cr}_{\alpha_i}`$ of $`k`$ bodies generate an algebra isomorphic to $`\mathrm{Cl}(W, q|_W)`$,
   where $`W \subset V \oplus V^*`$ is the span of the $`X_i`$ and $`\alpha_i`$ and $`q`$ is the pairing; its dimension is
   $`2^{\dim W} \le 256`$.
2. With $`d`$ adjoined, $`[\mathrm{ev}_X, d] = L_X`$ and the $`L_X^n`$ are independent: infinitely many independent
   monomials.
3. $`\mathcal D = \alpha \wedge \iota_X = \iota_\Phi`$, the insertion operator of $`\Phi = X \otimes \alpha`$ (a degree-0 algebraic derivation), and
   $`\Phi`$ is a connection on the worldlines in the sense of Kolář, Michor and Slovák, Chapter III:
   $`\Phi^2 = \Phi`$, with image the tangent line of the flow. Its curvature, the Nijenhuis torsion of $`\Phi`$,
   is $`-\Omega \otimes X`$.

*Proof.* (1) The map $`\mathrm{Cl}(W) \to \mathrm{Cl}(V \oplus V^*) = \mathrm{End}(\Lambda V^*)`$ is injective for any subspace, since the associated
graded map $`\Lambda W \to \Lambda(V \oplus V^*)`$ is. (2) $`L_X^n`$ is a differential operator of order $`n`$. (3) For $`\xi, \eta`$ with
horizontal parts $`h\xi = \xi - \alpha(\xi) X`$, $`\Phi[h\xi, h\eta] = \alpha([h\xi, h\eta]) X = -d\alpha(h\xi, h\eta) X = -\Omega(\xi, \eta) X`$. *Checked*:
Part H (dimensions 4 and 16 for one and two bodies), Part I (the torsion in the flow box,
and the Leibniz rule for $`\mathcal D`$). $`\square`$

(3) is MF10 in the language of the monograph. For two bodies $`W`$ is 4-dimensional and $`q|_W`$ is
non-degenerate exactly when $`\Gamma_{XY}\Gamma_{YX} \neq 1`$; then the algebra is $`\mathrm{Cl}(2, 2) \cong M_4(\mathbb R)`$.

**Answer to GB-SP3, in part.** Pointwise there are finitely many independent monomials, and
no word is new beyond the Clifford algebra of $`W`$; the only invariant is the matrix of clock
factors. With $`d`$ there are infinitely many. The algebra then contains $`\mathrm{cr}_\beta`$ for every form $`\beta`$ in
the differential algebra of the clocks ($`[d, \mathrm{cr}_\alpha] = \mathrm{cr}_{d\alpha}`$, $`[L_X, \mathrm{cr}_\alpha] = \mathrm{cr}_a`$) and $`\mathrm{ev}_V`$ for every $`V`$ in the Lie
algebra of the $`X_i`$ ($`[L_X, \mathrm{ev}_Y] = \mathrm{ev}_{[X, Y]}`$), so its new words are the natural forms and vector fields of
the bodies: GB-SP5 again, for several bodies. By Frölicher and Nijenhuis (1956; KMS §8) every
graded derivation of forms is $`\iota_K + L_L`$ for unique vector-valued forms $`K, L`$, with commutators
given by their brackets; the derivation part is therefore generated by the $`X_i \otimes \alpha_j`$, and the
candidates for new two-body words are the mixed brackets $`[X \otimes \alpha, Y \otimes \beta]`$ (HH-SP3).

---

## 6. What Kolář, Michor and Slovák offer for GB-SP5

Read: the authors' shortened version (contents, preface, chapter introductions, index), not
the book.

- *Results that bear on it.* §25: for $`p > 0`$ every natural operator $`\Lambda^p T^* \to \Lambda^{p+1} T^*`$ is a constant
  multiple of $`d`$, without assuming linearity. Chapter VII: the natural bilinear operators
  taking a vector field and a $`k`$-form to a $`k`$-form form a 2-parameter family (so they are spanned
  by $`L_X \omega`$ and $`d\iota_X \omega`$), and those of Frölicher–Nijenhuis type a 10-parameter family. §34:
  multilinear natural operators by the representation theory of Lie algebras of vector
  fields. Chapter XI: every linear natural operator commutes with Lie derivatives.
- *Methods.* Chapter V (finite order, a nonlinear Peetre theorem), §24 (homogeneous function
  theorem; $`GL`$-invariant tensors are generated by Kronecker deltas), §28 (orbit reduction).
- *Not there*, as far as the introductions show: the nonlinear classification for a pair
  $`(X, \alpha)`$ with $`\alpha X = 1`$.

---

## 7. GB-SP5 restated

Two corrections to its wording. $`L_X = \iota_X d + d\iota_X`$ is redundant in the list. And "exactly" can hold
only for operations that are smooth on all bodies: where $`d\alpha \wedge d\alpha \neq 0`$, the ratio of 4-forms
$`(\alpha \wedge a \wedge da)/(d\alpha \wedge d\alpha)`$ is a natural function and $`d\alpha`$ is invertible, so there are natural operations
that are not words.

*A route, with the monograph's methods; a sketch, not a proof.* By HH1, a natural operation on
bodies is an operation on the jets of $`A`$ that is equivariant under the stabilizer of $`\partial_t`$, the
maps $`(t, x) \mapsto (t + f(x), \varphi(x))`$. The homotheties $`x \mapsto \lambda x`$ lie in it and send $`A`$ to $`\lambda A(t, \lambda x)`$, so
every jet of $`A`$ goes to zero as $`\lambda \to 0`$. Hence a smooth natural function of a body is constant, the
homogeneous function theorem with weights should make every smooth natural operation
polynomial in the jets, and the invariant tensor theorem applies to the $`GL(3)`$ part. If so, the
only natural vector fields smooth on all bodies are constant multiples of $`X`$: a spatial
component needs an upper index, which $`GL(3)`$-invariant tensors built from lower-index jets
cannot supply. Restated as HH-SP4.

---

## 8. Verification

[`src/verify_heat_and_helicity.py`](../src/verify_heat_and_helicity.py), SymPy, exact; about
10 s. Forms as dictionaries over sorted index tuples with $`d`$, $`\wedge`$, $`\iota`$ and $`L`$; a 4D Riemann
tensor (Part C); $`16 \times 16`$ matrices (Part H). 32 checks, all pass.

| Part | Checks | For |
|---|---|---|
| A | flow box; HH2; $`\mathcal M\, da = L_X \Omega`$; HH3 in both forms | HH1–HH3 |
| B | rigid rotation: $`a = d \ln\gamma`$, $`\Omega \neq 0`$, $`a \wedge da = 0`$, $`\alpha \wedge d\alpha \neq 0`$, zero pull-back to $`t = \text{const}`$ | HH3, HH4 |
| C | Fermi frame: Riemann $`= 0`$ for all $`g(t)`$, $`\Omega = 0`$, $`a \wedge da = -N^{-2}\, dt \wedge g \wedge \dot g`$ | HH3 |
| D | thrust and spin-up: $`a \wedge da = g k\, dx \wedge dy \wedge dz`$; Pfaff class 4 | HH3 |
| E | HH5; constant $`\ell`$: unit flow for $`r > \ell`$, $`v = \ell/r`$, $`\alpha = u_t\, d(t - \ell\phi)`$ | HH5 |
| F | helicity without spin, $`H/m^2 = \sqrt2\pi^{3/2}/2`$; rotor with spin and zero helicity density | HH4 |
| G | Belinfante spin density: zero helicity density, spin $`\tfrac12`$ | §3 |
| H | algebra dimensions 4 and 16 | HH7(1) |
| I | Nijenhuis torsion of $`X \otimes \alpha`$ is $`-\Omega \otimes X`$; Leibniz rule for $`\mathcal D`$ | HH7(3) |

Two test expectations were corrected while the checks were written: the sign in HH5
($`+u_t^2`$), and the normalisation in Part G (the momentum density is half the curl of the spin
density). **Not verified:** the readings of §2 beyond the conditions stated; HH6 beyond the
algebra shown; the Schrödinger remark; the sketch of §7; the readings of the monograph, of
Kiehn and of the other cited papers.

---

## 9. Open items

- **HH-SP1.** Make the Thomas reading of HH3 quantitative: is the Thomas rotation over a closed
  velocity loop of a non-rotating rigid body an integral of $`a \wedge L_X a`$ along the worldline?
- **HH-SP2.** Kiehn's topological spin is $`A \wedge G`$, with $`G`$ an excitation 2-form. Is there a 2-form $`G`$ of a body
  or a system (for instance with $`dG`$ the particle current) for which $`p \wedge G`$ gives $`P \wedge L`$?
- **HH-SP3.** Classify the two-body words $`[X \otimes \alpha, Y \otimes \beta]`$ (Frölicher–Nijenhuis) and say which are
  relative acceleration, Wigner rotation or something new. Continues GB-SP3.
- **HH-SP4.** Are the natural operations smooth on all bodies $`(X, \alpha)`$ exactly the polynomial words in
  $`d`$, $`\wedge`$, $`\iota_X`$ and $`\alpha`$? Make the sketch of §7 a proof, or find a counterexample. Supersedes GB-SP5.
- **HH-SP5.** The Tolman reading holds for Killing flows. What does $`a = f\, d\Phi`$ with $`f \neq 1`$ mean, and is $`\Phi`$
  a temperature away from equilibrium?

---

## 10. What this does for the ladder

It answers GB-SP1 (no) and GB-SP4, answers GB-SP3 in part and restates GB-SP5. It moves the
link between spin and a body's clock from grade 3 to grades 1 and 2: spin is a second
moment of $`d\pi`$, a circulation, or a period. And it gives Kiehn's quantization a concrete
place on the ladder: on a ring, the spin of a fluid with a closed momentum form is a period.

---

## References

- R. M. Kiehn, "Periods on manifolds, quantization, and gauge", *J. Math. Phys.* 18 (1977)
  614–624, [doi:10.1063/1.523317](https://doi.org/10.1063/1.523317).
- R. M. Kiehn, "Thermodynamics and quantum cosmology",
  [arXiv:gr-qc/0603072](https://arxiv.org/abs/gr-qc/0603072), §9.2.
- R. M. Kiehn, "Topological-torsion and topological-spin as coherent structures in plasmas",
  [arXiv:physics/0102001](https://arxiv.org/abs/physics/0102001).
- H. K. Moffatt, "The degree of knottedness of tangled vortex lines", *J. Fluid Mech.* 35
  (1969) 117–129. *From memory.*
- J. D. Bekenstein, "Helicity conservation laws for fluids and plasmas", *Astrophys. J.* 319
  (1987) 207, [OSTI 5967851](https://www.osti.gov/biblio/5967851).
- C. Carathéodory, "Untersuchungen über die Grundlagen der Thermodynamik", *Math. Ann.* 67
  (1909) 355–386. *From memory.*
- R. C. Tolman and P. Ehrenfest, "Temperature equilibrium in a static gravitational field",
  *Phys. Rev.* 36 (1930) 1791. *From memory.*
- L. H. Thomas, "The motion of the spinning electron", *Nature* 117 (1926) 514. *From memory.*
- L. Onsager, *Nuovo Cimento* 6, Suppl. 2 (1949) 279; R. P. Feynman, *Prog. Low Temp. Phys.* 1
  (1955) 17. *From memory.*
- F. J. Belinfante, *Physica* 7 (1940) 449; H. C. Ohanian, "What is spin?", *Am. J. Phys.* 54
  (1986) 500. *From memory.*
- J. K. Lubański, *Physica* 9 (1942) 310. *From memory.*
- A. Frölicher and A. Nijenhuis, "Theory of vector-valued differential forms. Part I",
  *Indag. Math.* 18 (1956) 338–359. *From memory.*
- I. Kolář, P. W. Michor and J. Slovák, *Natural Operations in Differential Geometry*, Springer
  (1993); shortened version read,
  [author's page](https://www.mat.univie.ac.at/~michor/preprint-shadows/kmsbookh.html).
- J. Navarro and J. B. Sancho, "Natural operations on differential forms",
  [arXiv:1412.0840](https://arxiv.org/abs/1412.0840).
