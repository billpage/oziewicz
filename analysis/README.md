# Analysis

Derivations and review notes: what a paper of Oziewicz's appears to claim, the
derivation that tests it, and what was and was not checked. The notes form a
**derivation ladder**: each step states in its §0 what it inherits from the
steps before it and what it retracts.

Terms are defined in the [glossary](../GLOSSARY.md); to look up a theorem or
open item by its label, use [`INDEX.md`](INDEX.md).

## The ladder

Newest first: the most recent step is at the top, and the list runs back to
step 1 at the bottom. Each entry is repeated word for word under the note's own
title, and `check_abstracts` keeps the two copies equal.

- **4.** **[`clock_centre.md`](clock_centre.md)** \
  Step 3 found that a rotating body has no time function of its own and left
  open how its vorticity relates to Møller's spin (MF-SP1, MC-SP3). This note
  reads Pryce (1948) and Møller (1949) and corrects step 1. **Definition CS0**
  adds what a body as a congruence lacks: a place. **Theorem CS1**: for a closed
  system with total $`P`$ and bivector $`L`$, any covector $`\zeta`$ with $`\zeta(P) \ne 0`$ picks one line, the centre $`C[\zeta](\tau) = (\tau P - \mathrm{ev}_\zeta L)/\zeta(P)`$.
  This is Pryce's (2.8) with $`n`$ read as a clock, so it needs no metric, and a
  spin supplementary condition is a choice of clock. **Proposition CS2**: the
  spin is the trivector $`P \wedge L`$, independent of origin; two centres differ,
  modulo $`P`$, by $`(P \wedge L)(\zeta_1, \zeta_2, \cdot)/(\zeta_1(P) \zeta_2(P))`$, and all
  clocks give one line exactly when $`P \wedge L = 0`$. **Proposition CS3**: with the
  metric, the clock $`b(P, \cdot)`$ gives Pryce's definition (d), which he calls
  relativistically covariant and the most satisfactory, and Møller's centre of
  gravity; this answers MC-SP1 and corrects step 1: a covariant centre worldline
  exists, the "known" impossibility that *Many-body mass-centre* §2.1 cites to
  these authors is not what they say, and Oziewicz's own $`Z`$ with its clock has
  all that is needed to define it. What Pryce finds difficult is different: no
  definition is both covariant and has commuting coordinates. **Proposition
  CS4**: with one clock the centres of subsystems add; with each subsystem's own
  clock they do not, which is the pattern of step 2. **Proposition CS5**: $`S_{ij} = -(1/2) \int r^2 (d \pi)_{ij}`$ for a momentum density $`\pi`$, which supports
  Oziewicz's proposal that spin lies in $`dP`$, but only with mass as a density:
  two free bodies have $`d \alpha = 0`$ and $`S \ne 0`$, and on a rotor the $`\rho d \alpha`$ term alone gives $`-I \Omega`$. **Proposition CS6**: for axisymmetric dust
  the circulation of the clock is the specific angular momentum, so $`S = (c^2/4 \pi) \int \Delta \tau dm`$ with $`\Delta \tau`$ the Sagnac difference, and on a ring
  Møller's radius is $`c \Delta \tau/(4 \pi \gamma)`$. So the failure of a rotating
  body's clocks to close and the spread of its centres are one quantity. The
  time problem is not removed: a time function has to come from outside the
  body, and each outside clock has its own centre. Checked exactly with SymPy;
  CS1 and CS2 are also proved here, and CS6 is close to an identity. No new
  prediction.
- **3.** **[`metric_free_body.md`](metric_free_body.md)** \
  *Many-body mass-centre* gives each body a time-like derivation and a clock.
  This note drops "time-like", keeps only a pair $`(X, \alpha)`$ with $`\alpha X = 1`$, and asks how far that goes with no metric and no signature, whether the
  creation and evaluation operators can carry the weight put on them, and
  whether the paper's algebraic position space and time are adequate.
  **Definition MF0** fixes the setting and the factor $`\Gamma_{XY} = \alpha_X(Y)`$,
  which need not be symmetric. **Proposition MF1**: $`\{\mathrm{ev}_X, \wedge_\alpha\} = \alpha X`$
  gives the split with no metric; the image of $`\Pi`$ depends on the process alone
  and its kernel on the clock alone, and the clock is a contracting homotopy, so
  the Koszul complex has no homology. The operators are pointwise. **Proposition
  MF2**: the non-reciprocity (1.7.19), (1.7.20), (1.7.22) needs no metric; the
  direction of a relative velocity needs no clock, and its size does.
  **Proposition MF3**: the mass centre $`(P/M, \theta/M)`$, $`M^2 = \theta(P)`$, needs
  neither metric nor symmetry, and radiation is a square-zero pair with no
  split. **Theorem MF4**: if the bodies span and $`\Gamma`$ is symmetric, there is
  exactly one symmetric bilinear form $`b`$ with $`\alpha_i = b(X_i, \cdot)`$. Postulate
  1.6.3 is therefore the metric, not an addition to it: Oziewicz rejects
  Einstein's reciprocity of velocities and postulates a reciprocity of clocks,
  and that gives the metric and its isometry group. **Corollary MF5**: clocks
  can be chosen reciprocal for up to 10 bodies in dimension 4, so only the 11th
  tests the claim, and scale changes leave only cycle ratios. **Proposition
  MF6**: the signature is an output: $`\Gamma \ge 1`$ near every body gives one
  positive direction, $`\Gamma \le 1`$ gives a definite form, and $`\Gamma = 1`$ gives
  $`b = \alpha \otimes \alpha`$. **Proposition MF7**: unit processes form a surface $`L = 1`$ whose tangent plane is the natural clock, the only one with no first-order
  clock effect; reciprocity holds exactly when the surface is a central quadric,
  its centro-affine curvature decides whether $`c`$ is finite, and $`\Gamma \ge 1`$ is
  the reverse triangle inequality. **Proposition MF8**: requiring the mass
  centre to be a body whose vector and clock are both sums forces the quadric by
  a second route; on a non-quadric the two means differ. **Proposition MF9**:
  the paper's position space is not adequate: it gives two inequivalent
  definitions, and (3.1.18) names the factor algebra of the instant, which
  depends only on the clock. The basic algebra $`\mathrm{ev}_X b = 0 = \mathrm{ev}_X db`$ is the
  position space: it needs no clock and $`d`$ closes on it, also on a rotating
  disk, where the paper's factor differential does not exist. **Proposition
  MF10**: the clock is a connection on the worldline fibration: $`\Pi d \alpha`$ is
  its curvature, $`L_X \alpha`$ is Einstein's one-body acceleration without
  Christoffel symbols, and its holonomy on the disk is the Sagnac term.
  **Proposition MF11**: the clock is not a time: time scalars exist only where
  $`\alpha \wedge d \alpha = 0`$, and on a rotating body the reciprocal clock and a time
  function exclude each other. Checked exactly with SymPy except where the note
  says numerical; MF4 to MF8 and MF11 also rest on short proofs given here.
  Nothing here departs from standard relativity. Step 4 takes up the link
  between this vorticity and Møller's spin.
- **2.** **[`ternary_mass_centre.md`](ternary_mass_centre.md)** \
  Step 1 read the mass centre `Z` as the centre-of-momentum frame, and
  `supplement/bodies_first.md` read the ternary velocity `w(P, A, B)` as a
  family labelled by a third observer `P`. This note puts `Z` in the place of
  `P`, which Oziewicz's papers and the part of his correspondence that was
  read do not do; the question is his, the answers here go beyond what he
  published. **Definition TV0** fixes the notation. **Proposition TV1**: for
  `P` in the plane of `A` and `B`, `P ∧ w = A ∧ B`, so every coplanar eagle
  reads one bivector; this is (11.10) of Oziewicz's 2004 draft in other words.
  **Theorem TV2**: for two bodies `p_ZB = -p_ZA = (m_A m_B / M) w(Z, A, B)`
  and `v(Z, A, B) = (m_A v_AB - m_B v_BA) / M`, so the fraction in Oziewicz's
  (2.2.10) is a ternary velocity. **Corollary TV3**: a pair has one velocity,
  a Lorentz link and vector reciprocity in one rest space, with nothing
  exterior, so the conflict needs one `P` for all pairs; this corrects
  `bodies_first.md` §6. **Proposition TV4**: for three or more bodies `Z ∧ X_i
  ∧ X_j` is the sum of the other momenta wedged with `X_i ∧ X_j`, so `Z`
  leaves the plane of every pair; the eagle of RV3 is the mass centre of
  masses 4, 3, 12. **Proposition TV5**: `gamma_AB - 1 = cosh^2 r
  (gamma_ternary - 1)` with `r` the distance from `A` to the boost axis; this
  gives both halves of Oziewicz's Theorem 2.5 and answers RV-SP3.
  **Proposition TV10**: the ternary velocity of the 2004 draft, the binary
  velocity carried to the eagle's rest space, keeps the binary speed and is
  reciprocal only in the plane, whereas the boost-link of 2005 and 2007 is
  always reciprocal and slower; off the plane one eagle cannot have both.
  **Theorem TV6 (no-go)**: no Lorentz link depends covariantly on the pair
  alone, carries `A` to `B` and composes, because the Lorentz group is simple;
  the Galilei group has one. This is the exact form of a remark in §4 of the
  2004 draft. **Proposition TV7**: of the three properties the binary boost
  gives up composition (31.16° round the example triangle), ternary boosts at
  one eagle give up two (32.75°), and a lift based at `Z` gives up dependence
  on the pair alone. **Proposition TV8**: the Frobenius form of the algebra of
  observers has determinant `±(det gamma)^(2n)`, so it degenerates exactly
  when the bodies are linearly dependent; for three bodies that is the
  coplanar case Oziewicz and Page found in 2004. **Proposition TV9**:
  Oziewicz's reduced mass `mu_12` is Todorov's effective energy `epsilon_w`,
  and `v(Z, A, B)` is the velocity of Todorov's effective particle. The
  conflict therefore keeps one tooth, TV6, which bites the identification of
  velocity with an isometry; it is not a conflict with the relativity
  principle, and the rotation it leaves is Thomas precession. Checked exactly
  with SymPy, except where the note says numerical. No new prediction.
- **1.** **[`mass_centre.md`](mass_centre.md)** \
  Oziewicz's last word on the centre of inertia is chapter 2 of *Many-body
  mass-centre* (short version *J. Phys.: Conf. Ser.* 532 (2014) 012021; long
  version revised 11 April 2017), with corrections he sent by email up to
  September 2020. **Definition MC0** translates his symbols (`g`, `det g =
  -c^2`, body `X` with `(gX)X = det g`, clock, groupoid factor `gamma`, binary
  velocity `v_XY = Y/gamma - X`, Schrödinger energy `E_iG`) into standard
  covariant relativity. **Proposition MC1**: the binary velocity is the ordinary
  relative velocity of `Y` in the rest space of `X`; equations (1.7.15) and
  (1.7.19) to (1.7.23) hold exactly, and the boost that carries `X` to `Y`
  carries `v_XY` to `-v_YX`, so Einstein's reciprocity holds once the two
  vectors are compared in one rest space. **Proposition MC2**: the velocity
  groupoid is the pair groupoid of the set of bodies, so its associativity is
  automatic and is not a physical difference from the Lorentz group, whose
  isometries are fixed by Oziewicz's own postulates (1.6.1) to (1.6.5).
  **Theorem MC3**: the mass centre `Z` of Definition 2.1.3 is the 4-velocity of
  the total 4-momentum (the centre-of-momentum frame) and `M` is the invariant
  mass; (2.1.5), (2.1.6), (2.1.7) and (2.1.14) hold exactly for null radiation.
  **Corollary MC4**: the radicand of (2.1.15) is misprinted (`gamma_ZX - 1` for
  `gamma_ZX^2 - 1`), and it vanishes without radiation. **Proposition MC5**: the
  reduced momenta (2.2.4), (2.2.5), (2.2.8), (2.2.10) and (2.2.11) hold exactly
  without radiation, and (2.2.4) as printed is `c^2` times Planck's momentum,
  the factor Oziewicz reported missing on 5 September 2020. **Theorem MC6**: in
  the algebra of observers the mass centre is the idempotent `c = P/M^2`, the
  only trace-1 idempotent with `cP = P = Pc`; this settles the uniqueness
  question Oziewicz left open on 16 November 2012 and is the idempotent he
  described in November 2018. **Proposition MC7**: `Z` fixes the direction of
  the centre's worldline but not its position; each observer's energy centroid
  moves with `Z`, displaced by `(S x beta)/(Mc)` (Møller's disk), so the problem
  of Pryce (1948), which concerns the position, is not addressed. All of it is
  standard special relativity in another notation; what is not standard is the
  claim that it is impossible with the Lorentz group. Checked exactly with
  SymPy; the figure is numerical.

## Checks

```
PYTHONPATH=src python3 -m ozlib.check_abstracts analysis
PYTHONPATH=src python3 -m ozlib.check_index analysis
PYTHONPATH=src python3 -m ozlib.where_used groupoid
```
