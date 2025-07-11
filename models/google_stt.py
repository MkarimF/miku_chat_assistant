import speech_recognition as sr
import asyncio

class GoogleSTT:
    def __init__(self):
        self.recognizer = sr.Recognizer()


    async def recognize(self) -> str:

        # Step 1: rekam suara (blocking → to_thread)
        def record_audio():
            with sr.Microphone() as source:
                print("[GoogleSTT] Listening...")
                audio = self.recognizer.listen(source)
                return audio
        try:
            audio = await asyncio.to_thread(record_audio)
            return self.recognizer.recognize_google(audio, language="id-ID")
        except sr.UnknownValueError as e:
            print(f"[GoogleSTT] UnknownValueError: {e}")
            return "Maaf, saya tidak bisa mendengar apa yang kamu katakan"
        except sr.RequestError as e:
            print(f"[GoogleSTT] RequestError: {e}")
            return f"Terjadi kesalahan STT: {e}"
        except Exception as e:
            print(f"[GoogleSTT] Unexpected Error: {e}")
            return "Terjadi kesalahan yang tidak terduga saat mengenali suara"


        # # Step 2: konversi audio ke teks (blocking → to_thread)
        # def recognize_text():
        #     try:
        #         return self.recognizer.recognize_google(audio, language="id-ID")
        #     except sr.UnknownValueError:
        #         return "maaf miku tidak bisa mendengar apa yang kamu katakan"
        #     except sr.RequestError as e:
        #         return f"Terjadi kesalahan STT: {e}"

        # return await asyncio.to_thread(recognize_text)
        # Step 3: kembalikan teks
        # return await asyncio.to_thread(self.recognizer.recognize_google, audio, language="id-ID")