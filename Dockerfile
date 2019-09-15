FROM python:3.7.4-alpine3.10

COPY devpost-api/ /devpost-api/
WORKDIR /devpost-api

RUN apk add --no-cache build-base libxml2-dev libxslt-dev

RUN pip install pipenv
RUN pipenv sync

EXPOSE 5000
ENTRYPOINT pipenv run main:app --host 0.0.0.0 --port 8000