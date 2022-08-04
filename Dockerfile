FROM python:3.10-slim-buster

WORKDIR /app
COPY poetry.lock pyproject.toml /app/


RUN apt-get update && apt-get -y install gcc g++ \
    && pip install --upgrade pip poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev \
    && rm -rf /root/.cache/pip
 \

COPY . /app
WORKDIR /app

CMD ["python", "main.py"]