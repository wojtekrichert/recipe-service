import typer
import uvicorn

from recipe.settings import settings

app = typer.Typer()

DEFAULT_ENV_FILE = "../.env"


@app.command()
def run_server(
    host: str = typer.Option("0.0.0.0"),
    port: int = typer.Option(8000),
    reload: bool = typer.Option(False),
):
    uvicorn.run(settings.APP, host=host, port=port, reload=reload, lifespan="on")


def main():
    app()


if __name__ == "__main__":
    main()
