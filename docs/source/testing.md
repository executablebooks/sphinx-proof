# Testing

For code tests, sphinxcontrib-prettyproof uses `pytest`.

Run the tests with the following command:

```
>> cd sphinxcontrib-prettyproof
>> pytest
```

## Writing Tests

The module `sphinx.testing` is used to run sphinx builds for tests, in a temporary directory.

If creating a new source folder for test files, folder name should start with `test-`.
Your folder should reside inside the `tests/books` directory, which has been set as the root directory for tests.

The tests should start with:

```
@pytest.mark.sphinx('html', testroot="mybook")
```
In the above declaration, `html` builder is used. And `mybook` is the source folder which was created with the name `test-mybook` inside `tests/books` folder.

Sphinx Application API is available as a parameter to all the test functions:

```
@pytest.mark.sphinx('html', testroot="mybook")
def mytest(app):
```

## Code Style

Code is formatted using [black](https://github.com/ambv/black) and code style is tested using [flake8](http://flake8.pycqa.org) with style configuration set in `.flake8`.

Installing using `[code style]` will make the [pre-commit](https://pre-commit.com/) package available which will make sure the style is met before your commits are submitted. In addition, it will reformat for any lint errors.

To install `pre-commit` run the following

```bash
cd sphinxcontrib-prettyproof
pre-commit install
```

`black` and `flake8` can be run separately:

```shell
>>> black .
>>> flake8 .
```
