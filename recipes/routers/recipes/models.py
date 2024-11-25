"""Recipe SQL models."""
from sqlmodel import Field, SQLModel


class Recipe(SQLModel, table=True):
    """SQL model of single Recipe."""

    id: int | None = Field(default=None, primary_key=True)
    name: str