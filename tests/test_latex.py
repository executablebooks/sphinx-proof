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
