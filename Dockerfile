# Dockerfile

FROM python:3.8-alpine

LABEL maintainer="mapachana"

WORKDIR /app
COPY ./poetry.lock ./pyproject.toml ./tasks.py /app/

RUN apk update; apk add build-base; apk add libffi-dev; ln -s /usr/bin/python /usr/bin/python3.8; addgroup -S testgroup && adduser -S test -G testgroup
USER test
WORKDIR /app/test

RUN pip3 install invoke; pip install --user poetry

USER root
RUN apk del build-base; apk del libffi-dev
USER test

ENV PATH=$PATH:/home/test/.local/bin
ENV PATH=$PATH:/home/test/.poetry/bin

RUN  poetry config virtualenvs.create false; invoke installdeps --dev

ENTRYPOINT ["invoke", "test"]

