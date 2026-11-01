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
