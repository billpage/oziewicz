# Index of results and open items

This index lists every labelled result (theorem, proposition, lemma, corollary,
definition) and every labelled open item in the [analysis notes](README.md),
with a section reference, a one-line paraphrase and a standing. The notes cite
each other by label; the index says, for a label, what it says, where it is, and
whether it still stands.

**Read the note before relying on a result.** A row identifies a result; it does
not carry its hypotheses. The *Standing* column records what a later note did to
a result (corrected, restricted, retracted), which the note itself cannot say.

`PYTHONPATH=src python3 -m ozlib.check_index analysis` checks that every labelled
result and open item has a row here and that every link resolves. Words are
defined in the [glossary](../GLOSSARY.md).

## Prefix registry

| Prefix | Step | Note |
|---|---|---|
| MC | 1 | [`mass_centre.md`](mass_centre.md) |

## Results by note

### Step 1: [`mass_centre.md`](mass_centre.md)

| ID | § | Says | Standing |
|---|---|---|---|
| [Def MC0](mass_centre.md#2-dictionary) | 2 | Dictionary from Oziewicz's symbols (`det g = -c^2`, clock, `gamma`, binary velocity, `E_iG`) to standard covariant relativity | — |
| [Prop MC1](mass_centre.md#3-the-binary-velocity) | 3 | `v_XY = Y/gamma - X` is the velocity of `Y` in the rest space of `X`; (1.7.15)-(1.7.23) hold; the boost `X -> Y` carries `v_XY` to `-v_YX` | — |
| [Prop MC2](mass_centre.md#3-the-binary-velocity) | 3 | The velocity groupoid is the pair groupoid of the bodies; associativity is automatic; the metric postulates fix the Lorentz group | — |
| [Thm MC3](mass_centre.md#4-the-mass-centre-is-the-centre-of-momentum-frame) | 4 | Def. 2.1.3 gives `Z` along `sum p_i - G/c^2` and `M` the invariant mass; (2.1.5)-(2.1.7), (2.1.14) hold for null `G` | — |
| [Cor MC4](mass_centre.md#5-the-two-body-total-mass) | 5 | The radicand of (2.1.15) is misprinted (`gamma - 1` for `gamma^2 - 1`) and is zero without radiation | — |
| [Prop MC5](mass_centre.md#6-reduced-momentum-and-reduced-mass) | 6 | Reduced momenta (2.2.4)-(2.2.11) hold without radiation; (2.2.4) as printed is `c^2` times Planck's momentum | Radiation terms open (MC-SP5) |
| [Thm MC6](mass_centre.md#7-the-mass-centre-as-an-idempotent) | 7 | `c = P/M^2` is the unique trace-1 idempotent with `cP = P = Pc`; it is `Z ⊗ clock_Z` | — |
| [Prop MC7](mass_centre.md#8-what-the-mass-centre-leaves-open-position) | 8 | Every observer's centroid moves with `Z`, displaced by `(S x beta)/(Mc)` (Møller); `Z` fixes direction, not position | Checked on 8 cases; general statement is Møller's |

## Open items

| ID | Says | Status |
|---|---|---|
| [MC-SP1](mass_centre.md#10-open-items) | Which integral curve of `Z` is the mass centre? | open |
| [MC-SP2](mass_centre.md#10-open-items) | No law is given for the radiation `G`; the non-null interaction field is unchecked | open |
| [MC-SP3](mass_centre.md#10-open-items) | Relate spin in `dP` (Oziewicz 2018-2019) to the spin that sets Møller's disk | open |
| [MC-SP4](mass_centre.md#10-open-items) | Dynamics from binary accelerations relative to the mass centre | open |
| [MC-SP5](mass_centre.md#10-open-items) | Radiation terms of (2.2.8) and Clarification 2.2.3 | open |
| [MC-SP6](mass_centre.md#10-open-items) | Public link for the long version | open |
