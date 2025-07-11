import logging
import aiohttp
import asyncio
import tempfile
import os
from core.config import Config
from core.logger import logging
from pydub import AudioSegment
from pydub.playback import play
logger = logging.getLogger("Miku")
class Speaker:
    def __init__(self):
        self.config = Config()
        self.host = self.config.get("voicevox", "host")
        self.port = self.config.get("voicevox", "port")
        self.speaker_id = self.config.get("voicevox", "speaker_id")
        if not self.host or not self.port:
            raise ValueError("[CONFIG ERROR] voicevox.host dan port tidak boleh kosong")
        self.base_url = f"http://{self.host}:{self.port}"
        logger.info(f"[Speaker] VoiceVox base_url: {self.base_url}")

    async def say(self, text):
        temp = None
        try:
            async with aiohttp.ClientSession() as session:
                query_url = f"{self.base_url}/audio_query"
                
                #query audio sistesis
                async with session.post(query_url, params={"text": text, "speaker": self.speaker_id}) as query_resp:
                    if query_resp.status != 200:
                        logger.error(f"Failed to get audio query: {await query_resp.text()}")
                        return
                    audio_query = await query_resp.json()
                # Synthesis audio
                url_synthesis = f"http://{self.host}:{self.port}/synthesis"
                async with session.post(url_synthesis, params={"speaker": self.speaker_id}, json=audio_query) as synth_resp:
                    if synth_resp.status != 200:
                        logger.error(f"VoiceVox synthesis failed: {await synth_resp.text()}")
                        return

                    # Simpan hasil wav sementara
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp:
                        temp.write(await synth_resp.read())
                        temp.flush()
                    sound = AudioSegment.from_wav(temp.name)
                    play(sound)
                    
        except Exception as e:
            logger.exception(f"Speaker error: {e}")
            # return        
                    
            #         async with session.post(url_synthesis, json=query) as resp:
            #             audio_data = await resp.read()
                        
            # temp = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
            # temp.write(audio_data)
            # temp.close()
        
        finally:
            if temp and os.path.exists(temp.name):
                logger.info(f"Spoken text: {text}")
                os.remove(temp.name)
                return True