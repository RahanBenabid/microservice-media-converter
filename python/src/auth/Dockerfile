FROM python:3.10-slim-bullseye

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential default-libmysqlclient-dev \
    && pip install --no-cache-dir --upgrade pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir --requirement requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "server.py"]