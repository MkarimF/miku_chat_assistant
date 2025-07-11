import subprocess
import asyncio

class LLaMA3Engine:
    def __init__(self, model_path="./models/mistral-7b-instruct-v0.2.Q4_K_M.gguf",persona="You are Hatsune Miku, a cheerful virtual idol assistant. Respond concisely and with a friendly tone."):
        self.model_path = model_path
        self.persona = persona
        self.context = []  # Simple context tracker untuk offline mode kalau sebelumnya pernah online
        

    async def ask(self, prompt: str, history=None) -> str:
        full_prompt = self.persona + "\n\n"
        if history:
            for msg in history:
                role = msg['role']
                content = msg['content']
                full_prompt += f"{role}: {content}\n"

        full_prompt += f"user : {prompt}\nassistant:"
        # kudu punya model ollama terus  run secara local
        proc = await asyncio.create_subprocess_exec(
            "ollama", "run", "llama3",
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        # full_prompt = prompt if not history else "\n".join([msg["content"] for msg in history]) + "\n" + prompt
        stdout, stderr = await proc.communicate(input=full_prompt.encode())
        if proc.returncode != 0:
            print("❌ [LLaMA3 ERROR]:", stderr.decode().strip())
            return "Maaf, terjadi kesalahan saat menjalankan model."
        return stdout.decode().strip()
