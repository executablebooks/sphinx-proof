from pathlib import Path
from subprocess import run
from bs4 import BeautifulSoup
import pytest
import os

path_tests = Path(__file__).parent.resolve()
path_book = path_tests.joinpath("books", "mybook")
path_html = path_book.joinpath("build", "html")
path_proof = path_html.joinpath("proof")


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
    assert path_proof.exists()


@pytest.fixture()
def test_proof(tmpdir, file_regression):
    """Test proof directive markup."""

    # assert each file exists in build
    proof_list = [
        "_proof_with_classname.rst",
        "_proof_no_classname.rst",
        "_proof_with_argument_content.rst",
        "_proof_with_labeled_math.rst",
        "_proof_with_unlabeled_math.rst",
    ]

    for idir in proof_list:
        fname = idir.split(".")[0] + ".html"
        path_proof_directive = path_proof.joinpath(fname)
        assert path_proof_directive.exists()

        # get content markup
        soup = BeautifulSoup(
            path_proof_directive.read_text(encoding="utf8"), "html.parser"
        )

        proof = soup.select("div.proof")[0]
        file_regression.check(
            str(proof), basename=idir.split(".")[0], extension=".html"
        )
