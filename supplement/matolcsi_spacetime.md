# Matolcsi's *Spacetime Without Reference Frames*: the special relativistic part

> A reading of chapter II (special relativistic spacetime models) of the book Oziewicz cited as the reference-frame-free account of relativity. Matolcsi's relative velocity of 1993 is, symbol for symbol, the binary velocity of step 1 (MT1). The book has its non-reciprocity, the boost that carries one mutual velocity to minus the other (MT2), and an addition formula that needs both mutual velocities of the middle pair, which is composition in the pair groupoid without the name (MT4). Boosts compose to a boost only for coplanar velocity values; the defect is the Thomas-Wigner rotation, which the book derives but does not name, and it makes "physically equal" vectors in different observer spaces a non-transitive relation (MT3). Its "regular observer" is the condition `α ∧ dα = 0` of step 3, and of its two rotating observers one is rigid, neither is regular (MT6). The book keeps the Lorentz group and says what it cannot do: boosts are not a subgroup and no rotation subgroup is singled out (MT7). Forty exact checks pass; no formula read from the book failed.

**Status.** Supplement (a reading of a published book, not a ladder step). Companion
script: [`src/verify_matolcsi.py`](../src/verify_matolcsi.py). Requested by Bill Page,
12 November 2026. The book is copyrighted and is not committed here. **Every statement of
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
(II.4.2.3), the year should read 1993. Nothing else is retracted.

---

## 1. The book and what was read

T. Matolcsi, *Spacetime Without Reference Frames*, Akadémiai Kiadó, Budapest, 1993,
ISBN 963 05 6433 5. Its copyright page says it is the revised and enlarged version of
*A Concept of Mathematical Physics: Models for Space-Time* (Akadémiai Kiadó, 1984), which
was not seen. Oziewicz's reference lists give the year as 1994 with the same ISBN.

The copy read is a 396-page PDF made from TeX. It prints **no page numbers**, and the
numbers in its table of contents run ahead of the PDF pages (by about 3 in Part One, about
6 in Part Two), so it is probably the author's own file and not the printed layout
(MT-SP5). This note therefore cites by section number only.

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
The words "Thomas" and "Wigner" do not occur in the OCR text of the book. The
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
domain in 1993 and does not call it a groupoid; Oziewicz (2004 draft; *Relativity
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
spoken sentence.

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
- **MT-SP2.** T. Matolcsi and A. Goher, "Spacetime without reference frames: an
  application to the velocity addition paradox", *Stud. Hist. Phil. Mod. Phys.* 32
  (2001) 83-99, cited by Oziewicz, is where the Thomas rotation is presumably treated by
  name. Not read.
- **MT-SP3.** Sources: whether the 1984 edition already has $`v_{u'u}`$ and II.4.3.2,
  and what the book's "Comments and bibliography" says of earlier work. The relation to
  Keres (1972), whom Oziewicz credits, is open (see MF-SP5).
- **MT-SP4.** Matolcsi's observer space $`\mathrm{E}_U`$ (the set of $`U`$-lines) against
  the basic algebra of MF9: the first is a set of leaves, the second the functions
  constant on them. Are the distances of II.6.3.3 on a non-regular rigid observer the
  quotient metric of the disk, and does II.6.8.6 give the known non-Euclidean geometry?
- **MT-SP5.** Provenance of the PDF and the year. *Mass-centre* (2014) gives a link to a
  copy on a former page of Bill Page's; whether the file is the author's distribution,
  and whether a 1994 printing exists, is not known.
- **MT-SP6.** The coplanarity criterion (II.1.3.9) and the general form of $`W`$ in MT3
  were checked on instances, not proved symbolically.

---

## 7. Verification

`PYTHONPATH=src python3 -u src/verify_matolcsi.py` (SymPy, exact; writes no files). Forty
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

No formula read from the book failed. One check failed on the first run because of the
example chosen for it (two velocities that partly cancel were used to show that a sum can
exceed 1); the example was replaced.

---

## References

- T. Matolcsi, *Spacetime Without Reference Frames* (Akadémiai Kiadó, Budapest 1993),
  ISBN 963 05 6433 5.
- T. Matolcsi and T. Gruber, "Spacetime without reference frames: an application to the
  kinetic theory", *Int. J. Theor. Phys.* 35 (1996) 1523-1539. Seen; Galilean, not used
  here.
- Z. Oziewicz, "Relativity groupoid, instead of relativity group", *Int. J. Geom. Methods
  Mod. Phys.* 4 (2007), [arXiv:math/0608770](https://arxiv.org/abs/math/0608770).
- Z. Oziewicz, *Many-body mass-centre* (2014); see `references/bibliography.md`.
- This repository: [`analysis/mass_centre.md`](../analysis/mass_centre.md) (MC),
  [`analysis/metric_free_body.md`](../analysis/metric_free_body.md) (MF),
  [`bodies_first.md`](bodies_first.md) (RV), [`velocity_draft.md`](velocity_draft.md).
