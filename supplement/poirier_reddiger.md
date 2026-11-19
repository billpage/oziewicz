# Poirier and Reddiger-Poirier in Oziewicz's terms: the worldline label is a function on the leaf space

> Poirier (2012) and Reddiger and Poirier (2025) describe one relativistic particle by a congruence of trajectories with a conserved probability flux. In Oziewicz's terms the congruence is a process $`X`$, the label $`C`$ of a world is a function with $`XC = 0`$ (a coordinate on his position space, the leaf space $`Z`$), and the Born rule is a measure on $`Z`$: the flux form $`\varpi = i_J\,\mathrm{vol}`$ is closed and horizontal, so it is basic (PR1, exact). Poirier's coordinate needs only $`X`$; his simultaneity surfaces and ensemble time need the clock to be integrable, and Reddiger and Poirier drop that need (PR3, exact on their rotating example, where $`\alpha\wedge d\alpha \ne 0`$). A clock's centre (CS1) and the Born mean weight the same worlds differently (PR4, exact).

**Status.** Supplement (background and reading, not a ladder step). Labels use the
prefix **PR**; the ladder's results are cited by their MF and CS labels from
[`analysis/metric_free_body.md`](../analysis/metric_free_body.md) and
[`analysis/clock_centre.md`](../analysis/clock_centre.md). Companion script:
[`src/verify_poirier_reddiger.py`](../src/verify_poirier_reddiger.py).
Prompted by Bill Page, 5 November 2026, as the preparation for ladder step 5.
Written by Claude (Anthropic) and subject to review. Every statement of what a paper
says is a reading of the cited equation or theorem, not a verified fact about its
authors. [PDF](https://github.com/billpage/oziewicz/releases/latest/download/poirier_reddiger.pdf)

Kiehn's topological arguments are deliberately left out; they come after step 5.

---

## 0. What this supplement inherits and retracts

**Inherits** from step 3 (`metric_free_body.md`): the pair $`(X, \alpha)`$ with
$`\alpha(X) = 1`$ (MF0), the position space as functions with $`Xf = 0`$ (MF9), and the
statement that a clock is a time only when $`\alpha \wedge d\alpha = 0`$ (MF11). From
step 4: a clock's centre (CS1) and the setting CS0.

**Retracts.** Nothing in the ladder. One sentence of the Project chat of 5 November is
qualified: "Poirier's $`C`$ is a coordinate on Keres's $`z`$-space" is true of the
label alone, and §3 says in what sense. It is not true of Poirier's natural coordinates
$`(c\lambda, C)`$, which need more than $`X`$ (PR3). §6 records that only Poirier uses the
many-worlds word, and as one option among readings.

---

## 1. What the two papers do

**Poirier (2012), arXiv:1208.6260.** A spin-0 massive particle in flat spacetime. A unit
timelike field $`U^\alpha`$, $`\eta(U, U) = -c^2`$, has one trajectory through every event.
The trajectories carry Lorentz-invariant labels $`C^i`$, constant along each one.
Simultaneity at a point is the subspace orthogonal to $`U`$; when these fit together,
$`U`$ is a normalised gradient $`\nabla\lambda`$ (Eq. 8) and $`\lambda`$ is an "ensemble
time", different from the proper time $`\tau`$ of each path. In natural coordinates
$`(c\lambda, C)`$ the metric is block diagonal. Postulate 1, that probability is conserved
along a trajectory, makes $`f(C)\, d^3C`$ conserved (Eqs. 18-21); the invariant density
$`\rho`$ and the flux $`j^\mu = \rho U^\mu = f(C) V^\mu`$ satisfy $`\partial_\mu j^\mu = 0`$
(Eqs. 24-28). An ensemble proper time $`T`$ is defined by $`dT = \langle d\tau \rangle_f`$
(Eq. 35), and coordinates $`P`$ with $`f(P) = 1`$ (Eq. 36) "uniformise" $`C`$.

**Reddiger and Poirier (2025), arXiv:2012.05212v7, Quantum Stud.: Math. Found. 12 (2025) 5.**
The same flux in curved spacetime, with the requirement that the initial hypersurface be
spacelike replaced by **transversality**: the future-directed causal current $`J_0`$ on a
hypersurface $`S_0`$ is nowhere tangent to it. Then $`\frac1c\, \iota_0^* i_{J_0} \mu`$ is a
volume form, and a probability once normalised (Theorem 2.1). The Lagrangian picture builds a "flowout"
from $`S_0`$ along $`V`$ (Definition 3.3), and the probability of a region $`U`$ of the
flowout depends only on its projection to $`S_0`$ (Theorem 3.1(5), Eq. 3.12g).
Example 2.1 takes $`J^i = \psi^\dagger \gamma^0 \gamma^i \psi`$ from the Dirac equation.
Example 3.1 is a rotating congruence in 2+1 Minkowski space for which the flowout of
$`t = 0`$ is not spacelike after $`\tau = 1/\omega`$. The ensemble reading is
methodological: footnote 55 says the trajectories need not be followed by particles.

---

## 2. The dictionary

| Poirier (2012) | Reddiger-Poirier (2025) | Oziewicz (this repository) |
|---|---|---|
| unit timelike field $`U^\alpha`$ | $`J`$ or $`V`$, future-directed causal | derivation $`X`$; with $`\alpha = -\eta(X, \cdot)`$ a body $`(X, \alpha)`$, MF0 |
| trajectory | integral curve, flow line | integral curve of $`X`$ |
| label $`C^i`$, $`U^\mu \partial_\mu C^i = 0`$ | point of $`S_0`$, via $`\mathrm{pr}_2`$ | function with $`XC = 0`$; coordinate on the leaf space $`Z`$ (MF9) |
| space of labels with density $`f(C)`$ | $`S_0`$ with $`P_0`$ | $`(Z, \mu)`$ |
| $`f(C)\, d^3C`$ conserved (Postulate 1) | Lagrangian continuity (3.13) | $`\varpi = \pi^*\mu`$, $`L_X \varpi = 0`$ (PR1) |
| $`j^\mu = \rho U^\mu`$, $`\partial_\mu j^\mu = 0`$ (27, 28) | $`J`$, continuity (Cor. 3.1) | $`\varpi = i_J \mathrm{vol}`$, $`d\varpi = 0`$ |
| simultaneity submanifolds orthogonal to $`U`$ | none required; transversal $`S_0`$ | $`\ker \alpha`$, integrable iff $`\alpha \wedge d\alpha = 0`$ (MF11); against any section of $`\pi`$ |
| ensemble time $`\lambda`$, proper time $`\tau`$ | the flow parameter $`\tau`$ | $`\alpha = N\, d\lambda`$ only if integrable; $`\alpha(\partial_\tau) = 1`$ always |
| ensemble proper time $`T`$ (35) | | the $`\mu`$-mean of the clock along the paths |
| uniformising $`P`$, $`f(P) = 1`$ (36) | | a $`\mu`$-normalised chart on $`Z`$ |

---

## 3. The Born weight is a measure on the leaf space

**Proposition PR1.** Let $`M`$ be an oriented manifold of dimension $`n+1`$ with volume
form $`\mathrm{vol}`$, $`X`$ a nowhere zero vector field, $`\rho`$ a function, $`J = \rho X`$ and
$`\varpi = i_J \mathrm{vol}`$. Then

1. $`i_X \varpi = 0`$;
2. $`d\varpi = (\mathrm{div}\, J)\, \mathrm{vol}`$;
3. if $`\mathrm{div}\, J = 0`$, then in a flow box $`(z^1, \dots, z^n, s)`$ with $`X = \partial_s`$
   one has $`\varpi = m(z)\, dz^1 \wedge \dots \wedge dz^n`$. So $`\varpi = \pi^* \mu`$ for the
   measure $`\mu = m\, d^n z`$ on the leaf space $`Z`$, and for a hypersurface $`S`$
   transversal to $`X`$ and a region $`U \subset S`$ in the box, $`\int_U \varpi = \mu(\pi(U))`$.

*Proof.* (1) $`i_X i_{\rho X} \mathrm{vol} = 0`$ by antisymmetry. (2) $`d i_J \mathrm{vol} = L_J \mathrm{vol} = (\mathrm{div}\, J)\, \mathrm{vol}`$,
since $`d\,\mathrm{vol} = 0`$. (3) By (1), $`\varpi`$ has no $`ds`$ term. By (2) and Cartan,
$`L_X \varpi = d i_X \varpi + i_X d\varpi = 0`$, which in the box reads $`\partial_s \varpi_I = 0`$.
A transversal $`S`$ is a graph $`s = h(z)`$ over $`\pi(U)`$, and the pull-back of
$`m\, d^n z`$ to it is $`m\, d^n z`$. ∎ (Part A: (1) and (2) with generic functions in 2+1; Part B: the box form in 1+1.)

No metric appears. The metric enters only to say that $`J`$ is timelike or causal and
future-directed, so that $`\rho > 0`$ and $`\mu`$ is positive. That the probability of a
region of the flowout depends on its projection to $`S_0`$ alone (Theorem 3.1(5)) is the
last statement of (3), with $`S_0`$ standing in for $`Z`$. Poirier's Postulate 1 is the
same fact in labels: $`f(C)\, d^3 C`$ does not change along a trajectory because $`\varpi`$ has
no $`s`$-dependence. The continuity equation (28) is $`d\varpi = 0`$.

This is the same kind of statement as CS1: a conserved current whose slice integral
does not depend on the slice, and no metric to say it.

---

## 4. Expanding "Poirier's $`C`$ is a coordinate on Keres's $`z`$-space"

**What is exact.** $`U^\mu \partial_\mu C^i = 0`$ says $`X C^i = 0`$, so each $`C^i`$ belongs to the algebra of
functions annihilated by $`X`$, which MF9 identifies as the scalars of the position
space of the body $`X`$. Three independent ones are local coordinates on $`Z = M/X`$.
Nothing else is meant by "$`C`$ labels the worldline". In the notation of PR1, $`m(z)\, d^n z = f(C)\, d^n C`$.
**Proposition PR2** (Part B, exact). For any parametrised congruence $`x(t, C)`$ in 1+1 with
$`\rho = f(C)/\partial_C x`$ and $`v = \partial_t x`$, the flux form is $`\rho\, dx - \rho v\, dt = f(C)\, dC`$,
with no $`dt`$ component. For the free Gaussian packet, $`\sigma(t) = \sigma_0 \sqrt{1 + (\hbar t / 2 m \sigma_0^2)^2}`$,
$`v = x \sigma'/\sigma`$ satisfies continuity, and the flux form is exactly $`dP`$ with
$`P = \frac12 (1 + \mathrm{erf}(x/\sqrt2 \sigma))`$, the probability to the left of the path. This is Poirier's
uniformising coordinate (36) in one dimension, and the paths are $`x = \sqrt2\, \sigma(t)\, \mathrm{erf}^{-1}(2 P - 1)`$.
The example is Galilean: it is the non-relativistic packet of Poirier's earlier work and uses no
metric, which is the point.

**What is not given.**

1. *Not unique.* Any diffeomorphism $`C \to C'(C)`$ is another label, and $`f`$ changes by the Jacobian.
   Only $`f\, d^3C`$ is invariant. The uniformising $`P`$ is a choice of chart in which
   $`\mu`$ is Lebesgue measure (unique up to volume-preserving maps, as Poirier says).
2. *Not a metric space.* Poirier's spatial metric $`\gamma_{ij}`$ in natural coordinates is the
   metric restricted to the orthogonal surfaces. $`Z`$ has none until $`X`$ and $`\eta`$ give
   a quotient metric, and that needs more than MF9.
3. *Not an observer's space.* In Oziewicz a position space belongs to a body, and other bodies sit
   at its points (*Many-body mass-centre* §1.1). Here $`U`$ comes from the state of one particle. $`Z`$ is the leaf space of
   *that ensemble*, and its points are alternatives for where that one particle is. The mathematical object is the same. The reading is not (§6).
4. *Local.* PR1 is a flow-box statement. That $`Z`$ is a manifold globally needs a free and proper quotient.
   Reddiger and Poirier avoid the question by working with $`S_0`$ and a flowout, and treat periodic integral curves in their Appendix C.

---

## 5. What the clock adds, and what Reddiger and Poirier drop

Poirier's $`C`$ needs only $`X`$. His $`\lambda`$ and the natural coordinates $`(c\lambda, C)`$
need $`U`$ to be a normalised gradient (Eq. 8), which by the Frobenius theorem is
$`\alpha \wedge d\alpha = 0`$ for $`\alpha = -\eta(U, \cdot)`$, exactly the condition of MF11.
When it fails there is no ensemble time and no orthogonal simultaneity surface.

**Proposition PR3** (Part C, exact). Reddiger and Poirier's Example 3.1 is, in 2+1 with
$`c = 1`$ and $`\gamma = \sqrt{1 + \omega^2 r^2}`$, the field $`V = (\gamma, \omega(-y, x))`$.

1. $`V`$ is a unit timelike field, and $`\mathrm{div}(\rho(r) V) = 0`$ for every $`\rho(r)`$.
2. With $`\phi_0 = \phi - \omega t/\gamma`$ constant along the paths, the flux form is
   $`\varpi = \rho\, \gamma\, r\; dr \wedge d\phi_0`$. It is basic: $`\mu = \rho \gamma r\, dr\, d\phi_0`$ on $`Z = \{(r, \phi_0)\}`$.
   On a slice $`t = \mathrm{const}`$ it restricts to $`\rho \gamma r\, dr\, d\phi`$, the Born density.
3. $`\alpha = \gamma\, dt - \omega r^2 d\phi`$ has
   $`\alpha \wedge d\alpha = -\dfrac{\omega r (2 + \omega^2 r^2)}{\gamma}\, dt \wedge dr \wedge d\phi \ne 0`$
   for every $`r > 0`$.
4. The flowout of $`t = 0`$ has radial tangent of norm $`1 - (\gamma' \tau)^2`$, $`\gamma' = \omega^2 r/\gamma`$, which is negative at some $`r`$ iff $`\omega \tau > 1`$.

So this congruence has a leaf space, a conserved measure on it and a Born rule, and
no time function. Poirier's §II construction does not apply to it, and Reddiger and
Poirier's does. In Oziewicz's terms the Born rule needs the pair $`(X, \mathrm{vol})`$
(PR1), and the simultaneity of Poirier needs the clock to be a time (MF11). They are
independent, and Reddiger and Poirier's contribution, read this way, is to use only the first.

CS6 integrated $`\oint \alpha`$ around the axis of a rigidly rotating body. The same
quantity is nonzero here. That it measures a spin for this congruence is not shown. See PR-SP1.

---

## 6. The two means, and the readings of $`Z`$

**Proposition PR4** (Part D, exact). Let a clock $`\zeta`$ (CS0) be transversal to the paths, so that
each world $`z \in Z`$ has a unique point $`\sigma_\zeta(z)`$ on $`\zeta = \tau`$, and let $`p(z)`$ be the
momentum of the path (constant along a free path). The centre of the clock (CS1) is the $`\zeta(p)`$-weighted mean of
$`\sigma_\zeta`$, and the Born mean is its $`\mu`$-weighted mean. Their difference is

```math
C_{\mathrm{CS1}} - C_\mu = \frac{\mathrm{Cov}_\mu\big(\zeta(p), \sigma_\zeta\big)}{E_\mu[\zeta(p)]} .
```

The two agree when $`\zeta(p)`$ is constant over the ensemble. For two free paths released
from one point with $`v = 3/5`$ and $`-4/5`$, equal $`\mu`$-weights and the laboratory clock
$`\zeta = dt`$, the energy weights are $`\gamma = 5/4`$ and $`5/3`$, and the difference of the
means is $`-1/10`$ at $`\tau = 1`$ (centre of energy $`-1/5`$, mean $`-1/10`$). Mirror
velocities give equal energies and no difference at any $`\tau`$.

So "the position of the particle" in this picture has at least two answers, and each is
exact for its own weights. Which one, if either, is what a position measurement estimates is the Pryce
and Newton-Wigner question (CS-SP4), and this note does not decide it.

**Readings of $`Z`$.** Poirier offers a reading in which each trajectory "literally represents
a different world", which he describes as unlike conventional many-worlds: the worlds
interact and do not branch. He calls it perhaps the most physically meaningful, and does
not require it. Reddiger and Poirier use the ensemble interpretation methodologically and
say (footnote 55) that particles need not follow the trajectories. Oziewicz's body is a
process, and $`Z`$ is where *other* bodies sit. I have found no probability in the papers
read for steps 1 to 4. The mathematics of PR1 supports all three readings equally, and
none of them is selected by it.

For wpmw (my reading of its ORIENTATION and `world_clocks.md`, not rechecked here): its worlds
are phase-space points that share one time, and the momentum is not a field on position
space, so worlds in position space cross. The congruence of this note is therefore not wpmw's
set of worlds in position space. It is the congruence of the extended phase space, where $`dt`$
is a closed clock, and there the leaf space at fixed $`t`$ is phase space itself. Whether
that is an instance of PR1 is a question for step 5, not a result.

---

## 7. Open items

- **PR-SP1.** Reddiger and Poirier's Example 2.1 takes the Dirac current $`J^\mu = \bar\psi \gamma^\mu \psi`$.
  Compute $`\alpha \wedge d\alpha`$ for $`\alpha = -\eta(J, \cdot)/|J|`$ and compare it with the spin density
  (Gordon decomposition; Holland 1992 as cited there). PR3 shows the structure; the Dirac case is unchecked.
- **PR-SP2.** When is $`Z`$ a manifold, and what replaces PR1 when integral curves close up?
- **PR-SP3.** Which mean is the position (PR4, CS-SP4)?

**For step 5.** PR1 gives the measure $`\mu`$ that clock_centre.md lacks, so CS1
can be restated as a mean over $`Z`$; PR4 says which weights it uses; PR3 says the
construction does not need $`\alpha \wedge d\alpha = 0`$.

---

## 8. Verification

`PYTHONPATH=src python3 -u src/verify_poirier_reddiger.py`. All checks are exact (SymPy); there is nothing numerical.

| Part | Checks | Method |
|---|---|---|
| A | PR1 (1) and (2) | generic functions in 2+1 |
| B | PR2: the flux form of $`x(t, C)`$; free Gaussian, $`\varpi = dP`$ | generic function in 1+1; closed forms |
| C | PR3 (1)-(4) | symbolic in $`r, \omega`$ |
| D | PR4: covariance identity; two worked cases | symbolic; rational |

Statements about what the papers say were checked against the extracted text of the cited equations
(Poirier: abstract, §I-III, §IV A to Eq. 40; Reddiger-Poirier: §2, §3 to Theorem 3.1 and Example 3.1).
The proofs of their theorems, their §3.3 onward and the appendices were not read.

---

## References

- [poirier2012](../references/bibliography.md): B. Poirier, "Trajectory-based theory of relativistic quantum particles", arXiv:1208.6260.
- [reddiger2025](../references/bibliography.md): M. Reddiger and B. Poirier, "Towards a probabilistic foundation of relativistic quantum theory: the one-body Born rule in curved spacetime", Quantum Stud.: Math. Found. 12 (2025) 5, arXiv:2012.05212.
- Oziewicz, *Many-body mass-centre*, as cited in `analysis/mass_centre.md`; Keres 1976, as in `references/bibliography.md`.
