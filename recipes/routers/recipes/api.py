"""All RestAPI related to recipes is here."""
from fastapi import APIRouter

recipes_router = APIRouter()

@recipes_router.get("/recipes/{recipe_id}", tags=["recipes"])
async def get_recipe(recipe_id: int):
    """Get single recipe by id."""
    return {"id": recipe_id}
