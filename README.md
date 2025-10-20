# sphinx-proof

[![Documentation Status][rtd-badge]][rtd-link]
[![Github-CI][github-ci]][github-link]
[![Coverage Status][codecov-badge]][codecov-link]
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/executablebooks/sphinx-proof/main.svg)](https://results.pre-commit.ci/latest/github/executablebooks/sphinx-proof/main)


**A proof extension for Sphinx**.

This package contains a [Sphinx](http://www.sphinx-doc.org/) extension
for producing proof, theorem, axiom, lemma, definition, criterion, remark, conjecture,
corollary, algorithm, example, property, observation, proposition and assumption directives.

## Features

- **15 directive types** for mathematical proofs and theorems
- **Automatic numbering** of directives
- **Cross-referencing** support via `prf:ref` role
- **33 languages supported** - Complete translations for all directive types in English plus 32 additional languages (Arabic, Bengali, Bulgarian, Chinese, Czech, Danish, Dutch, Finnish, French, German, Greek, Hebrew, Hindi, Hungarian, Indonesian, Italian, Japanese, Korean, Malay, Norwegian, Persian, Polish, Portuguese, Romanian, Russian, Spanish, Swedish, Thai, Turkish, Ukrainian, Urdu, Vietnamese)
- **Customizable styling** with multiple theme options


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
[github-ci]: https://github.com/executablebooks/sphinx-proof/workflows/ci.yml/badge.svg?branch=main
[github-link]: https://github.com/executablebooks/sphinx-proof
[codecov-badge]: https://codecov.io/gh/executablebooks/sphinx-proof/branch/main/graph/badge.svg
[codecov-link]: https://codecov.io/gh/executablebooks/sphinx-proof
