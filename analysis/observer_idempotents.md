# Observers as idempotents of the spacetime algebra: the orientation groupoid and the Wigner rotation

> Oziewicz (2007, §4) makes every body an idempotent of an associative algebra, and step 1 realised it as the rank-one projector $`X \otimes \mathrm{clock}_X`$ (MC6). This note represents the same bodies in the spacetime algebra $`A = \mathrm{Cl}(V, -g) \cong M_2(\mathbb H)`$, where a body squares to 1, and asks what products of the idempotents $`e_X = (1 + X)/2`$ contain. **Lemma OI1**: $`e_X Y e_X = \gamma_{XY} e_X`$, and the corner $`e_X A e_X`$ is a quaternion algebra, the spin of the rest space of $`X`$. **Proposition OI2**: $`e_Y e_X = \cosh(r/2)\, L_{YX} e_X`$, with $`L_{YX}`$ the boost of MC1 and $`r`$ the rapidity. **Theorem OI3**: round a triangle, $`e_X e_Z e_Y e_X = \tfrac18 (1 + XZ)(1 + ZY)(1 + YX)\, e_X`$, which is the product of the three $`\cosh(r/2)`$ times $`H e_X`$, with $`H`$ the Thomas-Wigner rotation of the boost loop, and $`\tan(\theta/2) = \sqrt{\det G}/(1 + \gamma_{XY} + \gamma_{YZ} + \gamma_{ZX})`$ with $`\det G`$ the polynomial of TV8. On step 2's example it gives TV7's $`\cos\theta = 25109/29341`$ exactly. The product $`(1 + XZ)(1 + ZY)(1 + YX)`$, its scalar part and the angle formula are Urbantke's (1990; Chruściel and Urbantke 2025), the formula is Macfarlane's (1962) and the hyperbolic Heron formula, and the equality of angle and area is Aravind's (1997); what is new, as far as the search found, is that the loop product of observer idempotents assembles Urbantke's product without square roots, for triangles and, path-ordered, for any polygon. In the notation of Baylis and Sobczyk (2004), OI2 is the idempotent form of their $`L^2 = u_B u_A`$, and OI3 is their polar decomposition $`L = BR`$ relative to the observer, with the Wigner rotation as the unitary factor. **Proposition OI4**: the corners $`e_Y A e_X`$ are 4-dimensional, and their unit elements form the gauge groupoid with isotropy $`\mathrm{Spin}(3)`$, the orientation groupoid asked for in TV-SP1, which is answered in part. The boost is a covariant section that fails to compose by exactly $`H`$, as TV6 requires. **Proposition OI5**: rank-one projectors of $`\mathrm{End}(V)`$ have 1-dimensional corners, which is what Oziewicz's postulate (8) demands, and real loops, so the algebra of MC6 carries only the pair groupoid, and $`\mathrm{Cl}(V, g)`$ has no idempotent of this kind. The representation decides whether the algebra of observers sees the rotation. Checked exactly with SymPy; the triangle also numerically. No new prediction.

*Ladder abstract — see the [full list](README.md#the-ladder).*

**Status.** Analysis note, step 5 of the ladder. Theorem prefix **OI**. Companion
script: [`src/verify_observer_idempotents.py`](../src/verify_observer_idempotents.py)
(Parts A to H; §11). Prompted by Bill Page, 20 November 2026: a correspondence on
null-vector models of observers asked whether observers as idempotents can compute a
non-collinear composition and its Wigner rotation from products alone. Derivation and
checks were drafted with Claude (Anthropic) and are subject to review, and no separate
reader has checked them; every claim about what a paper says is a reading of the cited
page.
[PDF](https://github.com/billpage/oziewicz/releases/latest/download/observer_idempotents.pdf)

---

## 0. What this note asks, inherits and retracts

**Question.** Oziewicz's bodies are idempotents. In which algebra do products of
idempotents carry the binary boost, the composition of boosts and the Wigner rotation,
and in which do they carry only a number?

**Inherits.** From step 1: the gamma factor and binary velocity MC0, MC1, the pair
groupoid MC2, the idempotent MC6. From step 2: the no-go theorem TV6, the rotation of
TV7 and its example, the polynomial $`\det G`$ of TV8, and the open item TV-SP1.

**Retracts or corrects.** Nothing. Two earlier statements are sharpened:

| Earlier statement | What happens to it |
|---|---|
| `ternary_mass_centre.md` TV8: for three bodies "the rotation is non-zero" is one condition with $`\det G \ne 0`$ | Made quantitative: $`\tan(\theta/2) = \sqrt{\det G}/(1 + \gamma_{XY} + \gamma_{YZ} + \gamma_{ZX})`$ (OI3) |
| `ternary_mass_centre.md` TV-SP1: does the orientation groupoid sit inside the algebra of observers? | Answered in part. It sits in the spacetime algebra as corners of the observer idempotents (OI4), and not in the algebra of MC6 (OI5). The element $`[[a, b], [b, c]]`$ is not taken up |

---

## 1. Sources

- Oziewicz (2007), §4, "Relativity Groupoid is an Algebra": the span of bodies and binary velocities is postulated to be an associative algebra in which every body is an idempotent, splitting vectors into space and time, eq. (4). Read in the arXiv v2 text.
- Hestenes (1966; 1974) for the spacetime algebra, the space-time split $`YX = (Y \cdot X) + Y \wedge X`$ and rotors.
- The idempotent $`(1 + \gamma_0)/2`$ is the standard primitive idempotent of $`\mathrm{Cl}(1, 3) \cong M_2(\mathbb H)`$; da Rocha and Vaz (2004) use it to build that isomorphism.
- Macfarlane (1962), as cited by Urbantke (1990), for the closed form of the Wigner angle, and the hyperbolic Heron formula (Glasgow notes) for the area of a triangle from the cosh of its sides.
- Urbantke (1990), read in full in its preprint form (UWThPh 1988-39). §2 proves that Fermi-Walker transport of a vector orthogonal to the world line is Levi-Civita transport, along the hodograph, on the velocity pseudosphere; the proof takes parallel transport in the embedding space followed by orthogonal projection, in infinitesimal steps, which is the method of Part G. Along a geodesic of velocity space this transport is the boost that carries $`u`$ to $`u'`$. §3 computes the Thomas-Wigner rotation of a geodesic triangle as the product of three boost rotors $`S = (e + u'u)/\sqrt{2(1 + (u', u))}`$, built as products of two reflections, in the Clifford algebra with $`(u, u) = +1`$, the $`A`$ of OI0. The product of the numerators has scalar part $`2(1 + (u, u'') + (u'', u') + (u', u))`$ (his eq. (5)), which gives $`\cos(\alpha/2)`$ (his last formula, "essentially Mc Farlane's"). That is the $`\Lambda`$ of OI3.
- Chruściel and Urbantke (2025), read in full (v1): a pedagogical expansion of Urbantke's §3 in the signature $`(-, +, \dots, +)`$, that is in $`\mathrm{Cl}(V, g)`$, where $`u^2 = -1`$. The boost is the product of the reflections in $`u`$ and $`u + v`$ (Prop. 4.2), with rotor proportional to $`-1 + vu = (u + v)u`$; their $`r`$ and $`|r|^2 = 2^3 \prod (1 + \gamma)`$ (eqs. (7.1)-(7.12)) are $`\Lambda`$ and $`\Lambda \tilde\Lambda`$ here, and eq. (7.20) is Macfarlane's formula.
- Aravind (1997), read in full. With the cosh and sinh rules of hyperbolic trigonometry alone, and the Lobachevskian metric of rapidity space (taken from Landau and Lifshitz), he shows that the Wigner angle of two composed boosts is the negative of the area of their rapidity triangle, and calls it an anholonomy, a geometric phase; his eq. (2) gives $`\tan(\Omega/2)`$ from two sides and the included angle. He extends this to polygons by triangulation, and notes that for a loop that is not planar the triangles' rotations must be combined as rotations, not added as areas. He credits the description by the Levi-Civita connection and holonomy to Urbantke (1990), read here (next item), and the infinitesimal case to Jordan (1988), which was not.
- Baylis and Sobczyk (2004), read in full: relativity in the spacetime algebra $`\mathrm{Cl}_{1,3}`$, which is the $`A`$ of OI0 with the same signature, and in the algebra of physical space $`\mathrm{Cl}_3 \cong \mathrm{STA}^+`$; the observer-dependent conjugation; the factorisation $`L = BR`$; absolute and relative APS. It uses no idempotents, groupoids or Wigner angle; §6.3 translates this note into its notation.
- Bargmann (1964) and Mukunda and Simon (1993) for the three-vertex invariant $`\mathrm{tr}(P_1 P_2 P_3)`$, whose phase is a geometric phase; Lévay (2004) for Thomas rotations as Uhlmann's parallel transport of qubit density matrices.

The literature search was short (about a dozen queries, 20 November 2026). It did not
find the identity of OI3 written as a product of observer idempotents, or the corners
of OI4 used as a groupoid of observers. Both may be in the literature; see OI-SP5.

---

## 2. Setting

**Definition OI0.** $`V`$ is Minkowski space with $`g`$ of signature $`(-, +, +, +)`$, $`c = 1`$,
as in MC0. The algebra is

```math
A=\mathrm{Cl}(V,-g)\cong G(1,3)\cong M_2(\mathbb H),\qquad uv+vu=-2\,g(u,v)\ \ (u,v\in V).
```

A body is a future unit time-like $`X`$, so in $`A`$

```math
X^2=-g(X,X)=1,\qquad X\cdot Y=-g(X,Y)=\gamma_{XY},\qquad e_X:=\tfrac12(1+X),\quad e_X^2=e_X .
```

The rapidity $`r_{XY}`$ has $`\cosh r_{XY} = \gamma_{XY}`$. The boost of MC1 that carries $`X`$ to
$`Y`$ in their plane is the rotor

```math
L_{YX}=\frac{1+YX}{\sqrt{2(1+\gamma_{XY})}},\qquad L_{YX}\,X\,\tilde L_{YX}=Y,\qquad \tilde L_{YX}=L_{XY}=L_{YX}^{-1},
```

where $`\tilde{\ }`$ is reversion. For three bodies $`G = [\gamma_{ij}]`$, $`\gamma_{ii} = 1`$, as in TV8.

The sign choice matters: in $`\mathrm{Cl}(V, g)`$ a body has $`X^2 = -1`$ and $`(1 + X)/2`$
is not idempotent (OI5).

---

## 3. One body

**Lemma OI1.** For every vector $`Y`$,

```math
e_X\,Y\,e_X=\gamma_{XY}\,e_X .
```

The corner $`e_X A e_X`$ is 4-dimensional, spanned by $`e_X`$ and $`B e_X`$ for the three
bivectors $`B`$ of the rest space of $`X`$, and multiplies as the quaternions. $`e_X`$ is
primitive: $`A e_X`$ has dimension 8, a minimal left ideal of $`M_2(\mathbb H)`$.

*Proof.* Write $`Y = \gamma_{XY} X + Y_\perp`$ with $`X \cdot Y_\perp = 0`$. Then $`X e_X = e_X X = e_X`$,
and $`Y_\perp`$ anticommutes with $`X`$, so $`e_X Y_\perp = Y_\perp (1 - X)/2`$ and
$`e_X Y_\perp e_X = Y_\perp (1 - X)(1 + X)/4 = 0`$. A rest-space bivector commutes with $`X`$;
a bivector containing $`X`$ anticommutes with it and is killed in the same way. ∎ (SymPy,
Part A, which also gives the remainder $`\tfrac14 Y (1 - X^2)`$ off the hyperboloid.)

So the idempotent of a body carries a copy of the quaternions: rotations of its rest
space, in their spin form. MC6's projector carries a copy of the real numbers (OI5).

---

## 4. Two bodies

**Proposition OI2.**

```math
e_Y\,e_X=\tfrac12(1+YX)\,e_X=\cosh\tfrac{r_{XY}}2\;L_{YX}\,e_X,\qquad L_{YX}\,e_X=e_Y\,L_{YX}.
```

Split by $`X`$,

```math
e_Y\,e_X=\tfrac12(1+\gamma_{XY})\,e_X+\tfrac12\,\gamma_{XY}\,v_{XY}\,e_X,\qquad v_{XY}=\frac{Y}{\gamma_{XY}}-X ,
```

with $`v_{XY}`$ the binary velocity of MC1, and $`v_{XY} X = Y \wedge X/\gamma_{XY}`$ Hestenes's
relative velocity. Since $`X e_X = e_X`$, also

```math
e_Y\,e_X=\tfrac12\,(X+Y)\,e_X :
```

the product of two observer idempotents is the bisector $`X + Y`$ times $`e_X`$. As $`1 + YX = (X + Y) X`$,
this is the boost written as the product of the reflections in $`X`$ and in $`X + Y`$, Urbantke's
construction (1990, §3; Chruściel and Urbantke 2025, Prop. 4.2).

*Proof.* $`e_Y e_X = \tfrac14(1 + Y)(1 + X)`$ and $`\tfrac12(1 + YX) e_X = \tfrac14(1 + X + YX + Y X^2)`$
agree because $`X^2 = 1`$. The intertwining is $`L e_X \tilde L = e_{L X \tilde L}`$. ∎ (SymPy,
Part B.)

So the product of two observer idempotents is the boost between them, with weight
$`\cosh(r/2)`$. This is the analogue of Oziewicz (2007, eq. (9)),
$`qp = \mathrm{tr}(qp)\{p + \varpi(p, q)\}`$: a scalar part and a part carrying the binary
velocity.

---

## 5. Three bodies: the loop is the Wigner rotation

**Theorem OI3.** For bodies $`X, Y, Z`$ put $`\Lambda = (1 + XZ)(1 + ZY)(1 + YX)`$. Then

```math
e_X\,e_Z\,e_Y\,e_X=\tfrac18\,\Lambda\,e_X=\cosh\tfrac{r_{XY}}2\cosh\tfrac{r_{YZ}}2\cosh\tfrac{r_{ZX}}2\;H\,e_X,\qquad H=L_{XZ}\,L_{ZY}\,L_{YX},
```

and:

1. $`H`$ commutes with $`X`$: it is a rotation of the rest space of $`X`$, the holonomy of the boost loop $`X \to Y \to Z \to X`$;
2. $`\Lambda`$ has grades 0 and 2 only, with $`\langle \Lambda \rangle_0 = 2(1 + \gamma_{XY} + \gamma_{YZ} + \gamma_{ZX})`$, $`\langle \Lambda \rangle_2^2 = -4 \det G`$ and $`\Lambda \tilde\Lambda = 8 (1 + \gamma_{XY})(1 + \gamma_{YZ})(1 + \gamma_{ZX})`$;
3. so the angle $`\theta`$ of $`H`$ has

```math
\cos\frac\theta2=\frac{1+\gamma_{XY}+\gamma_{YZ}+\gamma_{ZX}}{4\cosh\frac{r_{XY}}2\cosh\frac{r_{YZ}}2\cosh\frac{r_{ZX}}2},\qquad
\tan\frac\theta2=\frac{\sqrt{\det G}}{1+\gamma_{XY}+\gamma_{YZ}+\gamma_{ZX}} ;
```

4. the reverse loop gives $`\tfrac18 \tilde\Lambda e_X`$, the inverse rotation with the same scalar part;
5. the open product is the composite boost times the same rotation:

```math
e_Z\,e_Y\,e_X=\frac{(1+ZX)\,\Lambda\,e_X}{8(1+\gamma_{ZX})}=\cosh\tfrac{r_{ZY}}2\cosh\tfrac{r_{YX}}2\;L_{ZX}\,H\,e_X ;
```

6. for a closed polygon $`X 	o X_2 	o \dots 	o X_n 	o X`$ the same argument gives

```math
e_X\,e_{X_n}\cdots e_{X_2}\,e_X=2^{-n}\,(1+XX_n)(1+X_nX_{n-1})\cdots(1+X_2X)\,e_X=\Big(\prod_{\text{sides}}\cosh\tfrac{r}2\Big)\,H\,e_X ,
```

with $`H`$ the path-ordered product of the boosts round the polygon, and a diagonal costs only a
scalar, $`e_C\, e_X\, e_C = \cosh^2(r_{XC}/2)\, e_C`$ (OI1). So the product for a polygon is, up to
cosh weights, the product of the products for its triangles, and their rotations multiply in
order: for a polygon that is not planar they do not commute, and their angles do not add.

*Proof.* By OI2, $`e_Z e_Y e_X = \tfrac14 (1 + ZY)(1 + YX) e_X`$, using $`L e_X = e_Y L`$ twice.
Multiply on the left by $`e_X`$ and write $`(1 + ZY)(1 + YX) = (1 + ZX) \Lambda / (2(1 + \gamma_{ZX}))`$,
which holds because $`(1 + ZX)(1 + XZ) = 2(1 + \gamma_{ZX})`$. $`\Lambda`$ is a multiple of the
rotor $`H`$, which fixes $`X`$ and commutes with $`e_X`$, and $`e_X (1 + ZX) e_X = (1 + \gamma_{ZX}) e_X`$
by OI1. The grades and the scalar part follow from expanding $`\Lambda`$ with $`X^2 = Y^2 = Z^2 = 1`$;
the bivector part is $`ZY + X (Z \wedge Y) X`$ restricted to grade 2, twice the rest-space part of
$`Z \wedge Y`$ relative to $`X`$. ∎ (SymPy, Part C, for symbolic bodies on the hyperboloid;
Part G numerically for 500 random triples. Item 6: SymPy, Part E, exactly for a non-planar
quadrilateral, with its two triangles; Part G numerically for 200 random pentagons.)

*Example.* For step 2's bodies $`S, B, C`$ (TV7), $`\gamma_{SB} = 25/12`$, $`\gamma_{BC} = 9/4`$,
$`\gamma_{CS} = 37/24`$, and

```math
\langle e_S\,e_C\,e_B\,e_S\rangle_0=\tfrac{55}{64},\qquad \cos\theta=\frac{(1+\gamma_{SB}+\gamma_{BC}+\gamma_{CS})^2}{(1+\gamma_{SB})(1+\gamma_{BC})(1+\gamma_{CS})}-1=\frac{25109}{29341},
```

$`\theta \approx 31.16°`$: TV7's rotation of the binary boosts round the same triangle, now
read off a product of four idempotents (SymPy, Part D, exact). TV7 found that this angle is
the area of the triangle in velocity space, which is Aravind's result (1997); the formula for
$`\tan(\theta/2)`$ is the hyperbolic Heron formula, and the formula for $`\cos\theta`$ is Macfarlane's.

*Aravind's form.* Let the triangle have sides $`\eta = r_{XY}`$ and $`\lambda = r_{YZ}`$ and the angle
$`\pi - \phi`$ at $`Y`$, so that $`\gamma_{ZX} = \cosh\lambda\cosh\eta + \cos\phi\,\sinh\lambda\sinh\eta`$ (his
eq. (3), the cosh rule). Then

```math
1+\gamma_{XY}+\gamma_{YZ}+\gamma_{ZX}=4\cosh\tfrac\eta2\cosh\tfrac\lambda2\Big(\cosh\tfrac\eta2\cosh\tfrac\lambda2+\cos\phi\,\sinh\tfrac\eta2\sinh\tfrac\lambda2\Big),
```

```math
\det G=\big(\sinh\eta\,\sinh\lambda\,\sin\phi\big)^2 ,
```

so OI3's $`\tan(\theta/2) = \sqrt{\det G}/(1 + \gamma_{XY} + \gamma_{YZ} + \gamma_{ZX})`$ is Aravind's eq. (2),

```math
\tan\frac\theta2=\frac{\sin\phi\,\sinh\frac\lambda2\sinh\frac\eta2}{\cosh\frac\lambda2\cosh\frac\eta2+\cos\phi\,\sinh\frac\lambda2\sinh\frac\eta2},
```

up to his sign, which comes from his orientation and his passive convention (SymPy, Part D,
exact). The symmetric form needs no choice of vertex: $`\det G`$ is symmetric in the three bodies.

*What is known and what is not.* The product $`\Lambda`$ of the three boost rotors, its scalar
part, its norm and the angle formula are Urbantke's (1990, eq. (5) and the formula after it;
expanded by Chruściel and Urbantke 2025, eqs. (7.1)-(7.20)). The equality of angle and area and
its extension to polygons are Aravind's (1997). What was not found, in these papers or in the
search of §1, is the statement that the loop product of observer idempotents is
$`\tfrac18 \Lambda e_X`$: the idempotents assemble Urbantke's product, with its cosh weights and no
square root, from the bodies alone, for a triangle or a polygon. Item 6 is the algebraic form of Aravind's remark
on loops that are not planar: the order of the factors keeps the rotations in order.
$`\det G`$ is the polynomial that TV8 found in the Frobenius form, in Page's determinant
of 2004 and in the numerator of Oziewicz's $`\alpha`$; OI3 shows it is $`\sin^2`$ of half the
rotation, up to the weight $`(4 \prod \cosh(r/2))^2`$.

*Analogy.* For three pure quantum states the product $`P_1 P_2 P_3`$ of their projectors
has a trace whose phase is half the solid angle of the triangle on the Bloch sphere (the
Bargmann invariant). Here the corner is $`\mathbb H`$ instead of $`\mathbb C`$, the sphere is
the hyperboloid of velocities, and the "phase" is a rotation.

| Pure quantum states | Bodies |
|---|---|
| projector $`P`$, $`P M_n(\mathbb C) P \cong \mathbb C`$ | idempotent $`e_X`$, $`e_X A e_X \cong \mathbb H`$ |
| Bloch sphere | hyperboloid of unit time-like vectors |
| phase of $`\mathrm{tr}(P_1 P_2 P_3)`$ = half the solid angle | $`H`$ in $`e_X e_Z e_Y e_X`$, angle = area |

---

## 6. The orientation groupoid in the algebra

### 6.1 What the orientation groupoid is

A groupoid is a category in which every arrow has an inverse (Mackenzie 2005, Def. 1.1.1).
Its objects here are the bodies, the points of velocity space $`H`$; what differs is what an
arrow from $`X`$ to $`Y`$ remembers.

- **Pair groupoid** $`H \times H`$ (Mackenzie, Ex. 1.1.7; Oziewicz 2007, §3; MC2). One arrow for each ordered pair, the binary velocity. An arrow records *that* $`Y`$ moves relative to $`X`$ and how fast in which direction, and nothing else. Composition is forced, because there is only one arrow from $`X`$ to $`Z`$.
- **Orientation groupoid.** An arrow from $`X`$ to $`Y`$ is a Lorentz transformation $`\Lambda`$ with $`\Lambda X = Y`$, composed by multiplication. It also records how $`X`$'s spatial axes are carried onto $`Y`$'s: a velocity *and* a relative orientation of the two rest frames. This is the arrow that Einstein's practice uses between two inertial frames.

**Three descriptions of one groupoid.** With $`G = \mathrm{SO}^+(1, 3)`$ acting on $`H`$:

1. *Action groupoid* $`G \ltimes H`$ (Mackenzie, Ex. 1.1.9): arrows are pairs $`(\Lambda, X)`$ from $`X`$ to $`\Lambda X`$. Its vertex group at $`X`$, the arrows from $`X`$ to itself, is the stabilizer $`K_X \cong \mathrm{SO}(3)`$, the rotations of the rest space of $`X`$.
2. *Frame groupoid.* The rest space of $`X`$ is the tangent space $`T_X H`$, since both are $`\{v : g(X, v) = 0\}`$. Restricted to rest spaces, an arrow is an isometry $`T_X H \to T_Y H`$ that preserves handedness, and it determines $`\Lambda`$, because $`\Lambda X = Y`$ fixes the rest. So the orientation groupoid is the oriented orthonormal frame groupoid of $`TH`$, a subgroupoid of Mackenzie's frame groupoid $`\Phi(TH)`$ (Ex. 1.1.12). This is the reason for the name: an arrow is a way of identifying one rest frame with another, axes and orientation included.
3. *Gauge groupoid* of the principal bundle $`G(H, K)`$, $`\Lambda \mapsto \Lambda o`$ for a base body $`o`$ (Mackenzie, Ex. 1.1.15). The map $`(\Lambda, X) \mapsto \langle \Lambda u, u \rangle`$, with $`u`$ any element of $`G`$ with $`u o = X`$, is an isomorphism from the action groupoid; this short check is ours, not in the pages read.

Any two arrows from $`X`$ to $`Y`$ differ by an element of $`K_X`$, so once one is chosen, say the
boost, all of them are

```math
\mathrm{hom}(X,Y)=L_{YX}\,K_X .
```

Forgetting the rotation part of each arrow is Mackenzie's *anchor* $`(\beta, \alpha)`$ onto the pair
groupoid (Ex. 1.2.4), and the two groupoids differ in what a loop returns:

| | Pair groupoid | Orientation groupoid |
|---|---|---|
| arrow $`X \to Y`$ | the binary velocity $`v_{XY}`$ | a Lorentz $`\Lambda`$ with $`\Lambda X = Y`$ |
| arrows $`X \to X`$ | the identity only | rotations $`K_X`$ of the rest space |
| a loop $`X \to Y \to Z \to X`$ | the identity, always | a rotation, which depends on the path |
| in an algebra of idempotents | 1-dimensional corners (OI5) | 4-dimensional corners (OI4) |

**Sections.** To compare the two, pick one arrow for each pair, a *section*
$`s(Y \leftarrow X)`$. A section that also composed, $`s(Z \leftarrow Y)\, s(Y \leftarrow X) = s(Z \leftarrow X)`$,
would split the anchor: it would embed the pair groupoid in the orientation groupoid.

- *Based on a reference body.* Mackenzie (after Def. 1.3.1) notes that a transitive groupoid becomes a trivial groupoid once a reference point $`m`$ and arrows $`\sigma(x)`$ from $`m`$ to each $`x`$ are chosen, by $`(y, \lambda, x) \mapsto \sigma(y)\, \lambda\, \sigma(x)^{-1}`$. With $`m = Z`$ and $`\sigma(X) = L_{XZ}`$ this gives, at $`\lambda = 1`$, step 2's based lift $`L_{YZ} L_{XZ}^{-1}`$ (TV7). It composes, but it depends on $`Z`$, so it is not covariant.
- *Covariant.* The boost $`L_{YX}`$ is covariant and carries $`X`$ to $`Y`$. TV6 shows that no covariant section composes, and OI3 shows by how much the boost fails: round each triangle by the rotation $`H`$.

**Holonomy.** Urbantke (1990, §2) proved that Fermi-Walker transport of a gyroscope's axes
along a world line is Levi-Civita transport, along the hodograph, on the velocity pseudosphere,
and that along a geodesic of velocity space it is the boost that carries one velocity to the
other. So on rest spaces the boost $`L_{YX}`$ is parallel transport along the geodesic from $`X`$
to $`Y`$; Part G checks this numerically by his own method, transport followed by projection in
small steps. Aravind (1997) showed by hyperbolic trigonometry, without the connection, that the
Wigner angle is minus the area of the rapidity triangle, and called it an anholonomy. Velocity space has curvature $`-1`$ (Aravind's Lobachevskian metric), so by
Gauss-Bonnet transport round a geodesic triangle rotates by its area. That is why TV7 found the
Wigner angle equal to the area, and why OI3's formula is the hyperbolic Heron formula: the
Wigner rotation is the holonomy of the Levi-Civita connection of velocity space, read in the
orientation groupoid. Round a loop that is not planar, the holonomy is a path-ordered product
of rotations about different axes, which Aravind and Samuel and Sinha (as Aravind cites them)
describe as a non-Abelian geometric phase. In the orientation groupoid it is just the product
of the arrows round the loop, and in the algebra the product of the idempotents (OI3, item 6).

*Analogy.* Carry an arrow tangent to a sphere round a triangle of great circles, never
turning it relative to the path, and it comes back rotated by the area of the triangle.
Here the sphere is the hyperboloid of velocities and the arrow is a gyroscope's set of rest
axes. The pair groupoid records the trip and forgets the gyroscope; the orientation groupoid
carries the gyroscope, and Thomas precession is what it shows on return.

**Spin.** In $`A = \mathrm{Cl}(V, -g)`$ the arrows are rotors, and the isotropy is
$`\mathrm{Spin}(3) \cong \mathrm{SU}(2)`$, the unit quaternions of the corner $`e_X A e_X`$
(OI1). This double cover of the orientation groupoid distinguishes a rotation by $`2\pi`$
from the identity, as spinors do. In the algebra the formula above for
$`\mathrm{hom}(X, Y)`$ becomes $`e_Y A e_X = e_Y e_X \cdot e_X A e_X`$ (OI4, part 1).

### 6.2 The groupoid inside the algebra

**Proposition OI4.** For bodies $`X, Y`$ put $`\mathrm{hom}(X, Y) = e_Y A e_X`$. Then:

1. $`\mathrm{hom}(X, Y) = e_Y e_X \cdot e_X A e_X`$ is 4-dimensional, a free right module of rank 1 over the quaternions of $`X`$;
2. multiplication in $`A`$ composes $`\mathrm{hom}(Y, Z) \times \mathrm{hom}(X, Y) \to \mathrm{hom}(X, Z)`$, associatively, with identities $`e_X`$;
3. the elements $`L_{YX} Q e_X`$ with $`Q`$ a unit quaternion of the rest space of $`X`$ have inverses $`\tilde Q L_{XY} e_Y \in \mathrm{hom}(Y, X)`$; they form the gauge groupoid of $`\mathrm{Spin}^+(1, 3) \to`$ (bodies), with isotropy $`\mathrm{Spin}(3)`$, which double covers the orientation groupoid of TV-SP1;
4. the boost section $`s(Y \leftarrow X) = L_{YX} e_X = e_Y e_X/\cosh(r_{XY}/2)`$ is covariant and carries $`X`$ to $`Y`$, properties (a) and (b) of TV6, and fails (c) by exactly the rotation of OI3: $`s(Z \leftarrow Y)\, s(Y \leftarrow X) = s(Z \leftarrow X)\, H`$.

*Proof.* 1: $`e_Y a e_X = L_{YX} e_X \tilde L_{YX} a e_X`$, and $`e_X \tilde L_{YX} a e_X`$ lies in
$`e_X A e_X`$; $`L_{YX} e_X`$ is a multiple of $`e_Y e_X`$ by OI2. 2 is the Peirce
decomposition. 3: $`(\tilde Q L_{XY} e_Y)(L_{YX} Q e_X) = \tilde Q Q e_X = e_X`$, since $`Q`$ commutes
with $`e_X`$. 4 is OI3 (5). ∎ (SymPy, Part E, on step 2's bodies; the inverse with
$`X = \gamma_0`$ and a rational quaternion.)

So the arrows of the orientation groupoid are elements of $`A`$, composed by its product:
one boost and one rest-space rotation per arrow. Forgetting $`Q`$ leaves Oziewicz's pair
groupoid (MC2). TV6 says no choice of $`Q`$ for every pair can be covariant and compose; OI4
says what the failure is when $`Q = 1`$.

### 6.3 In the language of Baylis and Sobczyk

Baylis and Sobczyk (2004) compare relativity in the spacetime algebra (STA, here $`A`$) and
in the algebra of physical space (APS, $`\mathrm{Cl}_3`$, isomorphic to the even subalgebra
$`\mathrm{STA}^+`$). An observer $`A`$ carries an orthonormal frame $`\{\gamma^A_\mu\}`$ with
$`\gamma^A_0 = u_A`$; her proper basis $`\sigma^A_k = \gamma^A_k \gamma^A_0`$ generates her APS, and her
conjugation $`K^{\dagger A} = \gamma^A_0 \tilde K \gamma^A_0`$ (their eq. (22)) splits it into real parts
(scalars and vectors) and imaginary parts (bivectors and the pseudoscalar). The results of this
note translate as follows (SymPy, Part H, exact):

| Baylis and Sobczyk (2004) | This note |
|---|---|
| eq. (24): for a boost, $`L^2 = \gamma(1 + v) = u_B u_A`$ | OI2 without the square root: $`e_Y e_X = \tfrac12 (1 + YX) e_X`$, and $`(1 + YX)^2 = 2(1 + \gamma) YX`$ |
| eqs. (26)-(27): the space-time split $`r \gamma_0 = t + \mathbf r`$, $`t = r \cdot \gamma_0`$ | OI1: $`e_X Y e_X = \gamma_{XY} e_X`$ keeps the time part and kills the relative vector |
| eq. (22): the observer's conjugation $`K^{\dagger X} = X \tilde K X`$ | for even $`K`$, $`e_X K e_X = \tfrac12 (K + XKX)\, e_X`$: the scalar and the bivectors of the observer's APS, a quaternion algebra; that is the corner of OI1 |
| §II and eq. (23): $`L = BR`$, $`LL^{\dagger A} = B^2 = u_B u_A`$ | OI3 (5): $`L_{ZY} L_{YX} = L_{ZX} H`$ with $`L_{ZX}`$ hermitian and $`H`$ unitary for $`X`$ |
| observers as frames, related by a rotor (eq. (19)) | the pair groupoid on frames, below |
| relative APS: every observer referred to one absolute frame (eq. (44)) | the trivialisation by a reference body (§6.1, Sections) |

**The polar decomposition.** Every Lorentz rotor factors as $`L = BR`$, a boost $`B`$ hermitian
for $`A`$ times a rotation $`R`$ unitary for $`A`$, with $`LL^{\dagger A} = B^2 = u_B u_A`$. For the composite
of two boosts, $`L = L_{ZY} L_{YX}`$, relative to $`X`$, this gives $`B = L_{ZX}`$ and $`R = H`$. The Wigner
rotation is therefore the unitary factor of the composite boost relative to the first observer.
OI3 extracts it from a product of idempotents, with no square root to take.

**Frames, bodies and the three groupoids.** Baylis and Sobczyk's observer is a frame, a
point of the bundle $`P`$ of oriented orthonormal frames. Two frames are related by one
Lorentz transformation (their eq. (19); a rotor up to sign), so frames form a pair groupoid
$`P \times P`$. Forgetting which triad each body carries and keeping its velocity is division by
the rotations, Mackenzie's construction of the gauge groupoid (Ex. 1.1.15), and gives the
orientation groupoid. Forgetting the rotation part of the arrows, the anchor, gives Oziewicz's
pair groupoid on bodies:

```math
P\times P\ \longrightarrow\ (P\times P)/K\ \longrightarrow\ H\times H .
```

Their *absolute* APS keeps one conjugation per observer, as the corners $`e_Y A e_X`$ keep one
idempotent per body. Their *relative* APS refers every observer to one chosen frame and shows
that the transformation laws do not depend on the choice (eq. (44)). In groupoid terms this
is the trivialisation of §6.1 by a reference body. It is legitimate for the reason they give,
the equivalence of inertial frames, but it is a choice: Mackenzie's remark after Def. 1.3.1,
and TV6.

So step 5 can be stated entirely in their notation. What it adds is the observer idempotent:
it is not in $`\mathrm{STA}^+`$, so it cannot be an element of APS, and its corners carry the
orientation groupoid inside one associative algebra.

---

## 7. What the algebra of MC6 cannot see

**Proposition OI5.**

1. In $`\mathrm{End}(V)`$, with $`p_X = X \otimes \mathrm{clock}_X`$ (MC6), every corner $`p_Y\, \mathrm{End}(V)\, p_X`$ is 1-dimensional. Products of observer idempotents carry one number per pair, and the loop $`\mathrm{tr}(p_X p_Y p_Z) = \mathrm{tr}(p_Y p_X p_Z) = \gamma_{XY} \gamma_{YZ} \gamma_{ZX}`$ is the same for both orientations. That is Oziewicz's postulate (7) of 2007, automatically.
2. In $`\mathrm{Cl}(V, g) \cong G(3, 1) \cong M_4(\mathbb R)`$ a body has $`X^2 = -1`$, and $`(1 + X)/2`$ is not idempotent.

3. Oziewicz's postulate (8) of 2007, $`qAp = \mathrm{tr}(qAp)\{p + \varpi(p, q)\}`$ for all $`A`$, says that every corner $`q\, \mathrm{Obs}\, p`$ is spanned by the single element $`qp`$: corners are 1-dimensional. In $`\mathrm{Cl}(V, -g)`$ it fails, since $`e_Y A e_X`$ has dimension 4 (OI4).

(SymPy, Parts E and F, on step 2's bodies.)

So the same bodies, as idempotents in two algebras, give two groupoids, and postulate (8)
is the axiom that selects the smaller one. In $`\mathrm{End}(V)`$,
the corner is $`\mathbb R`$: there is room for $`\gamma`$ and nothing else, and the pair groupoid
is all that products can express. In $`\mathrm{Cl}(V, -g)`$, the corner is $`\mathbb H`$: there is
room for a rotation, and the loop product finds the Wigner rotation in it. In the
spacetime algebra the scalar part of the loop, $`(1 + \gamma_{XY} + \gamma_{YZ} + \gamma_{ZX})/8`$,
is also orientation-blind; the rotation is in the grade-2 part, which a real trace
discards.

---

## 8. What this does not do

- It makes no new prediction. The Wigner angle and its formulas are classical (§1).
- It uses the metric twice: to make a body square to 1, and to choose $`\mathrm{Cl}(V, -g)`$. Step 3's metric-free body $`(X, \alpha)`$ has no counterpart here (OI-SP1).
- It treats bodies as points of velocity space, without place or mass (step 4's centre is not used).
- It does not say whether Oziewicz's arrow $`\varpi(p, q)`$ of $`\mathrm{End}(V)`$ is an image of $`e_Y A e_X`$ under some map (OI-SP3).

---

## 9. Open items

- **OI-SP1.** Is there an observer idempotent for a metric-free body $`(X, \alpha)`$, $`\alpha X = 1`$? In $`\mathrm{Cl}(V \oplus V^*)`$ the element $`(\alpha \wedge)\, i_X`$ is idempotent of rank 8 in 16. What are its corners for two bodies, and does a loop of three carry anything without a metric?
- **OI-SP2.** In $`\mathrm{Cl}(V, g)`$, and in the even algebra (the algebra of physical space), what element plays the part of $`e_X`$? A covariant involution built from $`X`$ alone does not exist in $`\mathrm{Cl}(V, g)`$ (OI5); does one built from $`X`$ and an orientation? The rotors do not need one: Chruściel and Urbantke (2025) compute the Wigner rotation in $`\mathrm{Cl}(V, g)`$ with the rotor $`-1 + vu`$. What needs $`\mathrm{Cl}(V, -g)`$ is the packaging of the rotors as products of observer idempotents, and the corners. Partly answered for the even algebra (§6.3): there the observer enters through Baylis and Sobczyk's conjugation $`K \mapsto X \tilde K X`$, not through an idempotent, since $`e_X`$ is not even.
- **OI-SP3.** Is there a natural map from the corners $`e_Y A e_X`$ to Oziewicz's arrows $`\varpi(X, Y)`$ in $`\mathrm{End}(V)`$ that respects composition (2007, eq. (21))? The vector representation $`a \mapsto (v \mapsto a v \tilde a)`$ is quadratic, so it is not the obvious candidate.
- **OI-SP4.** With the mass centre $`Z`$ of a system (MC3), the corners give a rotation for every triangle of bodies and centres. Can the failure of cluster separability (TV-SP3) be written as such a holonomy, between $`e_Z`$ of a pair and $`e_Z`$ of the system?
- **OI-SP5.** The search of §1 was short. Aravind (1997), Baylis and Sobczyk (2004), Urbantke (1990) and Chruściel and Urbantke (2025) have since been read (§1, §5, §6.1, §6.3). Urbantke's rotor product is the $`\Lambda`$ of OI3; none of the four writes it as a product of observer idempotents or uses the corners. Jordan (1988), Macfarlane (1962), the rest of the literature on the algebra of physical space (Baylis 1999; Baylis and Jones 1989), and two later papers found in the search, on the Thomas-Wigner rotation as a holonomy of the spin bundle over the mass shell ([arXiv:2310.08121](https://arxiv.org/abs/2310.08121)) and on the geometry of the kinematic space of inertial observers ([arXiv:2012.00681](https://arxiv.org/abs/2012.00681)), were not read. The first bears directly on the $`\mathrm{Spin}(3)`$ corner of OI4. The idempotent form may be there in another guise.

---

## 10. What this does for the ladder

TV-SP1 is answered in part: the orientation groupoid is in the spacetime algebra, as the
corners of the observer idempotents, and not in the algebra of MC6. TV8's link between
$`\det G`$ and the rotation is now a formula. Oziewicz's postulate that a body is an
idempotent therefore holds in two algebras with different content, and the choice
between them is the choice between the pair groupoid and the orientation groupoid.

---

## 11. Verification

`PYTHONPATH=src python3 -u src/verify_observer_idempotents.py` runs every check below and
ends with `ALL CHECKS PASSED`. Parts A to F and H are exact (SymPy); Part G is numerical (NumPy).

| Part | What is checked | How |
|---|---|---|
| A | OI1, the corner, primitivity | symbolic $`X, Y`$ (remainder off the hyperboloid); $`\gamma_0`$ and one rational body |
| B | OI2, intertwining, the split by $`X`$, the bisector form | symbolic; on the hyperboloid by reduction of $`X_0^2`$ |
| C | OI3 (1), (2), (4), (5) | symbolic bodies in 3+1 on the hyperboloid |
| D | OI3 on TV7's example; OI3 equals Aravind's eq. (2) | exact rationals: $`55/64`$, $`25109/29341`$; half-rapidity polynomials reduced by $`\cosh^2 - \sinh^2 = 1`$ |
| E | OI4: dimension, rank 1, inverses, failure to compose; OI3 (6) for a non-planar quadrilateral, its triangles, and their non-commuting rotations | exact rationals |
| F | OI5 | exact rationals |
| H | §6.3: $`L^2 = u_B u_A`$, the space-time split, $`e_X K e_X`$ for even $`K`$, the polar decomposition | symbolic on the hyperboloid; exact rationals |
| G | OI3, and angle = area; OI3 (6) for pentagons; the boost is parallel transport on rest spaces (§6.1) | 500 random triples and 200 random skew pentagons, speeds up to $`0.95`$, errors below $`10^{-12}`$; transport by projection, error falling as $`1/N`$ |

---

## References

- Z. Oziewicz, "Relativity groupoid, instead of relativity group", *Int. J. Geom. Methods Mod. Phys.* 4 (2007), [arXiv:math/0608770](https://arxiv.org/abs/math/0608770). §4, eqs. (4)-(9), and §7, eq. (21), read in v2.
- D. Hestenes, *Space-Time Algebra*, Gordon and Breach (1966).
- D. Hestenes, "Proper particle mechanics", *J. Math. Phys.* 15 (1974) 1768-1777, [PDF](https://davidhestenes.net/geocalc/pdf/Proper_mechanics.pdf).
- R. da Rocha and J. Vaz Jr., "Conformal structures and twistors in the paravector model of spacetime", [arXiv:math-ph/0412074](https://arxiv.org/abs/math-ph/0412074). The idempotent $`(1 + \gamma_0)/2`$ and $`\mathrm{Cl}(1, 3) \cong M_2(\mathbb H)`$.
- A. J. Macfarlane, "On the restricted Lorentz group and groups homomorphically related to it", *J. Math. Phys.* 3 (1962) 1116-1129, [doi:10.1063/1.1703854](https://doi.org/10.1063/1.1703854). Not read; the formula as cited by Urbantke (1990) and by Chruściel and Urbantke (2025).
- P. T. Chruściel and H. Urbantke, "Thomas-Wigner rotation via Clifford algebras", [arXiv:2501.14855](https://arxiv.org/abs/2501.14855) (2025), Vienna preprint UWThPh 2025-1. Read in full (v1): Prop. 4.2, eqs. (7.1)-(7.20).
- H. Urbantke, "Physical holonomy, Thomas precession, and Clifford algebra", *Am. J. Phys.* 58 (1990) 747-750; erratum *Am. J. Phys.* 59 (1991) 1150. Read in full in the preprint version, Vienna UWThPh 1988-39: §2 (Fermi-Walker = Levi-Civita on the velocity pseudosphere), §3 and eq. (5); neither the published version nor the erratum was compared.
- University of Glasgow, "Hyperbolic area: Heron's formula" (course notes), [proof page](https://www.maths.gla.ac.uk/wws/cabripages/hyperbolic/hareaproof.html). For $`\tan(D/2) = \Delta/(1 + \alpha + \beta + \gamma)`$.
- K. C. H. Mackenzie, *General Theory of Lie Groupoids and Lie Algebroids*, London Math. Soc. Lecture Note Series 213, Cambridge University Press (2005). Read in the publisher's preview (preface, §§1.1-1.3), 20 November 2026: Def. 1.1.1, Examples 1.1.7, 1.1.9, 1.1.12, 1.1.15, 1.2.4, Def. 1.3.1 and the remark after it.
- P. K. Aravind, "The Wigner angle as an anholonomy in rapidity space", *Am. J. Phys.* 65 (1997) 634-636. Read in full: eqs. (1)-(4), the rapidity triangle, polygons and the note added in proof.
- T. F. Jordan, "Berry phases and unitary transformations", *J. Math. Phys.* 29 (1988) 2042-2052. Not read; as cited by Aravind.
- J. Samuel and S. Sinha, "Thomas rotation and polarised light", *Pramana* (to appear in 1997, as cited by Aravind). Not read.
- V. Bargmann, "Note on Wigner's theorem on symmetry operations", *J. Math. Phys.* 5 (1964) 862-868.
- N. Mukunda and R. Simon, "Quantum kinematic approach to the geometric phase. I. General formalism", *Ann. Phys.* 228 (1993) 205-268.
- P. Lévay, "Mixed state geometric phase from Thomas rotations", [arXiv:quant-ph/0312023](https://arxiv.org/abs/quant-ph/0312023).
- W. E. Baylis and G. Sobczyk, "Relativity in Clifford's geometric algebras of space and spacetime", [arXiv:math-ph/0405026](https://arxiv.org/abs/math-ph/0405026) (2004). Read in full (v1): eqs. (18)-(24), (26)-(27), (35), (44), §II on $`L = BR`$.
