from contextlib import asynccontextmanager
from fastapi import FastAPI
from hello.db import create_db_and_tables
from hello.route import router
from hello.config import Settings


class App(FastAPI):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.include_router(router)


@asynccontextmanager
async def lifespan(app: App):
    await create_db_and_tables(Settings().sqla_url)
    yield


app = App(lifespan=lifespan)
