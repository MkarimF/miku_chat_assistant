import asyncio
import logging
from core.config import Config
from core.logger import logging

logger = logging.getLogger("Miku")
class Brain:
    def __init__(self):
        self.config = Config()
        self.history = []
        self.mode = self.config.get("mode", "chat_engine")
        from core.llama3_engine import LLaMA3Engine
        from models.openai_chat import OpenAIEngine
        self.llama = LLaMA3Engine()
        self.openai = OpenAIEngine(self.config.get("openai", "api_key"))
        
        
    async def generate_response(self, prompt: str) -> str:
        self.history.append({"role": "user", "content": prompt})

        if await self.is_online() and self.mode != "offline":
            logger.info("Using OpenAI engine")
            result = await self.openai.ask(prompt, self.history)
        else:
            logger.info("Using LLaMA3 engine")
            result = await self.llama.ask(prompt, self.history)

        self.history.append({"role": "assistant", "content": result})
        return result

    async def is_online(self) -> bool:
        try:
            import aiohttp
            async with aiohttp.ClientSession() as session:
                async with session.get("https://api.openai.com") as r:
                    if r.status == 200:
                        return f"{r.status} Connection successful"
                    else:
                        return f"{r.status} Connection failed"
        except:
            return False
        

# class Brain : 
#     def __init__(self):
#         self.config = Config()
#         self.history = []
#         self.mode = self.config.get("model","chat_engine")
#         from models.llama import LLaMA3Engine
#         from models.openai_chat import OpenAIEngine
#         self.llama = LLaMA3Engine()
#         self.openai = OpenAIEngine(self.config.get("openai","api_key"))
#     async def generate_response(self, prompt : str) -> str :
#         self.history.append({"role": "user", "content": prompt})
        
#         if await self.is_online() and self.mode != "offline":
#             logger.info("Using OpenAI Engine for response generation.")
#             result = await self.openai.ask(prompt, self.history)
            
#         else:
#             logger.info("Using LLaMA3 Engine for response generation.")
#             result = await self.llama.ask(prompt, self.history)
#         self.history.append({"role": "assistant", "content": result})
#         return result
# async def is_online(self) -> bool:
#     try:
#         import aiohttp
#         async with aiohttp.ClientSession() as session:
#             async with session.get("https://api.openai.com") as r:
#                 return r.status == 200
#     except:
#          return False