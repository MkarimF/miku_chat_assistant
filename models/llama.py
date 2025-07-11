import subprocess
import asyncio

class LLaMA3Engine:
    def __init__(self, model_path="./models/mistral-7b-instruct-v0.2.Q4_K_M.gguf"):
        self.model_path = model_path
        self.context = []  # Simple context tracker for offline mode

    async def ask(self, prompt: str, history=None) -> str:
        # kudu punya ollama yang dimasukin ke model soalnya run nya offline
        proc = await asyncio.create_subprocess_exec(
            "ollama", "run", "llama3",
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        full_prompt = prompt if not history else "\n".join([msg["content"] for msg in history]) + "\n" + prompt
        stdout, stderr = await proc.communicate(input=full_prompt.encode())
        return stdout.decode().strip()