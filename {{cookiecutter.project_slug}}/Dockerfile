FROM python:{{cookiecutter.python_version}}-slim as base
WORKDIR /app

FROM base as builder
ENV PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=0 \
    POETRY_VIRTUALENVS_IN_PROJECT=true

RUN pip install poetry
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-dev --no-root --no-interaction --no-ansi
COPY . .
RUN poetry build && /app/.venv/bin/pip install dist/*.whl

FROM base as final
COPY --from=builder /app /app
CMD [ "/app/.venv/bin/{{cookiecutter.project_executable}}" ]
