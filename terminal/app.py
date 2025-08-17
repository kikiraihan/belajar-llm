import os
from transformers import pipeline
from dotenv import load_dotenv

# Load .env file (kalau ada)
load_dotenv()

# Ambil nama model dari env (default = bart-large-mnli)
model_name = os.getenv("MODEL_NAME", "facebook/bart-large-mnli")

classifier = pipeline(
    "zero-shot-classification",
    model=model_name
)

LABELS = ["Hacking LLM", "Chit Chat", "Fact Question"]

print("=== Text Classification Terminal ===")
print(f"Loaded model: {model_name}")
print("Ketik 'exit' untuk keluar.\n")

while True:
    text = input("Masukkan teks: ")
    if text.lower() == "exit":
        print("Keluar dari program.")
        break

    result = classifier(text, candidate_labels=LABELS)
    label = result["labels"][0]
    score = result["scores"][0]

    print(f"Label: {label}, Score: {score:.4f}\n")
