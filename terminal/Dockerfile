FROM cnstark/pytorch:2.3.0-py3.10.15-ubuntu22.04

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Pre-download model-model
RUN python -c "from transformers import pipeline; pipeline('zero-shot-classification', model='facebook/bart-large-mnli')"
RUN python -c "from transformers import pipeline; pipeline('zero-shot-classification', model='valhalla/distilbart-mnli-12-1')"
RUN python -c "from transformers import pipeline; pipeline('zero-shot-classification', model='MoritzLaurer/deberta-v3-small-zeroshot-v1')"

# Copy seluruh kode
COPY . .

# Default model (bisa dioverride via .env)
ENV MODEL_NAME=facebook/bart-large-mnli

CMD ["python", "app.py"]
