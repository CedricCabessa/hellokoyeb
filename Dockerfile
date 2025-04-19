FROM ghcr.io/astral-sh/uv:python3.13-alpine

COPY . /app
WORKDIR /app

RUN uv sync

ENTRYPOINT ["uv", "run"]
CMD ["uvicorn", "--host", "0.0.0.0", "main:app"]