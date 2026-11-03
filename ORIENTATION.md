# Orientation

**A guide for a reader arriving with no context: what this repository is for, which
words mean what, and what is established, open or retracted.** It is a stub. It is
written first so that the sections exist, and each fills in as notes are added.

---

## 0. Status and provenance

Created 31 October 2026 as a scaffold. The first analysis note,
[`analysis/mass_centre.md`](analysis/mass_centre.md), was added on 1 November
2026, step 2, [`analysis/ternary_mass_centre.md`](analysis/ternary_mass_centre.md),
on 2 November 2026, and step 3, [`analysis/metric_free_body.md`](analysis/metric_free_body.md),
on 3 November 2026, with step 4, [`analysis/clock_centre.md`](analysis/clock_centre.md), the same day. When this document and a note disagree, the note is right.

Zbigniew Oziewicz (died 2020) worked in mathematical physics, including the
mathematics of relativity (relative velocity, groupoids and categories in place of
groups) and many-body mass centres. Bill Page was a co-author of one of the papers
listed in [`references/bibliography.md`](references/bibliography.md) (*Concepts of
relative velocity*, with Oziewicz). That is a relationship, not independence: a
reading of this work by one of its co-authors should be weighed accordingly.

The notes here are readings. They state what a paper appears to claim, in the
notes' own words, and then test what can be tested. A statement of what Oziewicz
claimed is an interpretation until it is checked against the paper. Follow the link
in the bibliography and read the original.

## 1. What the repository is trying to do

Examine, in detail and sceptically, parts of Oziewicz's work on the conceptual and
mathematical foundations of relativity and quantum mechanics. For each claim the
aim is to say: what is asserted, what it depends on, whether it can be reproduced
exactly (by computer algebra where possible, numerically otherwise), and what
remains unchecked.

## 2. The central idea

Oziewicz rewrites relativity with bodies as primitives: each body is a time-like
vector with its own clock and its own rest space ("position space"), velocities
are arrows between bodies (a groupoid, with one zero velocity per body), and a
many-body system has a mass centre that is itself a body. Step 1 of the ladder
reads his last statement of this, the mass centre of *Many-body mass-centre*
(2014; long version 2017), and finds it to be standard special relativity in a
coordinate-free notation: the binary velocity is the usual relative velocity, the
mass centre is the centre-of-momentum frame, and the Lorentz group is fixed by his
own metric postulates. What his construction does not address (step 4 says more) is the position of
the centre, which is where the known difficulty lies. Step 2 puts the mass centre
in the place of the third observer of his ternary velocity, which goes beyond what
he published. For two bodies that removes the problem, and his (2.2.10) turns out to
be a ternary velocity. For three or more bodies it does not: no Lorentz link can
depend on the pair alone and also compose, which is the part of his "astonishing
conflict" that survives, and it is a statement about velocity as an isometry, not
about the relativity principle. Step 3 goes below the metric, with a body as a pair
of a process and a clock. Velocity, its non-reciprocity and the mass centre survive
without a metric. Oziewicz's symmetric gamma turns out to be the metric itself, and the
signature follows from the sign of `gamma - 1`. His algebraic position space is the wrong
object (the basic algebra is the right one), and his clock is a connection, not a time.
Step 4 reads Pryce and Møller and corrects step 1: a covariant centre worldline exists.
Each clock picks its own centre, the spin is `P ∧ L`, and on a rotating body the failure
of the clocks to close and the spread of the centres are one quantity.
Whether the rest of his programme (accelerations, rotation, spin in `dP`, the algebra
of observers) goes beyond a notation is what later notes must test.

## 3. Vocabulary

Terms are defined in [`GLOSSARY.md`](GLOSSARY.md). Labelled results and open
items are listed in [`analysis/INDEX.md`](analysis/INDEX.md).

## 4. Established, open, retracted

| Standing | Meaning | Items |
|---|---|---|
| Established | derived and checked exactly (or numerically, saying which) | Step 1: MC1 to MC6 (SymPy); MC7 on eight cases (SymPy). Step 2: TV1 to TV5, TV7 to TV10 (SymPy); TV6 proved by hand. Step 3: MF1 to MF3, MF9, MF10 (SymPy); MF4 to MF8, MF11 proved by hand with instances checked. Step 4: CS1, CS2, CS5 proved and checked (SymPy); CS3, CS4, CS6 on examples |
| Open | stated, not yet settled | MC-SP2 to MC-SP5 (MC-SP1, MC-SP6 answered); TV-SP1, TV-SP3 to TV-SP5 (TV-SP2 answered); MF-SP1 to MF-SP6; CS-SP1 to CS-SP5 |
| Retracted | withdrawn, kept with the reason | The June 2025 Project-chat summaries of *Many-body mass-centre* (not in this repository; see step 1, §0) and their applications to Pioneer, rotation curves, wide binaries and cosmic rays ([`supplement/bodies_first.md`](supplement/bodies_first.md) §7) |

A retracted or negative result is recorded the same way as a positive one, and a
new note says what it inherits from, and retracts of, the notes before it.
