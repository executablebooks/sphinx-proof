# Testing

```{proof:solution} my-exercise2
blabla bla bla.
bla bla bla bla.
```

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
