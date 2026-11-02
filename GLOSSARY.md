# Glossary

Terms used in the notes of [`analysis/`](analysis) and
[`supplement/`](supplement), with what each means *here*. A word is listed if it
is used in more than one note, if it has more than one sense (Oziewicz's usage
often differs from the textbook's), or if it is borrowed from outside the
subject. Each entry says what the word denotes, where it is **defined**, and
what not to **confuse** it with. Where an entry and a note disagree, the note
is right.

**Where is a word used?** `PYTHONPATH=src python3 -m ozlib.where_used WORD`.
**Where is a theorem or open item?** [`analysis/INDEX.md`](analysis/INDEX.md).

### Based lift

The link `g_XY = L_{Z->Y} L_{Z->X}^-1` built from boosts out of one body `Z`. It
carries `X` to `Y` and composes exactly, and it is not a pure boost and depends on
`Z`. **Defined:**
[`ternary_mass_centre.md`](analysis/ternary_mass_centre.md#6-the-no-go-theorem),
Proposition TV7. **Not to confuse with** the binary boost, which does not compose,
or the ternary boost at `Z`, which does not either.

### Binary velocity

Oziewicz's `v_XY = Y/gamma_XY - X`: the velocity of body `Y` in the rest space of
body `X`. It is the standard covariant relative velocity. **Defined:** long
version of *Many-body mass-centre* (1.4.7), (1.7.14); read in
[`mass_centre.md`](analysis/mass_centre.md#3-the-binary-velocity) Proposition
MC1. **Not to confuse with** Einstein's velocity, which is referred to one
fixed rest space and composes non-associatively; Oziewicz calls that one
*ternary*.

### Body (material body)

A time-like vector (derivation) `X` with `g(X, X) = det g = -c^2`, that is `c`
times a 4-velocity. In Oziewicz's later usage (emails of November 2018) also the
energy-momentum one-form `P` of the body. **Defined:**
[`mass_centre.md`](analysis/mass_centre.md#2-dictionary), Definition MC0. **Not
to confuse with** a point particle: Oziewicz's body is a congruence, a whole
position space.

### Clock

The one-form `gX / det g` of a body `X`: it is 1 on `X` and vanishes on the rest
space of `X`, so it fixes the body's simultaneity. **Defined:**
[`mass_centre.md`](analysis/mass_centre.md#2-dictionary). **Not to confuse
with** proper time along a worldline.

### Eagle

The third observer `E` or `P` of a ternary velocity, from the eagle watching the
street and the bus in *Concepts of relative velocity* §2. In Oziewicz's phrase, a
"preferred exterior-observer". **Defined:**
[`bodies_first.md`](supplement/bodies_first.md#3-binary-and-ternary-velocity).
**Not to confuse with** an exterior body as such: what matters is whether the eagle
lies in the plane of the two bodies, and the mass centre of a pair does
([`ternary_mass_centre.md`](analysis/ternary_mass_centre.md#3-two-bodies-the-eagle-lies-in-the-plane)).

### Groupoid gamma (Minkowski factor)

`gamma_XY = (gX)Y / det g`. Numerically the Lorentz factor of the relative
motion of `X` and `Y`. **Defined:**
[`mass_centre.md`](analysis/mass_centre.md#2-dictionary). **Not to confuse
with** a different quantity: Oziewicz's Warning 1.6.4 says it is conceptually
distinct from the Lorentz factor; as a number it is the same.

### Mass centre (centre of inertia)

Two senses. (1) Oziewicz's `Z` of Definition 2.1.3: a body, the direction of the
total 4-momentum, i.e. the centre-of-momentum frame. (2) Pryce's and Møller's:
a worldline, the energy-weighted mean position, which depends on the observer.
**Defined:** [`mass_centre.md`](analysis/mass_centre.md#4-the-mass-centre-is-the-centre-of-momentum-frame)
Theorem MC3 for (1), Proposition MC7 for (2). **Not to confuse** the two: the
claim that a mass centre is impossible with the Lorentz group concerns (2), the
construction concerns (1).

### Position space

The space of places of one body `X`: the quotient "spacetime / `X`", or
algebraically the scalars `f` with `Xf = 0` and the forms in `ker ev_X`. In
Oziewicz's reading it belongs to the body, and there is no position space
without one. Needs no metric. **Defined:** *Many-body mass-centre* §1.1, §3.1;
*Concepts of relative velocity* §5; read in
[`bodies_first.md`](supplement/bodies_first.md#1-oziewiczs-reading-the-body-is-primitive).
**Not to confuse with** a hypersurface of simultaneous events, which needs a
clock and is a set of events, not of places.

### Reciprocity

Einstein's assumption that if `B` moves with velocity `v` relative to `A`,
then `A` moves with `-v` relative to `B`. Oziewicz's binary velocities are not
reciprocal as vectors, because `v_AB` and `v_BA` lie in different rest spaces;
they are reciprocal after the boost carries one rest space to the other.
**Defined:** [`mass_centre.md`](analysis/mass_centre.md#3-the-binary-velocity)
Proposition MC1, part 3; its role in the "astonishing conflict" in
[`bodies_first.md`](supplement/bodies_first.md#6-the-astonishing-conflict).
**Not to confuse with** the reciprocity of a ternary velocity for one fixed
observer, (2.3) of *Ternary relative velocity*, which holds as vectors.

### Split (projection, `Pi_X`)

The decomposition of a vector into a part along a body `X` and a part in its
rest space, `Y = gamma_XY X + Pi_X Y`. **Defined:**
[`mass_centre.md`](analysis/mass_centre.md#2-dictionary).

### Ternary velocity

The velocity `w(E, S, B)` of a body `B` relative to `S` as observed by a third
body `E`: the solution of `L_{E∧w} S = B` with `E.w = 0` (*Concepts of relative
velocity* §3), the boost-link. His 2004 draft used the name for another object, the
binary velocity carried to the rest space of `E`; the two agree only in the plane
([`ternary_mass_centre.md`](analysis/ternary_mass_centre.md#5-how-far-the-ternary-falls-below-the-binary),
Proposition TV10). It equals the binary velocity when `E` lies in the plane of `S`
and `B`, and differs from it by a Thomas-Wigner rotation otherwise.
**Defined:** [`bodies_first.md`](supplement/bodies_first.md#3-binary-and-ternary-velocity),
Propositions RV2 and RV3. **Not to confuse with** the binary velocity, which
needs no third body. At the mass centre of a pair it is the fraction in (2.2.10)
([`ternary_mass_centre.md`](analysis/ternary_mass_centre.md#3-two-bodies-the-eagle-lies-in-the-plane),
Theorem TV2).

### Thomas-Wigner rotation

The rotation left by boosts that do not close: the product of the boosts round a
triangle of bodies, or the difference between a ternary and a binary boost. It equals
the area of the triangle in velocity space, and it is the physical content of the
non-associativity of Einstein addition. **Defined:**
[`bodies_first.md`](supplement/bodies_first.md#3-binary-and-ternary-velocity)
Proposition RV3;
[`ternary_mass_centre.md`](analysis/ternary_mass_centre.md#6-the-no-go-theorem)
Theorem TV6. **Not to confuse with** a failure of associativity of the groupoid, which
is automatic and carries no orientation.
