from hello.schema import Cat
from hello.models import CatEntity


class CatRepository:
    def __init__(self, session):
        self.session = session

    def list_cats(self) -> list[Cat]:
        cats = self.session.query(CatEntity).all()
        return [Cat.model_validate(cat.model_dump()) for cat in cats]

    def add_cat(self, cat: Cat) -> Cat:
        cat_entity = CatEntity.model_validate(cat.model_dump())
        self.session.add(cat_entity)
        return Cat.model_validate(cat_entity.model_dump())
