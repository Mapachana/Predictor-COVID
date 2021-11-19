# Dockerfile

FROM python:3.8-alpine

WORKDIR /app
COPY ./poetry.lock ./pyproject.toml ./tasks.py /app/

RUN apk update; apk add curl; ln -s /usr/bin/python /usr/bin/python3.8; addgroup -S testgroup && adduser -S test -G testgroup
USER test
WORKDIR /app/test

RUN pip3 install invoke; curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

USER root
RUN apk del curl
USER test

ENV PATH=$PATH:/home/test/.local/bin
ENV PATH=$PATH:/home/test/.poetry/bin

RUN  poetry config virtualenvs.create false; invoke installdeps --dev

ENTRYPOINT ["invoke", "test"]

