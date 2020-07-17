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
    name="sphinxcontrib-theorem",
    version=VERSION,
    url="https://github.com/najuzilu/sphinxcontrib-pretty-proof",
    download_url="https://github.com/najuzilu/sphinxcontrib-pretty-proof/archive/{}.tar.gz".format(
        VERSION
    ),
    license="BSD",
    author="QuantEcon",
    author_email="admin@quantecon.org",
    description='A Sphinx extension for producing proofs, theorems, lemmas, definitions, remarks, corollaries, conjectures and algorithms.',
    long_description=LONG_DESCRIPTION,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Sphinx",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Framework :: Sphinx :: Extension",
    ],
    platforms="any",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["docutils", "sphinx", "sphinx-book-theme"],
    extras_require={
        # "code_style": ["flake8<3.8.0,>=3.7.0", "black", "pre-commit==1.17.0"],
        "testing": ["coverage", "pytest>=3.6,<4", "pytest-cov", "pytest-regressions",],
    },
    namespace_packages=["sphinxcontrib"],
)
