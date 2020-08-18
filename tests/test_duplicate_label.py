from pathlib import Path
from subprocess import run
import pytest
import os


path_tests = Path(__file__).parent.resolve()
path_book = path_tests.joinpath("books", "duplicate_label")
path_html = path_book.joinpath("build", "html")


def test_build(capfd):
    # Clean build
    os.chdir(path_book)

    run(f"make clean".split())
    assert path_book.joinpath("conf.py").exists()

    run(f"make html".split(), check=True)
    out, err = capfd.readouterr()

    assert "WARNING: duplicate algorithm label" in err
