FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    && rm -rf /var/lib/apt/lists/*

COPY src/ src/
COPY artifacts/ artifacts/
COPY logs/ logs/

COPY src/deployment/requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH=/app

CMD ["uvicorn", "src.deployment.api:app", "--host", "0.0.0.0", "--port", "8000"]
