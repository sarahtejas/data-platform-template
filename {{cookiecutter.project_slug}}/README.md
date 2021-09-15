# {{cookiecutter.project_name}}
Write the description for {{cookiecutter.project_name}} here.


## Development
This project is setup with [poetry](https://python-poetry.org/docs/) to install a base set of dependenies for dev and the production environment.

### Prerequisites
1. Poetry; to install poetry `$ brew install poetry`
1. poetry install

### Testing
This project is setup to use the [pytest](https://docs.pytest.org/en/stable/) test running.

To run the tests run: 
```
$ poetry run pytest
```

### Linting
This project is setup to use two linters:
- [mypy](https://mypy.readthedocs.io/en/stable/)
- [pylint](https://pylint.pycqa.org/en/latest/)

To run the linters run:
```
poetry run pylint {{cookiecutter.project_slug}}
poetry run mypy {{cookiecutter.project_slug}}
```

### Formatting
This project is setup to be formatted with [black](https://black.readthedocs.io/en/stable/)

To run the formatter run:
```
poetry run black {{cookiecutter.project_slug}}
```

### Editor integration
If you use the popular VSCode editor the following config will setup all of the dev tool, (except tests), to run whenever a file is saved. To use place the config in a `.vscode/settings.json` file in the repo directory.
```
{
  "python.linting.mypyEnabled": true,
  "python.linting.mypyPath": "mypy",
  "python.linting.pylintPath": "pylint",
  "python.formatting.blackPath": "black",
  "editor.formatOnSave": true,
  "python.formatting.provider": "black",
  "python.linting.enabled": true,
  "python.pythonPath": "<path to your poetry virtualenv python>",
  "python.linting.pylintUseMinimalCheckers": false,
  "[python]": {
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  }
}
