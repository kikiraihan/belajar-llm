Oke! Kita bisa atur supaya aplikasi **langsung jalan di background** dengan `docker compose up -d --build`, dan kamu bisa masuk ke container **kalau perlu** via `docker exec -ti <container> bash` tanpa ada perubahan besar di kode.

Beberapa catatan:

1. **Terminal interaktif (`input()`)**:

   * Kalau jalan di background (`-d`), `input()` tidak bisa langsung diakses.
   * Solusi:

     * Tetap bisa jalan di background, tapi untuk interaksi, masuk ke container pakai `docker exec -ti ollama-client bash` lalu jalankan `python app.py`.
     * Atau ubah script jadi **API (FastAPI)** supaya tidak perlu `input()` langsung.

2. **Kode Python**:

   * Kalau tetap mau interaktif di container, tidak perlu diubah.
   * Kalau mau auto-run saat container start, bisa ganti `CMD ["python", "app.py"]` → tetap jalan di background, tapi interaksi harus lewat exec.

---

Berikut contoh **full setup Docker Compose** yang bisa jalan di background, tapi tetap bisa interaktif via `docker exec`:

---

### Struktur Folder

```
project/
 ├── docker-compose.yml
 └── app/
     ├── Dockerfile
     ├── requirements.txt
     └── app.py
```

---

### docker-compose.yml

```yaml
version: "3.8"

services:
  ollama:
    image: ollama/ollama:latest
    container_name: ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_data:/root/.ollama  # cache model di host

  app:
    build: ./app
    container_name: ollama-client
    depends_on:
      - ollama
    environment:
      - MODEL_NAME=mistral
    stdin_open: true
    tty: true  # penting biar bisa attach dan interaktif

volumes:
  ollama_data:
```

---

### app/Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

CMD ["python", "app.py"]
```

---

### app/requirements.txt

```
python-dotenv
requests
```

---

### app/app.py (tidak perlu diubah dari versi interaktif)

```python
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
```

---

### Cara Jalankan

1. Build & run background:

```bash
docker compose up -d --build
```

2. Kalau mau interaktif, masuk container:

```bash
docker exec -ti ollama-client bash
python app.py
```

3. Ollama akan jalan otomatis di container `ollama`, Python app bisa jalan di container `ollama-client`.

---

✅ Kesimpulan:

* **Tidak ada perubahan besar di kode** untuk interaktif, cukup `stdin_open: true` + `tty: true` di docker-compose.
* **Auto-download model** Ollama di container karena kita mount volume (`ollama_data`).
* Bisa jalan di background (`-d`) tapi interaksi harus lewat `docker exec`.

---

Kalau mau, saya bisa bikinkan **versi API** supaya **langsung bisa request dari luar VPS tanpa masuk container**.
Apakah mau saya buatkan versi itu juga?
