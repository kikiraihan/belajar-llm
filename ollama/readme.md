
### Cara Jalankan

1. Build & run background:

```bash
docker compose up -d --build

# pull satu kali saja
docker exec -it ollama ollama pull mistral
```

2. Kalau mau interaktif, masuk container:

```bash
docker exec -ti ollama-client bash
python app.py
```

3. Ollama akan jalan otomatis di container `ollama`, Python app bisa jalan di container `ollama-client`.