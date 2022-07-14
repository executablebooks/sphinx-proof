# sphinx-proof

[![Documentation Status][rtd-badge]][rtd-link]
[![Github-CI][github-ci]][github-link]
[![Coverage Status][codecov-badge]][codecov-link]

**A proof extension for Sphinx**.

This package contains a [Sphinx](http://www.sphinx-doc.org/en/master/) extension
for producing proof, theorem, axiom, lemma, definition, criterion, remark, conjecture,
corollary, algorithm, example, property, observation, proposition and assumption directives.


## Get started

To get started with `sphinx-proof`, first install it through `pip`:

```
pip install sphinx-proof
```

then, add `sphinx_proof` to your sphinx `extensions` in the `conf.py`

```python
...
extensions = ["sphinx_proof"]
...
```


## Documentation

See the [Sphinx Proof documentation](https://sphinx-proof.readthedocs.io/en/latest/) for more information.


## Contributing

We welcome all contributions! See the [EBP Contributing Guide](https://executablebooks.org/en/latest/contributing.html) for general details, and below for guidance specific to sphinx-proof.


[rtd-badge]: https://readthedocs.org/projects/sphinx-proof/badge/?version=latest
[rtd-link]: https://sphinx-proof.readthedocs.io/en/latest/?badge=latest
[github-ci]: https://github.com/executablebooks/sphinx-proof/workflows/continuous-integration/badge.svg?branch=master
[github-link]: https://github.com/executablebooks/sphinx-proof
[codecov-badge]: https://codecov.io/gh/executablebooks/sphinx-proof/branch/master/graph/badge.svg
[codecov-link]: https://codecov.io/gh/executablebooks/sphinx-proof
