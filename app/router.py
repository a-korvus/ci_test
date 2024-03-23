"""Routes in this app."""

from typing import Annotated

from fastapi import APIRouter, HTTPException, Path, status

from .models import Recipe
from .queries import get_all_recipes, get_recipe_by_id
from .schemas import NotFoundMessage, RecipeSchema, RecipeSchemaDeatil

router = APIRouter(prefix="/cookbook/api", tags=["cookbook"])


@router.get(
    "/recipes",
)
async def all_recipes() -> list[RecipeSchema]:
    """Get the list of recipes."""
    return await get_all_recipes()  # type: ignore


@router.get(
    path="/recipes/{recipe_id}",
    responses={404: {"model": NotFoundMessage}},
)
async def recipe(
    recipe_id: Annotated[
        int,
        Path(
            title="Recipe ID",
            description="Your recipe ID, please",
        ),
    ],
) -> RecipeSchemaDeatil:
    """Get all data of recipe."""
    recipe: Recipe | None = await get_recipe_by_id(recipe_id)
    if not recipe:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Recipe not found",
        )

    return RecipeSchemaDeatil.model_validate(recipe)
