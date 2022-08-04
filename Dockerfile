FROM python:3.10-slim-buster

ENV PUPPETEER_SKIP_CHROMIUM_DOWNLOAD true

WORKDIR /app

RUN apt-get update && apt-get install curl gnupg -y \
  && curl --location --silent https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
  && apt-get update \
  && apt-get install google-chrome-stable -y --no-install-recommends
  \

COPY poetry.lock pyproject.toml /app/

RUN apt-get update && pip install --upgrade pip poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev \
    && rm -rf /root/.cache/pip
 \

COPY . /app
WORKDIR /app

CMD ["python", "main.py"]