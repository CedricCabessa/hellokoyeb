from typing import Self
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlmodel import SQLModel

from hello.cat_repository import CatRepository

session = async_sessionmaker()


async def create_db_and_tables(sqla_url: str):
    engine = create_async_engine(sqla_url)

    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)

    session.configure(bind=engine)


class UnitOfWork:
    cat_repository: CatRepository

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exn_type, *args, **kwargs):
        pass


def create_unit_of_work() -> UnitOfWork:
    uow = SqlAlchemyUnitOfWork(session)
    return uow


class SqlAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session_factory: async_sessionmaker[AsyncSession]):
        self.session_factory = session_factory

    async def __aenter__(self) -> Self:
        self.session = self.session_factory()
        self.cat_repository = CatRepository(self.session)
        return self

    async def __aexit__(self, exn_type, *args, **kwargs):
        if exn_type is None:
            await self.session.commit()
        else:
            await self.session.rollback()
        await self.session.close()
