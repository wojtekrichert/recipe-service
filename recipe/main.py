from fastapi import APIRouter, FastAPI

from recipe.settings import settings


def register_routers(rest_app):
    domain_router = APIRouter()

    rest_app.include_router(
        domain_router,
        prefix=settings.ENDPOINT,
    )


def get_app():
    rest_app = FastAPI(
        docs_url=f"{settings.ENDPOINT}/docs",
        redoc_url=f"{settings.ENDPOINT}/redoc",
        openapi_url=f"{settings.ENDPOINT}/openapi.json",
        debug=settings.DEBUG,
    )
    register_routers(rest_app)
    return rest_app


app = get_app()
