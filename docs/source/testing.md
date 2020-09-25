# Testing

For code tests, `sphinx-proof` uses [pytest](https://docs.pytest.org/).

Run the tests with the following command:

```shell
>> cd sphinx-proof
>> pip install -e .[testing]
>> pytest
```

To run the tests in multiple isolated environments, you can also run [tox](https://tox.readthedocs.io/)

```shell
>> cd sphinx-proof
>> tox
```

To test the build of documentation run

```shell
>> cd sphinx-proof
>> tox docs-update
```

or

```shell
>> cd sphinx-proof/docs
>> make clean
>> make html
```

## Unit Testing

We use [pytest](https://docs.pytest.org/en/latest/) for testing, [pytest-regression](https://pytest-regressions.readthedocs.io/en/latest/) to regenerate expected outcomes of test and [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) for checking coverage.

To run tests with coverage and an html coverage report:

```bash
pytest -v --cov=sphinx_proof --cov-report=html
```

## Writing Tests

The module `sphinx.testing` is used to run sphinx builds for tests, in a temporary directory.

If creating a new source folder for test files, folder name should start with `test-`.
Your folder should reside inside the `tests/books` directory, which has been set as the root directory for tests.

The tests should start with:

```python
@pytest.mark.sphinx('html', testroot="mybook")
```
In the above declaration, `html` builder is used. And `mybook` is the source folder which was created with the name `test-mybook` inside `tests/books` folder.

Sphinx Application API is available as a parameter to all the test functions:

```python
@pytest.mark.sphinx('html', testroot="mybook")
def mytest(app):
```

## Code Style

Code is formatted using [black](https://github.com/ambv/black) and code style is tested using [flake8](http://flake8.pycqa.org) with style configuration set in `.flake8`.

Installing using `[code style]` will make the [pre-commit](https://pre-commit.com/) package available which will make sure the style is met before your commits are submitted. In addition, it will reformat for any lint errors.

To install `pre-commit` run the following

```bash
cd sphinx-proof
pre-commit install
```

`black` and `flake8` can be run separately:

```shell
>>> black .
>>> flake8 .
```
