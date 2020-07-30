# sphinxcontrib-pretty-proof

[![Documentation Status](https://readthedocs.org/projects/sphinxcontrib-pretty-proof/badge/?version=latest)](https://sphinxcontrib-pretty-proof.readthedocs.io/en/latest/?badge=latest)


**A proof extension for Sphinx**.

This package contains a [Sphinx](http://www.sphinx-doc.org/en/master/) extension
for producing proof, theorem, axiom, lemma, definition, criteria, remark, conjecture, corollary, algorithm and exercise directives.

```{warning}
sphinxcontrib-pretty-proof `0.1.0a` is in a development stage and may change rapidly.
```


## Get started

To get started with `sphinxcontrib-pretty-proof`, first install it through `pip`:

```
pip install sphinxcontrib-pretty-proof
```

then, add `sphinxcontrib.pretty_proof` to your sphinx `extensions` in the `conf.py`

```python
...
extensions = ["sphinxcontrib.pretty_proof"]
...
```


## Installation


**Step 1:** To install the extension you need to clone the repository then run:

```python
python setup.py install
```

**Step 2:** Add `sphinxcontrib.pretty_proof` to your sphinx `extensions` in the `conf.py`

**Step 3:** Build using ``make html``


## Test

```{proof:proof} This is a
proof directive.
```

```{proof:theorem} Title
This is a theorem directive.
```

```{proof:axiom} Title
This is a theorem directive.
```

```{proof:lemma} Title
This is a theorem directive.
```

```{proof:definition} Title
This is a theorem directive.
```

```{proof:corollary} Title
This is a theorem directive.
```

```{proof:conjecture} Title
This is a theorem directive.
```

```{proof:algorithm} Title
This is a theorem directive.
```

```{proof:criteria} Title
This is a theorem directive.
```

```{proof:exercise} Title
This is a theorem directive.
```