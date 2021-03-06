FROM python:3.9

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1

WORKDIR /app
    
RUN pip install poetry
ADD poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false ; \
    poetry install --no-dev --no-ansi

ADD ./ /app