"""Schemas for the database models."""

from pydantic import BaseModel, ConfigDict, Field


class RecipeSchema(BaseModel):
    """Schema of the Recipe model for creating the model."""

    name: str = Field(examples=["Пирог"], max_length=250)
    cooking_time: int = Field(examples=[30])
    views_qty: int = 0

    model_config = ConfigDict(from_attributes=True)


class RecipeSchemaDeatil(BaseModel):
    """Schema of the Recipe model for displaying the model."""

    name: str = Field(examples=["Пирог"], max_length=250)
    cooking_time: int = Field(examples=[30])
    description: str | None = Field(
        examples=["Пирог с черничным вареньем"],
        default=None,
    )
    ingridients: list["RecipesIngridientsSchema"] | None = None

    model_config = ConfigDict(from_attributes=True)


class IngridientSchema(BaseModel):
    """Schema of the Ingridient model for creating the model."""

    name: str = Field(examples=["Мука"], max_length=250)
    description: str | None = Field(
        examples=["Мука пшеничная"],
        default=None,
    )

    model_config = ConfigDict(from_attributes=True)


class RecipesIngridientsSchema(BaseModel):
    """Schema of the RecipesIngridients model."""

    ingridient: "IngridientSchema"

    model_config = ConfigDict(from_attributes=True)


class NotFoundMessage(BaseModel):
    """Response of a 404 error."""

    message: str = Field(default="Not Found error")
