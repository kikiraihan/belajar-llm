from transformers import pipeline

# Load model zero-shot (multi-class)
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"  # ringan & sudah support zero-shot
)

# Label candidate
LABELS = ["Hacking LLM", "Chit Chat", "Fact Question"]

print("=== Text Classification Terminal ===")
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
