# sphinx-proof

```{toctree}
:hidden:

install
syntax
testing
zreferences
```

[![Documentation Status][rtd-badge]][rtd-link]
[![Github-CI][github-ci]][github-link]
[![Coverage Status][codecov-badge]][codecov-link]

**A proof extension for Sphinx**.

This package contains a [Sphinx](http://www.sphinx-doc.org/en/master/) extension
for producing proof, theorem, axiom, lemma, definition, criterion, remark, conjecture,
corollary, algorithm, example, property, observation, proposition and assumption directives.

**Features**:

1. directives are automatically numbered
2. supports directive options such as `class`, `label`, and `nonumber`
3. can easily be referenced through `prf:ref` role

(getting-started)=
## Getting Started

To get started with `sphinx-proof`, first install it through `pip`:

```bash
pip install sphinx-proof
```

### Juputer-Book Project

Add `sphinx_proof` to your [extra_extensions](https://jupyterbook.org/advanced/sphinx.html#custom-sphinx-extensions) config in `_config.yml`

```yaml
sphinx:
  extra_extensions:
    - sphinx_proof
```

you may then use `jb build <project>` and the extension will be used by your `JupyterBook` project.

### Sphinx Project

Add `sphinx_proof` to your sphinx `extensions` in the `conf.py`

```python
...
extensions = ["sphinx_proof"]
...
```

you may then build using `make html` and the extension will be used by your `Sphinx` project.


[rtd-badge]: https://readthedocs.org/projects/sphinx-proof/badge/?version=latest
[rtd-link]: https://sphinx-proof.readthedocs.io/en/latest/?badge=latest
[github-ci]: https://github.com/executablebooks/sphinx-proof/workflows/continuous-integration/badge.svg?branch=master
[github-link]: https://github.com/executablebooks/sphinx-proof
[codecov-badge]: https://codecov.io/gh/executablebooks/sphinx-proof/branch/master/graph/badge.svg
[codecov-link]: https://codecov.io/gh/executablebooks/sphinx-proof
