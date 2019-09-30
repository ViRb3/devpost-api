FROM alpine:3.10

COPY devpost-api/ /devpost-api/
WORKDIR /devpost-api

RUN apk add --no-cache python3 py3-lxml

RUN pip3 install pipenv
RUN pipenv install --system --deploy --ignore-pipfile

EXPOSE 5000
ENTRYPOINT gunicorn --bind 0.0.0.0:5000 wsgi:app
