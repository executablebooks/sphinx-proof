from pathlib import Path
from subprocess import run
from bs4 import BeautifulSoup
import os

path_tests = Path(__file__).parent.resolve()
path_book = path_tests.joinpath("books", "mybook")
path_html = path_book.joinpath("build", "html")
path_algo = path_html.joinpath("algorithm")


def test_build(tmpdir):
    """Test building the book template and a few test configs."""
    os.chdir(path_book)

    # Clean build
    run("make clean".split())
    assert path_book.joinpath("conf.py").exists()

    # Build the book
    run("make html".split(), check=True)

    assert path_book.joinpath("build").exists()
    assert path_html.joinpath("index.html").exists()
    assert path_algo.exists()


def test_algorithm(tmpdir, file_regression):
    """Test algorithm directive markup."""

    # assert each file exists in build
    algo_list = [
        "_algo_labeled_titled_with_classname.rst",
        "_algo_nonumber.rst",
    ]

    for idir in algo_list:
        fname = idir.split(".")[0] + ".html"
        path_algo_directive = path_algo.joinpath(fname)
        assert path_algo_directive.exists()

        # get content markup
        soup = BeautifulSoup(
            path_algo_directive.read_text(encoding="utf8"), "html.parser"
        )

        algo = soup.select("div.algorithm")[0]
        file_regression.check(str(algo), basename=idir.split(".")[0], extension=".html")


def test_reference(tmpdir, file_regression):
    """Test algorithm ref role markup."""

    algo_list = [
        "_algo_numbered_reference.rst",
        "_algo_text_reference.rst",
    ]

    for idir in algo_list:
        fname = idir.split(".")[0] + ".html"
        path_algo_directive = path_algo.joinpath(fname)
        assert path_algo_directive.exists()

        # get content markup
        soup = BeautifulSoup(
            path_algo_directive.read_text(encoding="utf8"), "html.parser"
        )

        algo = soup.select("p")[0]
        file_regression.check(str(algo), basename=idir.split(".")[0], extension=".html")
