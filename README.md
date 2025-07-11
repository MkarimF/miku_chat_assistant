## 📜 License

This project is licensed under a **Custom Non-Commercial License**.

You are free to use, modify, and share the code **as long as it is not used commercially**.

For commercial inquiries, please contact the author.

# 🎤 Miku Assistant - Offline Virtual Idol AI Assistant

> Virtual assistant berbasis Python dengan persona **Hatsune Miku**, mampu bicara, mendengarkan, dan menjawab baik secara online (OpenAI) maupun offline (LLaMA3 via Ollama). 🚀

---

## 🧠 Fitur Utama

- ✅ **Voice Recognition (STT)**: Online (`Google STT`) dan siap untuk offline (`Whisper`)  
- ✅ **Natural Language Response**:
  - Online: OpenAI GPT (fallback jika tersedia)
  - Offline: LLaMA3 (via Ollama)
- ✅ **Voice Output (TTS)**: Diperkuat oleh **VoiceVox**
- ✅ **Switching Engine**: Online & offline bisa diganti tanpa kehilangan konteks
- ✅ **Command Logging** & class-based async architecture

---

## 🛠️ Struktur Proyek
```bash
miku-to-life/
│
├── config/ # File konfigurasi API, model, dan default character
│ └── config.yml
│
├── core/ # Komponen utama assistant
│ ├── assistant.py # Orkestrator utama
│ ├── brain.py # Chat engine switching
│ ├── config.py # Loader config.yml
│ ├── microphone.py # Handler STT (Google / Whisper)
│ ├── speaker.py # Handler VoiceVox TTS
│ └── camera.py # (Opsional, future feature)
│
├── models/ # Model backend
│ ├── openai_chat.py # OpenAI wrapper
│ ├── llama3_engine.py # Ollama LLaMA3 interface
│ └── whisper/ # (Opsional)
│
├── ui/ # GUI (PyQt + QAsync)
│ └── window.py
│
├── main.py # Entry point
├── requirements.txt # Dependencies
└── README.md # (Kamu sedang lihat ini 😉)
```
---

## 🚀 Cara Menjalankan

1. **Install dependencies**:

```bash
pip install -r requirements.txt
```

2. **Jalankan VoiceVox Engine**
Download dan jalankan:
👉 https://voicevox.hiroshiba.jp

```bash
voicevox_engine
```
3. **(Opsional) Jalankan Ollama & Pull model**

```bash
ollama run llama3
```

4. **Jalankan Assistant**

```bash
python main.py
```

📦 Konfigurasi
Edit config/config.yml sesuai kebutuhan:

```bash
openai:
  api_key: "YOUR_API_KEY"
  model: "gpt-4"

voicevox:
  host: "localhost"
  port: 50021
  speaker_id: 3

engine:
  default: "llama3"  # atau "openai"
```

🎯 Roadmap Selanjutnya
 🎥 Kamera deteksi wajah (aktif saat user muncul)

 🎭 Integrasi dengan Live2D / gambar animasi Miku (via PyQt atau Unity bridge)

 📆 Reminder/jadwal harian (pakai apscheduler)

 🎮 Interaksi custom command: buka YouTube, nyalain lagu, dll

❤️ Credits
Ollama

VoiceVox

SpeechRecognition

Hatsune Miku ❤️