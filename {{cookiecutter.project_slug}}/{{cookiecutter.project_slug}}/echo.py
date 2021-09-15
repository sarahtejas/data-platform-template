import typer
from {{cookiecutter.project_slug}}  import get_file


def noop(noop_str: str) -> str:
    """
    noop noop just returns that is passed to it.

    :param noop_str: The value to be returned.
    :type noop_str: str
    :return: The parameter foo
    :rtype: str
    """
    return noop_str


def main(ctx: typer.Context):
    """
    Main prints out a string in the resources/echo/echo.txt file

    :param ctx: The context object passed to the task.
    :type ctx: invoke.Context
    :return: The result of the echo.
    :rtype: invoke.Result
    """
    echo_file = get_file(["echo", "echo.txt"])
    echo_str = ""
    with open(echo_file) as file:
        echo_str = file.read()
    return print(f"{noop(echo_str)}")
