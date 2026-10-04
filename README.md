# freevoice
🎙️ FreeVoice: A lightning-fast, bilingual (EN/LT) voice-to-text assistant. Uses OpenAI Whisper and local LLMs to transcribe and clean up speech instantly. Hold a key, speak, and it types for you! ✨



 # 🎙️ FreeVoice

**FreeVoice** is a high-performance, privacy-focused voice assistant designed to turn your speech into perfectly formatted text instantly. By combining **OpenAI Whisper** for transcription and **Local LLMs** (via LM Studio or Odysseus) for grammar refinement, FreeVoice allows you to dictate text anywhere on your computer with zero latency and 100% privacy.

## ✨ Key Features

*   **🎙️ Instant Transcription:** Powered by OpenAI's Whisper model for high accuracy.
*   **🧠 AI Grammar Refinement:** Automatically cleans up "umms," "ahhs," and messy grammar using a local LLM.
*   **🌍 Bilingual Auto-Detect:** Seamlessly switches between **English (EN)** and **Lithuanian (LT)** without manual configuration.
*   **⌨️ Global Dictation:** Types your cleaned text directly into any active window (Discord, Browser, IDEs, etc.).
*   **🔒 100% Local & Private:** Your voice and text never leave your machine. No cloud subscriptions required!
*   **⚡ Hotkey Trigger:** Hold a single key (e.g., `CTRL`) to record; release to type.

## 🛠️ Installation

### Prerequisites (Linux)
You will need Python 3.10+, FFmpeg, and PortAudio installed:
```bash
sudo apt update
sudo apt install ffmpeg portaudio19-dev python3-pip
