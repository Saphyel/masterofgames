FROM python:3.8-slim AS prod

WORKDIR /app

RUN pip install poetry;poetry config virtualenvs.create false
ADD poetry.lock pyproject.toml /app/
RUN poetry install --no-dev

ADD ./ /app
