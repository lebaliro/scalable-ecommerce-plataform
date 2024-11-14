FROM python:3.11

RUN apt update

RUN pip install poetry

WORKDIR /app

COPY . .

RUN poetry install
