# Residência - Trilhas em Tecnologias: IA Generativa & RAG

Repositório destinado às atividades desenvolvidas durante o programa de Residência - Trilhas em Tecnologias: IA Generativa & RAG.
Aluna: Sueli da Hora Moreira
Aula: 01 - Configuração de Ambiente e Primeira Conexão com LLM

## Sobre a atividade

Nesta primeira aula, o objetivo foi configurar o ambiente de desenvolvimento em Python, utilizar o gerenciador de pacotes `uv` e realizar a primeira interação com um Large Language Model (LLM) utilizando a API do OpenRouter.

## Tecnologias utilizadas

* Python
* OpenRouter API
* OpenAI Python SDK (compatível com OpenRouter)
* `uv` (Gerenciador de pacotes e ambientes)
* python-dotenv
* Antigravity
* Git e GitHub

## Estrutura do projeto
```text
.
├── AULA_01/
│   └── hello_llm.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

O arquivo `.env` é utilizado apenas localmente para armazenar a chave da API e **não deve ser versionado**. Da mesma forma, a pasta do ambiente virtual (`.venv/`) gerada pelo `uv` deve ser ignorada pelo Git e não enviada para o repositório.

## Configuração do projeto com `uv`

### 1. Inicializar e instalar dependências

Com o `uv` instalado, você pode criar o ambiente e sincronizar as dependências rapidamente:

```bash
uv venv
uv pip install -r requirements.txt
```
Configure o arquivo `.env` com a sua chave de acesso do OpenRouter (`OPENROUTER_API_KEY`).

### 2. Executar o script principal:
```bash
uv run python hello_llm.py
```