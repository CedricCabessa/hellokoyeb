from typing import Annotated
from hello import service
from fastapi import APIRouter, Depends
from hello.schema import Cat
from hello.db import create_unit_of_work, UnitOfWork

router = APIRouter()

Uow = Annotated[UnitOfWork, Depends(create_unit_of_work)]


@router.get("/")
async def hello():
    return {"message": "Hello World"}


@router.get("/cats")
async def cats(uow: Uow) -> list[Cat]:
    return service.get_cats(uow)


@router.post("/cats")
async def add_cat(uow: Uow, cat: Cat) -> Cat:
    return service.add_cat(uow, cat)
