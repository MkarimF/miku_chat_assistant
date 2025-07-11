import json
import os
from datetime import datetime
from core.logger import logging

logger = logging.getLogger("Miku")
class TaskManager:
    def __init__(self, path="data/tasks.json"):
        self.path = path
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if not os.path.exists(path):
            with open(path, 'w') as f:
                json.dump([], f)
                
    async def handle_task(self, prompt):
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task = {
            "time": now,
            "prompt": prompt
        }
        with open(self.path,"W")as f:
            task = json.load(f)
        task.append(task)
        with open(self.path, 'w') as f:
            json.dump(task, f, indent=4)
        logger.info(f"Task added: {task}")
        