# Dockerfile

FROM python:3.8-alpine

WORKDIR /app
COPY . /app

RUN apk update; apk add curl

RUN addgroup -S testgroup && adduser -S test -G testgroup
USER test

RUN pip3 install invoke; curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -; PATH=$PATH:/home/test/.local/bin; which invoke

# ESTO ES ENTRY POINT RUN invoke test

