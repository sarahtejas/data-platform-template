from invoke import MockContext, Result

from {{cookiecutter.project_slug}} import get_file
from {{cookiecutter.project_slug}}.echo import echo


def test_noop():
    assert 0 == echo.noop(0)


def test_echo():
    with open(get_file(['echo', 'echo.txt'])) as file:
        file_contents = file.read()
        ctx = MockContext(run=Result(file_contents))
        res = echo.main(ctx)
        assert file_contents == res.stdout
