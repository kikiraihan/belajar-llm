🔹 Jalankan

1. Build:
docker compose up --build -d


2. Sekali saja (kecuali model lain), Ollama akan download model (misalnya mistral):
docker exec -it ollama ollama pull mistral

3. Coba masuk ke app:
docker attach ollama-client

Lalu input teks → akan diklasifikasikan via Ollama API 🎉