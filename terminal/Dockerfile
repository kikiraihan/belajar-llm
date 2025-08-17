FROM python:3.11-slim

# Install system dependencies yang dibutuhkan
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    zlib1g-dev \
    libncurses5-dev \
    libncursesw5-dev \
    uuid-dev \
    curl git \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy dan install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy script Python
COPY app.py .

# Jalankan script secara interaktif
CMD ["python", "app.py"]
