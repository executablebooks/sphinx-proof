# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

VERSION = "v0.1.0a"

LONG_DESCRIPTION = """
This package contains a `Sphinx <http://www.sphinx-doc.org/en/master/>`_ extension
for producing proof, theorem, lemma, definition, remark, conjecture, corollary and
algorithm directives.

This project is maintained and supported by `najuzilu <https://github.com/najuzilu>`_.
"""

requires = ["Sphinx>=0.6"]

setup(
    name="sphinxcontrib-pretty-proof",
    version=VERSION,
    python_requires=">=3.6",
    author="QuantEcon",
    author_email="admin@quantecon.org",
    url="https://github.com/najuzilu/sphinxcontrib-pretty-proof",
    download_url="https://github.com/najuzilu/sphinxcontrib-pretty-proof/archive/{}.tar.gz".format(
        VERSION
    ),
    project_urls={
        "Documentation": "",
        "Source": "",
        "Tracker": "",
    },
    description="A Sphinx extension for producing proofs, theorems, lemmas, definitions, remarks, corollaries, conjectures and algorithms.",
    # long_description=open("./README.md", "r").read(),
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="BSD",
    packages=find_packages(),
    install_requires=[
        "docutils>=0.15",
        "sphinx",
        "sphinx-book-theme"
    ],
    extras_require={
        "code_style": [
            "flake8<3.8.0,>=3.7.0",
            "black",
            "pre-commit==1.17.0"
        ],
        "testing": [
            "coverage",
            "pytest>=3.6,<4",
            "pytest-cov",
            "pytest-regressions",
        ],
    },
    entry_points={"sphinxcontrib.pretty_proof": ["sphinxcontrib_pretty_proof = sphinxcontrib_pretty_proof"]},
    package_data={
        "sphinxcontrib_pretty_proof": [
            "_static/*"
        ]
    },
    include_package_data=True,
    namespace_packages=["sphinxcontrib"],
)
