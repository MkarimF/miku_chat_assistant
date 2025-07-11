from llama_cpp import Llama

# Ganti dengan lokasi modelmu nanti
MODEL_PATH = "models/mistral-7b-instruct-v0.2.Q4_K_M.gguf"

def test_llama_model():
    llm = Llama(
        model_path=MODEL_PATH,
        n_ctx=2048,
        n_threads=4,  # sesuaikan dengan jumlah core CPU kamu
        verbose=True
    )

    prompt = "Hello, who are you?"
    result = llm(prompt, max_tokens=100, stop=["</s>"])

    print("\n🧠 LLaMA Output:\n", result["choices"][0]["text"])

if __name__ == "__main__":
    test_llama_model()