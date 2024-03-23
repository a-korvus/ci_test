"""Database models."""

from typing import Annotated

from sqlalchemy import BigInteger, ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

intpk = Annotated[int, mapped_column(primary_key=True)]
name_exist = Annotated[str, mapped_column(String(250), nullable=False)]


class Base(DeclarativeBase):
    """Base model for the database models."""

    ...


class Recipe(Base):
    """The database model of a recipe."""

    __tablename__ = "recipe_table"

    id: Mapped[intpk]
    name: Mapped[name_exist]
    description: Mapped[str | None]
    cooking_time: Mapped[int] = mapped_column(
        nullable=False,
        comment="in minutes",
    )
    views_qty: Mapped[int] = mapped_column(
        BigInteger(),
        default=0,
    )

    ingridients: Mapped[list["RecipesIngridients"]] = relationship(
        back_populates="recipe",
        lazy="joined",
    )

    def __repr__(self) -> str:
        """Show string representation of an object."""
        return f"Recipe (id={self.id!r}, name={self.name!r})"


class Ingredient(Base):
    """The database model of an ingredient."""

    __tablename__ = "ingredient_table"

    id: Mapped[intpk]
    name: Mapped[name_exist]
    description: Mapped[str | None]

    recipes: Mapped[list["RecipesIngridients"]] = relationship(
        back_populates="ingridient",
        lazy="joined",
    )

    def __repr__(self) -> str:
        """Show string representation of an object."""
        return f"Ingridient (id={self.id!r}, name={self.name!r})"


class RecipesIngridients(Base):
    """Association model for many-to-many relationships.

    Between Recipe and Ingridient models.
    """

    __tablename__ = "recipes_ingridients_table"

    recipe_id: Mapped[int] = mapped_column(
        ForeignKey("recipe_table.id"),
        primary_key=True,
    )
    ingridient_id: Mapped[int] = mapped_column(
        ForeignKey("ingredient_table.id"),
        primary_key=True,
    )

    recipe: Mapped["Recipe"] = relationship(
        back_populates="ingridients",
        lazy="joined",
    )
    ingridient: Mapped["Ingredient"] = relationship(
        back_populates="recipes",
        lazy="joined",
    )
