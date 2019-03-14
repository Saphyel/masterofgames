FROM python:3.7-alpine

WORKDIR /app

ENV PIPENV_DEV=1
ENV PIPENV_SYSTEM=1

ADD * ./
RUN pip install pipenv;pipenv install --deploy
