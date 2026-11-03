# Orientation

**A guide for a reader arriving with no context: what this repository is for, which
words mean what, and what is established, open or retracted.** Current to step 4 of
the ladder, 3 November 2026.

---

## 0. Status and provenance

| Where | What is there |
|---|---|
| [`analysis/`](analysis/README.md) | The derivation ladder, four steps so far: [`mass_centre.md`](analysis/mass_centre.md) (1 November 2026), [`ternary_mass_centre.md`](analysis/ternary_mass_centre.md) (2 November), [`metric_free_body.md`](analysis/metric_free_body.md) and [`clock_centre.md`](analysis/clock_centre.md) (3 November) |
| [`supplement/`](supplement/README.md) | [`bodies_first.md`](supplement/bodies_first.md), his reading of relativity in his own terms; [`velocity_draft.md`](supplement/velocity_draft.md), a summary of an unpublished draft of 2004; [`oziewicz_on_science.md`](supplement/oziewicz_on_science.md), his views on the practice of science (§3 below) |
| [`talks/`](talks/README.md) | His talk to the Natural Philosophy Alliance, 2009, as narrated slides |
| [`references/bibliography.md`](references/bibliography.md) | Links to the papers, with what was and was not checked for each |

The scaffold dates from 31 October 2026. When this document and a note disagree,
the note is right. Earlier notes are not rewritten when a later one corrects them:
the places are marked, and the *Standing* column of
[`analysis/INDEX.md`](analysis/INDEX.md) records what happened.

Zbigniew Oziewicz (died 2020) worked in mathematical physics, including the
mathematics of relativity (relative velocity, groupoids and categories in place of
groups) and many-body mass centres. Bill Page was a co-author of one of the papers
listed in the bibliography (*Concepts of relative velocity*, with Oziewicz) and
corresponded with him, and the notes are in part a
[memorial](README.md#in-memoriam). That is a relationship, not independence: a
reading of this work by one of its co-authors should be weighed accordingly. The
notes are drafted with Claude (Anthropic), and nothing here has had external peer
review ([`AI-USE.md`](AI-USE.md)).

The notes are readings. They state what a paper appears to claim, in the notes' own
words, and then test what can be tested. A statement of what Oziewicz claimed is an
interpretation until it is checked against the paper. Follow the link in the
bibliography and read the original. Not every source can be followed: step 1 works
from a long version of 2017 that is not known to be public, and its §1 maps the
equation numbers to the public version of 2015; the draft of 2004 is not known to be
public either, and `velocity_draft.md` is a summary of it, not a substitute.

## 1. What the repository is trying to do

Examine, in detail and sceptically, parts of Oziewicz's work on the conceptual and
mathematical foundations of relativity and quantum mechanics. For each claim the
aim is to say: what is asserted, what it depends on, whether it can be reproduced
exactly (by computer algebra where possible, numerically otherwise), and what
remains unchecked.

So far the ladder covers the kinematics of special relativity and the mass centre.
Quantum mechanics has not been taken up; the nearest point is Pryce's difficulty
with commuting coordinates (CS-SP4).

**Where to start.** §2 here, then `bodies_first.md` or the talk for his view, then
the ladder from step 1. [`analysis/README.md`](analysis/README.md) has an abstract
of each step, newest first.

## 2. The central idea

Oziewicz rewrites relativity with bodies as primitives: each body is a time-like
vector with its own clock and its own rest space ("position space"), velocities
are arrows between bodies (a groupoid, with one zero velocity per body), and a
many-body system has a mass centre that is itself a body.

| Step | Question | Finding |
|---|---|---|
| 1 | What does the mass centre of *Many-body mass-centre* (2014; long version 2017), his last statement of this, define? | Standard special relativity in a coordinate-free notation. The binary velocity is the usual relative velocity, the mass centre `Z` is the centre-of-momentum frame, and his metric postulates fix the Lorentz group (MC1 to MC3). |
| 2 | Can `Z` be the third observer of his ternary velocity? This goes beyond what he published. | For two bodies, yes, and his (2.2.10) turns out to be a ternary velocity (TV2, TV3). For three or more, `Z` leaves the plane of each pair (TV4), and no Lorentz link can depend on the pair alone, carry one body to the other and compose (TV6). That is the part of his "astonishing conflict" that survives. It is a statement about velocity as an isometry, not about the relativity principle. |
| 3 | What remains below the metric, with a body as a pair of a process and a clock? | Velocity, its non-reciprocity and the mass centre survive (MF1 to MF3). His symmetric gamma turns out to be the metric itself (MF4), and the signature follows from the sign of `gamma - 1` (MF6). His algebraic position space is not adequate, and the basic algebra is (MF9). His clock is a connection, not a time (MF10, MF11). |
| 4 | How are the vorticity of a clock, spin and the position of the centre related? | A correction to step 1: a covariant centre worldline exists (CS3). It needs the angular momentum `L`, which his chapter 2 does not supply, as well as `Z` and its clock. Pryce's difficulty is a different one: no definition is both covariant and has commuting coordinates. Each clock picks its own centre (CS1), and the spin is `P ∧ L` (CS2). For stationary axisymmetric dust, the failure of a rotating body's clocks to close and the spread of its centres are one quantity (CS6). |

Taken together: no step departs from standard relativity or gives a new prediction,
and no statement has been found that holds in his reading and fails in the textbook
one (RV-SP2). What is not standard is his claim that an intrinsic mass centre is
impossible with the Lorentz group, and that claim does not hold up (CS3). What is
his own is the presentation, several of the results (step 2, §10 says which) and
the questions. Step 3 adds a map of where each assumption enters.

Whether the rest of his programme goes beyond a notation is what later notes must
test: dynamics from relative accelerations (MC-SP4), which needs a place for each
body as well as a process; a law for radiation (MC-SP2); orientation and spin in
the groupoid (TV-SP1). The algebra of observers has so far given results on the mass
centre and on linear dependence (MC6, TV8). Spin in `dP` holds as a second moment,
with mass as a density (CS5).

## 3. Oziewicz on how science is done

Oziewicz argued, in print and in talks, that science is and must be subjective, that
it should be based on dissent, that everybody has a right to be right, that a subject
on which everybody agrees is not a subject of science, and, against Popper, that no
criterion separates science from pseudo-science. These views are in *Science must
never be objective* and *Are peer reviewers Guardians of the Truth?* (both 2013) and
his 2009 talk. [`supplement/oziewicz_on_science.md`](supplement/oziewicz_on_science.md)
gives the place of each slogan and paraphrases his case against Popper. Its quotations
from the first paper come from a long copy of it, because the printed article has not
been seen. A reader needs these views for three reasons.

**"Subjective" has a technical sense as well as a general one (Bill Page's reading).**
Technically, the subjective choice is the observer, the reference body or the aether,
and what changes with that choice is stated exactly. Generally, it is scientific
opinion. As a reading of this document, not a claim of his, the technical sense can
be seen at work in the mathematics: the groupoid has one zero velocity per body, and
in step 4 each clock has its own centre, with CS2 giving the difference exactly.

**The repository does not share all of it.** He held that science needs no criterion
for deciding who is right, and these notes check derivations. They ask whether an
identity holds, whether a construction composes and whether a statement follows from
its premises. They take no position on which theory nature chooses, and they treat
no claim as wrong, or right, for being unorthodox. His own papers assert mathematical
results as true or false, so he evidently did not hold mathematical correctness to be
a matter of opinion. Whether he would accept this division is open. The README does
not claim that he would.

**His statements about science need the same care as his physics.** He does not
reconcile what he said about refutation in 2009 (he would welcome an experiment that
showed his theory wrong) with what he said in 2013 (refutation by experiment is not
the judge of science), so neither position should be attributed to him alone. Two
statements of fact in the 2013 paper, on the 1919 eclipse data and the OPERA neutrino
measurement, are not adopted here. The supplement, §4, gives both cases with sources.

## 4. Vocabulary

Terms are defined in [`GLOSSARY.md`](GLOSSARY.md). Labelled results and open
items are listed in [`analysis/INDEX.md`](analysis/INDEX.md). Oziewicz's usage often
differs from the textbook's. *Velocity* needs its qualifier (binary, ternary,
Einstein's), and *clock* is a covector, not a time.

## 5. Established, open, retracted

| Standing | Meaning | Items |
|---|---|---|
| Established | derived and checked exactly (or numerically, saying which) | Step 1: MC1 to MC6 (SymPy); MC7 on eight cases (SymPy). Step 2: TV1 to TV5, TV7 to TV10 (SymPy); TV6 proved by hand. Step 3: MF1 to MF3, MF9, MF10 (SymPy); MF4 to MF8, MF11 proved by hand with instances checked. Step 4: CS1, CS2, CS5 proved and checked (SymPy); CS3, CS4 on examples; CS6 for dust (SymPy). Supplement: the RV results (SymPy), and 98 exact checks of the 2004 draft and its 2007 revision (SymPy; one side remark in (9.6) fails) |
| Open | stated, not yet settled | MC-SP2, MC-SP4, MC-SP5; TV-SP1, TV-SP3 to TV-SP5; MF-SP2 to MF-SP6; CS-SP1 to CS-SP5; RV-SP2, RV-SP4; VD-SP1, VD-SP2. In part: MC-SP3 and MF-SP1 (by CS5, CS6), RV-SP1 (by MF6, MF7) |
| Answered | an open item since closed | MC-SP1 (CS3), MC-SP6, TV-SP2, RV-SP3 (TV5) |
| Corrected | an earlier statement changed by a later note, which says how in its §0 | `mass_centre.md` §§8, 9 on the worldline (CS3), §6 on `mu_kl` (TV2, TV9); `bodies_first.md` §2 on the metric and position space (MF4, MF9), §4 on Pryce's problem (CS3), §6 on reciprocity (TV3) |
| Retracted | withdrawn, kept with the reason | The June 2025 Project-chat summaries of *Many-body mass-centre* (not in this repository; see step 1, §0) and their applications to Pioneer, rotation curves, wide binaries and cosmic rays ([`supplement/bodies_first.md`](supplement/bodies_first.md) §7) |

"Established" means that a mathematical step was reproduced. It does not mean that
Oziewicz's claim is true or that a reading of it is faithful
([`AI-USE.md`](AI-USE.md#what-verified-means-here)). What happened to his claims is
in the Assessment section of each note.

A retracted or negative result is recorded the same way as a positive one, and a
new note says what it inherits from, and retracts of, the notes before it.
