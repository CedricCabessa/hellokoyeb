from typing import Self
from sqlalchemy.orm import Session, sessionmaker, Session
from sqlmodel import SQLModel, create_engine

from hello.cat_repository import CatRepository

session = sessionmaker()


def create_db_and_tables():
    sqlite_file_name = "database.db"
    sqlite_url = f"sqlite:///{sqlite_file_name}"

    connect_args = {"check_same_thread": False}
    engine = create_engine(sqlite_url, connect_args=connect_args)

    SQLModel.metadata.create_all(engine)
    session.configure(bind=engine)


class UnitOfWork:
    cat_repository: CatRepository

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exn_type, *args, **kwargs):
        pass


def create_unit_of_work() -> UnitOfWork:
    uow = SqlAlchemyUnitOfWork(session)
    return uow


class SqlAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session_factory: sessionmaker[Session]):
        self.session_factory = session_factory

    def __enter__(self) -> Self:
        self.session = self.session_factory()
        self.cat_repository = CatRepository(self.session)
        return self

    def __exit__(self, exn_type, *args, **kwargs):
        if exn_type is None:
            self.session.commit()
        else:
            self.session.rollback()
        self.session.close()
