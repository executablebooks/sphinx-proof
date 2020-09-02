from bs4 import BeautifulSoup
import pytest
import os

@pytest.mark.sphinx('html', testroot="mybook")
@pytest.mark.parametrize("idir",["_algo_labeled_titled_with_classname.html", "_algo_nonumber.html"])
def test_algorithm(app, idir, file_regression):
    """Test algorithm directive markup."""
    app.build()
    path_algo_directive = (app.outdir / "algorithm" / idir)
    assert path_algo_directive.exists()

    # get content markup
    soup = BeautifulSoup(
        path_algo_directive.read_text(encoding="utf8"), "html.parser"
    )
    algo = soup.select("div.algorithm")[0]
    file_regression.check(str(algo), basename=idir.split(".")[0], extension=".html")

@pytest.mark.sphinx('html', testroot="mybook")
@pytest.mark.parametrize("idir",["_algo_numbered_reference.html", "_algo_text_reference.html"])
def test_reference(app, idir, file_regression):
    """Test algorithm ref role markup."""
    app.builder.build_all()
    path_algo_directive = (app.outdir / "algorithm" / idir)
    assert path_algo_directive.exists()
    # get content markup
    soup = BeautifulSoup(
        path_algo_directive.read_text(encoding="utf8"), "html.parser"
    )

    algo = soup.select("p")[0]
    file_regression.check(str(algo), basename=idir.split(".")[0], extension=".html")

@pytest.mark.sphinx('html', testroot='duplicatelabel')
def test_duplicate_label(app, warnings):
    app.build()
    assert "WARNING: duplicate algorithm label" in warnings(app)