from hello.db import UnitOfWork
from hello.schema import Cat


async def get_cats(uow: UnitOfWork) -> list[Cat]:
    async with uow:
        return await uow.cat_repository.list_cats()


async def add_cat(uow: UnitOfWork, cat) -> Cat:
    async with uow:
        return await uow.cat_repository.add_cat(cat)
