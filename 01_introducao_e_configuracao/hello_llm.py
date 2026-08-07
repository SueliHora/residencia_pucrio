import os
from dotenv import load_dotenv
from openai import OpenAI

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configura o cliente para usar o OpenRouter
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

# Usa o modelo definido no .env ou assume o padrão do OpenRouter
modelo = os.getenv("OPENAI_MODEL", "openai/gpt-4o-mini")

# Faz a requisição para a IA
response = client.chat.completions.create(
    model=modelo,
    messages=[
        {
            "role": "user", 
            "content": "Escreva uma mensagem de boas-vindas para uma aula de Introdução à Inteligência Artificial, introduzindo o tema e perguntando se há dúvidas."
        }
    ],
    store=True,
)

# Imprime a resposta da IA no terminal
print("\nResposta da IA:")
print(response.choices[0].message.content)