# Documentation

## Examples

```{math}
\DeclareMathOperator*{\argmax}{arg\,max}
\DeclareMathOperator*{\argmin}{arg\,min}
```

````{proof:theorem} Orthogonal-Projection-Theorem
:label: opt

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
_Source:_ [QuantEcon](https://python-advanced.quantecon.org/orth_proj.html#The-Orthogonal-Projection-Theorem)

{proof:ref}`opt` or {proof:ref}`Orthogonal-Projection-Theorem <opt>` can be referenced through the `:label:` option.

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
_Source:_ [QuantEcon](https://python-advanced.quantecon.org/orth_proj.html#The-Orthogonal-Projection-Theorem)


```{proof:axiom}
```
_Source:_


````{proof:lemma}
If $\hat P$ is the fixed point of the map $\mathcal B \circ \mathcal D$ and $\hat F$ is the robust policy as given in [(7)](https://python-advanced.quantecon.org/robustness.html#equation-rb-oc-ih), then

```{math}
:label: rb_kft

K(\hat F, \theta) = (\theta I - C'\hat P C)^{-1} C' \hat P  (A - B \hat F)
```
````
_Source:_ [QuantEcon](https://python-advanced.quantecon.org/robustness.html#Appendix)


````{proof:definition}
The *economical expansion problem* (EEP) for
$(A,B)$ is to find a semi-positive $n$-vector $p>0$
and a number $\beta\in\mathbb{R}$, such that

$$
&\min_{\beta} \hspace{2mm} \beta \\
&\text{s.t. }\hspace{2mm}Bp \leq \beta Ap
$$

````
_Source:_ [QuantEcon](https://python-advanced.quantecon.org/von_neumann_model.html#Duality)


```{proof:criteria}
```
_Source:_


```{proof:remark}
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
_Source:_ [QuantEcon](https://python-advanced.quantecon.org/black_litterman.html)


```{proof:conjecture}
```
_Source:_


```{proof:corollary}
```
_Source:_


```{proof:algorithm} Ford–Fulkerson

**Inputs** Given a Network $G=(V,E)$ with flow capacity $c$, a source node $s$, and a sink node $t$

**Output** Compute a flow $f$ from $s$ to $t$ of maximum value

1. $f(u, v) \leftarrow 0$ for all edges $(u,v)$
2. While there is a path $p$ from $s$ to $t$ in $G_{f}$ such that $c_{f}(u,v)>0$ for all edges $(u,v) \in p$:

	1. Find $c_{f}(p)= \min \{c_{f}(u,v):(u,v)\in p\}$
	2. For each edge $(u,v) \in p$

		1. $f(u,v) \leftarrow f(u,v) + c_{f}(p)$ *(Send flow along the path)*
		2. $f(u,v) \leftarrow f(u,v) - c_{f}(p)$ *(The flow might be "returned" later)*
```
_Source:_ [Wikipedia](https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm).


```{proof:exercise}
```


## Source



## Contribute

<!-- `sphinxcontrib-prettyproof` is an open project and we welcome your feedback and contributions! To contribute to `sphinxcontrib-prettyproof`, see [Contribute to `sphinxcontrib-prettyproof`](). -->

