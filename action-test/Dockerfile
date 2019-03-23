FROM python:3.7-alpine

LABEL "com.github.actions.name"="Run unit test"
LABEL "com.github.actions.description"="Execute all the unit test from the code base"
LABEL "com.github.actions.icon"="shield"
LABEL "com.github.actions.color"="green"

ENV PIPENV_DEV=1
ENV PIPENV_SYSTEM=1

RUN pip install pipenv

ADD entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]