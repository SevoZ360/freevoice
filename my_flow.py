import whisper
import sounddevice as sd
import numpy as np
import pyautogui
import requests
import time
import scipy.io.wavfile as wav
import os
import keyboard  # New library for holding keys

# --- CONFIGURATION ---
LM_STUDIO_URL = "http://localhost:1234/v1/chat/completions"
WHISPER_MODEL_NAME = "tiny" 
SAMPLE_RATE = 16000
TRIGGER_KEY = 'enter'  # The key you hold down
# ---------------------

print("⏳ Loading AI models into memory... Please wait...")
whisper_model = whisper.load_model(WHISPER_MODEL_NAME)
print("✅ Models Loaded!")
print(f"🚀 READY! HOLD DOWN [{TRIGGER_KEY.upper()}] TO TALK, RELEASE TO SEND.")

def record_while_held(filename):
    """Records audio in chunks as long as the trigger key is held."""
    audio_chunks = []
    
    # Wait for the user to press the key
    print(f"👉 Press and HOLD [{TRIGGER_KEY.upper()}]...")
    keyboard.wait(TRIGGER_KEY)
    
    print("🎤 RECORDING... (Release key to stop)")
    
    # Start recording chunks of audio
    # We record in small 0.1s chunks so we can detect the key release quickly
    while keyboard.is_pressed(TRIGGER_KEY):
        chunk = sd.rec(int(0.1 * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
        sd.wait()
        audio_chunks.append(chunk)
    
    print("✅ Recording stopped.")
    
    if len(audio_chunks) > 0:
        # Combine all chunks into one array
        full_audio = np.concatenate(audio_chunks, axis=0)
        wav.write(filename, SAMPLE_RATE, full_audio)
        return True
    return False

def transcribe_audio(filename):
    print("👂 Transcribing...")
    result = whisper_model.transcribe(filename)
    return result['text'].strip()

def clean_with_ai(text):
    print(f"🧠 Thinking (Gemma 4)...")
    prompt = f"Clean up this messy speech transcript into a clear, natural message. Output ONLY the corrected text and nothing else. Transcript: '{text}'"
    
    payload = {
        "model": "local-model",
        "messages": [
            {"role": "system", "content": "You are a helpful text-cleaning assistant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    try:
        response = requests.post(LM_STUDIO_URL, json=payload, timeout=15)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"❌ LM Studio Error: {e}")
        return text 

def type_text(text):
    print(f"⌨️ Typing: {text}")
    time.sleep(0.5) # Small pause to ensure focus is on the right window
    pyautogui.write(text)
    pyautogui.press('enter')

def main():
    audio_file = "temp_audio.wav"
    
    try:
        while True:
            # 1. Record while key is held
            success = record_while_held(audio_file)
            
            if success:
                # 2. Transcribe
                raw_text = transcribe_audio(audio_file)
                
                if not raw_text or len(raw_text) < 2:
                    print("⚠️ No speech detected.")
                    continue
                    
                print(f"📝 Raw: {raw_text}")
                
                # 3. AI Clean up
                clean_text = clean_with_ai(raw_text)
                print(f"✨ Cleaned: {clean_text}")
                
                # 4. Type it out
                type_text(clean_text)
            else:
                print("⚠️ No audio recorded.")

    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    finally:
        if os.path.exists(audio_file):
            os.remove(audio_file)

if __name__ == "__main__":
    main()

