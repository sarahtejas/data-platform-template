import logging
import os
import pathlib
from importlib.metadata import version
from typing import List

import rollbar

# package version
__version__ = version("{{cookiecutter.project_slug}}")


def get_file(filename: List[str]) -> str:
    """
    get_file gets a file from the resources directory
    according to the provided filepath list.

    :param filename: Where to look in the resources folder for the file.
    :type filename: List[str]
    :return: The contents of the file.
    :rtype: str
    """
    parent_dir = pathlib.Path(__file__).parent.absolute()
    filepath = os.path.join(parent_dir, "resources", *filename)

    return filepath


def configure_logger():
    """
    configure_log_level Configures the global logger from the environment.

    Borrowed from the python logging docs,
    https://docs.python.org/3/howto/logging.html
    Uses the following environment variable to initialize the logger:
    - LOG_LEVEL

    :raises ValueError: If the level is invalid
    """
    level = os.environ.get("LOG_LEVEL", "info")
    try:
        numeric_level = int(level)
    except ValueError:
        numeric_level = getattr(logging, level.upper(), None)
        if not isinstance(numeric_level, int):
            raise ValueError("Invalid log level: %s" % level)
    logger = logging.getLogger(__package__)
    logger.setLevel(numeric_level)
    return logger


def initialize_rollbar():
    """
    initialize_rollbar Initializes the globar rollbar library.

    Uses the following environment variables to initialize the library:
    - ROLLBAR_TOKEN
    - ROLLBAR_ENVIRONMENT
    """
    token = os.environ.get("ROLLBAR_TOKEN", "")
    environment = os.environ.get("ROLLBAR_ENVIRONMENT")
    rollbar.init(token, environment)
