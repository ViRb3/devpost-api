FROM python:3.7.4-alpine3.10 AS base

COPY devpost-api/ /devpost-api/
WORKDIR /devpost-api

RUN apk add --no-cache py3-lxml

RUN pip3 install poetry
RUN poetry config settings.virtualenvs.create false
RUN poetry install

# --------------------------------------------------------------------------

FROM base AS test

ENTRYPOINT python3 test.py

# --------------------------------------------------------------------------

FROM base AS release

EXPOSE 5000
ENTRYPOINT gunicorn --bind 0.0.0.0:5000 wsgi:app
