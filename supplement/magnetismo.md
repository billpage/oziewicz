# Oziewicz's *Magnetismo e Electricidad* (2014–2020): a body is a pair of polarisers

> A summary of Oziewicz's unpublished lecture notes on electricity and magnetism for chemistry students (UNAM, FES Cuautitlán, 2014 to 2020; last version 18 July 2020), which are the main source for his operators of observation. A body $`P = E_P L_P`$ with its clock carries four idempotents built from creation and evaluation; on forms they are the derivation $`\mathcal D = \mathrm{cr}_{\mathrm{clock}} \circ \mathrm{ev}_L`$, which keeps simultaneity, and the algebra map $`\mathcal M = \mathrm{ev}_L \circ \mathrm{cr}_{\mathrm{clock}}`$, which keeps the forms of the body's places, with $`\mathcal D + \mathcal M = \mathrm{id} = \mathcal U^2`$ for the unipotent $`\mathcal U = \mathrm{ev}_L + \mathrm{cr}_{\mathrm{clock}}`$ (MG1). The notes split the electromagnetic field by $`\mathcal M`$ into magnetic and electric parts and Maxwell's $`dF = 0`$ into Gauss and Faraday. Checked exactly: the operator identities hold, but two definitions (7.4.2, 7.4.5) exchange places and simultaneity (MG2); the "private differential" $`d_{\mathcal M}`$ exists exactly when the simultaneity ideal $`\mathrm{clock} \wedge \Lambda`$ is a differential ideal, that is when the clock does not rotate, $`\mathrm{clock} \wedge d\,\mathrm{clock} = 0`$: the algebraic Frobenius theorem, with no points needed (MG3); with a rotating clock the magnetic Gauss law gains a term $`-\Omega \wedge E`$ and Faraday's law the acceleration term that the notes derive in §7.7 (MG4); and the metric intertwines the vector and form operators only for a clock normalised by $`g(L, L) = 1`$ (MG5). MG1, MG2 and MG5 are $`F`$-linear and hold over any commutative ring (MG1 checked as polynomial identities); MG3 and MG4 need $`d`$. The unipotent's idempotent $`\tfrac12(1 + \mathcal U)`$ is not in the notes; it needs no metric (step 6, GB2–GB3), and with a metric it is step 5's $`e_X`$.

**Status.** Supplement (summary of an unpublished text, not a ladder step). Labels use the prefix **MG**.
Companion script: [`src/verify_magnetismo.py`](../src/verify_magnetismo.py). Requested by Bill Page,
21 November 2026, as the source for ladder step 6. The text is Oziewicz's *Magnetismo e
Electricidad*, "Version Julio 18, de 2020", 111 pages, sent to Bill Page on 20 July 2020;
the earlier version of 10 May 2014 (77 pages, *Electricidad e Magnetismo*) was sent on 23 July 2020.
Neither is public, and neither is committed here. An English translation of chapters 4
and 7 exists in a private repository; it is not a source for this summary, which reads the
Spanish. **Every statement of what the notes say is a reading**, and Oziewicz's Spanish is
paraphrased, not quoted. Drafted with Claude (Anthropic) and subject to review. Revised 22
November 2026 to read the notes in Oziewicz's algebraic setting ($`F`$-linear operations against
derivations, the algebraic form of MG3, ranks rather than dimensions, MG1 over any commutative
ring) and to point forward to steps 6 and 7.
[PDF](https://github.com/billpage/oziewicz/releases/latest/download/magnetismo.pdf)

Notation: $`L`$ is a body's Length vector and $`S`$ its clock, $`S(L) = 1`$ (the notes' $`L_P`$ and
$`\mathrm{reloj}_P`$); $`\mathrm{cr}`$ and $`\mathrm{ev}`$ are creation, $`\mathrm{cr}_\alpha = \alpha \wedge`$, and evaluation, $`\mathrm{ev}_X = \iota_X`$;
$`\mathcal L_L = \mathrm{ev}_L \circ d + d \circ \mathrm{ev}_L`$. The setting is Oziewicz's: $`F`$ a commutative $`\mathbb R`$-algebra of scalar fields, $`L`$ in the $`F`$-module
$`\mathrm{der}\,F`$ of its derivations, $`S`$ in the dual module, as in MF0; scalars such as $`S(L)`$ and $`E_P`$ are
elements of $`F`$. Points, a manifold and a dimension appear only when a representation of $`F`$ is
chosen, as in the checks of §6. Calligraphic $`\mathcal D, \mathcal M, \mathcal U`$ act on forms, roman
$`D, M, U`$ on multivectors, as in the notes' §4.8. Equation and section numbers are those of the
2020 version unless marked 2014.

---

## 0. What this supplement inherits and retracts

**Inherits.** From step 1 ([`mass_centre.md`](../analysis/mass_centre.md)): the body as a rank-one
idempotent $`X \otimes \mathrm{clock}_X`$ (MC6). From step 3
([`metric_free_body.md`](../analysis/metric_free_body.md)): the split MF1, in which $`\Pi = \mathrm{ev}_X \wedge_\alpha`$ is
the notes' $`\mathcal M`$ and $`D = \wedge_\alpha \mathrm{ev}_X`$ their $`\mathcal D`$; the clock as a connection, MF10, whose
part 2 is the scalar case of MG3; time and $`\alpha \wedge d\alpha`$, MF11. From step 5
([`observer_idempotents.md`](../analysis/observer_idempotents.md)): $`e_X = \tfrac12(1 + X)`$ in $`\mathrm{Cl}(V, -g)`$ (OI1).

**Points forward to.** Step 6 ([`grammar_of_a_body.md`](../analysis/grammar_of_a_body.md)): the three
observers $`\mathcal D`$, $`\mathcal M`$, $`e`$ (GB2), and $`e`$ without a metric (GB3). Step 7
([`heat_and_helicity.md`](../analysis/heat_and_helicity.md)): $`\mathcal D = \iota_\Phi`$ and $`\mathcal M = \Lambda(1 - \Phi)`$ for the observer
tensor field $`\Phi = L \otimes S`$, whose curvature is the rotation (HH7 and the remark after it); the
vorticity identity behind MG4 (HH2).

**Retracts.** Nothing. MF1 was written without this source; it states the split that the
notes had stated in 2014 (§2.9 there), and this supplement supplies the citation.

---

## 1. The text

The notes are a course for second-year students of industrial chemistry, written in
Spanish, Oziewicz's second language, with set exercises in every section (*Evalúe su
compresión*, *Comparta*, *Reflexionar*) and a running polemic against the "Science Museum",
his name for physics taught in the language of 1900. He taught from them from 2014 to the
spring of 2020. In July 2020 he decided to publish them privately and asked for
endorsements; on 20 July he counted them among his five unpublished books, and one of the
two (with his algebra lectures given in Vilnius in 2015) that he thought ready to print.

| 2020 chapter | 2014 chapter | pages (2020) | content |
|---|---|---|---|
| 1 Prólogo, 2 Syllabus | — | 13–22 | prologue (begun, by G. P. Wene), course rules, "what you will learn" |
| 3 Differential calculus with Ricci's waves | 1 | 23–38 | calculus on rings without limits |
| 4 Hermann Grassmann in 1844 | 2 | 39–52 | two Grassmann algebras; creation, evaluation; nilpotents, unipotents, idempotents |
| 5 Derivations of Grassmann's algebra | 3 | 53–64 | derivations, Lie bracket, $`d`$, the Lie derivation $`(d + \mathrm{ev}_X)^2`$ |
| 6 Integral laws | 4 | 65–72 | spin as the source of magnetism; three faces of electricity and of magnetism; $`\partial^2 = 0 \iff d^2 = 0`$ |
| 7 Relativity or absolutivity? | 5 | 73–97 | the body and its idempotents; the private differential; Maxwell split; the metric as "environment" |
| 8 Photographs, lists, index | — | 98–111 | |

The 2014 and 2020 texts of chapters 4–7 agree in substance; 2020 renumbers (2014 §2.9 is
2020 §4.8; 2014 §5.3 is 2020 §7.3) and adds the photographs. The statements read in MG2 are the same in both.

---

## 2. Chapter by chapter

**Chapter 3: calculus on rings.** A process is a derivation of the ring of scalar fields (a
vector field), so that calculus starts from an $`\mathbb R`$-algebra $`F`$ and its derivations, not from limits.
A covector is a "Ricci wave" with crests. Two vocabulary items recur later: a vector $`X`$ with
$`\alpha X = 0`$ runs along the crests of $`\alpha`$, and $`\alpha`$ is then an "$`X`$-place" (§3.7.1–3.7.3); a vector
$`L`$ with $`\alpha L = 1`$ is the "Length" of $`\alpha`$, and $`\alpha`$ is the clock of $`L`$, its simultaneity (§3.7.4–3.7.5).

**Chapter 4: Grassmann.** There are two Grassmann algebras, of multivectors and of
multiforms, with no word mixing the two alphabets (§4.2.1). Creation $`\mathrm{cr}_X = X \wedge`$ raises
degree; evaluation is its transpose, $`\mathrm{ev}_X = (\mathrm{cr}_X)^*`$ (4.4.2), so $`\mathrm{ev}_{X \wedge Y} = \mathrm{ev}_Y \circ \mathrm{ev}_X`$ (4.4.5). Oziewicz
rejects "interior product": an evaluation is a contraction, not a product (§4.4.2).
Evaluation by a vector of degree one is postulated to be a derivation of degree $`-1`$ (4.4.9),
or derived from Laplace's expansion of determinants (§5.2). His analogy throughout is
chemical: creation adds an electron, evaluation ionises, and Grassmann's $`X \wedge X = 0`$ is
Pauli's exclusion. From the four nilpotents $`\mathrm{cr}_\alpha, \mathrm{cr}_X, \mathrm{ev}_\alpha, \mathrm{ev}_X`$ (4.6.1) and
$`\mathrm{ev}_X \mathrm{cr}_\alpha + \mathrm{cr}_\alpha \mathrm{ev}_X = \alpha X`$ (4.7.1) he builds two unipotents and four idempotents (§§4.7–4.8; MG1).
A bivector $`X \wedge Y`$ of two processes is their relative velocity, and
$`\mathrm{clock}_X(X \wedge Y) = \gamma\, v_{XY}`$ (4.2.15) is the binary velocity of step 1; heat capacities and the
Joule–Thomson coefficient are read the same way, as bivectors of thermodynamic processes.

**Chapter 5: derivations.** The graded commutator of derivations is a derivation (5.1.7);
$`d`$ is the nilpotent derivation of degree $`+1`$, and $`d^2 = 0`$ is "the definition of differential
calculus" (5.4.6). The Lie derivation is the square $`\mathcal L_X = (d + \mathrm{ev}_X)^2`$ (5.4.2, 5.5.3), credited to
Ślebodziński (1931), Oziewicz's teacher. §5.2 restates the idempotents with the remark
that an idempotent spin state is a pure state, and sets (5.2.7)–(5.2.10) as an exercise: $`M D = 0 = D M`$, $`\mathrm{cr}_\alpha \circ M = 0`$,
$`M \circ \mathrm{cr}_\alpha = \mathrm{cr}_\alpha \circ D = \mathrm{cr}_\alpha`$, $`D \circ \mathrm{ev}_X = \mathrm{ev}_X \circ M = \mathrm{ev}_X`$. The last two lines compose the vector-side $`M`$, $`D`$
with operators on forms. Read on forms with $`\mathcal M`$, $`\mathcal D`$, each composition holds in the reverse
order (checked): $`\mathcal M \circ \mathrm{cr}_\alpha = 0`$, $`\mathrm{cr}_\alpha \circ \mathcal M = \mathcal D \circ \mathrm{cr}_\alpha = \mathrm{cr}_\alpha`$, $`\mathrm{ev}_X \circ \mathcal D = \mathcal M \circ \mathrm{ev}_X = \mathrm{ev}_X`$.

**Chapter 6: integral laws.** Spin, not moving charge, is the source of magnetism (§6.1).
Each field has three "faces", each measured differently: for electricity, the force vector
$`\mathbf E`$, the work form $`E`$ (intensive) and the induced surface charge $`D`$ (extensive); for
magnetism, the force vector $`\mathbf B`$, the work bi-form $`B`$ and the induced line current $`H`$. The
integral is defined through the boundary, and $`\partial^2 = 0 \iff d^2 = 0`$ (§6.3.5).

**Chapter 7: the body.** Following Minkowski (1908), a material body is a vector $`P`$ with a
clock; $`\mathrm{clock}_P(L_P) = 1`$, $`P = E_P L_P`$, and $`E_P = \mathrm{clock}_P(P)`$ is its internal energy (7.2.1), an element of $`F`$, so an
energy field rather than a number. The
pair gives the idempotents $`\mathcal M, \mathcal D`$ (7.3.2), and $`\mathcal M`$ is a polariser that passes the forms of
the body's places, such as $`dx`$ for $`L = \partial_t`$ (7.3.5–7.3.7, Figure 7.2). §7.4 defines places and
simultaneity by these operators (MG2); §7.5 the private differential (MG3); §§7.6–7.7 split
Maxwell's law (MG4); §7.8 makes a body inertial if $`\mathcal M \circ d \circ \mathcal D = 0`$ and $`\mathcal L_L S = 0`$ (7.8.6); §7.9
defines $`E_L = \mathrm{ev}_L F`$ and $`B_L = \mathcal M F`$, so $`F = B_L + S \wedge E_L`$ (7.9.1)–(7.9.2), as Minkowski's relative
fields. §7.11 makes the metric an "environment" $`g`$ that pairs each vector with its clock,
$`\mathrm{clock}_X = gX/(gX)X`$ (7.11.2), which needs $`(gX)X`$ to be a unit of $`F`$, and intertwines the vector and form operators (MG5). §7.16
lists absolute concepts (bodies, events, the field, the speed of light in vacuum) against
relative ones (velocity, kinetic energy, places, $`E`$, $`B`$): relativity should be called
"absolutivity".

---

## 3. The observer operators, checked

**MG1 (four idempotents and a unipotent).** For a vector $`X`$ and a 1-form $`\alpha`$ with $`\alpha X = 1`$:

```math
\mathcal D=\mathrm{cr}_\alpha\circ\mathrm{ev}_X\in\text{der-alg},\quad \mathcal M=\mathrm{ev}_X\circ\mathrm{cr}_\alpha\in\text{alg-map},\quad \mathcal U=\mathrm{ev}_X+\mathrm{cr}_\alpha,\qquad \mathcal D+\mathcal M=\mathrm{id}=\mathcal U^2,
```

and likewise $`D = \mathrm{cr}_X \circ \mathrm{ev}_\alpha`$, $`M = \mathrm{ev}_\alpha \circ \mathrm{cr}_X`$, $`U = \mathrm{ev}_\alpha + \mathrm{cr}_X`$ on multivectors (§4.8, (5.2.5)–(5.2.6)).
These identities follow from (4.7.1) and $`\mathrm{ev}_X^2 = \mathrm{cr}_\alpha^2 = 0`$ alone, for a module of any rank: for
example $`\mathcal U^2 = \mathrm{ev}_X \mathrm{cr}_\alpha + \mathrm{cr}_\alpha \mathrm{ev}_X = \alpha X`$ and $`\mathcal D^2 = \mathrm{cr}_\alpha (\alpha X - \mathrm{cr}_\alpha \mathrm{ev}_X)\, \mathrm{ev}_X = \mathcal D`$; that $`\mathcal D`$ is a
derivation and $`\mathcal M`$ an algebra map is HH7(3) and MF1. Checked: idempotency, the split, the
(even) derivation and algebra-map properties, (4.7.1) in degrees 1–3, and (4.7.8)–(4.7.11), first
on random rational data and then symbolically, with generic $`X`$, $`\alpha`$ and generic forms, as
polynomial identities with integer coefficients modulo $`\alpha X - 1`$ (with $`\tfrac12`$ for $`e`$), so over
every commutative ring $`F`$ in a free module of rank 4. They are $`F`$-linear. On 1-forms $`\mathcal D \beta = \beta(X)\,\alpha`$, which is
the projector of MC6, and $`\mathcal M = 1 - \mathcal D`$. Not in the notes, and checked: $`\mathcal U \mathcal D \mathcal U = \mathcal M`$, so the two
idempotents are conjugate by the body's own unipotent. The same identities (except (4.7.8)–(4.7.11)) were
checked again with SageMath's exterior algebra in ranks 2 to 8 over $`\mathbb{Z}`$ and in ranks 2 to 6
over $`\mathrm{GF}(3)`$ and $`\mathrm{GF}(2)`$ ([`cartan_calculus_in_sympy.md`](cartan_calculus_in_sympy.md) §13.6).

**MG2 (places and simultaneity).** The forms of the body's places are
$`\mathrm{im}\,\mathcal M = \ker \mathcal D = \ker \mathrm{ev}_L`$, a subalgebra; the forms of its simultaneity are
$`\mathrm{im}\,\mathcal D = \ker \mathcal M = S \wedge \Lambda`$, an ideal. This is MF1, part 2, and it is what the notes say in §7.3
and in (7.4.7). Two definitions say otherwise. (7.4.2) gives $`\mathcal M \alpha = 0 \iff \mathrm{ev}_X \alpha = 0`$, and (7.4.5)
gives $`\mathcal D \beta = 0 \iff S \wedge \beta = 0`$. Checked counterexample to both: clock $`dt`$, $`L = \partial_t`$, $`dx`$ has
$`\mathrm{ev}_L\,dx = 0`$ and $`\mathcal D\,dx = 0`$, but $`\mathcal M\,dx = dx`$ and $`dt \wedge dx \ne 0`$. The 2014 text has the same two
lines, (5.4.2) and (5.4.5). Read with (7.4.6), which calls the simultaneity an ideal, the
intent is clear: the two conditions are exchanged.

**MG3 (the private differential exists exactly when the clock does not rotate).**
§7.5 asks for $`d_{\mathcal M}`$ on the places with $`d_{\mathcal M} \circ \mathcal M = \mathcal M \circ d`$ (7.5.2), and asks the student to deduce
$`\mathcal M \circ d \circ \mathcal D = 0`$ and $`(d_{\mathcal M})^2 = 0`$ (7.5.5)–(7.5.6). For every form $`\beta`$ (checked, with polynomial
fields and a rotating, accelerated clock):

```math
\mathcal M\,d\,\mathcal D\,\beta=(\mathcal M\,dS)\wedge\mathrm{ev}_L\beta,\qquad \mathcal M\,dS=\mathrm{ev}_L(S\wedge dS)=dS-S\wedge\mathcal L_LS ,
```

the second identity being the notes' own (7.8.5). So $`d_{\mathcal M}`$ is well defined exactly when
$`\mathcal M\,dS = 0`$, which is equivalent to $`S \wedge dS = 0`$ (since $`S \wedge \mathcal M\,dS = S \wedge dS`$ and $`\mathcal M\,dS`$ is a form of
the places). Then $`(d_{\mathcal M})^2 \mathcal M = \mathcal M\,d^2 = 0`$. In the notation of the October review of the algebra
of observers, $`\mathcal M\,dS = \Omega`$ is the rotation 2-form and $`\mathcal L_L S = a`$ the acceleration, $`dS = S \wedge a + \Omega`$;
MF10, part 2, is the case $`\beta = df`$. In Oziewicz's algebraic terms the statement is the Frobenius theorem for ideals. The
simultaneity forms $`I = S \wedge \Lambda = \mathrm{im}\,\mathcal D`$ are an ideal (MG2), and $`\mathrm{im}\,\mathcal M \cong \Lambda/I`$ as algebras. The
private differential is the differential that $`d`$ induces on the quotient $`\Lambda/I`$; it exists exactly
when $`I`$ is a differential ideal, $`dI \subset I`$. Since $`d(S \wedge \beta) = dS \wedge \beta - S \wedge d\beta`$, this holds exactly when $`dS \in I`$,
that is when $`\mathcal M\, dS = 0`$, that is when $`S \wedge dS = 0`$; the last step uses only the Length, because
$`\mathrm{ev}_L(S \wedge \mu) = \mu`$ for $`\mu`$ in $`\mathrm{im}\,\mathcal M`$, so $`S \wedge`$ is injective there. No points, leaves or partitions of unity
enter; the vector $`L`$ with $`S(L) = 1`$ does the work. In step 7's terms $`\mathcal M\, dS = \Omega`$ is the curvature of
the observer $`\Phi = L \otimes S`$ (the remark after HH7). Oziewicz's inertial body (7.8.6) asks for $`\Omega = 0`$ and $`a = 0`$,
that is $`dS = 0`$; the second condition of (7.8.6) follows from the first, since $`\mathcal L_L S = \mathrm{ev}_L\,dS`$.

**MG4 (Maxwell split for any clock).** With $`F = B + S \wedge E`$, $`B = \mathcal M F`$, $`E = \mathrm{ev}_L F`$ (7.9.2), $`dF = 0`$
splits into $`\mathcal M\,dF = 0`$ and $`\mathrm{ev}_L\,dF = 0`$ (7.6.2). Checked for $`F = dA`$ and the rotating,
accelerated clock:

```math
\mathcal M\,dB+\Omega\wedge E=0,\qquad \mathcal L_LB-\mathcal M\,dE+a\wedge E=0 .
```

The second is the notes' (7.7.4), derived there for a general clock; the version of §7.6,
$`\mathcal L_L B - d_{\mathcal M} E = 0`$ (7.6.8), is the case $`S = dt`$ and fails for the test clock. The first is the
magnetic Gauss law; the notes write it as $`d_{\mathcal M} B = 0`$ (7.6.3), which needs $`\Omega = 0`$ (MG3), and the
check confirms that $`\mathcal M\,dB \ne 0`$ when $`\Omega \ne 0`$. The last lines of (7.7.4) also use $`d_{\mathcal M}`$ and so hold only
for a non-rotating clock. With the sign $`F = B - \tau \wedge E`$ these are the first pair of the
observer-dependent Maxwell equations of the October review ($`d_s B = \Omega \wedge E`$,
$`\mathcal L_T B + d_s E = a \wedge E`$); the notes have them in 2014, without the rotation term.

**MG5 (the metric as intertwiner).** (7.11.4) states $`g \circ \mathrm{cr}_X = \mathrm{cr}_{gX} \circ g`$, $`g \circ \mathrm{ev}_\alpha = \mathrm{ev}_{g^{-1}\alpha} \circ g`$ and
$`g \circ U = \mathcal U \circ g`$, $`g \circ D = \mathcal D \circ g`$, $`g \circ M = \mathcal M \circ g`$, with $`g`$ extended to multivectors. The first two
hold; the last three need $`\alpha = gX`$, which with (7.11.2) means $`g(X, X) = 1`$. Checked: they hold
for the clock $`gX`$ and fail for a time-like $`X`$ with $`g(X, X) = -1`$, where (7.11.2) gives the clock
$`-gX`$. The notes fix no sign convention, and "time-like, $`g(X, X) = -1`$" presupposes an ordering of
$`F`$, which the algebraic setting does not supply; so this is a missing normalisation, not an error;
it is the convention of step 5, where $`X^2 = -g(X, X) = 1`$.

Other points (the normalisation $`\mathrm{clock}(g^{-1}\mathrm{clock}) = \det g^{-1}`$ in (7.8.4); the term $`\mathcal L_L(M^p F)`$ in (7.7.1), presumably $`\mathcal L_L(\mathcal D F)`$; references to a "Unit 1" that is not in this version) are listed with the translation.

**Kinematics and dynamics.** MG1, MG2 and MG5 are $`F`$-linear: they commute with multiplication
by scalar fields, hold event by event in any representation, and say nothing about
acceleration or rotation. MG3 and MG4 need $`d`$, a derivation that is not $`F`$-linear. This is the
division of Oziewicz (2007), whose abstract assigns kinematics to the associative Frobenius
algebra and dynamics to the "non-associative Frölicher-Richardson operator algebra"; step 7
takes up the second for one body (HH7, HH10).

---

## 4. Two ways to write an observer, and a third

The notes give a body two operators on forms and call them a pair of polarisers (§7.9.2):

- $`\mathcal D`$, a **derivation**, extends the rank-one projector $`\beta \mapsto \beta(L)\,S`$ of MC6 from 1-forms to all forms
  so that it counts the clock factor (0 or 1). It is the tool for splitting fields: $`\mathcal D F = S \wedge E`$.
- $`\mathcal M`$, an **algebra map**, extends the complementary projector multiplicatively. It is the
  tool for restricting the whole algebra to the places: it is what $`d_{\mathcal M}`$ needs.

On 1-forms they are the observer of 2007 and its complement; above degree 1 they are two
different extensions of it, $`\mathcal M = \Lambda(1 - X \otimes \alpha)`$ (MF1) and $`\mathcal D = \mathrm{id} - \mathcal M`$. On 1-forms their images
are direct summands of rank 1 and $`n - 1`$ (3 in spacetime), as for the rank-one projectors of OI5,
which carry no orientation. Ranks need $`\mathrm{der}\,F`$ finitely generated and projective (MF0); the
operator identities do not. Step 7 writes both as extensions of one tensor field, the observer
$`\Phi = L \otimes S`$: $`\mathcal D = \iota_\Phi`$ and $`\mathcal M = \Lambda(1 - \Phi)`$. Both are unchanged by the rescaling $`(L, S) \mapsto (fL, S/f)`$, $`f`$ a
unit of $`F`$, while $`\mathcal U`$ is not. That may be why the notes build on $`\mathcal D`$ and $`\mathcal M`$: they depend only on
the observer, not on the body's energy scale. This is a reading; the notes do not say so.

The notes also give the unipotent $`\mathcal U = \mathrm{ev}_L + \mathrm{cr}_S`$, but use it only in the split (4.8.1) and in
(7.11.4). Its idempotent $`e = \tfrac12(1 + \mathcal U)`$ is not in the text. It is a third observer: $`e\,\mathcal D\,e = e\,\mathcal M\,e = \tfrac12 e`$
(checked), and with a metric clock, $`S = gL`$, $`g(L, L) = 1`$,
$`\mathcal U`$ is the Clifford action of $`L`$ and $`e`$ is step 5's $`e_X`$. So the operator that sees the
Wigner rotation (OI3) is built from Oziewicz's unipotent, not from his idempotents. An earlier
version of this supplement said that $`e`$ needs the metric, or at least a symmetric clock factor;
step 6 settled it: $`e`$ needs no metric, and the symmetrised clock factor $`s_{XY} = \tfrac12(\alpha Y + \beta X)`$
appears by itself, $`e_X\, \mathcal U_Y\, e_X = s_{XY}\, e_X`$, round a triangle giving a rotation or a boost by the sign of
a determinant of clock factors (GB2, GB3). Like $`\mathcal U`$, $`e`$ changes under the rescaling, so it
depends on the body and not only on the observer.

---

## 5. What the notes do not contain

- No second body enters the operators: there is no product $`\mathcal M_Y \mathcal M_X`$, no relative velocity
  beyond (4.2.15), and no Wigner rotation.
- The rotation of a clock appears only as the obstruction to $`d_{\mathcal M}`$ ((7.8.5) and the
  definition of inertia); it is not named as vorticity, and the spin of §6.1 is not connected
  to it. Steps 3 and 4 make that connection ($`\alpha \wedge d\alpha`$, MF11; CS5, CS6).
- The polarisers are $`F`$-linear. Everything that needs $`d`$ (MG3, MG4) is in chapter 7, and
  the notes give it as exercises, with hints, not as proofs.

---

## 6. Verification record

[`src/verify_magnetismo.py`](../src/verify_magnetismo.py), SymPy, exact; about four minutes. The checks
use one representation: forms on $`\mathbb R^4`$, a free module of rank 4, as dicts over basis masks.
Chapter 4 is checked twice: with random rational $`(X, \alpha)`$, and symbolically with generic $`X`$, $`\alpha`$ and
generic forms, reducing modulo $`\alpha X - 1`$, so that the identities hold over every commutative ring.
Chapter 7 uses a polynomial Length field and a clock that both rotates and accelerates, and
$`F = dA`$ for a polynomial $`A`$; a counterexample in this representation refutes a general statement.
36 checks, all pass: chapters 4 and 5 (MG1, (5.2.9)–(5.2.10) and the third observer $`e`$, 9
checks with rationals and 7 symbolic), chapter 7 (MG2–MG4, 18, and one set-up check), (7.11.4)
(MG5, 1). The expected failures (MG2's counterexamples, (7.6.8) for a rotating clock, (7.11.4)
with $`g(X, X) = -1`$) are asserted as failures. The algebraic form of MG3 (differential ideal) is
proved by hand from the identity $`\mathcal M\, d\, \mathcal D\, \beta = (\mathcal M\, dS) \wedge \mathrm{ev}_L \beta`$, which is checked.

**Not verified:** the readings of the text (paraphrased from the Spanish), the history in
§§1–2, and the claim that the 2014 and 2020 texts agree in substance outside the lines
compared.

---

## References

- Z. Oziewicz, *Magnetismo e Electricidad*, lecture notes (Spanish), UNAM FES Cuautitlán,
  version of 18 July 2020, 111 pp.; earlier version *Electricidad e Magnetismo*, 10 May 2014,
  77 pp. Unpublished; sent to B. Page on 20 and 23 July 2020. Not committed.
- Z. Oziewicz, "Relativity groupoid, instead of relativity group", *Int. J. Geom. Methods Mod.
  Phys.* 4 (2007), [arXiv:math/0608770](https://arxiv.org/abs/math/0608770).
- H. Minkowski, "Die Grundgleichungen für die elektromagnetischen Vorgänge in bewegten
  Körpern", *Nachr. Ges. Wiss. Göttingen* (1908) 53–111. Cited through the notes; not re-read.
- W. Ślebodziński, "Sur les équations canoniques de Hamilton", *Bull. Acad. Roy. de Belg.* 17
  (1931) 864–870. Cited from memory, through the notes (the Lie derivative); not re-read.
- The ladder: [`mass_centre.md`](../analysis/mass_centre.md) (MC6),
  [`metric_free_body.md`](../analysis/metric_free_body.md) (MF1, MF10, MF11),
  [`clock_centre.md`](../analysis/clock_centre.md) (CS5, CS6),
  [`observer_idempotents.md`](../analysis/observer_idempotents.md) (OI1, OI3, OI5),
  [`grammar_of_a_body.md`](../analysis/grammar_of_a_body.md) (GB2, GB3),
  [`heat_and_helicity.md`](../analysis/heat_and_helicity.md) (HH2, HH7, HH10).
