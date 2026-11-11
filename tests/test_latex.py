import re

from TexSoup import TexSoup
import pytest


@pytest.mark.sphinx("latex", testroot="mybook")
def test_latex_build(app, file_regression):
    """Test algorithm directive markup."""
    app.build()
    path_algo_directive = app.outdir / "sphinx-prooftest.tex"
    assert path_algo_directive.exists()

    # get content markup
    file_content = TexSoup(path_algo_directive.read_text(encoding="utf8"))
    file_regression.check(str(file_content.document), extension=".tex", encoding="utf8")


LATEX_FIGURE = re.compile(
    r"\\begin\{figure\}\[(?P<align>[^\]]*)\](?P<body>.*?)\\end\{figure\}", re.DOTALL
)
# A figure's :name: becomes \label{\detokenize{<docname>:<name>}}
LATEX_FIGURE_NAME = re.compile(r"\\label\{\\detokenize\{[^:}]*:(?P<name>[^}]+)\}\}")


def latex_figures(tex):
    """Map each figure's name to (figure placement, sphinxadmonition depth).

    A figure without a name is collected under None. A name seen twice
    fails, so no figure can drop out of the comparison unnoticed.
    """
    figures = {}
    for figure in LATEX_FIGURE.finditer(tex):
        before = tex[: figure.start()]
        depth = before.count(r"\begin{sphinxadmonition}") - before.count(
            r"\end{sphinxadmonition}"
        )
        name = LATEX_FIGURE_NAME.search(figure["body"])
        key = name["name"] if name else None
        assert key not in figures, f"two figures share the name {key!r}"
        figures[key] = (figure["align"], depth)
    return figures


@pytest.mark.sphinx("latex", testroot="latexfigure")
def test_latex_figure_in_admonition(app):
    """Figures inside prf directive boxes must not float (#169).

    A floating figure environment inside the sphinxadmonition box stops
    LaTeX with "Not in outer par mode".
    """
    app.build()
    tex = (app.outdir / "sphinx-prooftest.tex").read_text(encoding="utf8")

    assert latex_figures(tex) == {
        "fig-numbered-theorem": ("H", 1),
        "fig-unnumbered-lemma": ("H", 1),
        # prf:proof and note boxes come from Sphinx's own admonition visitors
        "fig-proof": ("H", 1),
        "fig-note": ("H", 1),
        # Figures after a nested box closes are still inside the outer box
        "fig-nested-lemma": ("H", 2),
        "fig-after-nested-lemma": ("H", 1),
        "fig-definition-in-note": ("H", 2),
        # Figures after the boxes float again, so the counter was restored
        "fig-outside": ("htbp", 0),
    }
