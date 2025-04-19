from hello import service
from fastapi import APIRouter
from hello.schema import Cat
from hello.db import create_unit_of_work

router = APIRouter()


@router.get("/")
async def hello():
    return {"message": "Hello World"}


@router.get("/cats")
async def cats() -> list[Cat]:
    return service.get_cats(create_unit_of_work())
