"""Main file that connects all routes & run server."""
from fastapi import APIRouter, FastAPI

from recipes.settings import settings


def register_routers(rest_app: FastAPI):
    """
    Register routers.

    :param FastAPI rest_app: FastAPI application instance
    """
    domain_router = APIRouter()

    rest_app.include_router(
        domain_router,
        prefix=settings.ENDPOINT,
    )


def get_app():
    """
    Create FastAPI instance with settings stored in .env file.

    :return FastAPI: FastAPI server instance
    """
    rest_app = FastAPI(
        docs_url=f"{settings.ENDPOINT}/docs",
        redoc_url=f"{settings.ENDPOINT}/redoc",
        openapi_url=f"{settings.ENDPOINT}/openapi.json",
        debug=settings.DEBUG,
    )
    register_routers(rest_app)
    return rest_app


app = get_app()
