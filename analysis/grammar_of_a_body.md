# The grammar of a body: natural operations, three observers, and what fails at grade three

> A body is a process $`X`$ with a clock $`\alpha`$, $`\alpha X = 1`$, and Cartan's calculus offers only a few operations to build from it. By the theorems of Palais (1959) and Navarro and Sancho, the coordinate-free operations on forms are exactly those built from $`d`$, $`\wedge`$ and linear combinations, so for forms the grammar of the calculus is its invariance; this note takes that as its method. **Theorem GB1**: every operator built from $`X`$, $`\alpha`$, $`d`$, $`\wedge`$ and evaluation is natural, including the observer operators. **Proposition GB2**: one body carries three observers, Oziewicz's derivation $`\mathcal D = \alpha \wedge \iota_X`$ and algebra map $`\mathcal M = \iota_X (\alpha \wedge \cdot)`$, with $`\mathcal D + \mathcal M = 1`$, and $`e = \tfrac12(1 + \mathcal U)`$ built from his unipotent $`\mathcal U = \iota_X + \alpha \wedge`$; $`\mathcal U \mathcal D \mathcal U = \mathcal M`$ and $`e \mathcal D e = e \mathcal M e = \tfrac12 e`$, and with a metric clock $`e`$ is step 5's $`e_X`$. **Proposition GB3**: $`e`$ needs no metric; its corner sees only the symmetrised clock factor $`s_{XY} = \tfrac12(\alpha_X Y + \alpha_Y X)`$, and round a triangle the loop is a rotation if $`\det S > 0`$ and a boost if $`\det S < 0`$, both of which occur; this answers OI-SP1. **Proposition GB4**: the forms of one body are the Pfaff sequence $`\alpha, d\alpha, \alpha \wedge d\alpha, d\alpha \wedge d\alpha`$; split by the body, $`d\alpha = \alpha \wedge a + \Omega`$ is acceleration plus rotation, $`\alpha \wedge d\alpha = \alpha \wedge \Omega`$ and $`d\alpha \wedge d\alpha = 2\, \alpha \wedge a \wedge \Omega`$; the Frobenius condition survives a change of clock scale, the top class does not, and for the momentum form $`p = E\alpha`$, $`p \wedge dp = E^2 \alpha \wedge d\alpha`$. **Proposition GB5**: in Kiehn's reading of Cartan's formula as a first law, a body's own process does no internal-energy change and its heat is its acceleration, $`Q = W = a`$. **Proposition GB6**: grade 3 is where observer-independence fails, three times: $`P \wedge L`$ (the spread of centres), $`\alpha \wedge d\alpha`$ (no time function) and $`X \wedge Y \wedge Z`$ (the Wigner rotation, $`T^2 = -\det G`$); at grade 4, $`L \wedge L = 2\, C \wedge P \wedge L`$ adds nothing, and $`X \wedge Y \wedge Z \wedge W = 0`$ exactly when two triangle rotations commute. Checked exactly with SymPy. No new prediction.

*Ladder abstract — see the [full list](README.md#the-ladder).*

**Status.** Analysis note, step 6 of the ladder. Theorem prefix **GB**. Companion
script: [`src/verify_grammar_of_a_body.py`](../src/verify_grammar_of_a_body.py) (Parts A
to G; §10). Prompted by Bill Page, 21–22 November 2026: an AI-generated note on
"geometric synthesis" in exterior calculus, read against Oziewicz's last programme (the
body as $`P + dP + P \wedge dP + dP \wedge dP`$, in his letters of 2019–2020), with the
request to take seriously the idea that the right formalism guides the ontology, as
Kiehn did for Cartan's calculus. The operators are Oziewicz's, from his lecture notes
*Magnetismo e Electricidad* (summarised in [`supplement/magnetismo.md`](../supplement/magnetismo.md)).
Derivation and checks were drafted with Claude (Anthropic) and are subject to review,
and no separate reader has checked them; every claim about what a paper says is a
reading of the cited page, and the letters are paraphrased.
[PDF](https://github.com/billpage/oziewicz/releases/latest/download/grammar_of_a_body.pdf)

---

## 0. What this note asks, inherits and retracts

**Question.** Few expressions can be formed from a process and a clock in Cartan's
calculus. If the grammar is a guide to the ontology, which of those expressions are the
body's intrinsic properties, which operators are its observers, and where does the grammar
stop?

**Inherits.** From step 1: the rank-one idempotent MC6. From step 2: TV6, TV8. From step 3:
the body $`(X, \alpha)`$ and clock factors $`\Gamma_{XY} = \alpha_X Y`$ (MF0), the split MF1, MF4 (a symmetric
$`\Gamma`$ on spanning bodies is a metric), MF10, MF11. From step 4: the spin $`P \wedge L`$ and the
centre $`C[\zeta]`$ (CS1, CS2), CS5, CS6. From step 5: $`e_X = \tfrac12(1 + X)`$, OI1, OI3, OI5 and the open
item OI-SP1. From the supplement on *Magnetismo*: MG1–MG4.

**Retracts or corrects.** Nothing. One earlier item is answered:

| Earlier statement | What happens to it |
|---|---|
| `observer_idempotents.md` OI-SP1: is there an observer idempotent for a metric-free body, and does a loop of three carry anything without a metric? | Answered (GB3): $`e = \tfrac12(1 + \mathcal U)`$ in $`\mathrm{Cl}(V \oplus V^*)`$; its loop is a rotation or a boost, decided by the sign of $`\det S`$ |

---

## 1. The method: grammar is invariance

**Natural operations.** Let $`\mathcal{M}f_n`$ be the category of $`n`$-manifolds and local
diffeomorphisms. A *natural bundle* is a functor from $`\mathcal{M}f_n`$ to bundles over them, such as
$`\Lambda^k T^*`$ or $`T \oplus T^*`$; a *natural operator* $`F \to G`$ between two of them is a family of
operators $`D_M`$, one for each manifold, with $`D_N(\phi^* s) = \phi^*(D_M s)`$ for every local diffeomorphism $`\phi`$,
that is, a natural transformation between the functors of sections (Kolář, Michor and
Slovák 1993). A natural operator is one whose definition needs no
choice of coordinates.

**Two theorems.** Palais (1959): every linear natural operator from $`p`$-forms to $`(p+1)`$-forms
is a constant multiple of $`d`$. Navarro and Sancho (2014): the natural operations from given
forms to forms are exactly those built from linear combinations, $`\wedge`$ and $`d`$. Read the
other way round, a coordinate-free expression in forms must be a word of Cartan's grammar,
and every such word is coordinate-free. For forms, grammar and invariance are the same
thing, and that is the precise content of Kiehn's conviction that Cartan's calculus is the
language of physics (Kiehn and Baldwin 2001).

**What the theorems do not give.**

1. *Truth.* A grammatical word is invariant; whether it vanishes is decided by dynamics.
   That $`L_X dv = 0`$ in Kelvin's theorem needs the Euler equation.
2. *The body's own symmetry.* A body has more structure than a manifold, and a smaller
   symmetry: the clock of a given process may change, and its scale is the body's energy
   (GB4). An expression intrinsic to the body must be invariant under that change too, or
   say which clock it uses.
3. *Vector fields.* The two theorems are about forms. With a vector field among the data,
   evaluation $`\iota_X`$, the Lie derivative and the bracket are natural as well; whether they and
   $`d`$, $`\wedge`$ generate all natural operations on a pair $`(X, \alpha)`$ is not settled here (GB-SP5).

**Definition GB0 (body and its operators).** A *body* is a pair $`(X, \alpha)`$ of a vector field and
a 1-form with $`\alpha X = 1`$ (MF0; *Magnetismo* (7.2.1), with $`X = L_P`$ the Length of the clock). On
forms it carries the operators $`\mathrm{ev}_X = \iota_X`$ and $`\mathrm{cr}_\alpha = \alpha \wedge`$, and

```math
\mathcal D=\mathrm{cr}_\alpha\,\mathrm{ev}_X,\qquad \mathcal M=\mathrm{ev}_X\,\mathrm{cr}_\alpha,\qquad \mathcal U=\mathrm{ev}_X+\mathrm{cr}_\alpha,\qquad e=\tfrac12(1+\mathcal U).
```

With $`E`$ the body's energy, $`P = EX`$ is its process and $`p = E\alpha`$ its momentum form.

**Theorem GB1 (the observers are natural).** $`\mathcal D`$, $`\mathcal M`$, $`\mathcal U`$ and $`e`$, as functions of the body, are
natural: $`\phi^*(\mathcal O_{X,\alpha}\beta) = \mathcal O_{\phi^* X, \phi^* \alpha}(\phi^* \beta)`$ for $`\mathcal O \in \{\mathcal D, \mathcal M, \mathcal U, e\}`$ and every local diffeomorphism $`\phi`$.

*Proof.* Pull-back commutes with $`\wedge`$ and with evaluation, $`\phi^*(\iota_X\beta) = \iota_{\phi^*X}\phi^*\beta`$, and the four
operators are words in these. *Checked* (Part G4) for a polynomial diffeomorphism with
unit Jacobian, three forms of degrees 0–2, and $`\phi^* d = d \phi^*`$. $`\square`$

The theorem is easy; its use is as a filter. Every statement below is a word in this
grammar, and so needs no observer, coordinates or metric unless it names one.

---

## 2. One body has three observers

**Proposition GB2.** For a body $`(X, \alpha)`$:

1. $`\mathcal D^2 = \mathcal D`$, $`\mathcal M^2 = \mathcal M`$, $`\mathcal D + \mathcal M = 1 = \mathcal U^2`$; $`\mathcal D`$ is a derivation and $`\mathcal M`$ an algebra map (*Magnetismo* §4.8, MG1).
2. On 1-forms, $`\mathcal D\beta = \beta(X)\,\alpha`$ is the projector MC6 and $`\mathcal M = 1 - \mathcal D`$ its complement; on all forms,
   $`\mathcal M = \Lambda(1 - X \otimes \alpha)`$ (MF1) and $`\mathcal D = 1 - \mathcal M`$.
3. $`\mathcal U \mathcal D \mathcal U = \mathcal M`$.
4. $`e^2 = e`$, and $`e\,\mathcal D\,e = e\,\mathcal M\,e = \tfrac12 e`$.
5. Let $`h = -g`$, step 5's form, in which a body has $`h(X, X) = 1`$, and let $`\alpha = h(X, \cdot)`$. Then $`c(Y) = \iota_Y + h(Y, \cdot) \wedge`$
   represents $`\mathrm{Cl}(V, h) = \mathrm{Cl}(V, -g)`$ on forms, $`c(X) = \mathcal U`$, and $`e`$ is the image of step 5's $`e_X`$.

*Proof.* (1) $`\mathcal D^2 = \alpha \wedge \iota_X \alpha \wedge \iota_X = \alpha \wedge (1 - \alpha \wedge \iota_X)\iota_X = \mathcal D`$, using $`\iota_X(\alpha \wedge \beta) = \beta - \alpha \wedge \iota_X \beta`$, the
anticommutator $`\{\mathrm{ev}_X, \mathrm{cr}_\alpha\} = \alpha X = 1`$; the same identity gives $`\mathcal D + \mathcal M = 1`$, and
$`\mathcal U^2 = \mathrm{ev}_X^2 + \mathrm{cr}_\alpha^2 + \{\mathrm{ev}_X, \mathrm{cr}_\alpha\} = 1`$. (3) $`\mathcal U \mathcal D \mathcal U = (\mathrm{ev}_X + \mathrm{cr}_\alpha)\,\mathrm{cr}_\alpha \mathrm{ev}_X\,(\mathrm{ev}_X + \mathrm{cr}_\alpha) = \mathrm{ev}_X \mathrm{cr}_\alpha \mathrm{ev}_X \mathrm{cr}_\alpha = \mathcal M^2 = \mathcal M`$. (4) $`e^2 = \tfrac14(1 + 2\,\mathcal U + \mathcal U^2) = e`$. From $`\mathcal U \mathcal D = \mathrm{ev}_X \mathrm{cr}_\alpha \mathrm{ev}_X = \mathrm{ev}_X`$ and $`\mathcal D \mathcal U = \mathrm{cr}_\alpha`$,
$`(1 + \mathcal U)\,\mathcal D\,(1 + \mathcal U) = \mathcal D + \mathrm{ev}_X + \mathrm{cr}_\alpha + \mathcal M = 1 + \mathcal U`$, so $`e \mathcal D e = \tfrac14(1 + \mathcal U) = \tfrac12 e`$, and $`e \mathcal M e = e - e\mathcal D e`$. (5) With
$`c(Y)^2 = \{\iota_Y, h(Y, \cdot)\wedge\} = h(Y, Y)`$ (Chevalley 1954), so $`c`$ represents $`\mathrm{Cl}(V, h)`$, and $`c(X) = \mathcal U`$. *Checked*: Part A,
(1)–(4) with symbolic $`X, \alpha`$ and rational pairs, (5) with $`h = \mathrm{diag}(1, -1, -1, -1)`$ and a rational body. $`\square`$

**Reading.** The two graded observers of *Magnetismo* are conjugate by the body's own
unipotent and are seen equally by the ungraded one. $`\mathcal D`$ splits fields
($`F = \mathcal M F + \alpha \wedge \iota_X F`$, MG4); $`\mathcal M`$ restricts the algebra to the places and carries the private
differential when there is one (MG3). Neither has corners larger than the projectors of
OI5, so neither sees an orientation. $`e`$, built from $`\mathcal U`$, has the quaternionic corners of
OI1 when the clock is metric. The grammar offers all three; the choice of observer
decides whether rotation is visible.

---

## 3. The third observer needs no metric

**Proposition GB3.** Let $`(X, \alpha)`$, $`(Y, \beta)`$, $`(Z, \gamma)`$ be bodies with operators $`\mathcal U_X, \mathcal U_Y, \mathcal U_Z`$ on forms
and idempotents $`e_X = \tfrac12(1 + \mathcal U_X)`$, etc. Write $`s_{XY} = \tfrac12(\alpha Y + \beta X)`$, the symmetrised clock factor
(MF0), and $`S`$ for the $`3 \times 3`$ matrix with ones on the diagonal and $`s`$ off it.

1. $`\mathcal U_X \mathcal U_Y + \mathcal U_Y \mathcal U_X = 2 s_{XY}`$, and $`e_X\, \mathcal U_Y\, e_X = s_{XY}\, e_X`$.
2. $`e_X e_Z e_Y e_X = \tfrac18 \Lambda\, e_X`$ with $`\Lambda = (1 + \mathcal U_X \mathcal U_Z)(1 + \mathcal U_Z \mathcal U_Y)(1 + \mathcal U_Y \mathcal U_X)`$, as in OI3.
3. The scalar part of $`\Lambda`$ is $`2(1 + s_{XY} + s_{YZ} + s_{ZX})`$, and the rest squares to a scalar:
   $`(\Lambda - \langle \Lambda \rangle_0)^2 = -4 \det S`$.
4. So the loop is a rotation (of angle $`\theta`$, $`\tan(\theta/2) = \sqrt{\det S}/(1 + s_{XY} + s_{YZ} + s_{ZX})`$) when $`\det S > 0`$,
   and a boost when $`\det S < 0`$; both signs occur among bodies with arbitrary clocks.

*Proof.* (1) is the anticommutator of GB0 applied to two bodies:
$`\{\mathrm{ev}_X + \mathrm{cr}_\alpha, \mathrm{ev}_Y + \mathrm{cr}_\beta\} = \alpha Y + \beta X`$. Then $`e_X \mathcal U_Y e_X = \tfrac14(\mathcal U_Y + \mathcal U_X \mathcal U_Y + \mathcal U_Y \mathcal U_X + \mathcal U_X \mathcal U_Y \mathcal U_X)`$, and
$`\mathcal U_X \mathcal U_Y \mathcal U_X = 2 s_{XY} \mathcal U_X - \mathcal U_Y`$ gives $`s_{XY}(1 + \mathcal U_X)/2`$. (2) and (3) are OI3's algebra, which used only
$`X^2 = 1`$ and the anticommutators. (4) In the spin representation a unit element $`\cos(\theta/2) + B\sin(\theta/2)`$
has $`B^2 = -1`$ for a rotation, $`B^2 = +1`$ for a boost. *Checked*: Part B symbolically; Part C on 12
random rational triangles of metric-free bodies, where both signs of $`\det S`$ occurred. $`\square`$

**Reading.** OI-SP1 asked whether a metric-free body has an observer idempotent and whether
a loop of three carries anything. It does, and the loop carries a rotation only when the
symmetrised clock factors of the three bodies have the right signature. The Wigner
*rotation* is therefore not a consequence of the grammar; it needs what step 3 called the
signature as an output (MF6). The antisymmetric part of the clock factors, Oziewicz's
non-reciprocity, is invisible to $`e`$.

---

## 4. The Pfaff sequence of one body

**Proposition GB4.** For a body $`(X, \alpha)`$, write $`a = \iota_X d\alpha = L_X \alpha`$ and $`\Omega = \mathcal M\, d\alpha = \iota_X(\alpha \wedge d\alpha)`$.

1. $`d\alpha = \mathcal D\, d\alpha + \mathcal M\, d\alpha = \alpha \wedge a + \Omega`$, with $`\iota_X a = \iota_X \Omega = 0`$: acceleration and rotation.
2. $`\alpha \wedge d\alpha = \alpha \wedge \Omega`$, $`d\alpha \wedge d\alpha = 2\, \alpha \wedge a \wedge \Omega`$, and $`\alpha \wedge d\alpha \wedge d\alpha = 0`$ in four dimensions.
3. Under $`\alpha \to f\alpha`$, $`(f\alpha) \wedge d(f\alpha) = f^2\, \alpha \wedge d\alpha`$, but the vanishing of $`d\alpha \wedge d\alpha`$ is not preserved:
   $`\alpha = dt + x\,dy`$ has $`d\alpha \wedge d\alpha = 0`$, and $`d(e^z \alpha) \wedge d(e^z \alpha) = 2 e^{2z}\, dz \wedge dt \wedge dx \wedge dy`$.
4. For the momentum form $`p = E\alpha`$: $`p \wedge dp = E^2\, \alpha \wedge d\alpha`$ and $`dp \wedge dp = E^2\, d\alpha \wedge d\alpha + 2E\, dE \wedge \alpha \wedge d\alpha`$.

*Proof.* (1) is GB2(1) applied to $`d\alpha`$ with $`\mathcal D\, d\alpha = \alpha \wedge \iota_X d\alpha`$; $`L_X \alpha = \iota_X d\alpha + d(\alpha X) = a`$. (2)
$`\alpha \wedge \alpha = 0`$ kills the first term; $`\Omega \wedge \Omega`$ is a 4-form annihilated by $`\iota_X`$, hence $`0`$; the rest
expands. (3), (4) by the Leibniz rule. *Checked*: Part D (1)–(2) pointwise with symbolic
coefficients; Part G1–G2 (3)–(4) with general functions. $`\square`$

**Kiehn's classes.** The sequence $`\alpha, d\alpha, \alpha \wedge d\alpha, d\alpha \wedge d\alpha`$ is what Kiehn calls the Pfaff
sequence of a 1-form, and the largest non-vanishing term fixes its Pfaff topological
dimension, 1 to 4 (Kiehn and Baldwin 2001). For a clock:

| class | condition | for the body | where on the ladder |
|---|---|---|---|
| ≤ 2 | $`\alpha \wedge d\alpha = 0`$ | a time function exists; the private differential $`d_{\mathcal M}`$ exists | MF11; MG3 |
| 3 | $`\alpha \wedge d\alpha \ne 0`$, $`d\alpha \wedge d\alpha = 0`$ | rotating clock, acceleration in the rotation plane | CS5, CS6 |
| 4 | $`d\alpha \wedge d\alpha \ne 0`$ | acceleration along the rotation axis | — |

By (3) the first row is a property of the process alone; the boundary between rows 3
and 4 depends on the scale of the clock, and by (4) on the body's energy. Kiehn encodes
a system by an action 1-form defined up to a factor; for a body, the factor is $`E`$. The
reading that does not depend on the scale is the class of $`p`$, not of $`\alpha`$. The two always agree on
row ≤ 2, since $`p \wedge dp = E^2 \alpha \wedge d\alpha`$, and on the boundary between rows 3 and 4 when $`dE \wedge \alpha \wedge d\alpha = 0`$. In Oziewicz's letters of 2019 the body
was $`P + dP + P \wedge dP + dP \wedge dP`$ with $`P`$ the momentum: that is the Pfaff sequence of $`p`$, and (4) says
how it differs from the clock's.

---

## 5. Kiehn's first law for a body

Kiehn reads Cartan's formula $`L_V A = \iota_V dA + d(\iota_V A)`$ for a process $`V`$ and action $`A`$ as the first
law, $`Q = W + dU`$, and calls a process reversible when $`Q \wedge dQ = 0`$ (Kiehn, AMS abstract 1000-80-31).

**Proposition GB5.** (1) For the pair $`(X, \alpha)`$, $`U = \iota_X \alpha = 1`$, so $`dU = 0`$ and $`Q = W = a`$: the heat of a
body's own process is its acceleration. (2) For $`(P, p) = (EX, E\alpha)`$, $`U = p(P) = E^2`$ and $`Q = W + d(E^2)`$.
(3) Kiehn's reversibility for the clock is $`a \wedge da = 0`$; it is not implied by anything in the body's
definition.

*Proof.* (1)–(2) are Cartan's formula with $`\iota_X \alpha = 1`$ and $`\iota_P p = E^2`$. (3) The clock
$`dt + t(y\,dx + z\,dy + x\,dz)`$ with $`X = \partial_t`$ has $`a = y\,dx + z\,dy + x\,dz`$ and $`a \wedge da \ne 0`$. *Checked*: Part G3. $`\square`$

**Reading.** This is a dictionary, not a law: GB5 says only what Kiehn's words become for a
body. Its use is that it asks a question the ladder had not asked (GB-SP4): what does
$`a \wedge da \ne 0`$ mean for a single body, whose "work" on itself is its acceleration?

---

## 6. Grade three is where observer-independence fails

**Proposition GB6.**

1. For a closed system with momentum $`P`$ and angular momentum $`L`$, and the centre $`C[\zeta]`$ of any
   clock $`\zeta`$ (CS1): $`L \wedge L = 2\, C[\zeta] \wedge P \wedge L`$, and $`L_C = L - C \wedge P`$ has $`\iota_\zeta L_C = 0`$ and $`L_C \wedge L_C = 0`$.
2. For three bodies in $`\mathrm{Cl}(V, -g)`$, $`T = X \wedge Y \wedge Z`$ has $`T^2 = -\det G`$, with $`G`$ the Gram matrix of TV8, so the
   Wigner angle of OI3 is $`\tan(\theta/2) = \sqrt{-T^2}/(1 + \gamma_{XY} + \gamma_{YZ} + \gamma_{ZX})`$; its axis is the 1-form $`\varepsilon(X, Y, Z, \cdot)`$.
3. For a fourth body $`W`$, the loop rotors of the triangles $`XYZ`$ and $`XZW`$ commute exactly when
   $`X \wedge Y \wedge Z \wedge W = 0`$.

*Proof.* (1) $`L = L_C + C \wedge P`$ with $`L_C \wedge L_C = 0`$ (a simple 2-vector, since $`\iota_\zeta L_C = 0`$ puts it in a
3-dimensional space where every bivector is simple), so $`L \wedge L = 2\, C \wedge P \wedge L_C = 2\, C \wedge P \wedge L`$. (2) is
the Lagrange identity for the norm of a trivector. (3) Two rotations commute exactly when
their axes are parallel; the axes are the duals of the two trivectors. *Checked*: Part E
symbolically; Part F on step 2's bodies, with $`W`$ in and out of their 3-space. $`\square`$

**The table.**

| grade | one body (forms) | a system (vectors) | several bodies (vectors) |
|---|---|---|---|
| 3 | $`\alpha \wedge d\alpha`$: no time function, no private differential (MF11, MG3) | $`P \wedge L`$: the centres of different clocks differ (CS2) | $`X \wedge Y \wedge Z`$: no composing section; the Wigner rotation (TV6, OI3) |
| 4 | $`d\alpha \wedge d\alpha`$: acceleration along the axis (GB4) | $`L \wedge L = 2\, C \wedge P \wedge L`$: nothing new | $`X \wedge Y \wedge Z \wedge W`$: two triangle rotations fail to commute |

Each grade-3 entry is the obstruction to an observer-independent construction, and each
vanishes exactly when that construction can be made without choosing an observer. Step 4
(CS6) has already identified the first two entries for axisymmetric dust: the Sagnac
failure of the clocks is the spread of centres. In four dimensions the exterior algebra ends
at grade 4. So, to the question of whether a body has intrinsic properties that need higher
multivectors or forms: within $`(X, \alpha)`$ and $`(P, L)`$, spin is the last, apart from the grade-4 term of a
body's own clock. Charge needs another form, a current, and higher moments of a system
(Dixon 1970) are symmetric tensors, outside the exterior algebra.

**Spin, twice.** Oziewicz's late candidate for spin, $`P \wedge dP = E^2\, \alpha \wedge d\alpha`$ (GB4(4)), is local and
needs a clock field; Pauli–Lubański's $`P \wedge L`$ is global and needs places and an origin (CS2).
For two free point bodies the first vanishes and the second need not; for a rigid rotor they
agree through CS5. The grammar offers both, as different words.

---

## 7. What this does not do

- It does not classify the natural operations on a pair $`(X, \alpha)`$; it uses the theorems for forms
  and lists the operators it needs (GB-SP5).
- GB5 is a translation into Kiehn's vocabulary, not a physical claim; nothing here says a
  body exchanges heat.
- The grade-3 table is three facts side by side. Only CS6 connects two of them, and only for
  axisymmetric dust (GB-SP1).
- No prediction, and no new number.

---

## 8. Open items

- **GB-SP1.** For dust, is $`P \wedge L`$ (global) an integral of $`P \wedge dP`$ (local) in general, beyond the axisymmetric
  case of CS6, so that two rows of the grade-3 table are one quantity?
- **GB-SP2.** If every triangle of a family of metric-free bodies has $`\det S > 0`$, do their clock factors
  satisfy the Gram condition of MF4–MF7? That is, are "all loops are rotations" and
  "clocks are reciprocal" equivalent?
- **GB-SP3.** The algebra generated by the operators $`\mathrm{ev}`$, $`\mathrm{cr}`$ of several bodies (a subalgebra of $`\mathrm{Cl}(V \oplus V^*)`$,
  with $`d`$ adjoined for fields): which of its words are new? Bill Page asked Oziewicz in June
  2020 whether it has finitely many independent monomials.
- **GB-SP4.** What does Kiehn's irreversibility $`a \wedge da \ne 0`$ (GB5) mean for a single body, and is it
  related to its rotation $`\Omega`$?
- **GB-SP5.** Are the natural operations on a pair $`(X, \alpha)`$ with $`\alpha X = 1`$ exactly those built from $`d`$, $`\wedge`$, $`\iota_X`$, $`L_X`$
  and $`\alpha`$? Navarro and Sancho settle the case of forms alone; the monograph of Kolář, Michor and
  Slovák may contain the answer (not checked).

---

## 9. What this does for the ladder

It gives the observer operators a source (*Magnetismo*) and a status (natural, GB1); it
answers OI-SP1 (GB3); it organises steps 3–5 by grade (GB6); and it opens a line of
questions from Kiehn's reading (GB5, GB-SP4). A next step could take GB-SP1 or GB-SP2,
which are both statements about the ladder's own objects and both checkable.

---

## 10. Verification

[`src/verify_grammar_of_a_body.py`](../src/verify_grammar_of_a_body.py), SymPy, exact; runs in a few
seconds. Forms on $`\mathbb R^4`$ as $`16 \times 16`$ matrices of evaluation and creation (Parts A–E) or as
dicts over basis masks with polynomial coefficients (Part G); an exact Clifford algebra for
any symmetric form (Part F). 36 checks, all pass.

| Part | Checks | Result |
|---|---|---|
| A | nilpotents, $`\mathcal U^2 = \alpha X`$, $`\mathcal D + \mathcal M = \alpha X`$, idempotency, $`\mathcal U \mathcal D \mathcal U = (\alpha X) \mathcal M`$, derivation and algebra map, MC6, $`e \mathcal D e = e \mathcal M e = e/2`$ | GB2 |
| B | $`\{\mathcal U_X, \mathcal U_Y\} = 2 s_{XY}`$, $`e_X \mathcal U_Y e_X = s_{XY} e_X`$ | GB3(1) |
| C | triangle identity, scalar part, $`(\Lambda - \langle\Lambda\rangle_0)^2 = -4\det S`$, both signs | GB3(2)–(4) |
| D | $`d\alpha = \alpha \wedge a + \Omega`$, spatial parts, $`d\alpha \wedge d\alpha = 2\alpha \wedge a \wedge \Omega`$, $`\alpha \wedge d\alpha = \alpha \wedge \Omega`$, $`P \wedge dP = E^2 \alpha \wedge d\alpha`$ | GB4(1)–(2) |
| E | $`L \wedge L = 2C \wedge P \wedge L`$, $`L_C \wedge L_C = 0`$ | GB6(1) |
| F | $`T^2 = -\det G`$; commuting rotors iff the 4-vector vanishes | GB6(2)–(3) |
| G | rescaling (G1), momentum form (G2), Kiehn's first law and $`a \wedge da \ne 0`$ (G3), naturality under a polynomial diffeomorphism (G4) | GB1, GB4(3)–(4), GB5 |

One test expectation was corrected while the checks were written: $`\mathcal U \mathcal D \mathcal U = (\alpha X)\mathcal M`$, not $`(\alpha X)^2 \mathcal M`$.
**Not verified:** the readings of Kiehn, of *Magnetismo* and of the letters (interpretations);
the two naturality theorems are cited, not re-proved.

---

## References

- R. S. Palais, "Natural operations on differential forms", *Trans. Amer. Math. Soc.* 92
  (1959) 125–141, [doi:10.1090/S0002-9947-1959-0116352-7](https://doi.org/10.1090/S0002-9947-1959-0116352-7).
- J. Navarro and J. B. Sancho, "Natural operations on differential forms",
  [arXiv:1412.0840](https://arxiv.org/abs/1412.0840).
- I. Kolář, P. W. Michor and J. Slovák, *Natural Operations in Differential Geometry*, Springer
  (1993), [author's page](https://www.mat.univie.ac.at/~michor/preprint-shadows/kmsbookh.html).
- R. M. Kiehn and P. Baldwin, "Cartan's topological structure",
  [arXiv:math-ph/0101033](https://arxiv.org/abs/math-ph/0101033).
- R. M. Kiehn, "Non-equilibrium systems and irreversible processes — from the perspective of
  continuous topological evolution", AMS meeting 1000, abstract 1000-80-31,
  [PDF](https://www.ams.org/amsmtgs/2112_abstracts/1000-80-31.pdf).
- C. Chevalley, *The Algebraic Theory of Spinors*, Columbia University Press (1954).
- W. G. Dixon, "Dynamics of extended bodies in general relativity. I", *Proc. R. Soc. Lond. A*
  314 (1970) 499–527. Cited from memory.
- Z. Oziewicz, *Magnetismo e Electricidad*, lecture notes, 2014–2020, unpublished; see
  [`supplement/magnetismo.md`](../supplement/magnetismo.md).
- Z. Oziewicz and B. Page, correspondence 2018–2020, unpublished (paraphrased).
