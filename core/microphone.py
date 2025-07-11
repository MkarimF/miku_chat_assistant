import asyncio
from core.logger import logging
from models.google_stt import GoogleSTT
from models.whisper_stt import WhisperSTT
from core.config import Config

logger = logging.getLogger("Miku")
class Microphone:
    def __init__(self):
        self.config = Config()
        self.mode = self.config.get("mode", "stt_engine")
        self.google = GoogleSTT()
        self.whisper = WhisperSTT()
        
        
    async def listen(self) -> str :
        if await self.is_online() and self.mode != "offline":
            logger.info("Using Google STT")
            return await self.google.recognize()
        else:
            logger.info("Using Whisper STT")
            return await self.whisper.recognize()
        
    async def is_online(self) -> bool:
        try:
            import aiohttp
            async with aiohttp.ClientSession() as session:
                async with session.get("https://google.com") as r:
                    if r.status == 200:
                        return f"{r.status} Connection successful"
                    else:
                        return f"{r.status} Connection failed"
        except:
            return False