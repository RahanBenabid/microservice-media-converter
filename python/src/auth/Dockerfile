FROM python:3.10-slim-bullseye

# Install required system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    pkg-config \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir --requirement requirements.txt

COPY . .

# Set environment variables for your application
ENV MYSQL_HOST=db \
    MYSQL_PORT=3306 \
    MYSQL_USER=root \
    MYSQL_PASSWORD=password \
    MYSQL_DB=auth

# Expose the port the app runs on
EXPOSE 5000

CMD ["python", "server.py"]