"""ORM queries."""

from typing import Sequence

from sqlalchemy import insert, select

from .database import async_engine, async_session
from .models import Base, Ingredient, Recipe, RecipesIngridients
from .utils.some_data import ingridients, recipes, relationships


async def create_tables():
    """Create all tables."""
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def delete_tables():
    """Delete all tables."""
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def insert_data():
    """Insert some data into the database."""
    insert_recipes = insert(Recipe).values(recipes)
    insert_ingridients = insert(Ingredient).values(ingridients)
    insert_relationships = insert(RecipesIngridients).values(relationships)

    async with async_session() as session:
        await session.execute(insert_recipes)
        await session.execute(insert_ingridients)
        await session.execute(insert_relationships)
        await session.commit()


async def get_all_recipes() -> Sequence[Recipe]:
    """Get all recipes from the database."""
    async with async_session() as session:
        query = (
            select(Recipe)
            .order_by(Recipe.views_qty.desc())
            .order_by(Recipe.cooking_time)
        )
        result = await session.execute(query)
    return result.unique().scalars().all()


async def get_recipe_by_id(recipe_id: int) -> Recipe | None:
    """Get all data of recipe from the database."""
    async with async_session() as session:
        query = select(Recipe).where(Recipe.id == recipe_id)
        result = await session.execute(query)

    return result.unique().scalar()
