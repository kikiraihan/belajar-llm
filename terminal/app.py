import os
from dotenv import load_dotenv
from transformers import pipeline

# Load .env
load_dotenv()

# Ambil model dari ENV, default fallback
MODEL_NAME = os.getenv("MODEL_NAME", "facebook/bart-large-mnli")

try:
    print(f"✅ Load model: {MODEL_NAME}")
except UnicodeEncodeError:
    print(f"[INFO] Load model: {MODEL_NAME}")

classifier = pipeline(
    "zero-shot-classification",
    model=MODEL_NAME
)

LABELS = ["Hacking LLM", "Chit Chat", "Fact Question"]

print("=== Text Classification Terminal ===")
print("Ketik 'exit' untuk keluar.\n")

while True:
    text = input("Masukkan teks: ")
    if text.lower() == "exit":
        print("Keluar dari program.")
        break

    if not text.strip():
        print("⚠️ Teks tidak boleh kosong!\n")
        continue

    result = classifier(text, candidate_labels=LABELS)
    label, score = result["labels"][0], result["scores"][0]
    print(f"Label: {label}, Score: {score:.4f}\n")
