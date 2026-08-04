import os
import requests
from dotenv import load_dotenv

# Carrega a chave do .env da raiz
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

print("Conectando ao OpenRouter...")

# Chamada direta via API do OpenRouter (sem biblioteca da OpenAI)
response = requests.post(
    url="https://openrouter.ai/api/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    },
    json={
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": "Olá! Estou pronta para a aula de Introdução à IA."}
        ]
    }
)

resultado = response.json()

print("\nResposta da IA:")
print(resultado["choices"][0]["message"]["content"])