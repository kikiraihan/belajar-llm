import os
import requests
from dotenv import load_dotenv

# Load .env
load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "mistral")

print(f"✅ Load model (Ollama): {MODEL_NAME}")

LABELS = ["Hacking LLM", "Chit Chat", "Fact Question"]

print("=== Text Classification Terminal (Ollama) ===")
print("Ketik 'exit' untuk keluar.\n")

OLLAMA_API = "http://ollama:11434/api/generate"  # hostname service ollama di docker-compose

while True:
    text = input("Masukkan teks: ")
    if text.lower() == "exit":
        print("Keluar dari program.")
        break

    prompt = f"""
    Klasifikasikan teks berikut ke salah satu label berikut:
    {LABELS}

    Teks: "{text}"

    Jawaban hanya berupa satu label yang paling sesuai.
    """

    response = requests.post(OLLAMA_API, json={
        "model": MODEL_NAME,
        "prompt": prompt
    }, stream=True)

    output = ""
    for line in response.iter_lines():
        if line:
            data = line.decode("utf-8")
            if data.startswith("{\"response\""):
                chunk = eval(data)["response"]
                output += chunk

    print(f"Label: {output.strip()}\n")
