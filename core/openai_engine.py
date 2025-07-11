import aiohttp

class OpenAIEngine:
    def __init__(self, config):
        self.api_key = config.service('openai').get('api_key')
        self.model = config.service('openai').get('model', 'gpt-3.5-turbo')
        self.persona = config.get('persona', 'Hatsune Miku')

    async def ask(self, prompt: str) -> str:
        system_prompt = f"You are {self.persona}, a friendly Japanese virtual assistant who is always cheerful and helpful."
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        body = {
            "model": self.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        }
        async with aiohttp.ClientSession() as session:
            async with session.post("https://api.openai.com/v1/chat/completions", headers=headers, json=body) as resp:
                data = await resp.json()
                return data['choices'][0]['message']['content']