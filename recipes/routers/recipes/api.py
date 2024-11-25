"""All RestAPI related to recipes is here."""
from fastapi import APIRouter

recipes_router = APIRouter()

@recipes_router.get("/recipes/", tags=["recipes"])
async def get_recipe():
    return {"id": "test"}
