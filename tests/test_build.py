from pathlib import Path
from subprocess import run, PIPE
import pytest
import os

@pytest.mark.sphinx('html', testroot='mybook')
def test_build(app):
    """Test building the book template and a few test configs."""
    app.build()
    assert (app.outdir / "index.html").exists()
    assert (app.outdir / "algorithm").exists()
    assert (app.outdir / "proof").exists()


@pytest.mark.sphinx('html', testroot='missingref')
def test_missing_ref(app):
    # Clean build
    app.build()
    warning = app._warning.getvalue().strip()
    assert "WARNING: label 'foo' not found" in warning