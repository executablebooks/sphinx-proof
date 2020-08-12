# Documentation

## Example

```{proof:theorem}
```

```{proof:proof}
```

```{proof:axiom}
```

```{proof:lemma}
```

```{proof:definition}
```

```{proof:criteria}
```

```{proof:remark}
```

```{proof:conjecture}
```

```{proof:corollary}
```

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

```{proof:exercise}
```


## Source



## Contribute

`sphinxcontrib-pretty-proof` is an open project and we welcome your feedback and contributions! To contribute to `sphinxcontrib-pretty-proof`, see [Contribute to `sphinxcontrib-pretty-proof`]().

