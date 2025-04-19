from hello.schema import Cat
from hello.models import CatEntity


class CatRepository:
    def __init__(self, session):
        self.session = session

    def list_cats(self) -> list[Cat]:
        cats = self.session.query(CatEntity).all()
        return [Cat.model_validate(cat.model_dump()) for cat in cats]
