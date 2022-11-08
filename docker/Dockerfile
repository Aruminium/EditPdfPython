FROM python:3.9-buster as builder
ENV PYTHONUNBUFFERED=1
COPY requirements.txt /
RUN /usr/local/bin/python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

FROM python:3.9-slim-buster
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        libreoffice \
        fonts-takao-gothic \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /app
RUN adduser myuser && chown -R myuser /app
USER myuser

WORKDIR /app
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages/