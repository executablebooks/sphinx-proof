# sphinxcontrib-pretty-proof

[![Documentation Status](https://readthedocs.org/projects/sphinxcontrib-pretty-proof/badge/?version=latest)](https://sphinxcontrib-pretty-proof.readthedocs.io/en/latest/?badge=latest)


**A proof extension for Sphinx**.

This package contains a [Sphinx](http://www.sphinx-doc.org/en/master/) extension
for producing proof, theorem, axiom, lemma, definition, criteria, remark, conjecture, corollary, algorithm and exercise directives.

```{warning}
sphinxcontrib-pretty-proof `0.1.0a` is in a development stage and may change rapidly.
```

**Features**:

1. directives are automatically numbered
2. supports directive options such as `class`, `label`, and `nonumber`
3. can easily be referenced through `proof:ref` and `proof:numref` roles


```{toctree}
:hidden:

usage
```

## Get started

To get started with `sphinxcontrib-pretty-proof`, first install it through `pip`:

```bash
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

```bash
python setup.py install
```

**Step 2:** Add `sphinxcontrib.pretty_proof` to your sphinx `extensions` in the `conf.py`

**Step 3:** Build using ``make html``

