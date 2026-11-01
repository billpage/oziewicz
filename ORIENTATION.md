# Orientation

**A guide for a reader arriving with no context: what this repository is for, which
words mean what, and what is established, open or retracted.** It is a stub. It is
written first so that the sections exist, and each fills in as notes are added.

---

## 0. Status and provenance

Created 31 October 2026 as a scaffold. The first analysis note,
[`analysis/mass_centre.md`](analysis/mass_centre.md), was added on 1 November
2026. When this document and a note disagree, the note is right.

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
own metric postulates. What his construction does not address is the position of
the centre, which is where the known difficulty lies. Whether the rest of his
programme (accelerations, rotation, spin in `dP`, the algebra of observers) goes
beyond a notation is what later notes must test.

## 3. Vocabulary

Terms are defined in [`GLOSSARY.md`](GLOSSARY.md). Labelled results and open
items are listed in [`analysis/INDEX.md`](analysis/INDEX.md).

## 4. Established, open, retracted

| Standing | Meaning | Items |
|---|---|---|
| Established | derived and checked exactly (or numerically, saying which) | Step 1: MC1 to MC6 (SymPy); MC7 on eight cases (SymPy) |
| Open | stated, not yet settled | MC-SP1 to MC-SP5 (MC-SP6 answered) |
| Retracted | withdrawn, kept with the reason | The June 2025 Project-chat summaries of *Many-body mass-centre* (not in this repository; see step 1, §0) |

A retracted or negative result is recorded the same way as a positive one, and a
new note says what it inherits from, and retracts of, the notes before it.
