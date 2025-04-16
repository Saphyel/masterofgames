FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_NO_CACHE_DIR=1
ENV PIP_ROOT_USER_ACTION=ignore

ENV LITESTAR_APP=masterofgames.web:app
ENV PORT=80
EXPOSE $PORT

WORKDIR /app

COPY pyproject.toml ./

RUN pip install .

COPY masterofgames/ ./masterofgames/
COPY static/ ./static/
COPY templates/ ./templates/

#RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app/
#USER appuser

CMD ["uvicorn", "masterofgames.web:app", "--host", "0.0.0.0", "--port", "${PORT}"]
