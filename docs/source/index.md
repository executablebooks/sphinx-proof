# sphinxcontrib-prettyproof

```{toctree}
:hidden:

install
syntax
testing
zreferences
```

[![Documentation Status](https://readthedocs.org/projects/sphinxcontrib-prettyproof/badge/?version=latest)](https://sphinxcontrib-prettyproof.readthedocs.io/en/latest/?badge=latest)

**A proof extension for Sphinx**.

This package contains a [Sphinx](http://www.sphinx-doc.org/en/master/) extension
for producing proof, theorem, axiom, lemma, definition, criterion, remark, conjecture,
corollary, algorithm, exercise, example, property, observation and proposition directives.

```{warning}
sphinxcontrib-prettyproof `0.0.2` is in a development stage and may change rapidly.
```

**Features**:

1. directives are automatically numbered
2. supports directive options such as `class`, `label`, and `nonumber`
3. can easily be referenced through `proof:ref` role

(getting-started)=
## Getting Started

To get started with `sphinxcontrib-prettyproof`, first install it through `pip`:

```bash
pip install sphinxcontrib-prettyproof
```

### JuputerBook Project

Add `sphinxcontrib.prettyproof` to your [extra_extensions](https://jupyterbook.org/advanced/sphinx.html#custom-sphinx-extensions) config in `_config.yml`

```yaml
sphinx:
  extra_extensions:
    - sphinxcontrib.prettyproof
```

you may then use `jb build <project>` and the extension will be used by your `JupyterBook` project.

### Sphinx Project

Add `sphinxcontrib.prettyproof` to your sphinx `extensions` in the `conf.py`

```python
...
extensions = ["sphinxcontrib.prettyproof"]
...
```

you may then build using `make html` and the extension will be used by your `Sphinx` project.
