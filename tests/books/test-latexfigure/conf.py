# Test root for captioned figures inside prf directive boxes in LaTeX output
# (https://github.com/executablebooks/sphinx-proof/issues/169). The boxes are
# in a chapter, figures.rst, as in a book: boxes in the root document itself
# lose their numbers in LaTeX output.

project = "sphinx-proof Test"
copyright = "2020, QuantEcon Developers"
author = "QuantEcon Developers"

extensions = ["sphinx_proof"]
