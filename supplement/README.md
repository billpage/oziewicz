# Supplement

Background, worked test cases, and summaries of unpublished drafts (written for
this repository; the drafts themselves are not committed). Supplements are not
ladder steps: they cite the ladder's results by label, and their own labels are
not listed in `analysis/INDEX.md`.

- **[`bodies_first.md`](bodies_first.md)** (prefix RV). Oziewicz's reading of
  relativity, with the body rather than position space as primitive, from
  *Concepts of relative velocity* (2011) and *Many-body mass-centre* (2014;
  long version 2017). Separates a metric-free layer from the layer that needs
  the metric, shows that Einstein's ternary velocity reduces to the binary one
  when the observer lies in the plane of the two bodies (RV2) and differs by a
  Thomas-Wigner rotation otherwise (RV3), reads the "astonishing conflict" of
  *Ternary relative velocity* (2007): the formulas are right, the conflict
  needs more than its premises state (step 2 says what), and the proposed test (4.2) compares
  two quantities of standard relativity (RV5, RV6); and withdraws the 2025
  chat applications (Pioneer, rotation curves, wide binaries, cosmic rays).
  Companion script `src/verify_relative_velocity.py`.
- **[`oziewicz_on_science.md`](oziewicz_on_science.md)**. What Oziewicz said about
  how science should be done (science is subjective, based on dissent, everybody
  has a right to be right, against Popper's demarcation): each slogan with its
  place in his 2013 papers and his 2009 talk, a paraphrase of his case against
  Popper, and where it sits uneasily with itself (2009 against 2013 on
  refutation), with facts the 2013 paper states that this repository does not
  adopt, and with the method of this repository. Supports the README's In
  memoriam section.
- **[`velocity_draft.md`](velocity_draft.md)**. A summary of Oziewicz's unpublished draft
  *Why Einstein's addition of velocities is non-associative?* (22 November 2004,
  `velocity.pdf`, not committed and not known to be public): its argument section by
  section, 98 exact checks of it and of the public revision of March 2007 (one side remark
  in (9.6) fails), where its claims stand, and what the revision dropped and added. Its
  ternary velocity is not the boost-link of 2005 and 2007. Companion script `src/verify_velocity_draft.py`.
- **[`poirier_reddiger.md`](poirier_reddiger.md)** (prefix PR). Poirier (2012) and Reddiger and
  Poirier (2025) read in Oziewicz's terms: a dictionary, the Born weight as a measure on the leaf
  space of a congruence (PR1, no metric), what "Poirier's $`C`$ is a coordinate on Keres's
  $`z`$-space" does and does not mean (PR2), Reddiger and Poirier's rotating example as a leaf
  space and a Born measure without a time function (PR3), and the centre of a clock against the
  Born mean (PR4). Kiehn is deferred. Companion script `src/verify_poirier_reddiger.py`.
- **[`matolcsi_spacetime.md`](matolcsi_spacetime.md)** (prefix MT). A reading of chapter II
  (special relativistic spacetime models) of T. Matolcsi, *Spacetime Without Reference
  Frames* (1993), the book Oziewicz cited for the reference-frame-free method. Its relative
  velocity is the binary velocity of step 1 (MT1); it has the non-reciprocity and the boost
  that carries one mutual velocity to minus the other (MT2), the Thomas-Wigner rotation
  without the name, as the non-transitivity of "physically equal" vectors (MT3), and an
  addition formula that is composition in the pair groupoid (MT4). Its regular observer is
  `α ∧ dα = 0` (MT6). Where Matolcsi and Oziewicz part is the status of the boost: a
  convention with a price, or a false axiom. §8 adds the second edition (2018, CC BY 4.0)
  and Matolcsi and Gohér (2001): the velocity is the *standard* one, tied to a
  synchronization (MT8); the Thomas rotation is named (MT9); the addition formula changes
  form, and two displays of the second edition are misprints (MT8, MT10). §9: Oziewicz's clock form
  is a synchronization, his reciprocity of clocks is Einstein's (MT11), and a shared clock
  is his Galilean algebra inside Minkowski spacetime (MT12). 55 exact checks;
  the first edition is not committed.
  Companion script `src/verify_matolcsi.py`.
- **[`grassmann_to_clifford.md`](grassmann_to_clifford.md)**. A summary of Oziewicz's
  "From Grassmann to Clifford" (1986), every formula restated and keyed to the paper's
  equation numbers: the pair of Grassmann algebras of multivectors and multiforms as
  primary, exterior multiplication and its transpose as fermion operators with no metric,
  and the Clifford product on the same space from `γ_v = e_v + i_{φv}` for a linear map `φ`
  from vectors to covectors, not necessarily symmetric. Compared with three later texts.
  His own sequel (1997) constructs the product that 1986 postulates and concedes that the
  antisymmetric part `ω` of `φ` labels isomorphic algebras; its Conjecture 8.2 on the
  minimum polynomial of `γ^μ ⊗ γ_μ` holds in every dimension (§12.5). Jadczyk (2021) proves
  the construction and shows `ω` is a gauge; one sign in his eq. (68) is wrong under his
  own conventions (§10.4). Sobczyk's globally dual null vectors are the 1986 dual pair, his
  locally dual ones the 1986 construction for one `φ` (§11). Conclusion (§13): what is
  given without a choice is the evaluation of covectors on vectors; a metric is the choice
  of a subspace of the doubled space. 90 exact checks; none of the papers is committed.
  Companion script `src/verify_grassmann_clifford.py`.
- **[`magnetismo.md`](magnetismo.md)** (prefix MG). A summary of Oziewicz's unpublished lecture notes
  *Magnetismo e Electricidad* (UNAM FES Cuautitlán, 2014–2020; last version 18 July 2020, not
  committed), the source of his observer operators: a body with its clock carries a derivation
  `D` (simultaneity) and an algebra map `M` (places), `D + M = id = U²` for the unipotent
  `U = ev + cr` (MG1). Two definitions exchange places and simultaneity (MG2); the private
  differential exists exactly when the clock does not rotate (MG3); with a rotating clock the
  magnetic Gauss law gains `−Ω ∧ E` and Faraday's law the acceleration term (MG4); the metric
  intertwines vector and form operators only for `g(L, L) = 1` (MG5). The idempotent
  `(1 + U)/2`, not in the notes, is step 5's `e_X`. 29 exact checks. Companion script
  `src/verify_magnetismo.py`.
