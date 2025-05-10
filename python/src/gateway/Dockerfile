FROM python:3.10-slim-bullseye

# Install required system dependencies for mysqlclient
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    pkg-config \
    libmariadb-dev-compat \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir --requirement requirements.txt

COPY . .

# Expose the port the app runs on
EXPOSE 8080

# Command to run the application
CMD ["python", "server.py"]