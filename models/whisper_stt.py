import whisper
import sounddevice as sd
import numpy as np
import tempfile
import asyncio

class WhisperSTT:
    def __init__(self):
        self.model = whisper.load_model("base")

    async def recognize(self) -> str:
        fs = 16000
        duration = 5  # seconds
        print("[WhisperSTT] Recording...")
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        import sounddevice as sf
        sf.write(temp_file.name, recording, fs)
        result = self.model.transcribe(temp_file.name, language='id')
        return result["text"]