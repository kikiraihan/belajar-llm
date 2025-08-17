from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(title="Text Classification API")

# Load model zero-shot (multi-class)
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"  # ringan & sudah support zero-shot
)

# Label candidate
LABELS = ["Hacking LLM", "Chit Chat", "Fact Question"]

class TextRequest(BaseModel):
    text: str

@app.post("/classify")
def classify(request: TextRequest):
    result = classifier(request.text, candidate_labels=LABELS)
    # Ambil label dengan score tertinggi
    label = result["labels"][0]
    score = result["scores"][0]
    return {"label": label, "score": score}
