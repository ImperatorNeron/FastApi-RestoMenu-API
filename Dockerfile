FROM python:3.10.12-alpine

ENV PYTHONDOWNWRITTEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /application

RUN apk update && \
    apk add --no-cache python3-dev \
    gcc \
    musl-dev \
    libpq-dev \
    nmap
    
ADD pyproject.toml /application

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-root --no-interaction --no-ansi

COPY /app/* /application/app/

COPY entrypoint.sh /application/entrypoint.sh
COPY alembic.ini /application/alembic.ini

RUN chmod +x /application/entrypoint.sh
