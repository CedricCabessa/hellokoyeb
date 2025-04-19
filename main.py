from fastapi import FastAPI
from hello.db import create_db_and_tables
from hello.route import router
from hello.config import Settings


class App(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        create_db_and_tables(Settings().sqla_url)
        self.include_router(router)


app = App()
