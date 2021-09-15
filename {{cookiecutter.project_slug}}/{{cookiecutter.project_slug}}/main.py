import datetime
import logging

import rollbar
import typer
from datadog import initialize as initialize_datadog
from datadog import statsd
from {{cookiecutter.project_slug}} import configure_logger, echo, initialize_rollbar

log = logging.getLogger(__package__)
app = typer.Typer(
    name=__package__,
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
)


def run():
    """
    run The entrypoint of the typer application.

    This wraps the typer application in a rollbar callback. This is used to call out to
    rollbar if there are any uncaught exceptions.
    """
    try:
        # initialize global things
        initialize_rollbar()
        configure_logger()

        # Run the typer app
        app()

    except Exception as err:
        log.exception(err)
        rollbar.report_exc_info(extra_data={"project": "{{cookiecutter.project_slug}}"})
        raise


@app.callback()
def callback(
    ctx: typer.Context,
    statsd_host: str = typer.Option(
        "", help="Where to emit the datadog statsd metrics to.", envvar="STATSD_HOST"
    ),
    statsd_port: int = typer.Option(
        0,
        help="Which port on the host to emit datadog statsd metrics to.",
        envvar="STATSD_PORT",
    ),
):  # pylint: disable=too-many-arguments
    """
    Sets up the context object for the subcommands. Initializes datadog and s3 and
    makes them available via the context object.
    """
    ctx.obj = {}

    log.debug(
        "Initializing Datadog client emitting metrics to: %s, on port: %s ...",
        statsd_host,
        statsd_port,
    )
    initialize_datadog(statsd_host=statsd_host, statsd_port=statsd_port)
    ctx.obj["statsd"] = statsd
    log.debug("Datadog client initialized.")

    ctx.obj["now"] = datetime.datetime.utcnow()


# register commands

## test_typer
app.command()(echo.main)


if __name__ == "__main__":
    run()
