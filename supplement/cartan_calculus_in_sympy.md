# Cartan's calculus in SymPy: how the scripts in `src/` compute

> A tutorial on the machinery that the `verify_*.py` scripts use for the exterior algebra and Cartan's calculus. Each script carries its own copy, of twenty to a hundred lines, and the copies differ in naming and in the encoding of a basis form, so this note explains one version and gives a dictionary to the others. A differential form is a Python dictionary from basis forms to SymPy coefficients, the basis form keyed either by a sorted tuple of indices or by a bitmask. The wedge product, the interior product and the exterior derivative are each a double loop with a sign, and the sign is the parity of a count of index pairs, derived in §3 to §5; the Lie derivative is then Cartan's formula $`L_X = \iota_X d + d\iota_X`$. Pointwise operators are also written as $`2^n \times 2^n`$ matrices, in which evaluation is the transpose of creation and the two obey the canonical anticommutation relations; adding a bilinear form gives the Clifford product on the same space. The note then explains how a check is made exact (generic coefficients, rational spot checks, side conditions such as $`\alpha(X) = 1`$ handled exactly or modulo an ideal, unknown coefficients solved for, pullback by a diffeomorphism) and lists the conventions and pitfalls. A last section explains why the scripts do not use an existing library and surveys the alternatives (GAlgebra, SageMath, the Maple packages CLIFFORD and DifferentialGeometry, FriCAS, Lean with Mathlib), with what a check in coordinates proves about a result meant for every dimension. A cross-check with Maple's DifferentialGeometry package (58 checks, and eight objects compared term by term with the SymPy functions) confirms the conventions and the identities and records some traps in that package. The companion script runs 42 exact checks, including two that show a check can fail.

**Status.** Supplement: a tutorial on methods, not a reading of a paper and not a ladder
step. Requested by Bill Page, 22 November 2026. Drafted with Claude (Anthropic) and subject
to review. Companion script
[`src/verify_cartan_tutorial.py`](../src/verify_cartan_tutorial.py): a minimal version of
the machinery, with the code quoted below, and 42 exact checks (SymPy), labelled CT-A1 to
CT-J4 by the section letters of the script. **[verified]** marks a statement checked
there. The identities of §3 to §6 are textbook results; the checks certify the code, not
the mathematics. Statements about the other scripts describe their code at commit
`17c9f4c` and were read from it, not run.
[PDF](https://github.com/billpage/oziewicz/releases/latest/download/cartan_calculus_in_sympy.pdf)

---

## 1. What is computed, and the notation

Let $`V = \mathbb{R}^n`$ with coordinates $`x^0, \dots, x^{n-1}`$. In the scripts $`n = 4`$
and $`(x^0, x^1, x^2, x^3) = (t, x, y, z)`$. The coordinate vector fields are
$`\partial_i = \partial/\partial x^i`$ and the coordinate 1-forms $`dx^i`$, with
$`dx^i(\partial_j) = \delta^i_j`$.

For a set of indices $`S = \{i_1 < i_2 < \dots < i_k\} \subseteq \{0, \dots, n-1\}`$ write

```math
dx^S = dx^{i_1} \wedge dx^{i_2} \wedge \cdots \wedge dx^{i_k}, \qquad dx^{\varnothing} = 1, \qquad |S| = k .
```

The $`2^n`$ forms $`dx^S`$ are a basis of the Grassmann algebra $`\Lambda V^*`$ (at each
point). A form is $`\beta = \sum_S \beta_S\, dx^S`$, with coefficients $`\beta_S`$ that are
functions of the coordinates; it is a $`k`$-form, of degree $`k`$, if $`\beta_S = 0`$
whenever $`|S| \neq k`$. A vector field is $`X = X^i \partial_i`$ and a 1-form is
$`\alpha = \alpha_i\, dx^i`$ (summation over repeated indices). The evaluation of a
1-form on a vector is $`\alpha(X) = \alpha_i X^i`$.

The four operators on forms, in the notations of Oziewicz, of the textbooks and of the
scripts:

| Operator | Oziewicz (*Magnetismo*; 1986) | Textbook | Script names |
|---|---|---|---|
| creation, $`\beta \mapsto \alpha \wedge \beta`$ | $`\mathrm{cr}_\alpha`$; $`e_\alpha`$ | $`\alpha \wedge`$ | `wedge`, `wed`, `fw`, `cr`, `cre`, `E` |
| evaluation (interior product) | $`\mathrm{ev}_X`$; $`i_X`$ | $`\iota_X`$ | `iv`, `interior`, `fiv`, `ev`, `ann`, `I` |
| exterior derivative | $`d`$ | $`d`$ | `d`, `ext`, `fd` |
| Lie derivative | $`L_X`$ | $`L_X`$, $`\mathcal{L}_X`$ | `lie`, `flie` |

The first two act pointwise: $`(\alpha \wedge \beta)(p)`$ depends only on $`\alpha(p)`$ and
$`\beta(p)`$. They are linear over the functions $`F`$, the property Oziewicz calls
$`F`$-linear. The last two differentiate the coefficients.

## 2. A form is a dictionary

Every script stores a form as a Python `dict` whose keys name the basis forms $`dx^S`$ and
whose values are the coefficients $`\beta_S`$, any SymPy expression: an integer, a
`Rational`, a `Symbol`, or an undefined function such as `sp.Function("A1")(t, x, y, z)`.
Two encodings of the key are in use.

| Encoding | Key of $`dx^S`$ | Key of $`1`$ | Scripts |
|---|---|---|---|
| sorted tuple | `(i1, i2, ..., ik)` | `()` | `heat_and_helicity`, the `Form` class of `metric_free` |
| bitmask | $`\sum_{i \in S} 2^i`$ | `0` | `magnetismo`, `grammar_of_a_body`, `grassmann_clifford`, `observer_idempotents`, the `Grassmann` class of `metric_free` |

For example $`dt \wedge dy - 3x\, dx \wedge dz`$ is `{(0, 2): 1, (1, 3): -3*x}` with tuples
and `{0b0101: 1, 0b1010: -3*x}` = `{5: 1, 10: -3*x}` with bitmasks. Bit $`i`$ of the mask is
$`dx^i`$. The bitmask makes "is $`i`$ in $`S`$" a bit test and $`S \cup T`$, for disjoint
sets, the bitwise or.

A dictionary is in *canonical form* if every coefficient is expanded and no coefficient is
zero. Every operation ends with `clean`, so two forms are equal exactly when their
dictionaries are equal, and a form is zero exactly when its dictionary is empty:

```python
def clean(f):
    """canonical form: expanded coefficients, zeros dropped"""
    out = {}
    for k, v in f.items():
        v = sp.expand(v)
        if v != 0:
            out[k] = v
    return out


def add(*fs):
    out = {}
    for f in fs:
        for k, v in f.items():
            out[k] = out.get(k, 0) + v
    return clean(out)


def sm(c, f):
    return clean({k: c * v for k, v in f.items()})


def eq(f, g):
    return add(f, sm(-1, g)) == {}
```

The names vary (`scale`, `fsm`, `csm` for `sm`; `iszero`, `feq`, `ciszero`), and some
scripts call `sp.simplify` in place of `sp.expand`; §10 says when that matters. The point
of the dictionary is that nothing else is needed: there is no basis object, the zero
coefficients cost nothing, and the coefficients can be anything SymPy can differentiate.

## 3. The wedge product and its sign

For disjoint index sets $`A`$ and $`B`$,

```math
dx^A \wedge dx^B = \varepsilon(A, B)\, dx^{A \cup B}, \qquad
\varepsilon(A, B) = (-1)^{N(A, B)}, \qquad
N(A, B) = \#\{(a, b) \in A \times B : a > b\},
```

and $`dx^A \wedge dx^B = 0`$ if $`A \cap B \neq \varnothing`$. *Derivation.* Write the
factors of $`dx^A`$ and then those of $`dx^B`$, each in increasing order. Sort the list by
moving the factors of $`dx^B`$ to the left one at a time, smallest first. The factor
$`dx^b`$ has to pass exactly the $`dx^a`$ with $`a \in A`$ and $`a > b`$ (the factors of
$`B`$ already moved are smaller than $`b`$). Each exchange of two adjacent 1-forms gives a
factor $`-1`$, since $`dx^a \wedge dx^b = -dx^b \wedge dx^a`$. $`\square`$

*Example.* $`dx^{\{1,3\}} \wedge dx^{\{0,2\}}`$: the pairs with $`a > b`$ are $`(1,0)`$,
$`(3,0)`$, $`(3,2)`$, so $`N = 3`$ and
$`dx^1 \wedge dx^3 \wedge dx^0 \wedge dx^2 = -dx^0 \wedge dx^1 \wedge dx^2 \wedge dx^3`$.
**[verified]** CT-A1.

The two encodings count $`N(A, B)`$ in two ways.

- **Tuples.** `perm_sign(a + b)` counts the inversions of the concatenated tuple. The
  inversions inside `a` and inside `b` are zero because both are sorted, so the count is
  $`N(A, B)`$.
- **Bitmasks.** For each $`j \in B`$, the elements of $`A`$ above $`j`$ are the set bits of
  `a >> (j + 1)`, so $`N(A, B) = \sum_{j \in B} \mathrm{popcount}(a \gg (j+1))`$.

```python
def bits(m):
    """indices i with bit i set in m, increasing"""
    return [i for i in range(m.bit_length()) if m >> i & 1]


def sign_merge(a, b):
    """sign of dx^a ^ dx^b = sign * dx^(a|b), a & b == 0: (-1)^(pairs i in a, j in b, i > j)"""
    s = 1
    for j in bits(b):
        if bin(a >> (j + 1)).count("1") % 2:
            s = -s
    return s


def wedge(f, g):
    out = {}
    for a, ca in f.items():
        for b, cb in g.items():
            if a & b == 0:
                out[a | b] = out.get(a | b, 0) + sign_merge(a, b) * ca * cb
    return clean(out)
```

and with tuples

```python
def perm_sign(seq):
    s, seq = 1, list(seq)
    for i in range(len(seq)):
        for j in range(i + 1, len(seq)):
            if seq[i] > seq[j]:
                s = -s
    return s


def wedge_t(f, g):
    out = {}
    for a, ca in f.items():
        for b, cb in g.items():
            if set(a) & set(b):
                continue
            k = tuple(sorted(a + b))
            out[k] = out.get(k, 0) + perm_sign(a + b) * ca * cb
    return clean(out)
```

The two give the same product on random forms and on generic forms of every pair of
degrees. **[verified]** CT-A2, CT-A3. The product is associative, graded commutative,
$`\beta \wedge \gamma = (-1)^{pq} \gamma \wedge \beta`$ for a $`p`$-form $`\beta`$ and a
$`q`$-form $`\gamma`$, and $`\alpha \wedge \alpha = 0`$ for a 1-form. **[verified]** CT-B1
to CT-B3.

`grammar_of_a_body` calls the sign function `wedge_basis` and returns `(0, 0)` for
overlapping sets; `magnetismo` calls it `sign_merge` and loops over all $`n`$ bits.

## 4. The interior product

On a basis form, with the positions $`p`$ of the indices counted from $`0`$,

```math
\iota_X\, dx^{i_0} \wedge \cdots \wedge dx^{i_{k-1}}
= \sum_{p=0}^{k-1} (-1)^p\, X^{i_p}\, dx^{i_0} \wedge \cdots \wedge \widehat{dx^{i_p}} \wedge \cdots \wedge dx^{i_{k-1}},
```

where the hat means omission. This is the contraction of $`X`$ into the *first* slot,
$`(\iota_X \beta)(Y_1, \dots, Y_{k-1}) = \beta(X, Y_1, \dots, Y_{k-1})`$, with the
determinant normalisation $`dx^S(\partial_{i_0}, \dots, \partial_{i_{k-1}}) = 1`$. In the
bitmask encoding the position of $`i`$ in $`S`$ is the number of elements of $`S`$ below
$`i`$, `popcount(m & ((1 << i) - 1))`:

```python
def iv(V, f):
    """interior product i_V: contracts the first slot, sign (-1)^(position of i)"""
    out = {}
    for m, c in f.items():
        for i in bits(m):
            s = (-1) ** bin(m & ((1 << i) - 1)).count("1")
            out[m ^ 1 << i] = out.get(m ^ 1 << i, 0) + s * V[i] * c
    return clean(out)
```

With tuples the position is the loop index: `for pos, i in enumerate(a)` with sign
`(-1) ** pos` and key `a[:pos] + a[pos + 1:]` (`interior` in `heat_and_helicity`, `iv` in
`metric_free`). The vector field `V` is a list of $`n`$ components. For example
$`\iota_X(dt \wedge dx \wedge dy) = X^0\, dx \wedge dy - X^1\, dt \wedge dy + X^2\, dt \wedge dx`$.
**[verified]** CT-C4.

The properties used throughout the ladder are

```math
\iota_X \alpha = \alpha(X), \qquad \iota_X \iota_Y = -\iota_Y \iota_X, \qquad \iota_X \iota_X = 0,
```
```math
\iota_X(\beta \wedge \gamma) = (\iota_X \beta) \wedge \gamma + (-1)^r\, \beta \wedge \iota_X \gamma \qquad (\beta \text{ of degree } r),
```

the last being Oziewicz's (4.7.1) in *Magnetismo*: $`\iota_X`$ is an *antiderivation* of
degree $`-1`$. **[verified]** CT-C1 to CT-C3. The sign convention matters: contracting the
*last* slot instead gives an operator for which the rule above is false already for
$`\deg \beta = 1`$ (it is an antiderivation from the right). **[verified]** CT-C3'. The
1986 paper composes interior products of a product in reverse order,
$`i_{x \wedge y} = i_y i_x`$ (its eq. (12)); Jadczyk (2021) takes $`i_{f \wedge g} = i_f i_g`$,
and the two differ by a sign on 2-vectors (see
[`grassmann_to_clifford.md`](grassmann_to_clifford.md) §10.4).

## 5. The exterior derivative

On a monomial,

```math
d\big(c\, dx^S\big) = \sum_{i \notin S} \partial_i c\; dx^i \wedge dx^S
= \sum_{i \notin S} \varepsilon(\{i\}, S)\, \partial_i c\; dx^{S \cup \{i\}},
\qquad \varepsilon(\{i\}, S) = (-1)^{\#\{s \in S : s < i\}},
```

so the sign is the same bit count as for the interior product, and the new factor
$`dx^i`$ is put on the *left* (the standard convention, for which $`d`$ is an
antiderivation with the sign $`(-1)^p`$ below):

```python
def d(f, xs):
    """exterior derivative: d(c dx^m) = sum_i (d_i c) dx^i ^ dx^m"""
    out = {}
    for m, c in f.items():
        for i, x in enumerate(xs):
            if not m >> i & 1:
                s = sign_merge(1 << i, m)
                out[m | 1 << i] = out.get(m | 1 << i, 0) + s * sp.diff(c, x)
    return clean(out)
```

Here `xs` is the list of coordinate symbols; `magnetismo` and `grammar_of_a_body` use a
global list instead (`X4`, `CO`). With tuples the sign is `perm_sign((i,) + a)`.

The coefficients may be undefined functions. Then `sp.diff` returns `Derivative` objects,
SymPy orders the variables of a mixed derivative canonically, and `sp.expand` alone
decides that $`\partial_x \partial_y A - \partial_y \partial_x A = 0`$. That is why

```math
df = \partial_i f\, dx^i, \qquad d\,d = 0, \qquad
d(\beta \wedge \gamma) = d\beta \wedge \gamma + (-1)^p\, \beta \wedge d\gamma \qquad (\beta \text{ of degree } p)
```

can be checked on generic forms whose 16 coefficients are independent undefined functions
of $`(t, x, y, z)`$, with no simplification. **[verified]** CT-D1 to CT-D3.

## 6. Cartan's calculus

The Lie derivative of a form is computed from Cartan's formula,

```math
L_X = \iota_X d + d\, \iota_X ,
```

```python
def lie(V, f, xs):
    """Cartan's formula L_V = i_V d + d i_V"""
    return add(iv(V, d(f, xs)), d(iv(V, f), xs))


def bracket(U, V, xs):
    """[U, V]^i = U^j d_j V^i - V^j d_j U^i"""
    n = len(xs)
    return [sp.expand(sum(U[j] * sp.diff(V[i], xs[j]) - V[j] * sp.diff(U[i], xs[j])
                          for j in range(n))) for i in range(n)]
```

That Cartan's formula agrees with the definition of $`L_X`$ by the flow of $`X`$ is a
theorem (for example Kolář, Michor and Slovák, Chapter II); the scripts take the formula as
the definition and do not check the theorem. The structure is clearest with graded
commutators $`[P, Q] = PQ - (-1)^{pq} QP`$, where $`p`$, $`q`$ are the degrees of the
operators: $`\iota_X`$ has degree $`-1`$, $`d`$ degree $`+1`$, $`L_X`$ and $`\alpha \wedge`$
for a 0-form degree $`0`$. Then $`L_X = [\iota_X, d]`$ and

```math
[d, d] = 2d^2 = 0, \quad [\iota_X, \iota_Y] = 0, \quad [L_X, d] = 0, \quad
[L_X, \iota_Y] = \iota_{[X,Y]}, \quad [L_X, L_Y] = L_{[X,Y]},
```

with $`[X, Y]^i = X^j \partial_j Y^i - Y^j \partial_j X^i`$; and $`L_X`$ is a derivation of
degree $`0`$, $`L_X(\beta \wedge \gamma) = L_X \beta \wedge \gamma + \beta \wedge L_X \gamma`$,
with $`L_X u = X^i \partial_i u`$ on functions. All of these hold for generic vector fields
$`X`$, $`Y`$ and a generic form, with every component an undefined function of
$`(t, x, y, z)`$. **[verified]** CT-E1 to CT-E6. The bracket convention is fixed by the
fifth identity: with $`-[X, Y]`$ it fails. **[verified]** CT-E3'.

The scripts apply Cartan's calculus only to forms. For other tensors they work in
components: `lie11` in `heat_and_helicity` computes
$`(L_V T)^m{}_n = V^l \partial_l T^m{}_n - T^l{}_n \partial_l V^m + T^m{}_l \partial_n V^l`$
for a $`(1,1)`$ tensor stored as a $`4 \times 4`$ matrix, and the Nijenhuis torsion of
$`\Phi = X \otimes \alpha`$ in part I there is assembled from `bracket`.

### 6.1 A worked example: one body in flow-box coordinates

A body is a pair $`(X, \alpha)`$ with $`\alpha(X) = 1`$. Near any point there are
coordinates with $`X = \partial_t`$ and $`\alpha = dt + A`$, $`A = A_i(t, x, y, z)\, dx^i`$
($`i = 1, 2, 3`$) (Lemma HH1 of [`heat_and_helicity.md`](../analysis/heat_and_helicity.md)).
Its acceleration and rotation are

```math
a = \iota_X d\alpha, \qquad \Omega = d\alpha - \alpha \wedge a .
```

```python
Af = form1([0] + [sp.Function(f"A{i}")(*XS) for i in (1, 2, 3)])
alpha = add({1: 1}, Af)                     # dt + A
Xb = [1, 0, 0, 0]                           # d_t
dal = d(alpha, XS)
acc = iv(Xb, dal)                           # a
Om = add(dal, sm(-1, wedge(alpha, acc)))    # Omega
```

with `form1(c)` the 1-form $`c_i\, dx^i`$ and `XS = (t, x, y, z)`. Then
$`a = \partial_t A`$, $`\iota_X a = 0`$, $`\iota_X \Omega = 0`$ and, by Cartan's formula,
$`L_X \alpha = \iota_X d\alpha + d(\alpha(X)) = a`$. **[verified]** CT-H1 to CT-H3. A clock
need not be integrable: $`\alpha = dt + x\, dy`$ has
$`\alpha \wedge d\alpha = dt \wedge dx \wedge dy \neq 0`$ and $`d\alpha \wedge d\alpha = 0`$
(class 3). **[verified]** CT-H4.

## 7. Pointwise operators as matrices

An $`F`$-linear operator with constant coefficients is a linear map of the
$`2^n`$-dimensional space $`\Lambda V^*`$, so it is a $`2^n \times 2^n`$ matrix. The
simplest way to get the matrix is to apply the dictionary function to each basis form:
column $`m`$ holds the coefficients of the image of $`dx^m`$.

```python
def op_matrix(op, n=N):
    """the matrix of a linear operator on forms in the bitmask basis: column m is op(dx^m)"""
    M = sp.zeros(1 << n, 1 << n)
    for m in range(1 << n):
        for k, c in op({m: sp.Integer(1)}).items():
            M[k, m] = c
    return M


unit = lambda i: [int(j == i) for j in range(N)]                         # d_i as a list
cre = [op_matrix(lambda f_, i=i: wedge({1 << i: 1}, f_)) for i in range(N)]   # cr_{dx^i}
ann = [op_matrix(lambda f_, i=i: iv(unit(i), f_)) for i in range(N)]         # ev_{d_i}
```

The other scripts build the same matrices directly from the bit-count signs (`Grassmann._cre`
in `metric_free`, `cr` and `ev` in `grammar_of_a_body`, `E` in `grassmann_clifford`,
`wedge_mat` and `ev_mat` in `heat_and_helicity`). Write $`c_i = \mathrm{cr}_{dx^i}`$
(creation) and $`a_i = \mathrm{ev}_{\partial_i}`$ (annihilation).

**Evaluation is the transpose of creation,** $`a_i = c_i^{\mathsf T}`$. The basis $`dx^S`$
is orthonormal for the determinant pairing of forms with multivectors,
$`\langle dx^S, \partial_T \rangle = \delta_{ST}`$, and the interior product is the
transpose of exterior multiplication under that pairing; this is eq. (9) of the 1986
paper, where the roles of vectors and forms are exchanged. The scripts use it as
`ann = [c.T for c in cre]` and `I = [M.T for M in E]`. **[verified]** CT-F1.

**The canonical anticommutation relations (CAR) hold,** with $`\{P, Q\} = PQ + QP`$:

```math
\{a_i, c_j\} = \delta_{ij}\, 1, \qquad \{c_i, c_j\} = 0 = \{a_i, a_j\} .
```

**[verified]** CT-F2. This is the 1986 paper's eq. (16): exterior multiplication and its
transpose are fermion operators, and no metric is involved.

**Oziewicz's observers follow by linearity.** With $`\mathrm{cr}_\alpha = \alpha_i c_i`$ and
$`\mathrm{ev}_X = X^i a_i`$, $`\{\mathrm{ev}_X, \mathrm{cr}_\alpha\} = \alpha(X)\, 1`$. Hence
for $`U = \mathrm{ev}_X + \mathrm{cr}_\alpha`$, $`\mathcal D = \mathrm{cr}_\alpha \mathrm{ev}_X`$ and
$`\mathcal M = \mathrm{ev}_X \mathrm{cr}_\alpha`$ (the operators of *Magnetismo*),

```math
U^2 = \alpha(X)\, 1, \qquad \mathcal D + \mathcal M = \alpha(X)\, 1, \qquad \mathcal D \mathcal M = 0 ,
```

for symbolic $`X`$ and $`\alpha`$. **[verified]** CT-F3, CT-F4.

The matrix form buys three things the dictionaries do not give directly: ranks (kernels
and images, as in part A of `metric_free`), the dimension of the algebra generated by a
set of operators (`alg_dim` in `heat_and_helicity`, by growing a span of products until
its rank stops increasing), and the Clifford product of §8. It costs two things. Only
$`F`$-linear operators are matrices; $`d`$ and $`L_X`$ act on the coefficients and are
not. And the order of the basis differs between scripts: the matrix index is the bitmask
in `grammar_of_a_body`, `grassmann_clifford` and the script here; it is sorted by grade and
then bitmask in `metric_free` (`self.subs`); and it is the grade-by-grade order of
`itertools.combinations` in `heat_and_helicity`. Matrices from different scripts are
conjugate by a permutation, not equal entry by entry.

Left multiplication by a general form $`\beta = \sum_S \beta_S\, dx^S`$ is
$`\sum_S \beta_S\, c_{i_1} c_{i_2} \cdots c_{i_k}`$ (`Grassmann.lmul` in `metric_free`, the
blade operators `EB` in `grassmann_clifford`).

## 8. The Clifford product on the same space

Let $`\varphi`$ be an $`n \times n`$ matrix, a bilinear form on vectors with no symmetry
assumed, and put (1986, eq. (23.2); Chevalley's construction)

```math
\gamma_i = c_i + \varphi_{ij}\, a_j .
```

Then $`\{\gamma_i, \gamma_j\} = (\varphi_{ij} + \varphi_{ji})\, 1`$: only the symmetric part
of $`\varphi`$ enters the relations. And $`\gamma_i \gamma_j\, 1 = e_i \wedge e_j + \varphi_{ij}`$,
so applying products of $`\gamma`$'s to the unit $`1`$ (the column for $`m = 0`$) gives
the Clifford product of vectors as an element of the same $`2^n`$-dimensional space.
**[verified]** CT-G1, CT-G2 (for $`n = 3`$ and generic $`\varphi`$). Here
$`e_i`$ stands for the basis element with bitmask $`2^i`$; in the 1986 paper the
space is that of multivectors, and the code does not distinguish. How
`grassmann_clifford` extends $`\gamma`$ from vectors to all blades (the unipotent matrix
`W` and its inverse), and what the antisymmetric part of $`\varphi`$ does, is in
[`grassmann_to_clifford.md`](grassmann_to_clifford.md).

Two shortcuts are used for the Clifford product itself.

- **The blade table** (`observer_idempotents`, for $`Cl(V, -g)`$ in an orthonormal
  basis). For orthogonal generators with $`e_i^2 = \sigma_i`$ the product of basis blades
  is $`e_A e_B = \pm \big(\prod_{i \in A \cap B} \sigma_i\big)\, e_{A \triangle B}`$
  ($`\triangle`$ the symmetric difference, `a ^ b` on bitmasks), with the reordering sign
  $`(-1)^{N(A,B)}`$ of §3 now counted over all pairs, shared indices included. It is the
  Chevalley product for $`\varphi = \mathrm{diag}(\sigma)`$, on all $`16 \times 16`$ pairs of
  blades, and for $`\sigma = 0`$ it is the wedge product. **[verified]** CT-G3, CT-G4.
- **Word rewriting** (class `Cl` in `grammar_of_a_body`, for any symmetric $`B`$). An
  element is a dictionary from increasing words $`(i_1 < \dots < i_k)`$ to coefficients.
  Multiplying a word by a generator $`e_g`$ from the right uses
  $`e_\ell e_g = 2B_{\ell g} - e_g e_\ell`$ when the last letter $`\ell > g`$,
  $`e_g e_g = B_{gg}`$, and recursion; the results are memoised with `lru_cache`.

## 9. How a check is made exact

Every check computes the difference of the two sides and asks whether it is zero. What a
"yes" proves depends on what the coefficients are.

| Strategy | What a pass proves | Examples |
|---|---|---|
| Generic coefficients: independent `Symbol`s, or undefined `Function`s of the coordinates | The identity for all forms and fields (polynomial in the coefficients and their derivatives) | CT-B, CT-C, CT-D, CT-E; `magnetismo` chapter 4 "symbolically"; `grassmann_clifford` with generic $`\varphi`$ |
| Random rationals | Nothing in general: exact arithmetic at one point. A failure disproves | CT-A2, CT-J4; `magnetismo` chapter 4 first pass; `rational_pair` in `grammar_of_a_body` |
| Side condition kept as a symbol, or the identity checked modulo an ideal | The identity wherever the condition holds, over any commutative ring if the coefficients are integers | CT-J1 to CT-J3; `magnetismo` (`zero_mod`), `metric_free` part A |
| Unknown coefficients solved for | The answer within the ansatz only | `heat_and_helicity` parts K to M |
| Pullback by a diffeomorphism | Naturality, for the diffeomorphism used | CT-I; `grammar_of_a_body` part G4 |

**Generic coefficients.** `gform("f")` returns the form with 16 independent symbols
$`f_0, \dots, f_{15}`$ as coefficients, and `gform("F", args=XS)` one with 16 undefined
functions. An identity that is polynomial in the coefficients and holds with independent
symbols holds for every specialisation, so a pass with `expand` is a proof.

**Side conditions.** Many of Oziewicz's identities need $`\alpha(X) = 1`$. There are three
ways to impose it.

1. Normalise: choose numbers and divide $`\alpha`$ by $`\alpha(X)`$. Exact, but only at
   that point (CT-J4).
2. Keep $`s = \alpha(X)`$ as a polynomial in the symbols and check the homogenised
   identity, which holds exactly: $`\mathcal D^2 = s\mathcal D`$, $`\mathcal M^2 = s\mathcal M`$,
   $`s\, \mathcal M(f \wedge g) = \mathcal M f \wedge \mathcal M g`$. **[verified]** CT-J1, CT-J3.
3. Check membership in the ideal $`(s - 1)`$: divide each coefficient of the difference by
   $`s - 1`$ and test that the remainder is zero. A single polynomial is a Gröbner basis of
   the ideal it generates, so remainder zero is equivalent to membership.

```python
def zero_mod(f_):
    """each coefficient lies in the ideal (s - 1), s = alpha(X): remainder 0 on division"""
    rem = lambda c: sp.reduced(sp.expand(c), [s - 1], *GENS, order="lex")[1]
    return all(sp.expand(rem(c)) == 0 for c in f_.values())
```

$`\mathcal M(f \wedge g) - \mathcal M f \wedge \mathcal M g`$ is not zero, but it is zero
modulo $`s - 1`$: $`\mathcal M`$ is an algebra map exactly when $`\alpha(X) = 1`$.
**[verified]** CT-J2. With integer coefficients (and $`\tfrac12`$ where an idempotent
  needs it) the identity holds over every commutative ring in which those numbers make
  sense; this is how `magnetismo` states MG1.

**Unknown coefficients.** To find all operators of a given form, `heat_and_helicity`
writes an ansatz with unknown symbols, substitutes jets of a generic body, collects the
coefficients of every monomial in the jet variables with `sp.Poly(expr, *vars).coeffs()`,
and solves the resulting linear system with `sp.solve`. The result is complete only
within the ansatz, which is why HH8 and HH9 are stated "granted finite order and
polynomiality".

**Pullback.** For a map $`\phi`$ with Jacobian $`D\phi`$, forms pull back by substitution
and $`dx^i \mapsto d\phi^i`$, and vector fields by $`\phi^* V = (D\phi)^{-1} (V \circ \phi)`$:

```python
def pull_form(f_):
    """phi^* f = sum_m (c o phi) dphi^(i1) ^ ... ^ dphi^(ik)"""
    dphi = [form1([sp.diff(phimap[i], c) for c in XS]) for i in range(4)]
    out = {}
    for m, c in f_.items():
        term = {0: sp.sympify(c).subs(sub, simultaneous=True)}
        for i in bits(m):
            term = wedge(term, dphi[i])
        out = add(out, term)
    return out


def pull_vec(V):
    """phi^* V = (D phi)^-1 (V o phi)"""
    Vp = sp.Matrix([sp.sympify(v).subs(sub, simultaneous=True) for v in V])
    return [sp.expand(c) for c in J.inv() * Vp]
```

For the triangular map $`\phi(t, x, y, z) = (t + xy,\ x + z^2,\ y + z,\ z)`$, with
$`\det D\phi = 1`$ so that everything stays polynomial,
$`\phi^* d = d \phi^*`$, $`\phi^*(f \wedge g) = \phi^* f \wedge \phi^* g`$ and
$`\phi^* \iota_V = \iota_{\phi^* V} \phi^*`$, hence $`\phi^* L_V = L_{\phi^* V} \phi^*`$.
**[verified]** CT-I0 to CT-I3. One map is an example, not a proof of naturality; the
proof is that the operators are built from $`d`$, $`\wedge`$ and $`\iota`$.

**A check must be able to fail.** A check that passes whatever the code does proves
nothing. The companion script runs two checks with a deliberate error, the last-slot
interior product (CT-C3') and the opposite bracket (CT-E3'), and confirms that they fail.

## 10. `expand`, `simplify`, and when zero means zero

- `sp.expand` puts a polynomial (in symbols, undefined functions and their `Derivative`s)
  into a canonical form, so `expand(e) == 0` decides whether $`e = 0`$. It is fast, and it
  is what `clean` uses in the script here, `magnetismo`, `grammar_of_a_body` and
  `observer_idempotents`.
- For rational functions, `sp.cancel` (or `sp.together` and then `expand` of the
  numerator) is canonical. `expand` alone is not: it leaves
  $`1/(a - 1) - (a + 1)/(a^2 - 1)`$ as three non-cancelling terms, and `cancel` gives $`0`$.
- With square roots, exponentials or trigonometric functions there is no canonical form.
  `sp.simplify(e) == 0` is then a proof that $`e = 0`$, but a non-zero result is not a
  proof that $`e \neq 0`$. `heat_and_helicity` and the `Form` class of `metric_free` call
  `simplify` in `clean`; `heat_and_helicity` switches it off in part K (`SIMPLIFY = False`),
  where everything is polynomial and `simplify` would only cost time. Lorentz factors
  $`\gamma = 1/\sqrt{1 - v^2}`$ in `grammar_of_a_body` part F are given rational values
  ($`v = 3/5`$, $`4/5`$, …) so that $`\gamma`$ is rational.
- Cost. A product of two forms with $`p`$ and $`q`$ terms makes $`pq`$ products of
  coefficients, and `simplify` dominates everything else. Generic forms on
  $`\mathbb{R}^4`$ with undefined-function coefficients are cheap with `expand`
  (the 42 checks here take about 20 s) and slow with `simplify`.

## 11. Conventions and pitfalls

| Item | Convention or pitfall |
|---|---|
| Interior product | Contracts the first slot, sign $`(-1)^{\text{position}}`$ (§4). The last-slot version fails Oziewicz's (4.7.1). |
| Interior product of a product | 1986: $`i_{x \wedge y} = i_y i_x`$; Jadczyk: $`i_{f \wedge g} = i_f i_g`$. Different by a sign on 2-vectors. |
| Exterior derivative | New $`dx^i`$ on the left. |
| Lie bracket | $`[X, Y]^i = X^j \partial_j Y^i - Y^j \partial_j X^i`$, so that $`[L_X, L_Y] = L_{[X,Y]}`$. |
| Keys | Bit $`i`$ and tuple entry $`i`$ both mean $`dx^i`$ and coordinate number $`i`$ in the list `xs`. The unit form is `0` or `()`. |
| Canonical form | Equality of dictionaries is equality of forms only after `clean`. A coefficient left as `0*x` or unexpanded makes equal forms compare unequal. |
| Basis order of matrices | Bitmask, or grade then bitmask, or `itertools.combinations` (§7). Do not compare matrices across scripts. |
| `Symbol` against `Function` | `sp.Symbol("A1")` has zero derivatives; for a field use `sp.Function("A1")(t, x, y, z)`. |
| Fractions | In Python `1/2` is the float `0.5`. Write `sp.Rational(1, 2)` (`R(1, 2)` in several scripts). |
| Signs | `-1 ** p` is $`-(1^p) = -1`$; write `(-1) ** p`. |
| Substitution | `expr.subs({t: x, x: t})` substitutes one key after the other: $`t + x^2 \mapsto t + t^2`$. A coordinate change needs `simultaneous=True`, which gives $`x + t^2`$. **[verified]** CT-I4. |
| Default arguments in loops | `lambda f_, i=i: ...` binds the current `i`; without `i=i` every lambda sees the last value. |

## 12. Where each script uses what

| Script | Key | Form operators | Matrices | Clifford | Strategies |
|---|---|---|---|---|---|
| `verify_heat_and_helicity.py` | tuple | `wedge`, `interior`, `d`, `lie`, `bracket`; `lie11` for $`(1,1)`$ tensors | `wedge_mat`, `ev_mat`, `alg_dim` (combinations order) | | generic functions; ansatz and linear solve (K–M) |
| `verify_magnetismo.py` | bitmask | `wedge`, `iv`, `d`, `lie` | | | random rationals, then generic symbols modulo $`\alpha X - 1`$ (`zero_mod`) |
| `verify_metric_free.py` | bitmask (matrices); tuple (`Form`) | `wed`, `ext`, `iv`, `lie`, `dfun` | class `Grassmann`: `cre`, `ann`, `ev`, `wedge`, `lmul` (grade order) | | symbolic $`n = 3`$, rational $`n = 4`$; ranks |
| `verify_grammar_of_a_body.py` | bitmask | `fw`, `fiv`, `fd`, `flie`; `pull_form`, `pull_vec` | `cr`, `ev` (bitmask order) | class `Cl` (word rewriting) | random rationals, generic functions, pullback |
| `verify_grassmann_clifford.py` | bitmask | | `E`, `I = E.T`, blade operators `EB` | Chevalley $`\gamma`$, unipotent `W`, $`\exp(i_\omega)`$ as a finite sum | generic $`\varphi`$ |
| `verify_observer_idempotents.py` | bitmask | | | blade table for $`Cl(V, -g)`$ | symbolic bodies on the hyperboloid |
| `verify_cartan_tutorial.py` | both | all of §2 to §6 | `op_matrix` (bitmask order) | Chevalley $`\gamma`$, blade table | all five of §9 |

The remaining scripts (`mass_centre`, `ternary_mass_centre`, `clock_centre`,
`relative_velocity`, `velocity_draft`, `matolcsi`, `poirier_reddiger`) need no form
machinery: where a wedge appears it is a list of $`3 \times 3`$ minors (`wedge3`) or a
Gram determinant (`wedge2`).

## 13. Why hand-written code: libraries, other systems, proof assistants

Implementing Grassmann and Clifford algebras by computer has a long history, so it is fair
to ask why the scripts write their own. This section records the answer and the
alternatives, as background for anyone who wants to cross-check the scripts or extend
them.

### 13.1 What a check in coordinates proves

The project's results are meant to hold in any dimension and without a choice of basis.
The scripts check them in coordinates for $`n = 3`$ or $`n = 4`$. With generic
coefficients (§9) a pass proves the identity *for that* $`n`$, over any commutative ring
when the identity is polynomial with integer coefficients. For other $`n`$ it is evidence,
not proof. Hand proofs usually close the gap by a reduction that the scripts do not use:
two (anti)derivations of the same degree that agree on functions and on 1-forms agree on
all forms, because they are determined by their action on generators. So identities such as
$`[L_X, \iota_Y] = \iota_{[X,Y]}`$ need checking only in degrees 0 and 1, where the
coordinate computation is the same for every $`n`$. Results that are not statements about
derivations, such as the multiplicativity of $`\mathcal M`$ in §9, have no such shortcut.

### 13.2 Why the scripts do not use a library

- **The framework is metric-free.** Oziewicz keeps vectors and forms apart: $`\mathrm{ev}_X`$
  pairs a vector with a form, and no metric is involved. Geometric-algebra libraries are
  built around a metric, through which they define contraction and identify vectors with
  covectors.
- **The Clifford algebras are those of an arbitrary bilinear form.** The 1986 paper uses
  $`Cl(\varphi)`$ with $`\varphi`$ not necessarily symmetric (§8). Most packages accept only a
  quadratic form, that is, the symmetric part.
- **The coefficients are fields.** Cartan's calculus has to act on coefficients that are
  undefined functions of the coordinates, which SymPy differentiates directly.
- **Every sign is visible.** The core is about 50 lines without docstrings (§2 to §6), short enough to check by
  reading, and at $`n = 4`$ the algebra has only 16 dimensions, so speed does not matter.

The cost is duplication: five scripts carry their own copies (§12).

### 13.3 Alternatives

| System | What it offers | Fit here |
|---|---|---|
| [GAlgebra](https://github.com/pygae/galgebra), Python on SymPy | Geometric algebra with an arbitrary basis and metric; geometric calculus with differential operators | Contraction is defined by the metric. Not tested for this note |
| SageMath [`ExteriorAlgebra`, `CliffordAlgebra`](https://doc.sagemath.org/html/en/reference/algebras/sage/algebras/clifford_algebra_element.html) | Exterior algebra over a ring with an interior product by a dual element, contracting the first slot as in §4 and extended to products by $`\iota_{\beta \wedge \gamma} = \iota_\gamma \iota_\beta`$, the order of the 1986 eq. (12); Clifford algebras of a quadratic form | Close in convention for the exterior algebra; symmetric forms only for Clifford. Not tested |
| [CLIFFORD](https://github.com/fractal97/CLIFFORD), Maple (Abłamowicz; with Fauser from version 5) | Clifford algebras $`Cl(B)`$ of an arbitrary bilinear form, the antisymmetric part included; a product algorithm based on Chevalley's recursive formula; left contraction with respect to a bilinear form that may be left symbolic | The closest fit to the 1986 paper, and an independent implementation |
| Maple DifferentialGeometry (Anderson and Torre) | Forms, interior products, exterior and Lie derivatives, pullback and pushforward on coordinate charts | Same conventions as the scripts; used for the cross-check of §13.4 |
| FriCAS | `DeRhamComplex`, `CliffordAlgebra` (quadratic form) | Not checked for this note |
| Lean 4 with [Mathlib](https://leanprover-community.github.io/mathlib4_docs/Mathlib/LinearAlgebra/CliffordAlgebra/Contraction) | Basis-free Clifford algebras over any commutative ring; contraction by an element of the dual module (metric-free, like $`\mathrm{ev}`$); `CliffordAlgebra.equivExterior`, the linear isomorphism of a Clifford algebra with the exterior algebra when 2 is invertible; `changeForm`, which moves between Clifford algebras of quadratic forms differing by a bilinear form $`B`$; the exterior derivative on normed spaces, with $`d^2 = 0`$ under smoothness assumptions | Proofs for every dimension and every ring. Differential forms on manifolds were not yet in Mathlib in early 2026, and I found no Lie derivative of forms there |

Notes on the table:

- **CLIFFORD.** Bertfried Fauser was a student of Oziewicz and Rafał Abłamowicz a colleague
  (B. Page). Bill recalls CLIFFORD as a large package that depends closely on the Maple
  version and is hard to install; it is not installed on his Maple server at present. A
  current distribution is at <https://github.com/fractal97/CLIFFORD> (read at commit
  `e58c1f0`). Its README, by Abłamowicz and dated 14 December 2024, gives installation
  instructions for Maple 2020.2 under Windows 10. The repository holds a single zip with the
  package as a Maple library (`maple.lib`, `maple.ind`, dated June 2024), its help
  database, a `maple.ini` that adds the library's folder to `libname`, and a sample
  worksheet. BIGEBRA is not included, and the repository states no licence. The README lists
  the exports of `with(Clifford)`, among them `cmul`, `cmulNUM`, `cmulRS`, `wedge`, `LC`,
  `RC` and `clibilinear`. Whether the library loads in Maple 2022 under Linux has not been
  tried.
  Running the Chevalley checks of §8 and the observer identities of §7 and §9 in CLIFFORD
  would be a useful side exercise: the scripts are checked by their own code, so a sign
  convention shared by a script and its check passes unnoticed, and an independent
  implementation would catch it.
- **Lean.** Wieser and Song formalised Clifford algebras in Lean with an approach that does
  not require a choice of basis, which matches the intent of §13.1. Their Lean 4 blueprint
  follows Jadczyk (2019). Mathlib's differential forms on manifolds were formalised in a
  separate repository and, as of January 2026, were not yet upstreamed. Natural first
  targets are the algebraic statements of §7 to §9 (the CAR, $`U^2 = \alpha(X)`$, the
  observer identities, Chevalley's anticommutator). Bill has deferred Lean, possibly to a
  separate project.

### 13.4 A cross-check with Maple's DifferentialGeometry

Maple 2022 is available on Bill Page's server, so the form calculus of §3 to §6 and §9 was
checked against an implementation that shares no code with the scripts.
[`src/verify_cartan_dg.mpl`](../src/verify_cartan_dg.mpl) runs 58 checks in Maple, and
[`src/compare_cartan_dg.py`](../src/compare_cartan_dg.py) compares eight objects computed
by Maple with the same objects computed by the functions of §2 to §6. The run recorded
here used Maple 2022.2 on 23 November 2026 and ended with `CHECKS 58` and `FAILURES []`.
The Maple script needs Maple and is not run by CI; the comparison script carries the
recorded Maple output and runs without it.

**Conventions.** DifferentialGeometry agrees with the scripts on every convention of §11:
the wedge product has no factor $`\tfrac12`$ ($`dt \wedge dx = dt \otimes dx - dx \otimes dt`$),
`Hook` contracts the first slot with
$`\iota_{\partial_x} \iota_{\partial_t} (dt \wedge dx) = 1`$, the wedge sign of CT-A1 and the
interior product of CT-C4 come out the same, and `LieBracket` uses
$`[X, Y]^i = X^j \partial_j Y^i - Y^j \partial_j X^i`$.

**Identities.** On generic forms of degree 0 to 3 and generic vector fields, every
coefficient an undefined function of $`(t, x, y, z)`$, the identities of CT-C3, CT-D2,
CT-D3 and CT-E1 to CT-E5 hold (the product rules for every pair of degrees from 1 to 3 whose sum is at
most 4, at most 3 for $`d`$ because of the second trap below), and the
variants with a wrong sign fail. With the map $`\phi`$ of §9, CT-I1 to CT-I3 hold.

**Term by term.** For the vector fields $`X = (1 + y)\partial_t + x \partial_x + tz\, \partial_y + t\, \partial_z`$
and $`Y = x^2 \partial_t + z\, \partial_y - yt\, \partial_z`$, the forms
$`F_2 = xz\, dt \wedge dx + y\, dy \wedge dz + ty\, dt \wedge dz + \sin x\, dx \wedge dy`$,
$`F_3 = e^t y\, dt \wedge dx \wedge dz + x^3\, dx \wedge dy \wedge dz`$ and
$`A = dt + x\, dy + t^2 dz`$, Maple and the SymPy functions give the same $`dF_2`$,
$`\iota_X F_2`$, $`\iota_X F_3`$, $`L_X F_2`$, $`L_X F_3`$, $`A \wedge F_2`$, $`[X, Y]`$ and
$`L_X A`$, compared coefficient by coefficient. A single changed sign in Maple's output is
reported as a difference.

**Traps in DifferentialGeometry.** Most of these cost a run before they were understood.

- `Pushforward(Psi, V)` with two arguments returns $`D\Psi_p\, V(p)`$ as a function of
  the source point $`p`$, not composed with $`\Psi^{-1}`$, so it is not a vector field on
  the target. The push-forward needs the inverse as a third argument, a list of
  coordinate equations: `Pushforward(PhiInv, V, [t = ..., x = ..., ...])` with the
  equations of $`\phi`$ gives $`\phi^* V = (D\phi)^{-1}(V \circ \phi)`$, checked against the
  Jacobian.
- `ExteriorDerivative` of a form of top degree (a 4-form in four dimensions) raises an
  error instead of returning $`0`$. In a loop over degrees the error stops the loop, and
  results printed afterwards cover only the degrees reached. `LieDerivative` handles top
  degree correctly: $`L_{x \partial_x}(dt \wedge dx \wedge dy \wedge dz) = dt \wedge dx \wedge dy \wedge dz`$.
- `Hook` of a function raises an error instead of returning $`0`$.
- A sum of forms of different degrees is an error, so the inhomogeneous forms that the
  dictionaries of §2 hold (and that CT-B1 uses) are not available.
- `InverseTransformation` returns a transformation that prints like a list of equations.
- A DifferentialGeometry object is `_DG(list)`: its coefficient list is `op(1, w)[2]`, not
  `op(2, w)`.

What the cross-check does not cover: the matrices of §7 and the Clifford products of §8.
For the Clifford side the independent implementation would be CLIFFORD (§13.3).

## 14. Running the companion script

```
PYTHONPATH=src python3 -u src/verify_cartan_tutorial.py
```

It prints one line per check, `ok` or `FAIL`, ends with `all checks pass` and exit status
0, writes no files, and takes about 20 s. The sections A to J of the script are the
sections of this note in the order 2–3, 3, 4, 5, 6, 7, 8, 6.1, 9, 9.

## References

- Z. Oziewicz, "From Grassmann to Clifford", in J. S. R. Chisholm and A. K. Common (eds.),
  *Clifford Algebras and Their Applications in Mathematical Physics*, NATO ASI Series C 183
  (Reidel, Dordrecht 1986), pp. 245–255.
  <https://doi.org/10.1007/978-94-009-4728-3_20>. Equation numbers (9), (12), (16) and
  (23.2) as read in [`grassmann_to_clifford.md`](grassmann_to_clifford.md).
- Z. Oziewicz, *Magnetismo e Electricidad*, lecture notes, version of 18 July 2020; not
  public. Eq. (4.7.1) as read in [`magnetismo.md`](magnetismo.md).
- A. Jadczyk, "On the bundle of Clifford algebras over the space of quadratic forms",
  [arXiv:2103.09767](https://arxiv.org/abs/2103.09767).
- I. Kolář, P. W. Michor and J. Slovák, *Natural Operations in Differential Geometry*
  (Springer, 1993); the authors' online version is linked from
  <https://www.mat.univie.ac.at/~michor/preprint-shadows/kmsbookh.html>. Chapter II for the
  interior product, $`d`$, $`L_X`$ and their graded commutators; the chapter was not
  re-read for this note.
- R. Abłamowicz and B. Fauser, "Mathematics of CLIFFORD: a Maple package for Clifford and
  Grassmann algebras", Adv. Appl. Clifford Algebras 15 (2005) 157–181,
  <https://doi.org/10.1007/s00006-005-0009-9>,
  [arXiv:math-ph/0212031](https://arxiv.org/abs/math-ph/0212031). R. Abłamowicz, "Hecke
  algebras, SVD, and other computational examples with CLIFFORD",
  [arXiv:math/9910069](https://arxiv.org/abs/math/9910069).
- E. Wieser and U. Song, "Formalizing geometric algebra in Lean", Adv. Appl. Clifford
  Algebras 32 (2022), <https://doi.org/10.1007/s00006-021-01164-1>,
  [arXiv:2110.03551](https://arxiv.org/abs/2110.03551); Lean 4 blueprint
  <https://utensil.github.io/lean-ga/blueprint/blueprint.pdf>.
- Mathlib: `Mathlib.LinearAlgebra.CliffordAlgebra.Contraction` (link in §13.3) and
  `Mathlib.Analysis.Calculus.DifferentialForm.Basic`,
  <https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Calculus/DifferentialForm/Basic>;
  differential forms on manifolds: <https://github.com/urkud/DeRhamCohomology>.
- SymPy documentation: `Basic.subs` (the `simultaneous` flag), `reduced`, `Poly.coeffs`,
  <https://docs.sympy.org>. The script was run with SymPy 1.14.0.
