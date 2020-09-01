# Syntax Guide

```{note}
This documentation utilized the [Markedly Structured Text (MyST)](https://myst-parser.readthedocs.io/en/latest/index.html) syntax.
```

```{proof:proof}
This is a test directive.
```

## Proofs

A proof directive can be included using the `proof:proof` pattern. Unlike the other directives provided through this extension, a proof directive does not include any parameters nor does it require any arguments. A proof directive can easily be referenced through [targets](https://myst-parser.readthedocs.io/en/latest/using/syntax.html#targets-and-cross-referencing).


**Example**

````{proof:proof}
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
````{proof:proof}
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


## Theorems

A theorem directive can be included using the `proof:theorem` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your theorem that you can use to reference it with `{proof:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the theorem’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off theorem auto numbering.

	```{math}
	\DeclareMathOperator*{\argmax}{arg\,max}
	\DeclareMathOperator*{\argmin}{arg\,min}
	```

**Example**

````{proof:theorem} Orthogonal-Projection-Theorem
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
````{proof:theorem} Orthogonal-Projection-Theorem
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

### Referencing Theorems

You can refer to a theorem using the `{proof:ref}` role like: ```{proof:ref}`my-theorem` ```, which will replace the reference with the theorem number like so: {proof:ref}`my-theorem`. When an explicit text is provided, this caption will serve as the title of the reference. For example, ```{proof:ref}`Orthogonal-Projection-Theorem <my-theorem>` ``` will produce: {proof:ref}`Orthogonal-Projection-Theorem <my-theorem>`.

## Axioms

An axiom directive can be included using the `proof:theorem` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your axiom that you can use to reference it with `{proof:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the axiom’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off axiom auto numbering.

**Example**

```{proof:axiom} Completeness of $\mathbb{R}$
:label: my-axiom

Every Cauchy sequence on the real line is convergent.
```

**MyST Syntax**

``````md
```{proof:axiom} Completeness of $\mathbb{R}$
:label: my-axiom

Every Cauchy sequence on the real line is convergent.
```
``````

_Source:_ {cite}`economic-dynamics-book`

### Referencing Axioms

You can refer to an axiom using the `{proof:ref}` role like: ```{proof:ref}`my-axiom` ```, which will replace the reference with the axiom number like so: {proof:ref}`my-axiom`. When an explicit text is provided, this caption will serve as the title of the reference.


## Lemmas

A lemma directive can be included using the `proof:lemma` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your lemma that you can use to reference it with `{proof:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the lemma’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off lemma auto numbering.

**Example**

````{proof:lemma}
:label: my-lemma

If $\hat P$ is the fixed point of the map $\mathcal B \circ \mathcal D$ and $\hat F$ is the robust policy as given in [(7)](https://python-advanced.quantecon.org/robustness.html#equation-rb-oc-ih), then

```{math}
:label: rb_kft

K(\hat F, \theta) = (\theta I - C'\hat P C)^{-1} C' \hat P  (A - B \hat F)
```
````

**MyST Syntax**

``````md
````{proof:lemma}
:label: my-lemma

If $\hat P$ is the fixed point of the map $\mathcal B \circ \mathcal D$ and $\hat F$ is the robust policy as given in [(7)](https://python-advanced.quantecon.org/robustness.html#equation-rb-oc-ih), then

```{math}
:label: rb_kft

K(\hat F, \theta) = (\theta I - C'\hat P C)^{-1} C' \hat P  (A - B \hat F)
```
````
``````

_Source:_ [QuantEcon](https://python-advanced.quantecon.org/robustness.html#Appendix)

### Referencing Lemmas

You can refer to a lemma using the `{proof:ref}` role like: ```{proof:ref}`my-lemma` ```, which will replace the reference with the lemma number like so: {proof:ref}`my-lemma`. When an explicit text is provided, this caption will serve as the title of the reference.


## Definitions

A definition directive can be included using the `proof:definition` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your definition that you can use to reference it with `{proof:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the definition’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off definition auto numbering.

**Example**

````{proof:definition}
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
````{proof:definition}
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

### Referencing Definitions

You can refer to a definition using the `{proof:ref}` role like: ```{proof:ref}`my-definition` ```, which will replace the reference with the definition number like so: {proof:ref}`my-definition`. When an explicit text is provided, this caption will serve as the title of the reference.

## Criteria

A criterion directive can be included using the `proof:criterion` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your criterion that you can use to reference it with `{proof:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the criterion’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off criterion auto numbering.

**Example**

````{proof:criterion} Weyl's criterion
:label: weyls-criterion

Weyl's criterion states that the sequence $a_n$ is equidistributed modulo $1$ if
and only if for all non-zero integers $m$,

```{math}
\lim_{n \rightarrow \infty} \frac{1}{n} \sum_{j=1}^{n} \exp^{2 \pi i m a_j} = 0
```
````

**MyST Syntax**

``````md
````{proof:criterion} Weyl's criterion
:label: weyls-criterion

Weyl's criterion states that the sequence $a_n$ is equidistributed modulo $1$ if
and only if for all non-zero integers $m$,

```{math}
\lim_{n \rightarrow \infty} \frac{1}{n} \sum_{j=1}^{n} \exp^{2 \pi i m a_j} = 0
```
````
``````

_Source:_ [Wikipedia](https://en.wikipedia.org/wiki/Equidistributed_sequence#Weyl's_criterion)

### Referencing Criteria

You can refer to a criterion using the `{proof:ref}` role like: ```{proof:ref}`weyls-criterion` ```, which will replace the reference with the criterion number like so: {proof:ref}`weyls-criterion`. When an explicit text is provided, this caption will serve as the title of the reference.


## Remarks

A remark directive can be included using the `proof:remark` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your remark that you can use to reference it with `{proof:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the remark’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off remark auto numbering.

**Example**

```{proof:remark}
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
```{proof:remark}
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


### Referencing Remarks

You can refer to a remark using the `{proof:ref}` role like: ```{proof:ref}`my-remark` ```, which will replace the reference with the remark number like so: {proof:ref}`my-remark`. When an explicit text is provided, this caption will serve as the title of the reference.


## Conjectures

**Example**

```{proof:conjecture} Fake $\gamma$ conjecture
:label: my-conjecture

This is a dummy conjecture to illustrate that one can use math in titles.
```

**MyST Syntax**

``````md
```{proof:conjecture} Fake $\gamma$ conjecture
:label: my-conjecture

This is a dummy conjecture to illustrate that one can use math in titles.
```
``````

### Referencing Conjectures

You can refer to a conjecture using the `{proof:ref}` role like: ```{proof:ref}`my-conjecture` ```, which will replace the reference with the conjecture number like so: {proof:ref}`my-conjecture`. When an explicit text is provided, this caption will serve as the title of the reference.

## Corollaries

A corollary directive can be included using the `proof:corollary` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your corollary that you can use to reference it with `{proof:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the corollary’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off corollary auto numbering.

**Example**

```{proof:corollary}
:label: my-corollary

If $A$ is a convergent matrix, then there exists a matrix norm such
that $\vert \vert A \vert \vert < 1$.
```

**MyST Syntax**

``````md
```{proof:corollary}
:label: my-corollary

If $A$ is a convergent matrix, then there exists a matrix norm such
that $\vert \vert A \vert \vert < 1$.
```
``````

_Source:_ [QuantEcon](https://python-intro.quantecon.org/_static/lecture_specific/linear_models/iteration_notes.pdf)

### Referencing Corollaries

You can refer to a corollary using the `{proof:ref}` role like: ```{proof:ref}`my-corollary` ```, which will replace the reference with the corollary number like so: {proof:ref}`my-corollary`. When an explicit text is provided, this caption will serve as the title of the reference.


## Algorithms


An algorithm directive can be included using the `proof:algorithm` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your algorithm that you can use to reference it with `{proof:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the algorithm’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off algorithm auto numbering.

**Example**

```{proof:algorithm} Ford–Fulkerson
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
```{proof:algorithm} Ford–Fulkerson
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

### Referencing Algorithms

You can refer to a algorithms using the `{proof:ref}` role like: ```{proof:ref}`my-algorithm` ```, which will replace the reference with the algorithm number like so: {proof:ref}`my-algorithm`. When an explicit text is provided, this caption will serve as the title of the reference.

## Exercises

An exercise directive can be included using the `proof:exercise` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your exercise that you can use to reference it with `{proof:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the exercise’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off exercise auto numbering.

**Example**

```{proof:exercise}
:label: my-exercise

Recall that $n!$ is read as "$n$ factorial" and defined as
$n! = n \times (n - 1) \times \cdots \times 2 \times 1$.

There are functions to compute this in various modules, but let's
write our own version as an exercise.

In particular, write a function `factorial` such that `factorial(n)` returns $n!$
for any positive integer $n$.
```

**MyST Syntax**

``````md
```{proof:exercise}
:label: my-exercise

Recall that $n!$ is read as "$n$ factorial" and defined as
$n! = n \times (n - 1) \times \cdots \times 2 \times 1$.

There are functions to compute this in various modules, but let's
write our own version as an exercise.

In particular, write a function `factorial` such that `factorial(n)` returns $n!$
for any positive integer $n$.
```
``````

_Source:_ [QuantEcon](https://python-programming.quantecon.org/functions.html#Exercise-1)

### Referencing Exercises

You can refer to an exercise using the `{proof:ref}` role like: ```{proof:ref}`my-exercise` ```, which will replace the reference with the exercise number like so: {proof:ref}`my-exercise`. When an explicit text is provided, this caption will serve as the title of the reference.


## Examples

An example directive can be included using the `proof:example` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your example that you can use to reference it with `{proof:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the example’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off example auto numbering.

**Example**

````{proof:example}
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
````{proof:example}
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

### Referencing Examples

You can refer to an example using the `{proof:ref}` role like: ```{proof:ref}`my-example` ```, which will replace the reference with the example number like so: {proof:ref}`my-example`. When an explicit text is provided, this caption will serve as the title of the reference.


## Properties

A property directive can be included using the `proof:property` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your property that you can use to reference it with `{proof:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the property’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off property auto numbering.

**Example**

```{proof:property}
:label: my-property

This is a dummy property to illustrate the directive.
```

**MyST Syntax**

``````md
```{proof:property}
:label: my-property

This is a dummy property to illustrate the directive.
```
``````

### Referencing Properties

You can refer to a property using the `{proof:ref}` role like: ```{proof:ref}`my-property` ```, which will replace the reference with the property number like so: {proof:ref}`my-property`. When an explicit text is provided, this caption will serve as the title of the reference.

## Observations

An observation directive can be included using the `proof:observation` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your observation that you can use to reference it with `{proof:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the observation’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off observation auto numbering.

**Example**

```{proof:observation}
:label: my-observation

This is a dummy observation directive.
```

**MyST Syntax**

``````md
```{proof:observation}
:label: my-observation

This is a dummy observation directive.
```
``````

### Referencing Observations

You can refer to an observation using the `{proof:ref}` role like: ```{proof:ref}`my-observation` ```, which will replace the reference with the observation number like so: {proof:ref}`my-observation`. When an explicit text is provided, this caption will serve as the title of the reference.

## Propositions

A proposition directive can be included using the `proof:proposition` pattern. The directive is enumerated by default and can take in an optional title argument. The following options are also supported:

* `label` : text

	A unique identifier for your proposition that you can use to reference it with `{proof:ref}`. Cannot contain spaces or special characters.
* `class` : text

	Value of the proposition’s class attribute which can be used to add custom CSS or JavaScript.
* `nonumber` : flag (empty)

	Turns off proposition auto numbering.

**Example**

```{proof:proposition}
:label: my-proposition

This is a dummy proposition directive.
```

**MyST Syntax**

``````md
```{proof:proposition}
:label: my-proposition

This is a dummy proposition directive.
```
``````

### Referencing Propositions

You can refer to a proposition using the `{proof:ref}` role like: ```{proof:ref}`my-proposition` ```, which will replace the reference with the proposition number like so: {proof:ref}`my-proposition`. When an explicit text is provided, this caption will serve as the title of the reference.
