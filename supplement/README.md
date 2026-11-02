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
- **[`velocity_draft.md`](velocity_draft.md)**. A summary of Oziewicz's unpublished draft
  *Why Einstein's addition of velocities is non-associative?* (22 November 2004,
  `velocity.pdf`, not committed and not known to be public): its argument section by
  section, 67 exact checks of its formulas (one side remark in (9.6) fails), where its
  claims stand, and what later work kept and changed. Its ternary velocity is not the
  boost-link of 2005 and 2007. Companion script `src/verify_velocity_draft.py`.
