# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

VERSION = "v0.0.1b"

LONG_DESCRIPTION = """
This package contains a [Sphinx](http://www.sphinx-doc.org/en/master/) extension
for producing proof, theorem, lemma, definition, remark, conjecture, corollary and
algorithm directives.

This project is maintained and supported by [najuzilu](https://github.com/najuzilu).
"""

setup(
    name="sphinxcontrib-prettyproof",
    version=VERSION,
    python_requires=">=3.6",
    author="QuantEcon",
    author_email="admin@quantecon.org",
    url="https://github.com/najuzilu/sphinxcontrib-prettyproof",
    download_url="https://github.com/najuzilu/sphinxcontrib-prettyproof/archive/{}.tar.gz".format(
        VERSION
    ),
    project_urls={
        "Source": "https://github.com/najuzilu/sphinxcontrib-prettyproof",
        "Tracker": "https://github.com/najuzilu/sphinxcontrib-prettyproof/issues",
    },
    description="A Sphinx extension for producing proofs, theorems, lemmas, definitions, remarks, corollaries, conjectures and algorithms.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="BSD",
    packages=find_packages(),
    install_requires=["docutils>=0.15", "sphinx", "sphinx-book-theme"],
    extras_require={
        "code_style": ["flake8<3.8.0,>=3.7.0", "black", "pre-commit==1.17.0"],
        "testing": ["coverage", "pytest>=3.6,<4", "pytest-cov", "pytest-regressions",],
    },
    package_data={"sphinxcontrib": ["_static/*"]},
    include_package_data=True,
    namespace_packages=["sphinxcontrib"],
)
