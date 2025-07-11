import asyncio
from core.config import Config
from .logger import logging
from core.brain import Brain
from core.microphone import Microphone
from core.speaker import Speaker


class Assistant:
    def __init__(self):
        self.mic = Microphone()
        self.brain = Brain()
        self.speaker = Speaker()
        
    async def run(self):
        logging.info("Assistant is starting...")
        prompt = await self.mic.listen()
        logging.info(f"You said: {prompt}")
        #checing for task command
        if "tambah tugas" in prompt or "reminder" in prompt:
            # Here you would handle the task addition logic
            logging.info("Adding task to the list...")
            # For now, we just simulate a response
            print("Tugas telah ditambahkan ke daftar.")
            await self.task_manager.handle_task(prompt)
            return
        response = await self.brain.generate_response(prompt)
        if not response:
            logging.error("Failed to generate a response.")
            return
        logging.info(f"Assistant response: {response}")
        await self.speaker.say(response)