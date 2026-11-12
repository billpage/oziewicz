# Matolcsi's *Spacetime Without Reference Frames*: the special relativistic part

> A reading of chapter II (special relativistic spacetime models) of the book Oziewicz cited as the reference-frame-free account of relativity. Matolcsi's relative velocity of 1993 is, symbol for symbol, the binary velocity of step 1 (MT1). The book has its non-reciprocity, the boost that carries one mutual velocity to minus the other (MT2), and an addition formula that needs both mutual velocities of the middle pair, which is composition in the pair groupoid without the name (MT4). Boosts compose to a boost only for coplanar velocity values; the defect is the Thomas-Wigner rotation, which the book derives but does not name, and it makes "physically equal" vectors in different observer spaces a non-transitive relation (MT3). Its "regular observer" is the condition `α ∧ dα = 0` of step 3, and of its two rotating observers one is rigid, neither is regular (MT6). The book keeps the Lorentz group and says what it cannot do: boosts are not a subgroup and no rotation subgroup is singled out (MT7). The first edition is not the last word: the second edition (2018, CC BY 4.0) separates the observer from its synchronization and calls this velocity the *standard* relative velocity; a synchronization changes its size and not its direction (MT8). Matolcsi and Gohér (1996, 2001) name the Thomas rotation and say it measures the failure of transitivity (MT9). The second edition replaces the addition formula of 1993 by one that boosts the second velocity, and prints it with two coefficients exchanged (MT4, MT10). Oziewicz's observer, a vector with a clock form, is one of Matolcsi's inertial reference frames, and his reciprocity of clocks is Einstein's synchronization (MT11); one clock form shared by all bodies gives his Galilean algebra inside Minkowski spacetime (MT12). 55 exact checks pass; no formula of the first edition failed, and two displays of the second edition are misprints.

**Status.** Supplement (a reading of a published book, not a ladder step). Companion
script: [`src/verify_matolcsi.py`](../src/verify_matolcsi.py). Requested by Bill Page,
12 November 2026. The first edition (1993) is copyrighted and is not committed here; the
second (2018) is CC BY 4.0 and is linked in the references. §§1 to 7 were written from the
first edition; §8 was added the same day from the second edition and from Matolcsi and
Gohér (2001), after Bill Page found the author's page. **Every statement of
what the book says is a reading.** Formulas were read from page images, not from extracted
text, and each formula used below was then checked exactly; the prose was read from page
images for the sections listed in §1 and from OCR text elsewhere, and the note says which.
Drafted with Claude (Anthropic) and subject to review.

Notation. Section numbers are the book's, written II.x.y.z (chapter II, section x.y,
paragraph z). The book's symbols are kept: $`\mathrm{M}`$ is spacetime, an affine space
over the four-dimensional vector space $`\mathbf{M}`$; $`\mathbf{g}`$ is the Lorentz form
with signature $`(-,+,+,+)`$, written as a dot, $`x \cdot y`$; light speed is 1;
$`\mathrm{V}(1)`$ is the set of future-directed $`u`$ with $`u \cdot u = -1`$ (the book
calls them *velocity values*); $`\mathbf{E}_u = \{x : u \cdot x = 0\}`$ is the spacelike
subspace orthogonal to $`u`$; $`\pi_u x = x + u\,(u \cdot x)`$ is the projection onto
$`\mathbf{E}_u`$ along $`u`$; $`(a \otimes b) \cdot x = a\,(b \cdot x)`$. The book also
carries a one-dimensional space $`\mathbf{I}`$ of time intervals, so that its vectors have
physical dimensions ($`\mathrm{V}(1) \subset \mathbf{M}/\mathbf{I}`$); this note sets the
unit aside. Labels of this repository: MC (step 1), MF (step 3), RV
([`bodies_first.md`](bodies_first.md)).

---

## 0. What this supplement inherits and retracts

**Inherits** the binary velocity MC1, the pair groupoid MC2, the time-function condition
MF11 and the position space MF9. They are cited, not re-derived.

**Corrects.** `references/bibliography.md` listed the book as "Budapest 1994 … as cited by
Oziewicz; not re-checked". The title page and the copyright page of the copy read here
both say 1993 (§1). Step 1 and `bodies_first.md` cite "Matolcsi (1994)" for the statement
that mutual relative velocities lie in different rest spaces; the statement is in the book
(II.4.2.3), the year should read 1993.

**Retracts**, within this note (first version, same day): the remark in MT3 that the
Thomas rotation goes unnamed is true of the 1993 book only, and its reading as the failure
of transitivity is Matolcsi and Gohér's, not this note's (MT9); open items MT-SP2 and
MT-SP5 are answered (§8).

---

## 1. The book and what was read

T. Matolcsi, *Spacetime Without Reference Frames*, Akadémiai Kiadó, Budapest, 1993,
ISBN 963 05 6433 5. Its copyright page says it is the revised and enlarged version of
*A Concept of Mathematical Physics: Models for Space-Time* (Akadémiai Kiadó, 1984), which
was not seen. Oziewicz's reference lists give the year as 1994 with the same ISBN.

The copy read is a 396-page PDF made from TeX. It prints **no page numbers**, and the
numbers in its table of contents run ahead of the PDF pages (by about 3 in Part One, about
6 in Part Two), so it is not the printed layout. Its source is now known (§8.1): it is a conversion of
the PostScript file that the author's page distributes as the 1993 edition. This note
cites by section number only, and the numbers are those of the first edition; the second
edition renumbers chapters II.3 and II.6 (§8.2).

The book has two parts. Part One, *Spacetime models*, builds a non-relativistic (Galilean)
model in chapter I and a special relativistic one in chapter II, deliberately in parallel:
each has sections on fundamentals, world lines, observers, kinematics, observations,
splittings, reference frames and spacetime groups. Chapter III sketches general relativity.
Part Two is the mathematics (tensors, pseudo-Euclidean spaces, affine spaces, Lie groups).
The programme, as II.6.1 puts it, is that spacetime models are defined without the notion
of observer, and observers (then reference frames and coordinates) are defined *by means
of* the model. II.1.6.4 adds that present-day physics tacitly uses the arithmetic model
$`\mathbb{R}^{1+3}`$, whose extra structure invites confusions the abstract model avoids.

| Sections | How read |
|---|---|
| II.1.1 to II.1.3, II.1.4.1, II.1.4.2, II.1.6.3, II.1.6.4, II.1.7, II.1.8 | page images |
| II.3 (inertial observers), II.4 (kinematics), II.5 (observations) | page images, in full |
| II.6.1 to II.6.3, II.6.7.1 to II.6.7.3, II.6.7.6, II.6.8.1, II.6.8.2 | page images |
| II.7.1, II.9.1, II.9.2, II.10.1 | page images |
| II.6.5, II.6.6, II.6.8.5, II.6.9, II.9.3 | OCR text, statements only |
| the rest of II.1.4 to II.1.6, II.1.9, II.2, II.6.4, II.8, II.9.4, II.10.2 to II.10.7, II.11, III, chapter I | not read (MT-SP1) |

---

## 2. Dictionary

| Matolcsi 1993 | This repository | Where |
|---|---|---|
| velocity value $`u \in \mathrm{V}(1)`$ | body `X` with `g(X, X) = -1` | MC0 |
| $`-u \cdot u'`$ | Lorentz factor `gamma_XY` (the groupoid gamma) | MC0 |
| $`\mathbf{E}_u`$ | rest space of the body | MC1 |
| relative velocity $`v_{u'u}`$ of $`u'`$ with respect to $`u`$ | binary velocity `v_XY`, `X = u`, `Y = u'` | MT1 |
| Lorentz boost $`L(u', u)`$ from $`u`$ to $`u'`$ | the boost `B` of MC1, part 3 | MT2 |
| $`\pi_u = \mathbf{g} + u \otimes u`$, and $`-u \otimes u`$ | `1 - p` and the idempotent `p` of the body | velocity_draft §2 |
| space $`\mathrm{E}_U`$ of an observer: the set of its world lines | position space of a body | RV1, MF9 |
| regular observer | clock with `α ∧ dα = 0` | MT6, MF11 |
| observer $`U : \mathrm{M} \to \mathrm{V}(1)`$ (a field) | a body as a vector field with its clock | MF0 |

The order of indices is opposite: Matolcsi writes the observed first, $`v_{u'u}`$; this
repository writes the reference body first, `v_XY`.

---

## 3. The reading

### 3.1 The model (II.1.1 to II.1.3)

Absolute time is given up and *absolute light propagation* is put in its place: the future
light cone at each world point is a datum of the model, and the Euclidean structure that
each observer finds in its own space is derived from it (II.1.1.2 to II.1.1.5). The model
is the triple $`(\mathrm{M}, \mathbf{I}, \mathbf{g})`$ (II.1.2.1). There is no time and no
space in it.

Each $`u \in \mathrm{V}(1)`$ gives a split of vectors (II.1.3.2, II.1.3.5),

```math
h_u : \mathbf{M} \to \mathbf{I} \times \mathbf{E}_u, \qquad x \mapsto (-u \cdot x,\ \pi_u x), \qquad h_u^{-1}(t, q) = u\,t + q ,
```

and II.1.3.6 states the difference from the Galilean case in one sentence: there, one
spacelike subspace $`\mathbf{E}`$ serves every $`u`$; here, every $`u`$ has its own
$`\mathbf{E}_u`$. Everything that follows comes from that.

**Relative velocity (II.1.3.7; repeated as a Definition in II.4.2.2).**

```math
v_{u'u} := \frac{u'}{-u' \cdot u} - u \ \in\ \mathbf{E}_u, \qquad |v_{u'u}|^2 = |v_{uu'}|^2 = 1 - \frac{1}{(u' \cdot u)^2} .
```

If $`u \ne u'`$, the intersection $`\mathbf{E}_u \cap \mathbf{E}_{u'}`$ is two-dimensional,
and $`v_{u'u}`$ spans its orthogonal complement inside $`\mathbf{E}_u`$, as $`v_{uu'}`$ does
inside $`\mathbf{E}_{u'}`$.

**Lorentz boost (II.1.3.8).** $`L(u', u)`$ is defined as the linear map that sends $`u`$ to
$`u'`$, is the identity on $`\mathbf{E}_u \cap \mathbf{E}_{u'}`$, and sends $`v_{u'u}`$ to
$`-v_{uu'}`$. It is then given in closed form,

```math
L(u', u) = \mathbf{g} + \frac{(u' + u) \otimes (u' + u)}{1 - u' \cdot u} - 2\, u' \otimes u ,
```

with $`\mathbf{g}`$ standing for the identity map, and shown to be $`\mathbf{g}`$-orthogonal,
orientation- and arrow-preserving, with $`L(u', u)^{-1} = L(u, u')`$.

**Composition (II.1.3.9).** $`L(u'', u')\,L(u', u) = L(u'', u)`$ if and only if $`u, u',
u''`$ are coplanar. The proof is a direct computation. The book concludes that in general
the product of two boosts is not a boost.

### 3.2 Inertial observers (II.3)

An observer is a smooth field $`U : \mathrm{M} \to \mathrm{V}(1)`$ on a connected domain,
inertial if constant (II.3.1.1). Its *space* $`\mathrm{E}_U`$ is the set of its maximal
integral curves, the $`U`$-lines (II.3.1.3): a point of the observer's space is a world
line, not a point of spacetime. This is defined for every observer.

Time is defined only for inertial observers (II.3.2). Radar synchronisation gives: $`y`$
is simultaneous with $`x`$ according to $`U`$ when $`y - x \in \mathbf{E}_u`$. The time
$`\mathrm{I}_U`$ is the set of hyperplanes directed by $`\mathbf{E}_u`$. Both quotients
are affine spaces (II.3.2.4, II.3.3.2):

```math
s - t := -u \cdot (y - x) \quad (x \in t,\ y \in s), \qquad q' - q := \pi_u (x' - x) \quad (x' \in q',\ x \in q),
```

so the time of an inertial observer is a one-dimensional affine space over $`\mathbf{I}`$
and its space a three-dimensional Euclidean affine space over $`\mathbf{E}_u`$. The
splitting $`H_U : \mathrm{M} \to \mathrm{I}_U \times \mathrm{E}_U`$ is an affine bijection
over $`h_u`$ (II.3.4.2). Spaces of different inertial observers are affine spaces over
*different* vector spaces.

### 3.3 Kinematics (II.4)

A world line $`r`$ is seen by $`U`$ as a motion $`r_U : \mathrm{I}_U \to \mathrm{E}_U`$,
and (II.4.2.1) its derivative is $`\dot r / (-u \cdot \dot r) - u`$ at the corresponding
proper time. That is the reason for the definition of $`v_{u'u}`$: it is a derivative of a
position in $`\mathrm{E}_U`$ with respect to $`U`$-time, not a boost parameter.

**Non-reciprocity (II.4.2.2, II.4.2.3).** $`v_{u'u} = -v_{uu'}`$ if and only if $`u =
u'`$. The book says this contradicts "our habitual evidence", that textbooks take the two
to be opposite, and that "no harm comes" because textbooks work with components in bases
related by the boost, in which the components are opposite. Its stated reason for the
non-equality is that the two spaces are affine spaces over different vector spaces, and
it gives the relation $`L(u', u)\, v_{u'u} = -v_{uu'}`$.

**Addition (II.4.3).** The sum $`v_{u''u'} + v_{u'u}`$ is not $`v_{u''u}`$: its terms lie
in different spaces (II.4.3.1). Boosting the first term into $`\mathbf{E}_u`$ does not
help, since the sum can then be longer than 1. The Proposition of II.4.3.2 is

```math
v_{u''u} = \frac{\Big(v_{u''u'} - \dfrac{v_{u''u'} \cdot v_{uu'}}{|v_{uu'}|^2}\, v_{uu'}\Big)\sqrt{1 - |v_{uu'}|^2} + \Big(1 - \dfrac{v_{u''u'} \cdot v_{uu'}}{|v_{uu'}|^2}\Big)\, v_{u'u}}{1 - v_{u''u'} \cdot v_{uu'}} ,
```

and II.4.3.3 stresses that $`v_{u''u}`$ is not a function of $`v_{u''u'}`$ and
$`v_{u'u}`$ alone, nor of $`v_{u''u'}`$ and $`v_{uu'}`$ alone: both mutual velocities of
the pair $`(u, u')`$ are needed. The textbook formula appears on putting $`v :=
v_{u'u}`$ and $`-v := v_{uu'}`$, which II.4.3.4 writes with the remark "(but this is
impossible!)".

**Light (II.4.7).** For a lightlike direction $`w`$, $`v_{wu} := w/(-u \cdot w) - u`$
has length 1 for every $`u`$. The relative velocity of $`u`$ with respect to $`w`$ is
not defined. The aberration formula of II.4.7.3 is
$`\cos\theta = (\cos\theta' + |v_{uu'}|)/(1 + |v_{uu'}| \cos\theta')`$, where $`\theta`$
is the angle between $`v_{wu}`$ and $`v_{u'u}`$ in $`\mathbf{E}_u`$ and $`\theta'`$ the
angle between $`v_{wu'}`$ and $`-v_{uu'}`$ in $`\mathbf{E}_{u'}`$.

### 3.4 Observations (II.5)

**Physically equal vectors (II.5.1).** A vector of $`\mathbf{E}_u`$ and one of
$`\mathbf{E}_{u'}`$ cannot be compared as they stand. The book makes an explicit
*agreement*: $`q \in \mathbf{E}_u`$ and $`q' \in \mathbf{E}_{u'}`$ are called physically
equal when $`L(u', u)\,q = q'`$. It says the equality "makes no original sense", and then
(II.5.1.2) that it is symmetric but not transitive, by II.1.3.9: a line in your space
parallel to one in mine, and one in his parallel to yours, and his need not be parallel
to mine. It calls this "a rather embarrassing situation" with no escape, and concludes
that the opposite-velocity convention and the transitivity of parallelism exclude each
other.

**Lorentz contraction (II.5.2, II.5.3).** What $`U`$ sees at a $`U`$-instant of a figure
at rest for $`U_\mathrm{o}`$ is the image under $`A_{uu_\mathrm{o}}`$, the projection onto
$`\mathbf{E}_u`$ along $`u_\mathrm{o}`$ restricted to $`\mathbf{E}_{u_\mathrm{o}}`$. This
map is not the boost: it sends $`v_{uu_\mathrm{o}}`$ to $`-\sqrt{1 -
|v_{uu_\mathrm{o}}|^2}\; v_{u_\mathrm{o}u}`$, so it is not orthogonal, and

```math
|A_{uu_\mathrm{o}} e_\mathrm{o}|^2 = |e_\mathrm{o}|^2 - (v_{uu_\mathrm{o}} \cdot e_\mathrm{o})^2 .
```

The book insists that contraction and dilation (II.5.6) are statements about what one
observer finds of another's rod or clock, "illusory" in its word, and it separates them
from the difference of proper times along two world lines between the same two world
points, which is absolute (II.5.7.2). Rigid rods do not exist in the model (II.5.5):
measurement rests on clocks and light signals.

### 3.5 Non-inertial observers (II.6, in part)

II.6.1 denies that non-inertial observers need general relativity. A *simultaneity* is
an equivalence relation whose classes are world surfaces (spacelike hypersurfaces),
smooth in a stated sense (II.6.2.3). Each simultaneity $`\mathcal{S}`$ determines an
observer $`U_\mathcal{S}`$, the unit normal field. An observer is **regular** if it is
the normal field of some simultaneity, which is then unique (II.6.2.4); otherwise it has
no natural time, only artificial ones. Distances in the observer's space are defined by
integrating $`|\pi_{U}\, \mathrm{d}L|`$ along curves in an instant (II.6.3.3) and depend,
in general, on the simultaneity and the instant. The definition of *rigid* was not read;
from its use in II.6.7.5 it means that these lengths do not depend on the instant.

Two uniformly rotating observers are defined, with $`\Omega`$ a non-zero antisymmetric
map of $`\mathbf{E}_{u_\mathrm{o}}`$ and $`q = \pi_{u_\mathrm{o}}(x - o)`$:

```math
U_\mathrm{I}(x) = \Omega q + u_\mathrm{o}\sqrt{1 + |\Omega q|^2}, \qquad U_\mathrm{II}(x) = \frac{u_\mathrm{o} + \Omega q}{\sqrt{1 - |\Omega q|^2}} \quad (|\Omega q| < 1).
```

The first is global, not rigid (II.6.7.5) and not regular (II.6.7.6, with a direct
proof). The second lives inside the light cylinder, is rigid (II.6.8.5), is not regular
(stated as Exercise II.6.9.11), and its space is not Euclidean (II.6.8.6). The two
uniformly accelerated observers of II.6.5 and II.6.6 are regular according to the OCR
text; they were not read from images.

### 3.6 Splittings, frames, groups (II.7.1, II.9.1, II.9.2, II.10.1)

II.7.1.4 defines the *vector transformation rule* $`H_{u'u} := (\mathrm{id} \times
L(u, u'))\,(h_{u'}\,h_u^{-1})`$ from $`\mathbf{I} \times \mathbf{E}_u`$ to itself: take
the $`u'`$-components and carry the spatial one back to $`\mathbf{E}_u`$ by the boost.
With $`v = v_{u'u}`$ and $`\kappa = 1/\sqrt{1 - |v|^2}`$ (II.7.1.7),

```math
H_{u'u}(t, q) = \kappa\,\big(t - v \cdot q,\ -v\,t + D(v)\,q\big), \qquad D(v) = \frac{1}{\kappa}\Big(\mathrm{id} + \frac{\kappa^2}{\kappa + 1}\, v \otimes v\Big),
```

which for $`q`$ parallel to $`v`$ is the textbook Lorentz transformation (II.7.1.6). The
book separates two objects that the arithmetic model $`\mathbb{R}^{1+3}`$ lets one
confuse: a Lorentz transformation is a map $`\mathbf{M} \to \mathbf{M}`$; a
transformation rule is a map between component spaces. They are related by $`H_{u'u} =
h_u\, L(u, u')\, h_u^{-1}`$.

A *reference system* (II.9.1.1) is an observer, a simultaneity, and coordinatisations of
the resulting time and space; a *reference frame* is the coordinatisation of spacetime it
induces. A Lorentz reference frame is an origin with a positively oriented orthogonal
basis whose first vector is future timelike (II.9.2.2). So the order of construction is
model, observer, simultaneity, coordinates, the reverse of the textbook order.

II.10.1 defines the Lorentz group as $`\mathcal{O}(\mathbf{g})`$ with its four
components. II.10.1.4 notes that each $`u`$ has its own rotation group
$`\mathcal{O}(\mathbf{b}_u) = \{L : L u = u\}`$, that restriction to $`\mathbf{E}_u`$ is
not a homomorphism of the Lorentz group, and that there is consequently no "special
Lorentz group". II.10.1.5: for every orthochronous $`L`$ and every $`u`$,
$`R(L, u) := L(u, L u)\,L`$ lies in $`\mathcal{O}(\mathbf{b}_u)`$, so every Lorentz
transformation is a boost times a $`u`$-rotation; boosts are the counterpart of special
Galilean transformations but "do not form a subgroup".

---

## 4. Results

**MT1 (the relative velocity is the binary velocity).** Matolcsi's $`v_{u'u}`$ and the
binary velocity of MC1 are the same vector: `v_XY = Y/gamma_XY - X` with `X = u`,
`Y = u'`. So are their stated properties: orthogonality to the reference body, the
length $`1 - \gamma^{-2}`$, and non-reciprocity, for which an exact form is

```math
v_{u'u} + v_{uu'} = (u + u')\Big(\frac{1}{\gamma} - 1\Big), \qquad \gamma = -u \cdot u' .
```

(Exact, Part A.) Oziewicz credits the Lorentz-boost-free definition to Keres (1972) (*Many-body
mass-centre* §1.2.1) and the binary velocity field to Minkowski (abstract of *Relativity
groupoid*); the
book's own bibliography was read only in OCR text and no source for the formula was found
in it (MT-SP3).

**MT2 (the boost).** $`L(u', u)`$ of II.1.3.8 is $`\mathbf{g}`$-orthogonal with
determinant 1, sends $`u`$ to $`u'`$, fixes $`\mathbf{E}_u \cap \mathbf{E}_{u'}`$, and
sends $`v_{u'u}`$ to $`-v_{uu'}`$ (exact, Part B). The last statement is MC1, part 3, and
Theorem 8.1 (i) of Oziewicz's 2004 draft. Einstein's reciprocity is therefore, in
Matolcsi's account, a *convention for comparing two spaces* (II.5.1.1), neither a theorem
nor an error.

**MT3 (composition, and the rotation the book does not name).** The coplanarity criterion
of II.1.3.9 holds in the cases tried, in both directions (exact, Part C). For three
non-coplanar velocity values the defect

```math
W = L(u, u'')\,L(u'', u')\,L(u', u)
```

fixes $`u`$ and is a rotation of $`\mathbf{E}_u`$ about the normal to the plane of
$`v_{u'u}`$ and $`v_{u''u}`$. For speeds 3/5 and 4/5 at right angles its angle has
$`\cos = 35/37`$, which is the standard Thomas-Wigner value
$`(1 + \gamma_1 + \gamma_2 + \gamma_{12})^2 / ((1 + \gamma_1)(1 + \gamma_2)(1 +
\gamma_{12})) - 1`$. $`W`$ is $`R(L, u)`$ of II.10.1.5 for $`L = L(u'', u')\,L(u', u)`$.
The words "Thomas" and "Wigner" do not occur in the OCR text of the 1993 book; the
author's later papers name it (MT9). The
non-transitivity of II.5.1.2 is this rotation: carried round the triangle, a vector comes
back turned by $`W`$. This is the same fact as RV3, reached from the other side: RV3 fixes
one eagle and finds that Einstein's velocity depends on it; II.5.1.2 uses no eagle and
finds that pairwise identifications do not close.

**MT4 (the addition formula is groupoid composition).** The Proposition of II.4.3.2 holds
(exact, four triples, Part D), with the collinear case of II.4.3.3 for symbolic
$`\alpha`$. Three consecutive steps give $`v_{u'''u}`$ in either bracketing. That is not a
property of the formula: the formula computes $`v_{u''u}`$ from data that determine $`u'`$
and $`u''`$ given $`u`$, so the result depends only on the end points, which is MC2.
What II.4.3.3 adds is the precise statement of composability. To add $`v_{u''u'}`$ to
$`v_{u'u}`$ one also needs $`v_{uu'}`$, the same arrow read at its target; an arrow of
the groupoid is known only with both of its ends. Matolcsi has the composition and its
domain in 1993 and does not call it a groupoid. The second edition drops this form of the
formula and the remark of II.4.3.3 (MT10); Oziewicz (2004 draft; *Relativity
groupoid*, 2007) names the structure and denies that the boost has a place in it.

**MT5 (aberration).** The formula of II.4.7.3 holds with $`\theta'`$ measured from
$`-v_{uu'}`$ (exact, Part E). This agrees with point 6 of §6 in
[`velocity_draft.md`](velocity_draft.md), where Oziewicz asks why Matolcsi needs
$`\cos K \to -\cos K`$: the sign is the direction from which the angle is measured in
the second space. That item was written from Oziewicz's quotation; it is now checked
against the book.

**MT6 (regular observers and `α ∧ dα`).** Let $`\alpha = \mathbf{g}(U, \cdot)`$. A world
surface orthogonal to $`U`$ through every point is an integral manifold of
$`\mathrm{ker}\,\alpha`$, so by Frobenius's theorem $`U`$ is regular in the sense of
II.6.2.4 exactly when $`\alpha \wedge \mathrm{d}\alpha = 0`$, locally. That is the
condition of MF11 for a clock to have time scalars; the identification is this note's, the
book does not use differential forms. With $`\Omega`$ a rotation by $`\omega`$ in the
$`x y`$-plane (symbolic, Part H):

```math
(\alpha \wedge \mathrm{d}\alpha)_{txy} = -\frac{\omega\,(\omega^2 r^2 + 2)}{\sqrt{1 + \omega^2 r^2}} \ \ (U_\mathrm{I}), \qquad (\alpha \wedge \mathrm{d}\alpha)_{txy} = \frac{2\omega}{\omega^2 r^2 - 1} \ \ (U_\mathrm{II}), \qquad r^2 = x^2 + y^2 ,
```

neither of which vanishes anywhere, so neither observer is regular, as the book says.
$`U_\mathrm{II}`$ has vanishing projected symmetric gradient (Born rigid) and
$`U_\mathrm{I}`$ does not, as the book says. $`U_\mathrm{II}`$ is the rotating disk of
MF9 and MF10, `X = ∂_t + w ∂_φ` normalised. Matolcsi's verdict on it, "no natural time,
only artificial ones", is MF11, part 3, in other words.

**MT7 (what the book does with the Lorentz group).** It keeps it, as the automorphism
group of the model's vector structure, and uses the boost in three places only: to
compare vectors of two observer spaces (II.5.1.1), to define transformation rules
(II.7.1.4), and to decompose a Lorentz transformation (II.10.1.5). In each place it is
introduced as a choice ("we agreed", "handsome"). The formulas of II.7.1.7 and II.7.1.6
hold (exact, Part G).

---

## 5. Matolcsi and Oziewicz

**What they share.** No observer is built into the theory; each body or observer has its
own space; a relative velocity belongs to an ordered pair and lives in the space of the
first; mutual velocities are not opposite; velocities add only along a chain. On these
points *Relativity groupoid* and *Many-body mass-centre* restate, in another language,
what is in II.1.3, II.4.2 and II.4.3. *Mass-centre* cites the book; *Relativity groupoid* cites Matolcsi and Goher (2001).

**Where they part.**

1. *The boost.* For Matolcsi the boost $`L(u', u)`$ is the natural identification of two
   rest spaces and reciprocity is the convention it expresses; its price is the
   non-transitivity of II.5.1.2, which he accepts. For Oziewicz the identification is
   illegitimate and reciprocity is a false axiom (*Mass-centre* (1.2.2)). On the
   mathematics they agree (MT2, MC1). They differ on whether a convention with that
   price should be made at all.
2. *The Lorentz group.* Matolcsi shows what it does not contain (no boost subgroup, no
   distinguished rotation subgroup) and keeps it. Oziewicz concludes it "should be
   rejected". MC2 found that Oziewicz's own metric postulates fix the group; the book
   reaches the same position from the start, since its model *is* a Lorentz form.
3. *What is primitive.* Matolcsi starts from spacetime with a light cone and derives
   observers. Oziewicz starts from bodies and wants spacetime last. Step 3 (MF4) showed
   that reciprocity of clocks returns the metric, so on this point the two orders of
   construction meet.
4. *Time.* Matolcsi's regular observer and the condition `ζ ∧ dζ = 0` that *Mass-centre*
   (2.1.17) puts on the clock of the mass centre are the same condition (MT6). Matolcsi gives the non-regular case a positive treatment (artificial
   simultaneities, II.6.2.2); Oziewicz's papers do not.
5. *Algebra.* The idempotents, the algebra of observers and the Frölicher-Nijenhuis
   bracket are Oziewicz's; nothing like them is in the sections read.

**Oziewicz on Matolcsi.** In the 2009 talk (`talks/npa2009/notes/slide_50.md`) Oziewicz
says that Matolcsi discusses the non-opposite inverse velocity in his book "but he also
does not understand why it is so". The book's stated reason (II.4.2.3) is that spaces of
different inertial observers are affine spaces over different vector spaces. That is the
reason step 1 gives. If Oziewicz meant that the deeper reason is the groupoid, MT4 shows
the book has its content; if he meant that reciprocity is false and not conventional,
that is point 1, a disagreement and not a gap in understanding. This is a reading of one
spoken sentence. By 2009 Matolcsi had also published three papers on the Thomas rotation
(MT9), and his page lists Oziewicz's "The Lorentz boost-link is not unique" (2006) among
related work, so each knew of the other's.

*Analogy.* Each observer has a private map. Matolcsi says: to compare your map with mine,
slide one onto the other the shortest way, and accept that three maps compared in pairs
do not agree round the triangle, as on a sphere. Oziewicz says: do not slide maps; record
only how each map draws each other traveller.

---

## 6. Open items

- **MT-SP1.** Sections not read: the rest of II.1.4 to II.1.6, II.2 (world lines), II.6.4 to II.6.6
  (accelerated observers) from images, II.8, II.9.4, II.10.2 to II.10.7 (the
  $`u`$-split and Poincaré groups), II.11 (the non-relativistic limit), III, and all of
  chapter I. Chapter I matters if the Galilean and relativistic constructions are to be
  set side by side.
- **MT-SP2.** Answered by MT9: Matolcsi and Gohér (2001) was read. Still unread:
  Matolcsi and Gohér (1996), Matolcsi and Matolcsi (2005) on Thomas rotation and
  precession, and Matolcsi (1998) on synchronizations of the rotating disk, which bears
  on MT6 and MF11.
- **MT-SP3.** Sources (the 1984 book is on the author's page as a scan): whether the 1984 edition already has $`v_{u'u}`$ and II.4.3.2,
  and what the book's "Comments and bibliography" says of earlier work. The relation to
  Keres (1972), whom Oziewicz credits, is open (see MF-SP5).
- **MT-SP4.** Matolcsi's observer space $`\mathrm{E}_U`$ (the set of $`U`$-lines) against
  the basic algebra of MF9: the first is a set of leaves, the second the functions
  constant on them. Are the distances of II.6.3.3 on a non-regular rigid observer the
  quotient metric of the disk, and does II.6.8.6 give the known non-Euclidean geometry?
- **MT-SP5.** Answered in §8.1, except whether a 1994 printing exists. The author's page
  gives 1993 and 411 pages.
- **MT-SP7.** The second edition was compared with the first only in II.3, II.4.2, II.4.3,
  II.4.7, II.4.8, II.5.1 and the bibliography. A full comparison, and the reading of II.6
  from the second edition (clean text, new section 6.1), is the next pass.
- **MT-SP8.** Does Oziewicz say anywhere that the size of the binary velocity depends on
  the choice of clock, as MF2 and MT8 find, or that his clock form is a synchronization
  (MT11)? Bill Page does not recall it and will look in other documents; candidates are
  the Oziewicz and Page manuscript *The Many Relative Spaces of Galileo and Poincaré*,
  *Relative velocity: a dichotomy* (2010) and the "Zero" drafts.
- **MT-SP9.** MT12 against the literature on absolute synchronization (Tangherlini 1961;
  Selleri 1997; Matolcsi 1998), none of it read. Is MT12 there, and does it extend to
  non-inertial bodies, where a shared clock needs `α ∧ dα = 0`?
- **MT-SP6.** The coplanarity criterion (II.1.3.9) and the general form of $`W`$ in MT3
  were checked on instances, not proved symbolically.

---

## 7. Verification

`PYTHONPATH=src python3 -u src/verify_matolcsi.py` (SymPy, exact; writes no files). 55
checks, all pass.

| Part | Sections | What is checked | Kind |
|---|---|---|---|
| A | II.1.3.7, II.4.2 | relative velocity, its length, non-reciprocity, II.4.2.4, equality with `binary` of `verify_relative_velocity.py` | rational, 5 pairs |
| B | II.1.3.8 | the boost: orthogonal, det 1, (ii) to (iv) | rational, 5 pairs |
| C | II.1.3.9, II.5.1.2, II.10.1.5 | composition, the rotation $`W`$, 35/37, non-transitivity, $`R(L, u)`$ | rational instances |
| D | II.4.3 | addition formula, auxiliary formula, over-length sum, collinear case, bracketings | rational; $`\alpha`$ symbolic |
| E | II.4.7 | light speed 1 for every $`u`$, aberration | rational |
| F | II.5.2, II.5.3 | observed vectors, contraction | rational |
| G | II.7.1 | transformation rule, $`D(v)`$, Lorentz transformation | $`t`$, $`\lambda`$ symbolic |
| H | II.6.2.4, II.6.7, II.6.8 | `α ∧ dα` and rigidity of the two rotating observers | symbolic |
| J | §9; 2018 II.4.8.1 | an observer `T ⊗ τ` as a reference frame; shared clock form | rational |
| I | 2018 II.4.3.2, II.4.8; Gohér (35), (42), (46) | boosted addition formula, angle of the Thomas rotation, nonstandard synchronization, the two misprints | rational; $`v_s`$ symbolic |

No formula read from the first edition failed. One check failed on the first run because of the
example chosen for it (two velocities that partly cancel were used to show that a sum can
exceed 1); the example was replaced.

## 8. The second edition, and Matolcsi and Gohér (2001)

### 8.1 Editions and the copy read

The author's page at the Wigner Research Centre,
[wigner.hu/s/matolcsi](https://wigner.hu/s/matolcsi/), lists (read 12 November 2026):

| Year | Title, publisher | Remarks |
|---|---|---|
| 1984 | *A Concept of Mathematical Physics: Models for SpaceTime*, Akadémiai Kiadó, 236 p. | scan on the page; not read |
| 1993 | *Spacetime Without Reference Frames*, Akadémiai Kiadó, 411 p. | "revised reprint of the 1984 original"; file on the page |
| 2018 | the same title, Society for the Unity of Science and Technology, Budapest, ISBN 978-615-80157-3-8, 394 p. | "2nd, revised edition", edited by T. Fülöp and Á. Szabó; **CC BY 4.0** |
| 2020 | the same title, "2nd edition", Minkowski Institute Press, 396 p. | the page gives the 2018 file for it; not seen |

The file the page offers for 1993 is named `spacetime.pdf` but is a PostScript file
(dvips 5.86), 2 194 869 bytes. It is byte-for-byte identical to `matolcsi.ps` kept by Bill
Page beside the PDF read here (compared with `cmp`), and that PDF reports the same dvips
as its source. So the copy read in §§1 to 7 is the author-side distribution of the first
edition. The page states no licence for it. The year 1994 in Oziewicz's reference lists
is not supported by the title page, the copyright page, or the author's page.

### 8.2 What the second edition changes in chapter II

Read from the PDF's text layer, with the two displays quoted below checked on page images.
Not a full comparison (MT-SP7).

1. **Observer and synchronization are separated.** Chapter II.3 is now "Observers and
   synchronizations". A synchronization is defined on its own (new II.3.2.1) as a smooth
   equivalence relation with spacelike classes; a *reference frame* is a pair
   (synchronization, observer) (II.3.2.3); an *inertial reference frame* $`(u_s, u)`$ pairs
   the observer $`u`$ with the hyperplanes orthogonal to any $`u_s`$ (II.3.4.2); it is
   *standard* when $`u_s = u`$ (II.3.5.1). In 1993 the time of an inertial observer was
   simply the radar one. The second edition calls the textbook argument for it "a vicious
   circle", since a light speed presupposes a synchronization, and proves instead: the
   one-way speed of light equals the two-way speed only in standard inertial frames
   (II.3.5.2, II.3.5.3).
2. **The relative velocity is renamed.** $`v_{u'u}`$ has the same definition and is now
   the *standard* relative velocity (II.4.2.2). New II.4.8 gives the velocity of $`u'`$
   in a nonstandard frame $`(u_s, u)`$.
3. **The addition formula is replaced** (II.4.3.2; MT10).
4. **Renumbering and notation.** The general material on simultaneities moves from II.6.2
   to II.3.2, so II.6.3 to II.6.9 of 1993 become II.6.2 to II.6.8; the rotating observers
   are II.6.6 and II.6.7. $`\mathbf{E}_u`$ becomes $`\mathbf{S}_u`$, $`\mathbf{I}`$
   becomes $`\mathbb{T}`$, the splitting $`h_u`$ becomes $`\xi_u`$. "Reference system"
   and "reference frame" exchange roles: chapter II.9 is "Reference systems". Some
   cross-references still use the old numbers (II.3.2.4 cites "6.7.6").
5. **Unchanged** in the sections compared: II.4.2.2 to II.4.2.5, the non-reciprocity and
   its stated reason; II.5.1, physical equality and its non-transitivity, with the word
   "standard" added; II.4.7.3, aberration; the definition of a regular observer.
6. **Bibliography.** Entries [32] to [37] and after list work "based on the present
   theory" since 1993, among them the papers of MT9.

### 8.3 Results from the second edition and the paper

**MT8 (the binary velocity belongs to a synchronization).** For the observer $`u`$ with
the synchronization of $`u_s`$, new II.4.8.1 gives

```math
v_{u'(u_s, u)} = v_{u'u}\,\frac{(-u \cdot u')(-u_s \cdot u)}{-u_s \cdot u'} ,
```

a positive multiple of the standard velocity (exact, Part I). So the direction of a
relative velocity belongs to the pair of bodies, and its size to the pair together with
a synchronization. That is MF2 ("the direction of a relative velocity needs no clock, and
its size does"), reached by Matolcsi inside the metric theory. Matolcsi and Gohér say it
in a footnote to their definition: the relative velocity "concerns the standard
synchronisation". The consequence for this repository: the binary velocity of MC1 is the
*standard* one. Oziewicz's formula hides a choice of synchronization in the clock
$`-\mathbf{g}(X, \cdot)`$ exactly as the textbook formula hides one in its coordinates.
Whether his texts say so is a question for a later pass (MT-SP8).

For light with direction $`n_w`$ in the space of $`u`$, and
$`u_s = (u + v_s n_s)/\sqrt{1 - v_s^2}`$, the factor is $`1/(1 - v_s\, n_s \cdot n_w)`$ (symbolic, Part I), with
extremes $`1/(1 + v_s)`$ and $`1/(1 - v_s)`$ as II.4.8.2 says. The last display of
II.4.8.2 prints the factor as $`(1 - v_s\, n_s \cdot n_w)/\sqrt{1 - v_s^2}`$, which is
$`-u_s \cdot w`$ and not the factor: a misprint, inconsistent with the line above it and
with the extremes stated below it.

**MT9 (Matolcsi and Gohér 2001).** The paper restates II.1.3 and II.5.1 of the book,
gives a physical procedure with light signals that realises "physical equality"
(its Proposition 1 and Definition 1), and then names what the book left unnamed. Its
$`R_u(u', u'') := B(u, u'')\,B(u'', u')\,B(u', u)`$ is the $`W`$ of MT3, called "the
Thomas rotation of $`u`$ corresponding to $`u'`$ and $`u''`$" (Definition 2), and the
paper says in so many words that it measures the deviation of physical equality from
being transitive, and that it "corresponds to no real rotation". With $`a = -u' \cdot
u`$, $`b = -u'' \cdot u'`$, $`c = -u'' \cdot u`$, its equation (42) is

```math
\cos\varepsilon = 1 - \frac{1 + 2abc - (a^2 + b^2 + c^2)}{(1 + a)(1 + b)(1 + c)} ,
```

which holds for the four triples tried (exact, from the trace of $`W`$, Part I) and gives
35/37 for the example of MT3. The paper's diagnosis of Mocanu's velocity addition paradox
is that coordinate treatments boost every space vector into the space of an observer
"hidden in the coordinates", and so assume tacitly that physical equality is transitive.
The hidden observer is the eagle of RV3, and the diagnosis is that of
[`bodies_first.md`](bodies_first.md) §3. Matolcsi and Gohér had it in 2001; RV3 should
cite them.

**MT10 (two addition formulas).** The paper's (46), and the second edition's II.4.3.2,
use $`v = v_{u'u}`$ and $`v' = L(u, u')\,v_{u''u'}`$, the second velocity *boosted into*
$`\mathbf{E}_u`$, with $`\alpha = -u' \cdot u`$, $`\beta = -u'' \cdot u'`$, $`\gamma = -u''
\cdot u = \alpha\beta(1 + v \cdot v')`$:

```math
v_{u''u} = \frac{\alpha(\beta + \gamma)}{\gamma(1 + \alpha)}\, v + \frac{\beta}{\gamma}\, v' .
```

This holds (exact, four triples, Part I). The second edition prints it with the two
coefficients exchanged, $`(\beta/\gamma)\,v + \ldots\,v'`$; that form fails for three of
the four triples and fails the trivial case $`u'' = u'`$, where it gives $`v/\alpha`$
instead of $`v`$: a misprint. (It holds when $`\beta = \alpha\gamma`$, which one of the
four triples happens to satisfy.)

The two editions therefore state composition differently. The 1993 formula takes
$`v_{u''u'}`$ where it lives, in $`\mathbf{E}_{u'}`$, and needs $`v_{uu'}`$ beside
$`v_{u'u}`$ to connect the two spaces; no boost appears. The 2001 and 2018 formula
carries $`v_{u''u'}`$ into $`\mathbf{E}_u`$ by the boost first. The first is the form
closer to Oziewicz's groupoid (MT4), and it is the form the author gave up. The 1993
remark "(but this is impossible!)" on substituting $`-v`$ for $`v_{uu'}`$ is gone from
the second edition's II.4.3.3.

### 8.4 What this changes in §5

Point 1 of §5 stands and is sharpened. From 1996 on, Matolcsi makes the boost a
*physical procedure* (light signals between the two spaces), and from 2018 he separates
out a second convention, the synchronization, which the first edition had built into the
inertial observer. So Matolcsi's later position has two explicit conventions: standard
synchronization, and physical equality by boost. Oziewicz rejects the second (the boost
has no place in the groupoid). On the first, the earlier version of this section said he
rejects simultaneity as part of a body; that was wrong, and §9 replaces it: his observer
carries a clock form, which is a synchronization, and his metric postulate fixes it to be
the standard one.

## 9. Oziewicz's clock is a synchronization

Bill Page's question, 12 November 2026: what do Oziewicz's ideas imply for
synchronization, given that his "clock" may not be Matolcsi's? This section answers for
the inertial case only, from formulas already in this repository; what Oziewicz himself
wrote on synchronization has not been searched (MT-SP8).

**MT11 (an observer is a reference frame).** In *Relativity groupoid* an observer is a
rank-one idempotent $`p = T_p \otimes \tau_p`$ with $`\tau_p(T_p) = 1`$ (its eq. (14), as
read in step 3, MF0, and in the Project note `response_sobczyk_cruz.md`; not re-read
today). The kernel of $`\tau_p`$ is a hyperplane, and the hyperplanes parallel to it are
the classes of an affine synchronization in the sense of the second edition's II.3.4.1.
So $`p`$ is one of Matolcsi's inertial reference frames $`(u_s, u)`$: $`T_p`$ is parallel
to $`u`$, and $`\tau_p = -\mathbf{g}(u_s, \cdot)/(-u_s \cdot u)`$. The velocities agree:

```math
\frac{T_q}{\tau_p(T_q)} - T_p \ \in\ \mathrm{ker}\,\tau_p \qquad\text{and}\qquad v_{u'(u_s, u)} \ \in\ \mathbf{S}_u
```

differ by a multiple of $`u`$, so they are the same element of the quotient
$`\mathbf{M}/\langle u \rangle`$, which is the vector space of the observer's space.
Oziewicz represents that quotient by the kernel of the clock, Matolcsi by the orthogonal
complement of $`u`$; the two coincide exactly when $`u_s = u`$, and then both are the
standard $`v_{u'u}`$. (Exact, Part J.)

Three consequences.

1. *The clock is the synchronization, and more.* A clock form holds two things: its
   kernel (which occurrences are simultaneous) and its normalisation (a rate). Matolcsi's
   synchronization is the kernel alone; he takes the rate from the proper time of $`u`$.
   So "clock" in *Mass-centre* is a richer notion, as Bill Page suspected, but it contains
   a synchronization and cannot be had without one.
2. *Reciprocity of clocks is the standard synchronization.* Postulate 1.6.3 of
   *Mass-centre*, and (6), (7) of *Relativity groupoid*, force $`\tau_p = -\mathbf{g}(T_p,
   \cdot)`$ (MF4), which is $`u_s = u`$. So Oziewicz's metric theory uses Einstein's
   synchronization for every body, by postulate. By the second edition's II.3.5.3 that is
   the synchronization in which one-way and two-way light speeds agree. He rejects
   Einstein's reciprocity of velocities and keeps Einstein's synchronization; MF4 said
   this in the words "postulates a reciprocity of clocks".
3. *The size of the binary velocity is conventional to the same extent.* MT8 and MF2.
   The non-reciprocity $`v_{YX} \ne -v_{XY}`$ survives every choice, because the two
   vectors lie in different quotients.

**MT12 (a shared clock is an absolute synchronization).** Let all observers use one clock
form, $`\tau = -\mathbf{g}(u_s, \cdot)`$ for one fixed $`u_s`$, each normalised by
$`\tau(T_i) = 1`$. Then every relative velocity is $`T_j - T_i`$; all of them lie in the
one vector space $`\mathbf{E}_{u_s}`$; they add, $`v_{ij} + v_{jk} = v_{ik}`$; they are
reciprocal; and $`\Gamma_{ij} = 1`$ for all pairs (exact, Part J). This is the "Galilean
algebra" of *Relativity groupoid* §8 (all observers share a clock form, $`qp = q`$), and
it is the structure of Matolcsi's chapter I, a single $`\tau`$ and a single $`\mathbf{E}`$.
But here it sits inside Minkowski spacetime: the bodies and the light cone are unchanged,
and only the bookkeeping differs. In the literature on conventionality of simultaneity
this is the absolute (Tangherlini, Selleri) synchronization; Matolcsi and Gohér cite
Selleri (1997) for the light-speed paradox it leads to. That attribution is from memory
and from their reference list, not checked (MT-SP9).

So the contrast Oziewicz draws between the Galilean algebra and the relativity groupoid
is, kinematically, a contrast between two synchronization conventions for the same
bodies: one clock for all, or each body its own metric clock. What the shared clock gives
up is that $`T_i`$ is no longer the unit of proper time of body $`i`$, and MF6 shows the
price: with $`\Gamma = 1`$ the form reconstructed from the clocks is $`\tau \otimes
\tau`$, degenerate, so the clocks alone no longer return the metric. Whether Oziewicz saw
his §8 as a re-description of relativity or only as its contrast is a question for his
texts (MT-SP8).

*Analogy.* A railway may run every station clock on the capital's time, or each on its
own noon. The trains are the same; the timetables differ. With capital time, journey
times add along a line and "the same time" means one thing everywhere, but no station's
clock agrees with its own sun. Oziewicz's metric postulate is local noon for every
station; his Galilean algebra is capital time.

---

## References

- T. Matolcsi, *Spacetime Without Reference Frames* (Akadémiai Kiadó, Budapest 1993),
  ISBN 963 05 6433 5. Second, revised edition: Society for the Unity of Science and
  Technology, Budapest 2018, ISBN 978-615-80157-3-8, CC BY 4.0,
  [PDF](https://wigner.hu/s/matolcsi/old/pdf/konyv/Matolcsi_Spacetime_without_Reference_Frames_2018-07-31.pdf).
  Author's page: [wigner.hu/s/matolcsi](https://wigner.hu/s/matolcsi/).
- T. Matolcsi and A. Gohér, "Spacetime without reference frames: an application to the
  velocity addition paradox", *Stud. Hist. Phil. Mod. Phys.* 32 (2001) 83-99,
  [author's copy](https://wigner.hu/s/matolcsi/old/pdf/cikk/veladd.pdf). Read in full from
  its text layer; equations (35), (42), (46) checked.
- T. Matolcsi and T. Gruber, "Spacetime without reference frames: an application to the
  kinetic theory", *Int. J. Theor. Phys.* 35 (1996) 1523-1539. Seen; Galilean, not used
  here.
- Z. Oziewicz, "Relativity groupoid, instead of relativity group", *Int. J. Geom. Methods
  Mod. Phys.* 4 (2007), [arXiv:math/0608770](https://arxiv.org/abs/math/0608770).
- Z. Oziewicz, *Many-body mass-centre* (2014); see `references/bibliography.md`.
- This repository: [`analysis/mass_centre.md`](../analysis/mass_centre.md) (MC),
  [`analysis/metric_free_body.md`](../analysis/metric_free_body.md) (MF),
  [`bodies_first.md`](bodies_first.md) (RV), [`velocity_draft.md`](velocity_draft.md).
