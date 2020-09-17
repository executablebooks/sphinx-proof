from bs4 import BeautifulSoup
import pytest
import shutil


@pytest.mark.sphinx("html", testroot="mybook")
def test_warnings(app, warnings):
    build_path = app.srcdir.joinpath("_build")
    shutil.rmtree(build_path)
    app.build()
    assert "WARNING: label 'foobar' not found" in warnings(app)
    assert "WARNING: label 'wrong-ex-label' not found" in warnings(app)
    assert 'WARNING: Error in "proof:solution" directive' in warnings(app)


@pytest.mark.sphinx("html", testroot="mybook")
@pytest.mark.parametrize(
    "idir",
    [
        "_solution_with_exercise_nonumber_notitle.html",
        "_solution_with_exercise_nonumber_title.html",
        "_solution_with_exercise_nonumber_title_inlinemath.html",
        "_solution_with_exercise_nonumber_title_inlinemath2.html",
        "_solution_with_exercise_number.html",
        "_solution_with_label_and_class.html",
    ],
)
def test_solution(app, idir, file_regression):
    """Test solution directive markup."""
    app.build()
    path_solution_directive = app.outdir / "solution" / idir
    assert path_solution_directive.exists()

    # get content markup
    soup = BeautifulSoup(
        path_solution_directive.read_text(encoding="utf8"), "html.parser"
    )

    sol = soup.select("div.solution")[0]
    file_regression.check(str(sol), basename=idir.split(".")[0], extension=".html")


@pytest.mark.sphinx("html", testroot="mybook")
@pytest.mark.parametrize(
    "idir",
    [
        "_solution_ref_with_nonumber_notitle.html",
        "_solution_ref_with_nonumber_title.html",
        "_solution_ref_with_nonumber_title_inlinemath.html",
        "_solution_ref_with_nonumber_title_inlinemath2.html",
        "_solution_ref_with_number.html",
        "_solution_ref_wrong_solution_ref.html",
    ],
)
def test_reference(app, idir, file_regression):
    """Test solution ref role markup."""
    app.builder.build_all()
    path_solution_directive = app.outdir / "solution" / idir
    assert path_solution_directive.exists()
    # get content markup
    soup = BeautifulSoup(
        path_solution_directive.read_text(encoding="utf8"), "html.parser"
    )

    if idir == "_solution_ref_wrong_solution_ref.html":
        sol = str(soup.select("p")[0])
    else:
        sol = f'{soup.select("p")[0]}\n{soup.select("p")[1]}'
    file_regression.check(sol, basename=idir.split(".")[0], extension=".html")
