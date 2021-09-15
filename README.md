# data-platform-template
Template repository for data-platform projects

## How this all works
This repo houses a [cookiecutter](https://cookiecutter.readthedocs.io/en/1.7.2/) template for creating new python based data-platform jobs.

## Using this template
The template defines the following template variables 
- `full_name`: The author of the projects full name.
- `email`: The email associated with the project.
- `project_name`: The human readable name of the project.
- `project_slug`: The python package name/machine readable name for the project, defaults to `project_name.lower().replace(' ', '_').replace('-', '_')`
- `project_executabl`e`: The name of the executable created for the project, defaults to `project_slug.replace('_', '-')`
- `description`: A short description of the project.
- `version`: The version of the project, defaults to 0.0.1
- `python_version`: Which python version to use for the project, defaults to 3.8.

### Prerequisites
You will need the cookiecutter cli tool in order to generate a project from the this template. The python dependencies in the generated project are installed using poetry. You will need that as well
```
$ brew install cookiecutter poetry
```

### Project generation
1. Clone this repository
1. Run the cookiecutter tool on the cloned repo.
    - `$ cookiecutter <path to cloned repo>`
1. `$ cd <path to generated project folder>`
1. poetry install
1. poetry run pytest
