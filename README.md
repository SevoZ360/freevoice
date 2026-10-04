# 🎙️ FreeVoice

**FreeVoice** is a high-performance, privacy-focused voice assistant designed to turn your speech into perfectly formatted text instantly. By combining **OpenAI Whisper** for transcription and **Local LLMs** (via LM Studio or Odysseus) for grammar refinement, FreeVoice allows you to dictate text anywhere on your computer with zero latency and 100% privacy.

## ✨ Key Features

*   **🎙️ Instant Transcription:** Powered by OpenAI's Whisper model for high accuracy.
*   **🧠 AI Grammar Refinement:** Automatically cleans up "umms," "ahhs," and messy grammar using a local LLM.
*   **🌍 Bilingual Auto-Detect:** Seamlessly switches between **English (EN)** and **Lithuanian (LT)** without manual configuration.
*   **⌨️ Global Dictation:** Types your cleaned text directly into any active window (Discord, Browser, IDEs, etc.).
*   **🔒 100% Local & Private:** Your voice and text never leave your machine. No cloud subscriptions required!
*   **⚡ Hotkey Trigger:** Hold a single key (e.g., `CTRL`) to record; release to type.

---

## 🚀 Installation & Setup

Follow these steps to get **FreeVoice** running on your machine.

### 1. Install System Dependencies (Required)
Whisper requires `ffmpeg` to process audio. This is a system-level tool, not just a Python package.

**For Linux (Ubuntu/Debian):**
```bash
sudo apt update && sudo apt install ffmpeg portaudio19-dev -y

For macOS (using Homebrew):


brew install ffmpeg portaudio

For Windows:

Download ffmpeg from ffmpeg.org.
Add the bin folder to your System PATH.
Install PortAudio via terminal: pip install pipwin then pipwin install pyaudio.
2. Install Python Dependencies
Once the system tools are ready, install all the necessary Python libraries using pip.

Run this command in your terminal:


pip install openai-whisper sounddevice numpy pyautogui requests scipy keyboard
Note: We use openai-whisper (the official package) to ensure the best performance and compatibility.

3. Setup your Local AI (LM Studio / Odysseus)
FreeVoice is designed to work with local LLMs for maximum privacy.

Open LM Studio or Odysseus.
Load a model (e.g., Llama 3, Gemma, or Mistral).
Start the Local Server.
Ensure the server is running on http://localhost:1234.
4. Running FreeVoice
Navigate to your folder and run the script. On Linux/Mac, you may need sudo to allow the script to listen for your global hotkey:


sudo python my_flow.py
⌨️ How to Use
Hold your trigger key (Default is CTRL).
Speak your message in English or Lithuanian.
Release the key.
Wait a moment for the AI to process, and it will type automatically!
Happy Dictating! 🎙️✨

