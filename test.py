import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("🎙️ Coba bicara...")
    audio = r.listen(source)
    with open("mic_test.wav", "wb") as f:
        f.write(audio.get_wav_data())
print("🎧 Disimpan ke mic_test.wav")