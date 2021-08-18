from bs4 import BeautifulSoup
import pytest


@pytest.mark.sphinx("html", testroot="missingref")
def test_missing_ref(app, warnings):
    # Clean build
    app.build()
    assert "WARNING: label 'foo' not found" in warnings(app)


# Tests for algorithms
@pytest.mark.sphinx("html", testroot="mybook")
@pytest.mark.parametrize(
    "idir",
    [
        "algorithm/_algo_labeled_titled_with_classname.html",
        "algorithm/_algo_nonumber.html",
    ],
)
def test_algorithm(app, idir, file_regression):
    """Test algorithm directive markup."""
    app.build()
    path_algo_directive = app.outdir / idir
    assert path_algo_directive.exists()

    # get content markup
    soup = BeautifulSoup(path_algo_directive.read_text(encoding="utf8"), "html.parser")
    algo = soup.select("div.algorithm")[0]
    file_regression.check(str(algo), basename=idir.split(".")[0], extension=".html")


@pytest.mark.sphinx("html", testroot="mybook")
@pytest.mark.parametrize(
    "idir",
    ["algorithm/_algo_numbered_reference.html", "algorithm/_algo_text_reference.html"],
)
def test_reference(app, idir, file_regression):
    """Test algorithm ref role markup."""
    app.builder.build_all()
    path_algo_directive = app.outdir / idir
    assert path_algo_directive.exists()
    # get content markup
    soup = BeautifulSoup(path_algo_directive.read_text(encoding="utf8"), "html.parser")

    algo = soup.select("p")[0]
    file_regression.check(str(algo), basename=idir.split(".")[0], extension=".html")


@pytest.mark.sphinx("html", testroot="duplicatelabel")
def test_duplicate_label(app, warnings):
    app.build()
    assert "WARNING: duplicate algorithm label" in warnings(app)


# Tests for Proofs
@pytest.mark.sphinx("html", testroot="mybook")
@pytest.mark.parametrize(
    "idir",
    [
        "proof/_proof_with_classname.html",
        "proof/_proof_no_classname.html",
        "proof/_proof_with_argument_content.html",
        "proof/_proof_with_labeled_math.html",
        "proof/_proof_with_unlabeled_math.html",
    ],
)
def test_proof(app, idir, file_regression):
    """Test proof directive markup."""
    app.build()
    path_proof_directive = app.outdir / idir
    assert path_proof_directive.exists()

    # get content markup
    soup = BeautifulSoup(path_proof_directive.read_text(encoding="utf8"), "html.parser")

    proof = soup.select("div.proof")[0]
    file_regression.check(str(proof), basename=idir.split(".")[0], extension=".html")


# Tests for numbering
@pytest.mark.sphinx("html", testroot="mybook")
@pytest.mark.parametrize(
    "idir",
    [
        "algorithm/_algo_labeled_titled_with_classname.html",
        "theorem/_theorems_with_number.html",
    ],
)
def test_numbering(app, idir, file_regression):
    """Test numbering of different directives."""
    app.build()
    path_directive = app.outdir / idir
    assert path_directive.exists()

    # get content markup
    soup = BeautifulSoup(path_directive.read_text(encoding="utf8"), "html.parser")
    proof = soup.select("div.proof")[0]
    file_regression.check(str(proof), basename=idir.split(".")[0], extension=".html")
