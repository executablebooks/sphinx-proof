# Testing

For code tests, `sphinxcontrib-prettyproof` uses [pytest](https://docs.pytest.org/).

Run the tests with the following command:

```shell
>> cd sphinxcontrib-prettyproof
>> pip install -e .[testing]
>> pytest
```

To run the tests in multiple isolated environments, you can also run [tox](https://tox.readthedocs.io/)

```shell
>> cd sphinxcontrib-prettyproof
>> tox
```

To test the build of documentation run

```shell
>> cd sphinxcontrib-prettyproof
>> tox docs-update
```

or

```shell
>> cd sphinxcontrib-prettyproof/docs
>> make clean
>> make html
```

## Unit Testing

We use [pytest](https://docs.pytest.org/en/latest/) for testing, [pytest-regression](https://pytest-regressions.readthedocs.io/en/latest/) to regenerate expected outcomes of test and [pytest-cov](https://pytest-cov.readthedocs.io/en/latest/) for checking coverage.

To run tests with coverage and an html coverage report:

```bash
pytest -v --cov=sphinxcontrib --cov-report=html
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
