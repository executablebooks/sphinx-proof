from pathlib import Path
from subprocess import run, PIPE
import pytest
import os

path_tests = Path(__file__).parent.resolve()
path_book = path_tests.joinpath("books", "mybook")
path_root = path_tests.parent


def test_build_book(tmpdir):
    """Test building the book template and a few test configs."""

    os.chdir(path_book)

    # Clean build
    run(f"make clean".split())
    assert path_book.joinpath("conf.py").exists()

    # Build the book
    run(f"make html".split(), check=True)
    path_html = path_book.joinpath("build", "html")

    assert path_book.joinpath("build").exists()
    assert path_html.joinpath("index.html").exists()
    assert path_html.joinpath("algorithm").exists()
    assert path_html.joinpath("proof").exists()
