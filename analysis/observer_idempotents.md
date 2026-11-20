# Observers as idempotents of the spacetime algebra: the orientation groupoid and the Wigner rotation

> Oziewicz (2007, §4) makes every body an idempotent of an associative algebra, and step 1 realised it as the rank-one projector $`X \otimes \mathrm{clock}_X`$ (MC6). This note represents the same bodies in the spacetime algebra $`A = \mathrm{Cl}(V, -g) \cong M_2(\mathbb H)`$, where a body squares to 1, and asks what products of the idempotents $`e_X = (1 + X)/2`$ contain. **Lemma OI1**: $`e_X Y e_X = \gamma_{XY} e_X`$, and the corner $`e_X A e_X`$ is a quaternion algebra, the spin of the rest space of $`X`$. **Proposition OI2**: $`e_Y e_X = \cosh(r/2)\, L_{YX} e_X`$, with $`L_{YX}`$ the boost of MC1 and $`r`$ the rapidity. **Theorem OI3**: round a triangle, $`e_X e_Z e_Y e_X = \tfrac18 (1 + XZ)(1 + ZY)(1 + YX)\, e_X`$, which is the product of the three $`\cosh(r/2)`$ times $`H e_X`$, with $`H`$ the Thomas-Wigner rotation of the boost loop, and $`\tan(\theta/2) = \sqrt{\det G}/(1 + \gamma_{XY} + \gamma_{YZ} + \gamma_{ZX})`$ with $`\det G`$ the polynomial of TV8. On step 2's example it gives TV7's $`\cos\theta = 25109/29341`$ exactly. The angle formula is Macfarlane's (1962), the hyperbolic Heron formula; what is new, as far as a short search found, is that a product of observer idempotents yields it. **Proposition OI4**: the corners $`e_Y A e_X`$ are 4-dimensional, and their unit elements form the gauge groupoid with isotropy $`\mathrm{Spin}(3)`$, the orientation groupoid asked for in TV-SP1, which is answered in part. The boost is a covariant section that fails to compose by exactly $`H`$, as TV6 requires. **Proposition OI5**: rank-one projectors of $`\mathrm{End}(V)`$ have 1-dimensional corners, which is what Oziewicz's postulate (8) demands, and real loops, so the algebra of MC6 carries only the pair groupoid, and $`\mathrm{Cl}(V, g)`$ has no idempotent of this kind. The representation decides whether the algebra of observers sees the rotation. Checked exactly with SymPy; the triangle also numerically. No new prediction.

*Ladder abstract — see the [full list](README.md#the-ladder).*

**Status.** Analysis note, step 5 of the ladder. Theorem prefix **OI**. Companion
script: [`src/verify_observer_idempotents.py`](../src/verify_observer_idempotents.py)
(Parts A to G; §11). Prompted by Bill Page, 20 November 2026: a correspondence on
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
- Macfarlane (1962), through Chruściel and Urbantke (2025), for the closed form of the Wigner angle, and the hyperbolic Heron formula (Glasgow notes) for the area of a triangle from the cosh of its sides. Urbantke (1990), Thomas precession as holonomy with Clifford algebra, was found but not read.
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
relative velocity.

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
e_Z\,e_Y\,e_X=\frac{(1+ZX)\,\Lambda\,e_X}{8(1+\gamma_{ZX})}=\cosh\tfrac{r_{ZY}}2\cosh\tfrac{r_{YX}}2\;L_{ZX}\,H\,e_X .
```

*Proof.* By OI2, $`e_Z e_Y e_X = \tfrac14 (1 + ZY)(1 + YX) e_X`$, using $`L e_X = e_Y L`$ twice.
Multiply on the left by $`e_X`$ and write $`(1 + ZY)(1 + YX) = (1 + ZX) \Lambda / (2(1 + \gamma_{ZX}))`$,
which holds because $`(1 + ZX)(1 + XZ) = 2(1 + \gamma_{ZX})`$. $`\Lambda`$ is a multiple of the
rotor $`H`$, which fixes $`X`$ and commutes with $`e_X`$, and $`e_X (1 + ZX) e_X = (1 + \gamma_{ZX}) e_X`$
by OI1. The grades and the scalar part follow from expanding $`\Lambda`$ with $`X^2 = Y^2 = Z^2 = 1`$;
the bivector part is $`ZY + X (Z \wedge Y) X`$ restricted to grade 2, twice the rest-space part of
$`Z \wedge Y`$ relative to $`X`$. ∎ (SymPy, Part C, for symbolic bodies on the hyperboloid;
Part G numerically for 500 random triples.)

*Example.* For step 2's bodies $`S, B, C`$ (TV7), $`\gamma_{SB} = 25/12`$, $`\gamma_{BC} = 9/4`$,
$`\gamma_{CS} = 37/24`$, and

```math
\langle e_S\,e_C\,e_B\,e_S\rangle_0=\tfrac{55}{64},\qquad \cos\theta=\frac{(1+\gamma_{SB}+\gamma_{BC}+\gamma_{CS})^2}{(1+\gamma_{SB})(1+\gamma_{BC})(1+\gamma_{CS})}-1=\frac{25109}{29341},
```

$`\theta \approx 31.16°`$: TV7's rotation of the binary boosts round the same triangle, now
read off a product of four idempotents (SymPy, Part D, exact). TV7 found that this angle is
the area of the triangle in velocity space; the formula for $`\tan(\theta/2)`$ is the
hyperbolic Heron formula, and the formula for $`\cos\theta`$ is Macfarlane's.

*What is known and what is not.* The angle formulas, the holonomy reading and the
rotor $`L_{YX}`$ are known (§1). The statement that the loop product of observer
idempotents equals the cosh weights times $`H e_X`$ was not found in the short search.
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
- **OI-SP2.** In $`\mathrm{Cl}(V, g)`$, and in the even algebra (the algebra of physical space), what element plays the part of $`e_X`$? A covariant involution built from $`X`$ alone does not exist there (OI5); does one built from $`X`$ and an orientation?
- **OI-SP3.** Is there a natural map from the corners $`e_Y A e_X`$ to Oziewicz's arrows $`\varpi(X, Y)`$ in $`\mathrm{End}(V)`$ that respects composition (2007, eq. (21))? The vector representation $`a \mapsto (v \mapsto a v \tilde a)`$ is quadratic, so it is not the obvious candidate.
- **OI-SP4.** With the mass centre $`Z`$ of a system (MC3), the corners give a rotation for every triangle of bodies and centres. Can the failure of cluster separability (TV-SP3) be written as such a holonomy, between $`e_Z`$ of a pair and $`e_Z`$ of the system?
- **OI-SP5.** The search of §1 was short. Urbantke (1990), Chruściel and Urbantke (2025) beyond its abstract, Baylis and Sobczyk (2004), and the literature on the algebra of physical space were not read. The identity of OI3 may be there in another form.

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
ends with `ALL CHECKS PASSED`. Parts A to F are exact (SymPy); Part G is numerical (NumPy).

| Part | What is checked | How |
|---|---|---|
| A | OI1, the corner, primitivity | symbolic $`X, Y`$ (remainder off the hyperboloid); $`\gamma_0`$ and one rational body |
| B | OI2, intertwining, the split by $`X`$ | symbolic; on the hyperboloid by reduction of $`X_0^2`$ |
| C | OI3 (1), (2), (4), (5) | symbolic bodies in 3+1 on the hyperboloid |
| D | OI3 on TV7's example | exact rationals: $`55/64`$, $`25109/29341`$ |
| E | OI4: dimension, rank 1, inverses, failure to compose | exact rationals |
| F | OI5 | exact rationals |
| G | OI3, and angle = area | 500 random triples, speeds up to $`0.95`$, errors below $`10^{-12}`$ |

---

## References

- Z. Oziewicz, "Relativity groupoid, instead of relativity group", *Int. J. Geom. Methods Mod. Phys.* 4 (2007), [arXiv:math/0608770](https://arxiv.org/abs/math/0608770). §4, eqs. (4)-(9), and §7, eq. (21), read in v2.
- D. Hestenes, *Space-Time Algebra*, Gordon and Breach (1966).
- D. Hestenes, "Proper particle mechanics", *J. Math. Phys.* 15 (1974) 1768-1777, [PDF](https://davidhestenes.net/geocalc/pdf/Proper_mechanics.pdf).
- R. da Rocha and J. Vaz Jr., "Conformal structures and twistors in the paravector model of spacetime", [arXiv:math-ph/0412074](https://arxiv.org/abs/math-ph/0412074). The idempotent $`(1 + \gamma_0)/2`$ and $`\mathrm{Cl}(1, 3) \cong M_2(\mathbb H)`$.
- A. J. Macfarlane, "On the restricted Lorentz group and groups homomorphically related to it", *J. Math. Phys.* 3 (1962) 1116-1129, [doi:10.1063/1.1703854](https://doi.org/10.1063/1.1703854). Not read; the formula as cited by Chruściel and Urbantke.
- P. T. Chruściel and H. Urbantke, "Thomas-Wigner rotation via Clifford algebras", [arXiv:2501.14855](https://arxiv.org/abs/2501.14855). Abstract and introduction read.
- H. Urbantke, "Physical holonomy, Thomas precession, and Clifford algebra", *Am. J. Phys.* 58 (1990) 747. Not read.
- University of Glasgow, "Hyperbolic area: Heron's formula" (course notes), [proof page](https://www.maths.gla.ac.uk/wws/cabripages/hyperbolic/hareaproof.html). For $`\tan(D/2) = \Delta/(1 + \alpha + \beta + \gamma)`$.
- V. Bargmann, "Note on Wigner's theorem on symmetry operations", *J. Math. Phys.* 5 (1964) 862-868.
- N. Mukunda and R. Simon, "Quantum kinematic approach to the geometric phase. I. General formalism", *Ann. Phys.* 228 (1993) 205-268.
- P. Lévay, "Mixed state geometric phase from Thomas rotations", [arXiv:quant-ph/0312023](https://arxiv.org/abs/quant-ph/0312023).
- W. E. Baylis and G. Sobczyk, "Relativity in Clifford's geometric algebras of space and spacetime", [arXiv:math-ph/0405026](https://arxiv.org/abs/math-ph/0405026). Abstract only.
