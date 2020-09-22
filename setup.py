# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

VERSION = "v0.0.2a"

LONG_DESCRIPTION = """
This package contains a [Sphinx](http://www.sphinx-doc.org/en/master/) extension
for producing proof, theorem, axiom, lemma, definition, criterion, remark, conjecture,
corollary, algorithm, exercise, example, property, observation and proposition
directives.

This project is maintained and supported by [najuzilu](https://github.com/najuzilu).
"""

SHORT_DESCRIPTION = "A Sphinx extension for producing proofs, theorems, axioms, etc."

URL = f"https://github.com/executablebooks/sphinxcontrib-prettyproof/archive/{VERSION}.tar.gz"

# Define all extras
extras = {
    "code_style": ["flake8<3.8.0,>=3.7.0", "black", "pre-commit==1.17.0"],
    "testing": [
        "coverage",
        "pytest>=3.6,<4",
        "pytest-cov",
        "pytest-regressions",
        "beautifulsoup4",
        "myst-parser",
    ],
    "rtd": [
        "sphinx>=3.0",
        "sphinx-book-theme",
        "sphinxcontrib-bibtex",
        "myst-parser",
    ],
}

extras["all"] = set(ii for jj in extras.values() for ii in jj)

setup(
    name="sphinxcontrib-prettyproof",
    version=VERSION,
    python_requires=">=3.6",
    author="QuantEcon",
    author_email="admin@quantecon.org",
    url="https://github.com/executablebooks/sphinxcontrib-prettyproof",
    download_url=URL,
    project_urls={
        "Source": "https://github.com/executablebooks/sphinxcontrib-prettyproof",
        "Tracker": "https://github.com/executablebooks/sphinxcontrib-prettyproof/issues",
    },
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="BSD",
    packages=find_packages(),
    install_requires=["docutils>=0.15", "sphinx", "sphinx-book-theme"],
    extras_require=extras,
    include_package_data=True,
    namespace_packages=["sphinxcontrib"],
)
