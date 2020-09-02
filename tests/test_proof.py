from pathlib import Path
from subprocess import run, PIPE
from bs4 import BeautifulSoup
import pytest
import os

### just checking of path proof exists

@pytest.mark.sphinx('html', testroot="mybook")
@pytest.mark.parametrize("idir",[   
        "_proof_with_classname.html",
        "_proof_no_classname.html",
        "_proof_with_argument_content.html",
        "_proof_with_labeled_math.html",
        "_proof_with_unlabeled_math.html",
    ])
def test_proof(app, idir, file_regression):
    """Test proof directive markup."""
    app.build()
    path_proof_directive = app.outdir / "proof" / idir
    assert path_proof_directive.exists()

    # get content markup
    soup = BeautifulSoup(
        path_proof_directive.read_text(encoding="utf8"), "html.parser"
    )

    proof = soup.select("div.proof")[0]
    file_regression.check(
        str(proof), basename=idir.split(".")[0], extension=".html"
    )
