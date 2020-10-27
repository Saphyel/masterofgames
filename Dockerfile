FROM python:3.8-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK=1

WORKDIR /app
RUN useradd -m -r user ; chown user /app
    
RUN pip install poetry
ADD poetry.lock pyproject.toml /app/
RUN poetry config virtualenvs.create false ; \
    poetry install --no-dev

ADD ./ /app
USER user
