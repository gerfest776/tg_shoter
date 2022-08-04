FROM python:3.10-slim-buster

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN apt-get update \
    && apt-get -y install gcc g++ \
    && pip install --upgrade pip poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev \
    && rm -rf /root/.cache/pip
 \

RUN apt-get update && apt-get install -y \
	apt-transport-https \
	ca-certificates \
        locales \
        locales-all \
	hicolor-icon-theme \
	libcanberra-gtk* \
        dbus-x11 \
        mesa-utils \
        mesa-utils-extra \
        xpra \
        websockify \
	libgl1-mesa-dri \
	libgl1-mesa-glx \
	libpango1.0-0 \
	libpulse0 \
	libv4l-0 \
	--no-install-recommends \
	&& curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
	&& echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list \
	&& apt-get update && apt-get install -y \
	google-chrome-stable \
	--no-install-recommends \
	&& apt-get purge --auto-remove -y curl \
	&& rm -rf /var/lib/apt/lists/*

RUN groupadd -r chrome && useradd -r -g chrome -G audio,video chrome \
    && mkdir -p /home/chrome/Downloads && chown -R chrome:chrome /home/chrome

COPY . /app
WORKDIR /app

CMD ["python", "main.py"]