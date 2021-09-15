import pytest
import rollbar

from {{cookiecutter.project_slug}} import main


def test_rollbar_is_called_on_exception(mocker):
    mocker.patch("rollbar.report_exc_info")
    mocker.patch("os.environ.get", lambda val, default=None: default)
    mocker.patch.object(main.Program, "run", mocker.Mock(side_effect=Exception))
    with pytest.raises(Exception):
        main.program.run()
        rollbar.report_exc_info.assert_called_once_with(
            extra_data={"project": "{{cookiecutter.project_slug}}"}
        )
