# Syntax Guide

```{note}
This documentation utilized the [Markedly Structured Text (MyST)](https://myst-parser.readthedocs.io/en/latest/index.html) syntax.
```

This package utilizes a [Sphinx domain](https://www.sphinx-doc.org/en/master/usage/restructuredtext/domains.html) - named "proof" - to describe and link typeset markup objects (theorems, proofs, corollaries, etc.) which we think belong together. All directives follow the pattern `{<domain_name>:<typeset>}` while all the roles follow the pattern `{<domain_name>:ref}`. To utilize any directive in the `proof` domain follow the pattern `{prf:<typeset>}`. To reference any directive follow the pattern `{prf:ref}`.

## Collection of Directives

### Proofs

A proof directive can be included using the `prf:proof` pattern. Unlike the other directives provided through this extension, a proof directive does not include any parameters nor does it require any arguments. A proof directive can easily be referenced through [targets](https://myst-parser.readthedocs.io/en/latest/using/syntax.html#targets-and-cross-referencing).

The following option is supported:

* `class` : text

	Value of the proof’s class attribute which can be used to add custom CSS or JavaScript.


**Example**

````{prf:proof}
We'll omit the full proof.

But we will prove sufficiency of the asserted conditions.

To this end, let $y \in \mathbb R^n$ and let $S$ be a linear subspace of $\mathbb R^n$.

Let $\hat y$ be a vector in $\mathbb R^n$ such that $\hat y \in S$ and $y - \hat y \perp S$.

Let $z$ be any other point in $S$ and use the fact that $S$ is a linear subspace to deduce

```{math}
\| y - z \|^2
= \| (y - \hat y) + (\hat y - z) \|^2
= \| y - \hat y \|^2  + \| \hat y - z  \|^2
```

Hence $\| y - z \| \geq \| y - \hat y \|$, which completes the proof.
````

**MyST Syntax**

``````md
````{prf:proof}
We'll omit the full proof.

But we will prove sufficiency of the asserted conditions.

To this end, let $y \in \mathbb R^n$ and let $S$ be a linear subspace of $\mathbb R^n$.

Let $\hat y$ be a vector in $\mathbb R^n$ such that $\hat y \in S$ and $y - \hat y \perp S$.

Let $z$ be any other point in $S$ and use the fact that $S$ is a linear subspace to deduce

```{math}
\| y - z \|^2
= \| (y - \hat y) + (\hat y - z) \|^2
= \| y - \hat y \|^2  + \| \hat y - z  \|^2
```

Hence $\| y - z \| \geq \| y - \hat y \|$, which completes the proof.
````
``````

_Source:_ [QuantEcon](https://python-advanced.quantecon.org/orth_proj.html#The-Orthogonal-Projection-Theorem)


### Theorems

A theorem directive can be included using the `prf:theorem` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your theorem that you can use to reference it with `{prf:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the theorem’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off theorem auto numbering.

	```{math}
	\DeclareMathOperator*{\argmax}{arg\,max}
	\DeclareMathOperator*{\argmin}{arg\,min}
	```

**Example**

````{prf:theorem} Orthogonal-Projection-Theorem
:label: my-theorem

Given $y \in \mathbb R^n$ and linear subspace $S \subset \mathbb R^n$,
there exists a unique solution to the minimization problem

```{math}
\hat y := \argmin_{z \in S} \|y - z\|
```

The minimizer $\hat y$ is the unique vector in $\mathbb R^n$ that satisfies

* $\hat y \in S$

* $y - \hat y \perp S$


The vector $\hat y$ is called the **orthogonal projection** of $y$ onto $S$.
````

**MyST Syntax**

``````md
````{prf:theorem} Orthogonal-Projection-Theorem
:label: my-theorem

Given $y \in \mathbb R^n$ and linear subspace $S \subset \mathbb R^n$,
there exists a unique solution to the minimization problem

```{math}
\hat y := \argmin_{z \in S} \|y - z\|
```

The minimizer $\hat y$ is the unique vector in $\mathbb R^n$ that satisfies

* $\hat y \in S$

* $y - \hat y \perp S$


The vector $\hat y$ is called the **orthogonal projection** of $y$ onto $S$.
````
``````

_Source:_ [QuantEcon](https://python-advanced.quantecon.org/orth_proj.html#The-Orthogonal-Projection-Theorem)

#### Referencing Theorems

You can refer to a theorem using the `{prf:ref}` role like: ```{prf:ref}`my-theorem` ```, which will replace the reference with the theorem number like so: {prf:ref}`my-theorem`. When an explicit text is provided, this caption will serve as the title of the reference. For example, ```{prf:ref}`Orthogonal-Projection-Theorem <my-theorem>` ``` will produce: {prf:ref}`Orthogonal-Projection-Theorem <my-theorem>`.

### Axioms

An axiom directive can be included using the `prf:axiom` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your axiom that you can use to reference it with `{prf:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the axiom’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off axiom auto numbering.

**Example**

```{prf:axiom} Completeness of $\mathbb{R}$
:label: my-axiom

Every Cauchy sequence on the real line is convergent.
```

**MyST Syntax**

``````md
```{prf:axiom} Completeness of $\mathbb{R}$
:label: my-axiom

Every Cauchy sequence on the real line is convergent.
```
``````

_Source:_ {cite}`economic-dynamics-book`

#### Referencing Axioms

You can refer to an axiom using the `{prf:ref}` role like: ```{prf:ref}`my-axiom` ```, which will replace the reference with the axiom number like so: {prf:ref}`my-axiom`. When an explicit text is provided, this caption will serve as the title of the reference.


### Lemmas

A lemma directive can be included using the `prf:lemma` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your lemma that you can use to reference it with `{prf:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the lemma’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off lemma auto numbering.

**Example**

````{prf:lemma}
:label: my-lemma

If $\hat P$ is the fixed point of the map $\mathcal B \circ \mathcal D$ and $\hat F$ is the robust policy as given in [(7)](https://python-advanced.quantecon.org/robustness.html#equation-rb-oc-ih), then

```{math}
:label: rb_kft

K(\hat F, \theta) = (\theta I - C'\hat P C)^{-1} C' \hat P  (A - B \hat F)
```
````

**MyST Syntax**

``````md
````{prf:lemma}
:label: my-lemma

If $\hat P$ is the fixed point of the map $\mathcal B \circ \mathcal D$ and $\hat F$ is the robust policy as given in [(7)](https://python-advanced.quantecon.org/robustness.html#equation-rb-oc-ih), then

```{math}
:label: rb_kft

K(\hat F, \theta) = (\theta I - C'\hat P C)^{-1} C' \hat P  (A - B \hat F)
```
````
``````

_Source:_ [QuantEcon](https://python-advanced.quantecon.org/robustness.html#Appendix)

#### Referencing Lemmas

You can refer to a lemma using the `{prf:ref}` role like: ```{prf:ref}`my-lemma` ```, which will replace the reference with the lemma number like so: {prf:ref}`my-lemma`. When an explicit text is provided, this caption will serve as the title of the reference.


### Definitions

A definition directive can be included using the `prf:definition` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your definition that you can use to reference it with `{prf:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the definition’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off definition auto numbering.

**Example**

````{prf:definition}
:label: my-definition

The *economical expansion problem* (EEP) for
$(A,B)$ is to find a semi-positive $n$-vector $p>0$
and a number $\beta\in\mathbb{R}$, such that

$$
&\min_{\beta} \hspace{2mm} \beta \\
&\text{s.t. }\hspace{2mm}Bp \leq \beta Ap
$$

````

**MyST Syntax**

``````md
````{prf:definition}
:label: my-definition

The *economical expansion problem* (EEP) for
$(A,B)$ is to find a semi-positive $n$-vector $p>0$
and a number $\beta\in\mathbb{R}$, such that

$$
&\min_{\beta} \hspace{2mm} \beta \\
&\text{s.t. }\hspace{2mm}Bp \leq \beta Ap
$$
````
``````

_Source:_ [QuantEcon](https://python-advanced.quantecon.org/von_neumann_model.html#Duality)

#### Referencing Definitions

You can refer to a definition using the `{prf:ref}` role like: ```{prf:ref}`my-definition` ```, which will replace the reference with the definition number like so: {prf:ref}`my-definition`. When an explicit text is provided, this caption will serve as the title of the reference.

### Criteria

A criterion directive can be included using the `prf:criterion` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your criterion that you can use to reference it with `{prf:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the criterion’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off criterion auto numbering.

**Example**

````{prf:criterion} Weyl's criterion
:label: weyls-criterion

Weyl's criterion states that the sequence $a_n$ is equidistributed modulo $1$ if
and only if for all non-zero integers $m$,

```{math}
\lim_{n \rightarrow \infty} \frac{1}{n} \sum_{j=1}^{n} \exp^{2 \pi i m a_j} = 0
```
````

**MyST Syntax**

``````md
````{prf:criterion} Weyl's criterion
:label: weyls-criterion

Weyl's criterion states that the sequence $a_n$ is equidistributed modulo $1$ if
and only if for all non-zero integers $m$,

```{math}
\lim_{n \rightarrow \infty} \frac{1}{n} \sum_{j=1}^{n} \exp^{2 \pi i m a_j} = 0
```
````
``````

_Source:_ [Wikipedia](https://en.wikipedia.org/wiki/Equidistributed_sequence#Weyl's_criterion)

#### Referencing Criteria

You can refer to a criterion using the `{prf:ref}` role like: ```{prf:ref}`weyls-criterion` ```, which will replace the reference with the criterion number like so: {prf:ref}`weyls-criterion`. When an explicit text is provided, this caption will serve as the title of the reference.


### Remarks

A remark directive can be included using the `prf:remark` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your remark that you can use to reference it with `{prf:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the remark’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off remark auto numbering.

**Example**

```{prf:remark}
:label: my-remark

More generally there is a class of density functions
that possesses this feature, i.e.

$$
\exists g: \mathbb{R}_+ \mapsto \mathbb{R}_+ \ \ \text{ and } \ \ c \geq 0,
\ \ \text{s.t.  the density } \ \ f \ \ \text{of} \ \ Z  \ \
\text{ has the form } \quad f(z) = c g(z\cdot z)
$$

This property is called **spherical symmetry** (see p 81. in Leamer
(1978))
```

**MyST Syntax**

``````md
```{prf:remark}
:label: my-remark

More generally there is a class of density functions
that possesses this feature, i.e.

$$
\exists g: \mathbb{R}_+ \mapsto \mathbb{R}_+ \ \ \text{ and } \ \ c \geq 0,
\ \ \text{s.t.  the density } \ \ f \ \ \text{of} \ \ Z  \ \
\text{ has the form } \quad f(z) = c g(z\cdot z)
$$

This property is called **spherical symmetry** (see p 81. in Leamer
(1978))
```
``````

_Source:_ [QuantEcon](https://python-advanced.quantecon.org/black_litterman.html)


#### Referencing Remarks

You can refer to a remark using the `{prf:ref}` role like: ```{prf:ref}`my-remark` ```, which will replace the reference with the remark number like so: {prf:ref}`my-remark`. When an explicit text is provided, this caption will serve as the title of the reference.


### Conjectures

**Example**

```{prf:conjecture} Fake $\gamma$ conjecture
:label: my-conjecture

This is a dummy conjecture to illustrate that one can use math in titles.
```

**MyST Syntax**

``````md
```{prf:conjecture} Fake $\gamma$ conjecture
:label: my-conjecture

This is a dummy conjecture to illustrate that one can use math in titles.
```
``````

#### Referencing Conjectures

You can refer to a conjecture using the `{prf:ref}` role like: ```{prf:ref}`my-conjecture` ```, which will replace the reference with the conjecture number like so: {prf:ref}`my-conjecture`. When an explicit text is provided, this caption will serve as the title of the reference.

### Corollaries

A corollary directive can be included using the `prf:corollary` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your corollary that you can use to reference it with `{prf:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the corollary’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off corollary auto numbering.

**Example**

```{prf:corollary}
:label: my-corollary

If $A$ is a convergent matrix, then there exists a matrix norm such
that $\vert \vert A \vert \vert < 1$.
```

**MyST Syntax**

``````md
```{prf:corollary}
:label: my-corollary

If $A$ is a convergent matrix, then there exists a matrix norm such
that $\vert \vert A \vert \vert < 1$.
```
``````

_Source:_ [QuantEcon](https://python-intro.quantecon.org/_static/lecture_specific/linear_models/iteration_notes.pdf)

#### Referencing Corollaries

You can refer to a corollary using the `{prf:ref}` role like: ```{prf:ref}`my-corollary` ```, which will replace the reference with the corollary number like so: {prf:ref}`my-corollary`. When an explicit text is provided, this caption will serve as the title of the reference.


### Algorithms


An algorithm directive can be included using the `prf:algorithm` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your algorithm that you can use to reference it with `{prf:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the algorithm’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off algorithm auto numbering.

**Example**

```{prf:algorithm} Ford–Fulkerson
:label: my-algorithm

**Inputs** Given a Network $G=(V,E)$ with flow capacity $c$, a source node $s$, and a sink node $t$

**Output** Compute a flow $f$ from $s$ to $t$ of maximum value

1. $f(u, v) \leftarrow 0$ for all edges $(u,v)$
2. While there is a path $p$ from $s$ to $t$ in $G_{f}$ such that $c_{f}(u,v)>0$ for all edges $(u,v) \in p$:

	1. Find $c_{f}(p)= \min \{c_{f}(u,v):(u,v)\in p\}$
	2. For each edge $(u,v) \in p$

		1. $f(u,v) \leftarrow f(u,v) + c_{f}(p)$ *(Send flow along the path)*
		2. $f(u,v) \leftarrow f(u,v) - c_{f}(p)$ *(The flow might be "returned" later)*
```

**MyST Syntax**

``````md
```{prf:algorithm} Ford–Fulkerson
:label: my-algorithm

**Inputs** Given a Network $G=(V,E)$ with flow capacity $c$, a source node $s$, and a sink node $t$

**Output** Compute a flow $f$ from $s$ to $t$ of maximum value

1. $f(u, v) \leftarrow 0$ for all edges $(u,v)$
2. While there is a path $p$ from $s$ to $t$ in $G_{f}$ such that $c_{f}(u,v)>0$
	for all edges $(u,v) \in p$:

	1. Find $c_{f}(p)= \min \{c_{f}(u,v):(u,v)\in p\}$
	2. For each edge $(u,v) \in p$

		1. $f(u,v) \leftarrow f(u,v) + c_{f}(p)$ *(Send flow along the path)*
		2. $f(u,v) \leftarrow f(u,v) - c_{f}(p)$ *(The flow might be "returned" later)*
```
``````

_Source:_ [Wikipedia](https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm)

#### Referencing Algorithms

You can refer to a algorithms using the `{prf:ref}` role like: ```{prf:ref}`my-algorithm` ```, which will replace the reference with the algorithm number like so: {prf:ref}`my-algorithm`. When an explicit text is provided, this caption will serve as the title of the reference.


### Examples

An example directive can be included using the `prf:example` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your example that you can use to reference it with `{prf:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the example’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off example auto numbering.

**Example**

````{prf:example}
:label: my-example

Next, we shut down randomness in demand and assume that the demand shock
$\nu_t$ follows a deterministic path:


```{math}
\nu_t = \alpha + \rho \nu_{t-1}
```

Again, we’ll compute and display outcomes in some figures

```python
ex2 = SmoothingExample(C2=[[0], [0]])

x0 = [0, 1, 0]
ex2.simulate(x0)
```
````

**MyST Syntax**

``````md
````{prf:example}
:label: my-example

Next, we shut down randomness in demand and assume that the demand shock
$\nu_t$ follows a deterministic path:


```{math}
\nu_t = \alpha + \rho \nu_{t-1}
```

Again, we’ll compute and display outcomes in some figures

```python
ex2 = SmoothingExample(C2=[[0], [0]])

x0 = [0, 1, 0]
ex2.simulate(x0)
```
````
``````

_Source:_ [QuantEcon](https://python.quantecon.org/lq_inventories.html#Example-2)

#### Referencing Examples

You can refer to an example using the `{prf:ref}` role like: ```{prf:ref}`my-example` ```, which will replace the reference with the example number like so: {prf:ref}`my-example`. When an explicit text is provided, this caption will serve as the title of the reference.


### Properties

A property directive can be included using the `prf:property` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your property that you can use to reference it with `{prf:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the property’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off property auto numbering.

**Example**

```{prf:property}
:label: my-property

This is a dummy property to illustrate the directive.
```

**MyST Syntax**

``````md
```{prf:property}
:label: my-property

This is a dummy property to illustrate the directive.
```
``````

#### Referencing Properties

You can refer to a property using the `{prf:ref}` role like: ```{prf:ref}`my-property` ```, which will replace the reference with the property number like so: {prf:ref}`my-property`. When an explicit text is provided, this caption will serve as the title of the reference.

### Observations

An observation directive can be included using the `prf:observation` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your observation that you can use to reference it with `{prf:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the observation’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off observation auto numbering.

**Example**

```{prf:observation}
:label: my-observation

This is a dummy observation directive.
```

**MyST Syntax**

``````md
```{prf:observation}
:label: my-observation

This is a dummy observation directive.
```
``````

#### Referencing Observations

You can refer to an observation using the `{prf:ref}` role like: ```{prf:ref}`my-observation` ```, which will replace the reference with the observation number like so: {prf:ref}`my-observation`. When an explicit text is provided, this caption will serve as the title of the reference.

### Propositions

A proposition directive can be included using the `prf:proposition` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your proposition that you can use to reference it with `{prf:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the proposition’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off proposition auto numbering.

**Example**

```{prf:proposition}
:label: my-proposition

This is a dummy proposition directive.
```

**MyST Syntax**

``````md
```{prf:proposition}
:label: my-proposition

This is a dummy proposition directive.
```
``````

#### Referencing Propositions

You can refer to a proposition using the `{prf:ref}` role like: ```{prf:ref}`my-proposition` ```, which will replace the reference with the proposition number like so: {prf:ref}`my-proposition`. When an explicit text is provided, this caption will serve as the title of the reference.


### Assumptions

An assumption directive can be included using the `prf:assumption` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your assumption that you can use to reference it with `{prf:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the assumption’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off assumption auto numbering.

**Example**

```{prf:assumption}
:label: my-assumption

This is a dummy assumption directive.
```

**MyST Syntax**

``````md
```{prf:assumption}
:label: my-assumption

This is a dummy assumption directive.
```
``````

#### Referencing Assumptions

You can refer to an assumption using the `{prf:ref}` role like: ```{prf:ref}`my-assumption` ```, which will replace the reference with the assumption number like so: {prf:ref}`my-assumption`. When an explicit text is provided, this caption will serve as the title of the reference.

## How to Hide Content

Directive content can be hidden using the `dropdown` class which is available through [sphinx-togglebutton](https://sphinx-togglebutton.readthedocs.io/en/latest/). If your project utilizes the [MyST-NB](https://myst-nb.readthedocs.io/en/latest/) extension, there is no need to activate `sphinx-togglebutton` since it is already bundled with `MyST-NB`.

For Sphinx projects, add `"sphinx_togglebutton"` to your `extensions` list in `conf.py` to activate the extension

```python
extensions = [
    ...
    "sphinx_togglebutton"
    ...
]
```

For Jupyter Book projects, add `sphinx_togglebutton` under `extra_extensions`

```yaml
sphinx:
  extra_extensions:
    - sphinx_togglebutton
```

To hide the directive, simply add `:class: dropdown` as a directive option.

**Example**

```{prf:theorem}
:class: dropdown

This is an example of how to hide the content of a directive.
```

**MyST Syntax**:

````
```{prf:theorem}
:class: dropdown

This is an example of how to hide the content of a directive.
```
````
