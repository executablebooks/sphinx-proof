import shutil
from pathlib import pathlib

import pytest

from click.testing import CliRunner

@pytest.fixture()
def mybook(tmpdir):
    src = Path(__file__).parent.resolve().joinpath("books","mybook").absolute()
    dst = tmpdir.join("mybook")
    shutil.copytree(src, dst)
    mybook = Path(dst)
    yield mybook
    shutil.rmtree(dst)


@pytest.fixture()
def cli():
    """Provides a click.testing CliRunner object for invoking CLI commands.
    """
    runner = CliRunner()
    return runner


