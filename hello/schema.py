from pydantic import BaseModel
from uuid import UUID


class Cat(BaseModel):
    id: UUID
    name: str
    age: int
    breed: str
