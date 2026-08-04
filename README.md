# Residência - Trilhas em Tecnologias: IA Generativa & RAG

Repositório destinado às atividades desenvolvidas durante o programa de Residência - Trilhas em Tecnologias: IA Generativa & RAG.
Aluna: Sueli da Hora Moreira
Aula: 01 - Configuração de Ambiente e Primeira Conexão com LLM

## Sobre a atividade

Nesta primeira aula, o objetivo foi configurar o ambiente de desenvolvimento em Python, utilizar o gerenciador de pacotes `uv` e realizar a primeira interação com um Large Language Model (LLM) utilizando a API do OpenRouter.

## Tecnologias utilizadas

- **Python 3.12+**
- **OpenRouter API**
- **OpenAI Python SDK** (compatível com OpenRouter)
- **uv** (Gerenciador de pacotes, dependências e ambientes)
- **python-dotenv**
- **Antigravity IDE**
- **Git e GitHub**

## Estrutura do projeto
```text
.
├── AULA_01/
│   └── hello_llm.py
├── .env.example
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

Nota de Segurança: **O arquivo `.env` é utilizado apenas localmente para armazenar a chave da API e **não deve ser versionado**. Da mesma forma, a pasta do ambiente virtual (`.venv/`) gerada pelo `uv` deve ser ignorada pelo Git e não enviada para o repositório.

## Configuração do projeto com `uv`

### 1. Sincronizar o ambiente e dependências

Com o `uv` instalado, você pode criar o ambiente e sincronizar as dependências rapidamente:

```bash
uv sync
```
Configure o arquivo `.env` com a sua chave de acesso do OpenRouter (`OPENROUTER_API_KEY`).

### 2. Configurar variáveis de ambiente:
Configure o arquivo .env na raiz com as suas variáveis:
```env
OPENROUTER_API_KEY=sua_chave_aqui
OPENAI_MODEL=openai/gpt-4o-mini
```
### 3. Executar o script principal:
Execute o script apontando para a pasta correta onde ele está guardado:

```bash
uv run AULA_01/hello_llm.py
```
