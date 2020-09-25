# Installation

The **recommended** method of installation for most users is via `pip` as detailed
in {ref}`getting-started`.

You can also install directly from the repository to get the latest `development` version

## Latest Version

You can clone the repository:

```bash
git clone https://github.com/executablebooks/sphinx-proof
```

then run:

```bash
python setup.py install
```

## Package development

To install `sphinx-proof` for package development:

```bash
git clone https://github.com/executablebooks/sphinx-proof
cd sphinx-proof
git checkout master
pip install -e .[all]
```
