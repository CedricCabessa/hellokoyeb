from hello.db import UnitOfWork
from hello.schema import Cat


def get_cats(uow: UnitOfWork) -> list[Cat]:
    with uow:
        return uow.cat_repository.list_cats()


def add_cat(uow: UnitOfWork, cat) -> Cat:
    with uow:
        return uow.cat_repository.add_cat(cat)
