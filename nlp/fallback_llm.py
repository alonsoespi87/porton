from llama_cpp import Llama

llm = Llama(model_path="models/phi-2.gguf", n_ctx=2048)

def generate_response(prompt):
    result = llm(prompt=f"User: {prompt}\nAssistant:", stop=["User:", "\n"], max_tokens=100)
    return result["choices"][0]["text"].strip()
