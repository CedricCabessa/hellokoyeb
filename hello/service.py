from hello.db import UnitOfWork
from hello.schema import Cat


def get_cats(uow: UnitOfWork) -> list[Cat]:
    with uow:
        return uow.cat_repository.list_cats()
