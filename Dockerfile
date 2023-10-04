FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_ROOT_USER_ACTION=ignore
ENV PORT 80
EXPOSE $PORT

WORKDIR /app

COPY pyproject.toml /app/

RUN pip install .

COPY masterofgames/ /app/masterofgames/
COPY static/ /app/static/
COPY templates/ /app/templates/

CMD gunicorn masterofgames.manage:app --bind=0.0.0.0:$PORT
