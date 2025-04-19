from uuid import UUID

from sqlmodel import Field, SQLModel


class CatEntity(SQLModel, table=True):
    id: UUID = Field(primary_key=True)
    name: str
    age: int
    breed: str
