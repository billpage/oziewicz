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
| TV | 2 | [`ternary_mass_centre.md`](ternary_mass_centre.md) |

## Results by note

### Step 1: [`mass_centre.md`](mass_centre.md)

| ID | § | Says | Standing |
|---|---|---|---|
| [Def MC0](mass_centre.md#2-dictionary) | 2 | Dictionary from Oziewicz's symbols (`det g = -c^2`, clock, `gamma`, binary velocity, `E_iG`) to standard covariant relativity | — |
| [Prop MC1](mass_centre.md#3-the-binary-velocity) | 3 | `v_XY = Y/gamma - X` is the velocity of `Y` in the rest space of `X`; (1.7.15)-(1.7.23) hold; the boost `X -> Y` carries `v_XY` to `-v_YX` | — |
| [Prop MC2](mass_centre.md#3-the-binary-velocity) | 3 | The velocity groupoid is the pair groupoid of the bodies; associativity is automatic; the metric postulates fix the Lorentz group | — |
| [Thm MC3](mass_centre.md#4-the-mass-centre-is-the-centre-of-momentum-frame) | 4 | Def. 2.1.3 gives `Z` along `sum p_i - G/c^2` and `M` the invariant mass; (2.1.5)-(2.1.7), (2.1.14) hold for null `G` | — |
| [Cor MC4](mass_centre.md#5-the-two-body-total-mass) | 5 | The radicand of (2.1.15) is misprinted (`gamma - 1` for `gamma^2 - 1`) and is zero without radiation | — |
| [Prop MC5](mass_centre.md#6-reduced-momentum-and-reduced-mass) | 6 | Reduced momenta (2.2.4)-(2.2.11) hold without radiation; (2.2.4) as printed is `c^2` times Planck's momentum | Radiation terms open (MC-SP5); reading of `mu_kl` refined by TV2, TV9 |
| [Thm MC6](mass_centre.md#7-the-mass-centre-as-an-idempotent) | 7 | `c = P/M^2` is the unique trace-1 idempotent with `cP = P = Pc`; it is `Z ⊗ clock_Z` | — |
| [Prop MC7](mass_centre.md#8-what-the-mass-centre-leaves-open-position) | 8 | Every observer's centroid moves with `Z`, displaced by `(S x beta)/(Mc)` (Møller); `Z` fixes direction, not position | Checked on 8 cases; general statement is Møller's |

### Step 2: [`ternary_mass_centre.md`](ternary_mass_centre.md)

| ID | § | Says | Standing |
|---|---|---|---|
| [Def TV0](ternary_mass_centre.md#2-notation) | 2 | Notation: `w(P, A, B)`, `gamma_t`, `v(P, A, B)`, velocity space as hyperbolic space | — |
| [Prop TV1](ternary_mass_centre.md#3-two-bodies-the-eagle-lies-in-the-plane) | 3 | For `P` in the plane of `A`, `B`: `w = (P.B)A - (P.A)B`, `P ∧ w = A ∧ B`; one boost for all such `P` | — |
| [Thm TV2](ternary_mass_centre.md#3-two-bodies-the-eagle-lies-in-the-plane) | 3 | `p_ZB = -p_ZA = (m_A m_B / M) w(Z, A, B)`; `v(Z, A, B) = (m_A v_AB - m_B v_BA) / M`: the fraction in (2.2.10) is a ternary velocity | — |
| [Cor TV3](ternary_mass_centre.md#3-two-bodies-the-eagle-lies-in-the-plane) | 3 | A pair has one velocity, a Lorentz link and vector reciprocity in one rest space, with nothing exterior | — |
| [Prop TV4](ternary_mass_centre.md#4-three-or-more-bodies-the-eagle-leaves-the-plane) | 4 | `Z ∧ X_i ∧ X_j = sum_k (m_k / M) X_k ∧ X_i ∧ X_j`: `Z` leaves the plane of every pair; RV3's eagle is the mass centre of masses 4, 3, 12 | — |
| [Prop TV5](ternary_mass_centre.md#5-how-far-the-ternary-falls-below-the-binary) | 5 | `gamma_AB - 1 = cosh^2 r (gamma_t - 1)`; both halves of Theorem 2.5; RV-SP3 answered | — |
| [Prop TV10](ternary_mass_centre.md#5-how-far-the-ternary-falls-below-the-binary) | 5 | The 2004 ternary velocity keeps the binary speed and is reciprocal only in the plane; the boost-link is always reciprocal and slower | — |
| [Thm TV6](ternary_mass_centre.md#6-the-no-go-theorem) | 6 | No Lorentz link depends covariantly on the pair alone, carries `A` to `B` and composes; the Galilei group has one | Proved by hand; not machine-checked |
| [Prop TV7](ternary_mass_centre.md#6-the-no-go-theorem) | 6 | The three ways out on the example: 31.16°, 32.75°, and the based lift, which closes | — |
| [Prop TV8](ternary_mass_centre.md#8-the-algebra-of-observers-sees-the-same-line) | 8 | The Frobenius form has determinant `±(det gamma)^(2n)`; degenerate exactly for linearly dependent bodies; `gamma_t = gamma - alpha` | — |
| [Prop TV9](ternary_mass_centre.md#9-dynamics-where-two-bodies-work-and-three-do-not) | 9 | `mu_12` is Todorov's `epsilon_w`; `v(Z, A, B)` is the velocity of his effective particle | — |

## Open items

| ID | Says | Status |
|---|---|---|
| [MC-SP1](mass_centre.md#10-open-items) | Which integral curve of `Z` is the mass centre? | open |
| [MC-SP2](mass_centre.md#10-open-items) | No law is given for the radiation `G`; the non-null interaction field is unchecked | open |
| [MC-SP3](mass_centre.md#10-open-items) | Relate spin in `dP` (Oziewicz 2018-2019) to the spin that sets Møller's disk | open |
| [MC-SP4](mass_centre.md#10-open-items) | Dynamics from binary accelerations relative to the mass centre | open |
| [MC-SP5](mass_centre.md#10-open-items) | Radiation terms of (2.2.8) and Clarification 2.2.3 | open |
| [MC-SP6](mass_centre.md#10-open-items) | Public link for the long version | answered: 2015 version on Academia.edu (§1) |
| [TV-SP1](ternary_mass_centre.md#11-open-items) | The groupoid that keeps orientation; `[[a,b],[b,c]]` in the algebra; spin | open |
| [TV-SP2](ternary_mass_centre.md#11-open-items) | Sign of `alpha` on the 2005 slides; Theorem 10.5 of `velocity.pdf` | answered: slip in one line of slide 8 (§8); it is Theorem 11.5 |
| [TV-SP3](ternary_mass_centre.md#11-open-items) | Is the failure of cluster separability a rotation between `Z` of the pair and `Z` of the system? | open |
| [TV-SP4](ternary_mass_centre.md#11-open-items) | A three-body counterpart of TV2 for (2.2.11) | open |
| [TV-SP5](ternary_mass_centre.md#11-open-items) | The search of the correspondence was not exhaustive | open |
