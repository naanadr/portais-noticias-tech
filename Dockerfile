FROM python:3.8.1-alpine

ARG YOUR_ENV=development
WORKDIR /portais_tech

RUN apk add --no-cache gcc \
    musl-dev python3-dev \
    libffi-dev openssl-dev \
    libxml2-dev libxslt-dev bash

RUN $(test "$YOUR_ENV" = development) && apk add build-base libzmq zeromq-dev || true

RUN pip install "poetry==1.0.3"

COPY poetry.lock pyproject.toml /portais_tech/

RUN poetry config virtualenvs.create false \
  && poetry install $(test "$YOUR_ENV" = production && echo "--no-dev") --no-interaction --no-ansi

RUN $(test "$YOUR_ENV" = development) && apk del build-base zeromq-dev || true

COPY /portais_tech /portais_tech

ENTRYPOINT python runspiders.py
