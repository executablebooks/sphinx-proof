# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

VERSION = "v0.1.3"

LONG_DESCRIPTION = """
This package contains a [Sphinx](http://www.sphinx-doc.org/en/master/) extension
for producing proof, theorem, axiom, lemma, definition, criterion, remark, conjecture,
corollary, algorithm, example, property, observation, proposition, and
assumption directives.

This project is maintained and supported by [najuzilu](https://github.com/najuzilu).
"""

SHORT_DESCRIPTION = "A Sphinx extension for producing proofs, theorems, axioms, etc."

BASE_URL = "https://github.com/executablebooks/sphinx-proof"
URL = f"{BASE_URL}/archive/{VERSION}.tar.gz"

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
        "texsoup",
    ],
    "rtd": [
        "sphinx>=3.0",
        "sphinx-book-theme",
        "sphinxcontrib-bibtex",
        "myst-parser",
        "sphinx_togglebutton",
    ],
}

extras["all"] = set(ii for jj in extras.values() for ii in jj)

setup(
    name="sphinx-proof",
    version=VERSION,
    python_requires=">=3.6",
    author="QuantEcon",
    author_email="admin@quantecon.org",
    url=BASE_URL,
    download_url=URL,
    project_urls={
        "Source": BASE_URL,
        "Tracker": f"{BASE_URL}/issues",
    },
    description=SHORT_DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="BSD",
    packages=find_packages(),
    install_requires=["docutils>=0.15", "sphinx", "sphinx-book-theme"],
    extras_require=extras,
    include_package_data=True,
)
