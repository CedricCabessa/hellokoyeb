from fastapi import FastAPI
from hello.db import create_db_and_tables
from hello.route import router


class App(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        create_db_and_tables()
        self.include_router(router)


app = App()
