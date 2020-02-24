# version 1.0

FROM python:3.8.1-alpine

RUN apk add --no-cache gcc \
    musl-dev python3-dev \
    libffi-dev openssl-dev \
    libxml2-dev libxslt-dev bash \
  && pip install "poetry==1.0.3"

WORKDIR /portais_tech
COPY poetry.lock pyproject.toml /portais_tech/

RUN poetry config virtualenvs.create false \
  && poetry install $(test $YOUR_ENV="production" && echo "--no-dev") --no-interaction --no-ansi

COPY /portais_tech /portais_tech

ENTRYPOINT python runspiders.py
