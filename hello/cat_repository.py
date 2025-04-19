from __future__ import annotations
from typing import TYPE_CHECKING
from hello.schema import Cat
from hello.models import CatEntity
from sqlalchemy import select

if TYPE_CHECKING:
    from sqlalchemy.ext.asyncio import AsyncSession


class CatRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def list_cats(self) -> list[Cat]:
        query = await self.session.execute(select(CatEntity))
        cats = query.scalars().all()
        return [Cat.model_validate(cat.model_dump()) for cat in cats]

    async def add_cat(self, cat: Cat) -> Cat:
        cat_entity = CatEntity.model_validate(cat.model_dump())
        self.session.add(cat_entity)
        return Cat.model_validate(cat_entity.model_dump())
