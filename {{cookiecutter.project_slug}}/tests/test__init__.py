import logging
import os
from pathlib import Path

import pytest
import rollbar

from {{cookiecutter.project_slug}} import configure_logger, get_file, initialize_rollbar


@pytest.fixture
def filepath():
    return ["test_file.sql"]


def test_get_file_returns_expected_path(filepath):
    test_path = os.path.join(
        Path(__file__).parent.parent, "{{cookiecutter.project_slug}}", "resources", filepath[0]
    )
    file = get_file(filepath)

    assert test_path == file


def test_get_file_path_exists(filepath):
    file = get_file(filepath)

    assert Path(file).exists


def test_initialize_rollbar(mocker):
    mocker.patch("rollbar.init")
    initialize_rollbar()
    rollbar.init.assert_called_once()


def test_configure_logger(mocker):
    def mock_environ_get(val, default=""):
        if val == "LOG_LEVEL":
            return "warning"
        return default
    mocker.patch("os.environ.get", mock_environ_get)

    log = configure_logger()

    assert log.level == logging.WARNING
    assert log.name == "{{cookiecutter.project_slug}}"
