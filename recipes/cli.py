"""Commandline interface for running FastAPI server."""
import typer
import uvicorn

from recipes.settings import settings

app = typer.Typer()

DEFAULT_ENV_FILE = "../.env"


@app.command()
def run_server(
    host: str = typer.Option("0.0.0.0"),
    port: int = typer.Option(8000),
    reload: bool = typer.Option(False),
):
    """
    Run uvicorn server.

    :param str host: ip address or domain name
    :param int port: Port to allocate with server
    :param bool reload: reload server on code change
    """
    uvicorn.run(settings.APP, host=host, port=port, reload=reload, lifespan="on")


def main():
    """Run server."""
    app()


if __name__ == "__main__":
    main()
