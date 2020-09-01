from pathlib import Path
from subprocess import run, PIPE
from bs4 import BeautifulSoup
import pytest
import os

path_tests = Path(__file__).parent.resolve()
path_book = path_tests.joinpath("books", "mybook")
path_html = path_book.joinpath("build", "html")
path_algo = path_html.joinpath("algorithm")


def test_build(mybook):
    """Test building the book template and a few test configs."""
    assert mybook.joinpath("conf.py").exists()

    # Build the book
    run(f"make html".split(), check=True)

    build = mybook.joinpath("build")
    html = buid.joinpath("html")

    assert build.exists()
    assert html.joinpath("index.html").exists()
    assert build.joinpath("html","algorithm").exists()


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
