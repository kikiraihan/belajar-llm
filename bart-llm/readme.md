

## 🔹 Cara jalankan

1. Build & run di background:

```bash
docker compose up -d --build
```

2. Cek status container:

```bash
docker compose ps
```

3. Attach ke container interaktif kapanpun:

```bash
docker attach ollama-client
```

4. Jika mau detach **tanpa stop**, tekan: `Ctrl+P` lalu `Ctrl+Q`.

5. Kalau Ollama belum download model, masuk container Ollama:

```bash
docker exec -it ollama ollama pull mistral
```

---

✅ Dengan setup ini:

* Container Python app **tidak exit otomatis**, bisa attach kapan saja.
* Ollama service **selalu jalan di background**, siap dipanggil API.
* Model tersimpan di **volume `ollama_data`**, jadi tidak download ulang.

