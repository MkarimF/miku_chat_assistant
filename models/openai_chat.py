import openai

class OpenAIEngine:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    async def ask(self, prompt: str, history=None) -> str:
        messages = history if history else [{"role": "user", "content": prompt}]
        response = await openai.ChatCompletion.acreate(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message.content.strip()