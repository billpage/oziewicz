# The centre of a clock: spin and the failure of simultaneity

> Step 3 found that a rotating body has no time function of its own and left open how its vorticity relates to Møller's spin (MF-SP1, MC-SP3). This note reads Pryce (1948) and Møller (1949) and corrects step 1. **Definition CS0** adds what a body as a congruence lacks: a place. **Theorem CS1**: for a closed system with total $`P`$ and bivector $`L`$, any covector $`\zeta`$ with $`\zeta(P) \ne 0`$ picks one line, the centre $`C[\zeta](\tau) = (\tau P - \mathrm{ev}_\zeta\,L)/\zeta(P)`$. This is Pryce's (2.8) with $`n`$ read as a clock, so it needs no metric, and a spin supplementary condition is a choice of clock. **Proposition CS2**: the spin is the trivector $`P \wedge L`$, independent of origin; two centres differ, modulo $`P`$, by $`(P \wedge L)(\zeta_1, \zeta_2, \cdot)/(\zeta_1(P) \zeta_2(P))`$, and all clocks give one line exactly when $`P \wedge L = 0`$. **Proposition CS3**: with the metric, the clock $`b(P, \cdot)`$ gives Pryce's definition (d), which he calls relativistically covariant and the most satisfactory, and Møller's centre of gravity; this answers MC-SP1 and corrects step 1: a covariant centre worldline exists, the "known" impossibility that *Many-body mass-centre* §2.1 cites to these authors is not what they say, and Oziewicz's own $`Z`$ with its clock has all that is needed to define it. What Pryce finds difficult is different: no definition is both covariant and has commuting coordinates. **Proposition CS4**: with one clock the centres of subsystems add; with each subsystem's own clock they do not, which is the pattern of step 2. **Proposition CS5**: $`S_{ij} = -(1/2) \int r^2 (d \pi)_{ij}`$ for a momentum density $`\pi`$, which supports Oziewicz's proposal that spin lies in $`dP`$, but only with mass as a density: two free bodies have $`d \alpha = 0`$ and $`S \ne 0`$, and on a rotor the $`\rho d \alpha`$ term alone gives $`-I \Omega`$. **Proposition CS6**: for axisymmetric dust the circulation of the clock is the specific angular momentum, so $`S = (c^2/4 \pi) \int \Delta \tau dm`$ with $`\Delta \tau`$ the Sagnac difference, and on a ring Møller's radius is $`c \Delta \tau/(4 \pi \gamma)`$. So the failure of a rotating body's clocks to close and the spread of its centres are one quantity. The time problem is not removed: a time function has to come from outside the body, and each outside clock has its own centre. Checked exactly with SymPy; CS1 and CS2 are also proved here, and CS6 is close to an identity. No new prediction.

*Ladder abstract — see the [full list](README.md#the-ladder).*

**Status.** Analysis note, step 4 of the ladder. Theorem prefix **CS**. Companion
script: [`src/verify_clock_centre.py`](../src/verify_clock_centre.py) (Parts A to F;
§10). Prompted by Bill Page, 3 November 2026: having found that the time function
needs $`\alpha \wedge d \alpha = 0`$, link this vorticity to Møller's spin. Derivation and
checks were drafted with Claude (Anthropic) and are subject to review, and no
separate reader has checked them; every claim about what a paper says is a reading of
the cited page.
[PDF](https://github.com/billpage/oziewicz/releases/latest/download/clock_centre.pdf)

---

## 0. What this note asks, inherits and retracts

**Question.** What is the relation between the vorticity of a clock, the spin of a
system, and the position of its centre?

**Inherits.** From step 1: the mass centre MC3, the idempotent MC6, the disk MC7.
From step 3: the pair $`(X, \alpha)`$ MF0, reciprocity MF4, the clock as a connection
MF10, and MF11. Step 2's pattern, that a pair works and a third body does not, returns
in CS4.

**Retracts or corrects.**

| Earlier statement | What happens to it |
|---|---|
| `mass_centre.md` §9: "The frame $`Z`$ exists in both; the worldline is settled in neither" | Corrected. Pryce's (d) and Møller's centre of gravity are a covariant worldline with the Lorentz group (CS3) |
| `mass_centre.md` §8: the worldline is the part "in dispute", which Pryce and Møller left open | Corrected. They define it. The open point in Pryce is commuting coordinates (§4) |
| `mass_centre.md` MC-SP1 | Answered (CS3) |
| `mass_centre.md` MC-SP3 and `metric_free_body.md` MF-SP1 | Answered in part (CS5, CS6) |
| `bodies_first.md` §4: Oziewicz "argued away" Pryce's problem | Refined: there is less to argue away than that says (CS3) |
| `metric_free_body.md` §10: "Vorticity can reach $`S`$ only once mass becomes a density" | Stands for the second moment (CS5). For a stationary axisymmetric flow, the circulation of the clock alone gives $`S`$ (CS6) |

Sentences in earlier notes were not rewritten; the places are marked.

---

## 1. Sources

All were read in the pages cited, as page images where the text layer is poor.

- Pryce (1948), §§1 and 2 and the opening of §5 (p. 69). He lists six generalisations (a) to (f) of the Newtonian centre.
- Møller (1949), §1, pp. 253-260. He gives his Dublin lectures of 1947 as the fuller treatment and says Pryce got most of the results independently. The Dublin lectures were not read.
- Costa, Herdeiro, Natário and Zilhão (arXiv:1109.1019), for the language of centroids and supplementary conditions.
- Alba, Lusanna and Pauri (arXiv:hep-th/0102087), through a summariser only, for the comparison of the three centres.
- Rizzi, Ruggiero and Serafini (arXiv:gr-qc/0409105), eq. (30), for the Sagnac difference.

Fokker (1929) is cited by Pryce and by Møller and was not read.

---

## 2. A body needs a place

**Definition CS0 (setting).** $`A`$ is an affine space over $`V`$. A closed system has
a total momentum $`P`$ in $`V`$ and a bivector $`L`$ in $`\Lambda^2 V`$, about a chosen origin in $`A`$:

```math
L=\sum_k a_k\wedge p_k
```

for bodies with worldlines $`a_k + s p_k`$, and for a continuous system the same with
the sum over a slice of the conserved current $`\tau^b`$ (a $`V`$-valued three-form with
$`d \tau^b = 0`$). A **clock** here is a constant covector $`\zeta`$ with $`\zeta(P) \ne 0`$, and
the **centre** of $`\zeta`$ is the mean of positions on $`\zeta = \tau`$, weighted by $`\zeta`$
of momentum. Components are $`L^{ab} = \sum (a^a p^b - a^b p^a)`$ and
$`(\mathrm{ev}_\zeta\,L)^b = \zeta_a L^{ab}`$.

No metric appears, but something new does: a place $`a_k`$. Steps 1 to 3 gave a body
as a process and a clock. A process is a whole congruence, and $`L`$ depends on which
curve of it carries the mass. In the language of MF9, a body also needs a point of
its position space. That was the reason for the obstacle at the end of step 3. It also
means the affine structure of events is used, and §3.2 of *Many-body mass-centre*, which
calls the approach event-free, has no way to state any of this.

---

## 3. Each clock has its own centre

**Theorem CS1 (the centre of a clock).** For a closed system and a clock $`\zeta`$,

```math
C[\zeta](\tau)=\frac{\tau P-\mathrm{ev}_\zeta\,L}{\zeta(P)} .
```

This is a line parallel to $`P`$, whatever the interactions. Under a change of origin
by $`s`$, $`L \to L + s \wedge P`$ and the line is unchanged. It is the unique line along $`P`$
about which $`\mathrm{ev}_\zeta\,L = 0`$.

*Proof.* On $`\zeta(x) = \tau`$, contract $`L = \int (x \wedge \tau)`$:
$`\zeta_a L^{ab} = \int (\zeta(x) \tau^b - x^b \zeta_a \tau^a) = \tau P^b - \zeta(P) C^b`$. Conservation
makes $`L`$ and $`P`$ independent of the slice. For the last statement, the shift by $`C`$
gives $`\mathrm{ev}_\zeta(L - C \wedge P) = \mathrm{ev}_\zeta\,L - \zeta(C) P + \zeta(P) C = 0`$. ∎ (Part A: $`n = 4`$, three bodies,
symbolic; a collision at one event, which leaves every centre unchanged.)

This is not new. It is Pryce's (2.8), $`(s P^\mu + M^{\mu \nu} n_\nu)/(P^\sigma n_\sigma)`$, for
unit $`n`$, with his $`M`$ equal to $`L`$. What this note adds is the reading: $`n`$ enters only as a covector, so (2.8) needs no metric and no
Lorentz group. It is also the statement of Costa et al. that $`S^{ab} u_b = 0`$ selects
the centroid measured by $`u`$. So a **spin supplementary condition is a choice of clock**.
Definition (c) of Pryce, Møller's $`X(S)`$ (11) and CS1 are one object.

**Proposition CS2 (the spin).** The trivector $`P \wedge L`$ does not depend on the origin,
and modulo $`P`$,

```math
C[\zeta_1]-C[\zeta_2]=\frac{(P\wedge L)(\zeta_1,\zeta_2,\cdot)}{\zeta_1(P)\,\zeta_2(P)} .
```

All clocks give one line exactly when $`P \wedge L = 0`$, that is when $`L = a \wedge P`$ for some $`a`$.

*Proof.* Expanding, $`(P \wedge L)(\zeta_1, \zeta_2, \cdot) = \zeta_1(P) \mathrm{ev}_{\zeta_2}\,L - \zeta_2(P) \mathrm{ev}_{\zeta_1}\,L`$
plus a multiple of $`P`$. Divide by $`\zeta_1(P) \zeta_2(P)`$ and compare with CS1. If $`P \wedge L = 0`$
then $`L = a \wedge P`$ for some $`a`$, because the Koszul complex of $`P`$ is exact (MF1, with $`\wedge`$ in
place of $`\mathrm{ev}`$ by duality), and CS1 gives the line through $`a`$. ∎ (Part B, symbolic.)

The Pauli-Lubanski vector is the metric dual of $`P \wedge L`$. So the spin, like the centre
of a clock, needs no metric; the **size** of the disk does, because that needs to know
which clocks are allowed. A Galilean world has one clock, so one centre, whatever
$`P \wedge L`$ is. Pryce's condition after (2.9), that $`M^{\mu \nu} P^\sigma - M^{\sigma \nu} P^\mu`$ be a
multiple of $`P^\nu`$, is this statement for his $`n`$.

Oziewicz's split gives the same thing in his own language. With $`Z = P/M`$, a clock
$`\zeta`$ normalised on $`Z`$, and MF1, $`L = Z \wedge D + \Pi L`$: the idempotents divide $`L`$ into a
moment $`D`$, which vanishes on the centre of $`\zeta`$, and a spin $`\Pi L`$ in $`\mathrm{ker}\,\mathrm{ev}_\zeta`$.

---

## 4. What Pryce and Møller said

**Proposition CS3 (the intrinsic centre).** Given a metric, take $`\zeta = b(P, \cdot)`$. Then

1. $`C[b(P, \cdot)]`$ is Pryce's definition (d), with (2.11), and Møller's *centre de gravité*: the centre of mass in the rest frame of the system, carried to any frame by a Lorentz transformation. It depends on $`P`$ and $`L`$ only, so it is a covariant worldline of any closed system.
2. For a unit observer $`n`$ with velocity $`\beta`$ relative to $`Z`$, the displacement from it is Møller's (26), (27), $`(S \times \beta)/M`$, and with $`|\beta| < 1`$ these fill Møller's disk of radius (28), $`|S|/(Mc)`$.

(Part C: (2.8) and (2.11) as printed, on a boosted example; (26), (27) on five
observers of step 1's example.)

So MC-SP1 is answered: the integral curve of $`Z`$ that the system itself picks out is
the centre of the clock of $`Z`$. Oziewicz's construction contains everything needed:
Definition 2.1.3 gives $`Z`$ a simultaneity $`gZ/\det g`$, and only $`L`$ is missing. Axiom
1.6.2 fixes that clock, and MF4 says why it is singled out: it is the reciprocal one.

**What the sources say.** *Many-body mass-centre* §2.1 says that it is known, citing
Pryce, Møller and Landau-Lifshitz, that within the Lorentz group the intrinsic
mass-centre does not exist. That is not what Pryce or Møller say.

- Pryce (§1): definition (d) is "the most satisfactory", because it is covariant and applies to any system, including particles interacting through a field. He also says that no definition is wholly satisfactory, and the drawback he names for (d) is that the Poisson bracket of different coordinates does not in general vanish.
- Møller (pp. 255-256): there are infinitely many centres of mass, one for each Lorentz frame, all at rest in the rest frame $`S^\circ`$, and the one belonging to $`S^\circ`$ itself plays a special role; he calls it the centre of gravity.
- Pryce (§5): except for spin 0, it does not seem possible to find a definition both covariant and with commuting coordinates. This is the known difficulty, and it is a statement about canonical position, which matters for quantum theory.

Alba, Lusanna and Pauri, as summarised, give the three centres: Møller's centre of
energy (Pryce (c) in the frame in use), the covariant Fokker-Pryce centre of inertia
(Pryce (d)), and the canonical centre (Pryce (e)), with relations by spin terms.

Step 1 was right that the paper does not touch this, and wrong in saying the worldline
remains unsettled. Oziewicz's chapter 2 gives no position, so it does not improve on
(d). And (d) needs a metric, since that is what gives $`P`$ a clock of its own. So an
intrinsic centre does not call for abandoning the Lorentz group. With one clock for all
frames (Galilei) there is nothing to choose, and with many clocks the reciprocal one
does the choosing.

**Proposition CS4 (subsystems).**

1. With one clock, $`\zeta(P) C[\zeta]`$ adds over subsystems.
2. With each subsystem's own clock, the centre of the whole is not in general the weighted mean of the centres of the parts.

*Proof.* Part 1: CS1, since $`P`$ and $`L`$ add. Part 2 is the example of Part D, where the
difference is non-zero on the slice of the whole; the difference comes from CS2 applied
to each part with non-zero spin. ∎

This is the pattern of step 2 (TV6): one pair, or one clock, composes; a body's own
construction does not. "2-body is 3-body" in the sense of §2.1 holds, with a qualification:
the mass centre is a body with a line of its own, but that line is not built from
the lines of its parts.

---

## 5. Spin in $`dP`$

**Proposition CS5 (the second moment of $`d \pi`$).** Let $`\pi`$ be a rapidly decaying
momentum density on a rest space of the system, with zero total momentum. Then

```math
S_{ij}=-\tfrac12\int r^{2}\,(d\pi)_{ij}\,d^{3}x ,
```

independently of the origin. If $`\pi = \rho \alpha`$, then
$`d \pi = d \rho \wedge \alpha + \rho d \alpha`$.

*Proof.* Integrate by parts. A shift of origin by $`a`$ adds multiples of the total
momentum and of $`\int d \pi = 0`$. ∎

(Part E.) Two checks show what this does and does not say.

- Step 1's two free bodies, smeared into Gaussians: each $`d \alpha = 0`$, and the formula gives $`S = -24`$, all from $`d \rho \wedge \alpha`$.
- A rigid Gaussian rotor: the $`\rho d \alpha`$ term gives $`-I \Omega`$ and the $`d \rho \wedge \alpha`$ term gives $`+2 I \Omega`$.

This supports Oziewicz's proposal that spin lies in $`dP`$ (step 1, §1), read with $`P`$ a
density. It does not support a body with one mass and no density, since $`dP`$ for
$`P = m \alpha`$ knows nothing of places. Nor does it say that vorticity is spin, locally.
(2.1.17) cannot be the spin of the centre for free bodies with constant $`X_i`$, since then
$`Z`$ is constant and (2.1.17) is empty. If the $`X_i`$ are fields, $`\theta = M \zeta`$ gives
$`d \theta = \sum m_i d \alpha_i`$ and $`\zeta \wedge d \zeta = \theta \wedge d \theta / M^2`$ (MF10, part 5).

---

## 6. Where vorticity does give the spin

**Proposition CS6 (circulation).** Let $`u`$ be a stationary axisymmetric unit flow in
Minkowski space with clock $`\alpha = -g(u, \cdot)`$, and $`c = 1`$.

1. Round a circle of the axis symmetry, $`\oint \alpha = -2 \pi u_\phi`$, and by Stokes this is the flux of $`d \alpha`$ through the disk it bounds. $`u_\phi`$ is the angular momentum per unit rest mass.
2. For dust, with rest-mass element $`dm`$, $`S = \int u_\phi dm`$, and so $`S = -(1/2 \pi) \int (\oint \alpha) dm`$.
3. For rigid rotation $`\oint \alpha`$ is half the Sagnac difference $`\Delta \tau`$ in magnitude, and

```math
S=\frac{c^{2}}{4\pi}\int\Delta\tau\,dm .
```

4. On a ring of mass $`m`$, radius $`R`$, $`S = \gamma m R^2 \omega`$ and Møller's radius is $`R v/c = c \Delta \tau/(4 \pi \gamma)`$. In general, for dust with no binding, $`S/(Mc) = (c/4 \pi) \int \Delta \tau dm / \int \gamma dm`$.

(Part F. $`\Delta \tau`$ is (30) of Rizzi et al. Parts 1 and 2 are close to definitions; the
content is the reading.)

*Analogy.* Walk round the rim of a turntable, setting your watch to each neighbour's
as you go. When you return you are out by $`\Delta \tau/2`$. That is why no one slice of
simultaneity belongs to the turntable, and the centre of mass depends on the slice. The
disk of centres is that mismatch expressed as a length, and averaged over the mass.

This is the link asked for. MF11 says that the reciprocal clock of a rotating body is
not integrable, and that a time function must have a non-reciprocal clock, from outside the
body. CS1 says that each such clock has its own centre. CS6 says that the two
failures have one measure. So the time problem is not solved: the body has no time
function of its own, and the price of taking one from outside is an indeterminacy of
position of size $`|S|/(Mc)`$, which Møller's (29) shows is no larger than the body.

The statement is limited to dust. Stresses change the relation between momentum density
and the flow (open item CS-SP1).

---

## 7. Assessment

| Claim or question | Standing after this note |
|---|---|
| Intrinsic mass centre impossible with the Lorentz group (§1.1, §2.1) | Not what Pryce and Møller say; (d) is covariant (CS3) |
| Group-free approach gives a "perfect" mass-centre (§2.1) | It gives the frame $`Z`$. The worldline needs $`L`$ and the clock of $`Z`$, and then it is Pryce's (d) |
| Spin in $`dP`$ | Yes as a second moment, with a density (CS5) |
| (2.1.17) is the spin of the centre | Not for free bodies. Vorticity reaches $`S`$ by circulation in stationary flows (CS6) |
| Spin supplementary conditions | Each is a choice of clock (CS1) |
| Spin needs a metric | No: $`P \wedge L`$ (CS2). The disk's size does |
| Bodies are event-free | Not if a system has spin (CS0) |

---

## 8. Open items

- **CS-SP1.** Extend CS6 beyond dust, to a body with stresses, and to non-stationary flows. Which clock replaces $`-g(u, \cdot)`$ when energy current and rest-mass current differ?
- **CS-SP2.** The disk needs the allowed clocks. With MF7 they are the tangent planes of the unit surface. What is the disk on a non-quadric surface, and does it stay convex? How do the two mass centres of MF8 enter?
- **CS-SP3.** Is Møller's (29), that a system with positive energy density is larger than its disk, a statement about clocks? Can it be proved with $`\Gamma \ge 1`$?
- **CS-SP4.** Poisson brackets of the centres: Pryce's bracket for (d) is proportional to spin. Is that bracket a form of $`(P \wedge L)`$ on the space of clocks?
- **CS-SP5.** Keres's vortex fields (MF-SP1) were not taken up. Does his curl of relative velocity match the circulation of CS6 for the clock of the reference space?

---

## 9. What this does for the ladder

MC-SP1 is answered. MC-SP3 and MF-SP1 are answered in part. The remaining route to
dynamics (MC-SP4) now has a stated requirement: relative accelerations need a place
for each body, not only a process.

---

## 10. Verification

`PYTHONPATH=src python3 -u src/verify_clock_centre.py` runs every check below and ends
with `ALL CHECKS PASSED`. All parts are exact (SymPy).

| Part | What is checked | How |
|---|---|---|
| A | CS1, origin shift, a collision | $`n = 4`$, 3 bodies, symbolic; one rational case |
| B | CS2 | symbolic; one rational case for a clock that is no observer's |
| C | CS3: (2.8), (2.11), (26), (27) | rational examples, metric $`\mathrm{diag}(1, -1, -1)`$ |
| D | CS4 | one rational example |
| E | CS5 | Gaussians, symbolic width; a Gaussian rotor |
| F | CS6 | symbolic; a uniform disk |

CS1, CS2 and CS5 are proved here for general systems. The continuous form of CS1 is
proved by hand; the script checks bodies. CS3 and CS4 are checked on examples.

---

## References

- M. H. L. Pryce, "The mass-centre in the restricted theory of relativity and its connexion with the quantum theory of elementary particles", *Proc. R. Soc. Lond. A* 195 (1948) 62-81, [doi:10.1098/rspa.1948.0103](https://doi.org/10.1098/rspa.1948.0103).
- C. Møller, "Sur la dynamique des systèmes ayant un moment angulaire interne", *Ann. Inst. H. Poincaré* 11 (1949) 251-278, [Numdam](https://www.numdam.org/item/AIHP_1949__11_5_251_0/).
- L. F. O. Costa, C. Herdeiro, J. Natário and M. Zilhão, "Mathisson's helical motions for a spinning particle: are they unphysical?", [arXiv:1109.1019](https://arxiv.org/abs/1109.1019).
- D. Alba, L. Lusanna and M. Pauri, "Centers of mass and rotational kinematics for the relativistic N-body problem in the rest-frame instant form", [arXiv:hep-th/0102087](https://arxiv.org/abs/hep-th/0102087). Through a summariser.
- G. Rizzi, M. L. Ruggiero and A. Serafini, "Synchronization gauges and the principles of special relativity", [arXiv:gr-qc/0409105](https://arxiv.org/abs/gr-qc/0409105).
- Z. Oziewicz, "Many-body mass-centre: Homological Algebra for relativity of position-spaces", *J. Phys.: Conf. Ser.* 532 (2014) 012021, [doi:10.1088/1742-6596/532/1/012021](https://doi.org/10.1088/1742-6596/532/1/012021).
