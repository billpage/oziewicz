# Heat and helicity of a body: Kiehn's irreversibility, spin as a period

> Step 6 left four open items on the grammar of a body (GB-SP1, GB-SP3 to GB-SP5); this note takes them up. **Lemma HH1**: near any point a body is $`X = \partial_t`$, $`\alpha = dt + A(t, x)`$, a time-dependent connection on its worldlines, with acceleration $`a = \dot A`$ and rotation $`\Omega = d_x A - A \wedge \dot A`$. **Proposition HH2**: every body obeys the vorticity identity $`da = \alpha \wedge L_X a + L_X \Omega`$. **Proposition HH3**: so Kiehn's irreversibility splits, $`a \wedge da = -\alpha \wedge a \wedge L_X a + a \wedge L_X \Omega`$, so either the acceleration turns or the rotation changes about the acceleration. The rotation itself does not enter: a rigidly rotating body in Minkowski space is reversible, with $`a = d \ln \gamma`$, and a non-rotating Fermi frame whose acceleration $`g`$ turns is not, with $`a \wedge da \propto dt \wedge g \wedge \dot g`$; this answers GB-SP4. **Proposition HH4**: for dust $`\int_\Sigma p \wedge dp`$ is a conserved scalar, the helicity, and it is independent of the spin $`P \wedge L`$: circular flows have spin and no helicity, and a counter-helical flow has helicity and no spin; so GB-SP1 is answered no. **Proposition HH5**: for axisymmetric circular flow $`\alpha \wedge d\alpha = u_t^2\, dt \wedge d\phi \wedge d\ell`$, which vanishes exactly when the specific angular momentum $`\ell`$ is constant; a body that contains its axis then cannot rotate, but a ring can, as the potential vortex $`v = \ell/r`$, $`r > |\ell|`$. CS6's link between spin and the clock is the circulation, of grades 1 and 2, not grade 3. **Proposition HH6**: on such a ring with a closed momentum form, $`S = N \oint p/2\pi`$: the spin is a period, and Bohr–Sommerfeld gives the quantized vortex. **Proposition HH7**: pointwise the operators $`\mathrm{ev}`$, $`\mathrm{cr}`$ of several bodies generate the Clifford algebra of their span, of dimension $`2^{\dim W}`$; with $`d`$ the algebra is infinite; $`\mathcal D = \iota_\Phi`$ for the connection $`\Phi = X \otimes \alpha`$, whose curvature is $`-\Omega \otimes X`$. **Proposition HH8**: granted finite order and polynomiality, which follow from Kolář, Michor and Slovák (23.4, 24.1), the natural functions, vector fields, 1-forms and 2-forms of a body are exactly the words in $`d`$, $`\wedge`$, $`\iota_X`$ and $`\alpha`$, and so is $`\iota_X`$ of every natural 3-form; weight 3 is open. Checked exactly with SymPy. No new prediction.

*Ladder abstract — see the [full list](README.md#the-ladder).*

**Status.** Analysis note, step 7 of the ladder. Theorem prefix **HH**. Companion
script: [`src/verify_heat_and_helicity.py`](../src/verify_heat_and_helicity.py) (Parts A
to K; §8). Prompted by Bill Page, 22 November 2026: take up GB-SP1 and GB-SP4, with
Kiehn's link between $`a \wedge da = 0`$, period integrals and quantization, and the
spin of Pauli and Lubański; then judge from the shortened version of Kolář, Michor and
Slovák (1993) whether that book bears on GB-SP3 and GB-SP5; the full book was then read in
the sections cited in §6. Derivation and checks were
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
| `grammar_of_a_body.md` GB-SP5 | Answered for functions, vector fields, 1-forms and 2-forms, granted finite order and polynomiality (HH8); open beyond (§7) |

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

## 6. What Kolář, Michor and Slovák offer

Read: the full book ([PDF on the author's page](https://www.mat.univie.ac.at/~michor/kmsbookh.pdf)), in the sections cited below; not read cover to cover. Numbers are the book's.

- **§25.4.** For $`p > 0`$ every natural operator $`\Lambda^p T^* \to \Lambda^{p+1} T^*`$ is $`k\, d`$; linearity follows from naturality.
  For $`p = 0`$ (25.5) the natural operators are $`g \mapsto \varphi(g)\, dg`$ with $`\varphi`$ any smooth function: not polynomial.
- **§30.1, 30.3.** The bilinear natural operators $`T \oplus \Lambda^p T^* \to \Lambda^p T^*`$ are $`k_1\, d\iota_X \omega + k_2\, \iota_X d\omega`$; into $`\Lambda^{p-1} T^*`$ and
  $`\Lambda^{p+1} T^*`$ they are multiples of $`\iota_X \omega`$ and $`d(\iota_X d\omega)`$; into other degrees, zero.
- **§30.4, 30.5.** The bilinear natural operators $`\Omega^p(M; TM) \times \Omega^q(M; TM) \to \Omega^{p+q}(M; TM)`$ are spanned by ten
  operators built from the Frölicher–Nijenhuis bracket $`[P, Q]`$, the contraction $`C(\omega \otimes X) = \iota_X \omega`$, $`d`$ and
  $`I = \mathrm{Id}_{TM}`$; for $`p`$ or $`q \le 1`$, by those of the ten that make sense.
- **§8.13, 8.14.** A projector $`P \in \Omega^1(M; TM)`$ is a connection, with $`[P, P] = 2R + 2\bar R`$, where
  $`R(\xi, \eta) = P[(1 - P)\xi, (1 - P)\eta]`$ is the curvature and $`\bar R(\xi, \eta) = (1 - P)[P\xi, P\eta]`$ the cocurvature, and the Bianchi
  identity $`[P, R + \bar R] = 0`$ holds.
- **§23.4, 23.8, 23.9.** A criterion for natural operators to have finite order; and, on pairs $`(X, \omega) \in T \oplus T^*`$,
  a natural operator of infinite order and a non-regular one, both built from the natural
  function $`\iota_X \omega`$ and its iterates $`(\iota_X d)^k \iota_X \omega`$.
- **§24.1, 24.2.** The homogeneous function theorem: a smooth function on a product of vector
  spaces with $`k^b f(x_1, \dots, x_n) = f(k^{a_1} x_1, \dots, k^{a_n} x_n)`$, all $`a_i > 0`$, is a polynomial with $`\sum a_i d_i = b`$; the
  positivity of the weights is essential.
- **§34.18.** Grozman's classification of all bilinear natural operators between bundles of
  irreducible $`GL(n)`$-modules: order at most three. The book notes that the proof is not available
  in the literature.

**For one body.** For $`\Phi = X \otimes \alpha`$ the vertical line $`\mathrm{span}\, X`$ is integrable, so $`\bar R = 0`$, $`[\Phi, \Phi] = 2R`$, and
$`R = -\Omega \otimes X`$ (HH7(3)); the Bianchi identity reads $`[\Phi, R] = 0`$. Whether it is equivalent to the
vorticity identity HH2, which also follows from $`d^2 = 0`$ alone, is not checked (HH-SP6).

**For two bodies (GB-SP3).** For bodies $`P = X \otimes \alpha`$, $`Q = Y \otimes \beta`$ the contractions are $`C(P) = \alpha X = 1`$ and
$`C(Q) = 1`$, so in the list of §30.4 every term containing $`dC(P)`$ or $`dC(Q)`$ vanishes, and so do $`d(\iota_P C(Q))`$
and $`d(\iota_Q C(P))`$, since $`\iota_P`$ is algebraic and kills functions. Two survive:

```math
[X \otimes \alpha,\ Y \otimes \beta]\qquad\text{and}\qquad d\,C(\iota_P Q) \wedge I = d(\Gamma_{XY}\Gamma_{YX}) \wedge I ,
```

since $`\iota_P Q = (\beta \circ P) \otimes Y = \beta(X)\, \alpha \otimes Y`$ and so $`C(\iota_P Q) = \beta(X)\, \alpha(Y)`$ (Part J). The product of the two clock
factors is the quantity that decides in HH7 whether the two-body Clifford algebra is
degenerate. This classifies the restrictions to bodies of operators bilinear and natural on
all vector-valued 1-forms; a natural operation on pairs of bodies need not be such a
restriction, since bodies do not form a vector space.

---

## 7. GB-SP5 restated, and a route

**The wording.** $`L_X = \iota_X d + d\iota_X`$ is redundant in the list. "Exactly" can hold only for operations
that are smooth on all bodies: where $`d\alpha \wedge d\alpha \neq 0`$ the ratio of 4-forms $`(\alpha \wedge a \wedge da)/(d\alpha \wedge d\alpha)`$ is a
natural function and $`d\alpha`$ is invertible, so there are natural operations that are not words. And
the constraint $`\alpha X = 1`$ matters: for unconstrained pairs, KMS 23.8 and 23.9 give natural operators
of infinite order and non-regular ones, built from $`\iota_X \omega`$ and $`(\iota_X d)^k \iota_X \omega`$. For a body $`\iota_X \alpha = 1`$ and
every iterate vanishes, so that construction is not available.

**The route.** Bodies are all the sections of the natural bundle $`B = \{(X, \alpha) : \alpha X = 1\} \subset T \oplus T^*`$, a
submanifold of each fibre since the differential of $`\alpha X`$ never vanishes there. By HH1 a
natural operator on bodies is determined at a point by an operator on the jets of $`A`$ that is
equivariant under the stabilizer of the jet of $`\partial_t`$, which contains the maps $`(t, x) \mapsto (t + f(x), \varphi(x))`$.

1. *Finite order* (KMS 23.4). The flow-box body $`(\partial_t, dt)`$ is translation invariant, and the
   homotheties $`x \mapsto \lambda x`$, which preserve $`\partial_t`$, send $`A`$ to $`\lambda A(t, \lambda x)`$ and so carry every jet of $`A`$ into any
   neighbourhood of zero. That is the hypothesis of the corollary. Its other hypotheses
   (admissible, locally flat category; the bundle $`B`$ as in 20.3) have been checked only in
   outline.
2. *Polynomial* (KMS 24.1). In flow-box coordinates at the origin the jet $`\partial_t^j \partial_x^\beta A_i`$ has weight $`1 + |\beta| > 0`$
   under the homotheties, and the jets of $`A`$ fill a vector space. A component of the output with
   $`s`$ spatial indices scales as $`\lambda^s`$, so it is a polynomial in the jets of total weight $`s`$. In
   particular a natural function of a body is constant.
3. *Equivariance* under the rest of the stabilizer jet group: $`GL(3)`$ (the invariant tensor
   theorem, 24.3–24.8), the time shifts $`t \mapsto t + f(x)`$, and the higher jets of $`\varphi`$, as in the last
   step of the proof of 30.1. Not done.

Step 3 is done below for every component of weight at most 2.

**Proposition HH8 (weight at most 2).** Grant steps 1 and 2. Write $`a_n = L_X^n a`$ ($`n \ge 0`$), and recall $`\Omega = d\alpha - \alpha \wedge a`$.

1. The natural functions of a body are constants, and its natural vector fields are the
   constant multiples of $`X`$.
2. Its natural 1-forms are $`c\, \alpha + \sum_{n} c_n\, a_n`$.
3. Its natural 2-forms are the linear combinations, with constant coefficients, of
   $`d\alpha`$, $`d a_n`$, $`\alpha \wedge a_n`$ and $`a_m \wedge a_n`$ ($`m < n`$).
4. For every natural 3-form $`D`$, $`\iota_X D`$ is a linear combination of $`L_X^n \Omega`$ and $`a_m \wedge a_n`$ ($`m < n`$).

So for functions, vector fields, 1-forms and 2-forms the answer to HH-SP4 is yes: every
natural operation is a word. For 3-forms only the part $`\iota_X D`$ is settled; the rest of a 3-form,
and 4-forms, have weight 3 and 4.

*Proof.* Work in the flow box at the origin with jets $`a^{(j)}_i = \partial_t^j A_i`$ (weight 1) and $`\partial_k a^{(j)}_i`$ (weight 2). By
step 2, a component of the output with $`s`$ spatial indices is a polynomial of weight $`s`$ in these.

(1) A function has $`s = 0`$, so it is a constant. A vector field's spatial components scale as
$`\lambda^{-1}`$, and by KMS 24.1 a smooth function with a negative degree of homogeneity is zero; its
$`\partial_t`$ component is a constant.

(2)–(4) By the invariant tensor theorem (KMS 24.4), the $`GL(3)`$-equivariant candidates are
$`D_{0i} = \sum_j p_j\, a^{(j)}_i`$ for the components $`dt \wedge dx^i`$ (or $`dx^i`$), and

```math
D_{ki} = \sum_j q_j\, \bigl(\partial_k a^{(j)}_i - \partial_i a^{(j)}_k\bigr) + \sum_{j < l} r_{jl}\, \bigl(a^{(j)}_k a^{(l)}_i - a^{(j)}_i a^{(l)}_k\bigr)
```

for the components $`dx^k \wedge dx^i`$ (or $`dt \wedge dx^k \wedge dx^i`$). The second-order jets of $`x \mapsto \varphi(x)`$ change
$`\partial_k A_i`$ by a term symmetric in $`k, i`$ and so leave the candidates alone. A time shift $`t \mapsto t + f(x)`$ with
$`f(0) = 0`$ sends, at the origin,

```math
a^{(j)}_i \mapsto a^{(j)}_i + \delta_{j0}\, \partial_i f,\qquad \partial_k a^{(j)}_i \mapsto \partial_k a^{(j)}_i + a^{(j+1)}_i\, \partial_k f + \delta_{j0}\, \partial_k \partial_i f,\qquad dt \mapsto dt + df .
```

For a 1-form ($`D_0 = c`$ a constant, $`D_i = \sum_j p_j a^{(j)}_i`$) naturality requires $`p_0 = c`$ and nothing else:
(2). For a 2-form it requires $`p_0 = 0`$ and $`p_m = q_{m-1} + r_{0m}`$ for $`m \ge 1`$, the $`q_j`$ and the $`r_{jl}`$ with $`j \ge 1`$
being free. The words supply these: $`d\alpha`$ and $`da_n`$ give $`q_j = p_{j+1} = 1`$; $`\alpha \wedge a_n`$ gives $`p_{n+1} = r_{0,n+1} = 1`$;
$`a_m \wedge a_n`$ gives $`r_{m+1, n+1} = 1`$. They span the solution space: (3). For the $`dt \wedge dx^k \wedge dx^i`$
components of a 3-form, $`dt \mapsto dt + df`$ moves the change into the purely spatial components,
so the components themselves must be invariant: $`q_{m-1} + r_{0m} = 0`$, solved by $`L_X^n \Omega`$
($`= d_x a^{(n)} - \partial_t^n(A \wedge \dot A)`$ in the flow box) and $`a_m \wedge a_n`$: (4). *Checked*: Part K, with up to four time
derivatives ($`p_0, \dots, p_4`$, $`q_0, \dots, q_3`$, ten $`r_{jl}`$): solution spaces of dimension 14 for 2-forms and 10 for
the 3-form parts, each spanned by the words computed independently with the exterior
calculus; the second-order jets of $`\varphi`$, one $`GL(3)`$ matrix and the 1-form case also checked. The
pattern of the conditions is the same for every number of time derivatives. $`\square`$

What HH8 does not do: it rests on steps 1 and 2, whose hypotheses were checked in outline;
it uses the invariant tensor theorem without re-proving it; and it says nothing about
weight 3, where second spatial derivatives of $`A`$, the third-order jets of $`\varphi`$ and the
cubic terms first appear. Restated as HH-SP4.

---

## 8. Verification

[`src/verify_heat_and_helicity.py`](../src/verify_heat_and_helicity.py), SymPy, exact; about a
minute, most of it Part K. Forms as dictionaries over sorted index tuples with $`d`$, $`\wedge`$, $`\iota`$ and $`L`$; a 4D Riemann
tensor (Part C); $`16 \times 16`$ matrices (Part H). 45 checks, all pass.

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
| J | $`\iota_P Q = \beta(X)\, \alpha \otimes Y`$, $`C(\iota_P Q) = \beta(X)\, \alpha(Y)`$, $`C(P) = \alpha X`$ | §6 |
| K | weight $`\le 2`$: the conditions from time shifts and second-order jets; solution dimensions 14 (2-forms) and 10 (3-form parts), spanned by the words; 1-forms | HH8 |

Two test expectations were corrected while the checks were written: the sign in HH5
($`+u_t^2`$), and the normalisation in Part G (the momentum density is half the curl of the spin
density). **Not verified:** the readings of §2 beyond the conditions stated; HH6 beyond the
algebra shown; the Schrödinger remark; steps 1 and 2 of §7 (hypotheses of KMS 23.4 checked in
outline), on which HH8 rests; the general number of time derivatives in HH8 (by hand; Part K
checks up to four); which terms of KMS 30.4 survive on two bodies
(by hand, Part J checks only the contraction); the readings of the monograph, of Kiehn and
of the other cited papers.

---

## 9. Open items

- **HH-SP1.** Make the Thomas reading of HH3 quantitative: is the Thomas rotation over a closed
  velocity loop of a non-rotating rigid body an integral of $`a \wedge L_X a`$ along the worldline?
- **HH-SP2.** Kiehn's topological spin is $`A \wedge G`$, with $`G`$ an excitation 2-form. Is there a 2-form $`G`$ of a body
  or a system (for instance with $`dG`$ the particle current) for which $`p \wedge G`$ gives $`P \wedge L`$?
- **HH-SP3.** Among operators bilinear and natural on vector-valued 1-forms, only $`[X \otimes \alpha, Y \otimes \beta]`$ and
  $`d(\Gamma_{XY}\Gamma_{YX}) \wedge I`$ survive on two bodies (§6, by hand from KMS 30.4). Which of the components of the
  bracket are relative acceleration, Wigner rotation or something new, and which natural
  operations on pairs of bodies are not of this form? Continues GB-SP3.
- **HH-SP4.** Are the natural operations smooth on all bodies $`(X, \alpha)`$ exactly the polynomial words in
  $`d`$, $`\wedge`$, $`\iota_X`$ and $`\alpha`$? Yes for functions, vector fields, 1-forms and 2-forms, granted steps 1 and 2
  of §7 (HH8). Open: weight 3 (the spatial parts of 3-forms) and weight 4 (4-forms), mixed
  tensors, and a check of the hypotheses of KMS 23.4. Supersedes GB-SP5.
- **HH-SP5.** The Tolman reading holds for Killing flows. What does $`a = f\, d\Phi`$ with $`f \neq 1`$ mean, and is $`\Phi`$
  a temperature away from equilibrium?

- **HH-SP6.** Is the Bianchi identity $`[\Phi, R] = 0`$ of the connection $`\Phi = X \otimes \alpha`$ (KMS 8.14) equivalent to
  the vorticity identity HH2?
---

## 10. What this does for the ladder

It answers GB-SP1 (no) and GB-SP4, answers GB-SP3 in part and restates GB-SP5, with a
route to it from Kolář, Michor and Slovák. It moves the
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
  (1993), [PDF on the author's page](https://www.mat.univie.ac.at/~michor/kmsbookh.pdf); sections
  8, 23–25, 30 and 34 read.
- J. Navarro and J. B. Sancho, "Natural operations on differential forms",
  [arXiv:1412.0840](https://arxiv.org/abs/1412.0840).
