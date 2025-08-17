FROM python:3.9-slim

# Install OS deps
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download model dari HuggingFace
RUN python -c "from transformers import pipeline; pipeline('zero-shot-classification', model='facebook/bart-large-mnli')"

# Copy kode aplikasi
COPY app.py .

# Default command
CMD ["python", "app.py"]
