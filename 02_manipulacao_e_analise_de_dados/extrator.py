import os
import json
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv

# Carrega as chaves de ambiente do arquivo .env
load_dotenv()

# Inicializa o cliente apontando para o OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# Schema JSON estrito exigido na Tarefa 2 do professor
schema_metadados = {
    "name": "extracao_metadados_artigo",
    "strict": True,
    "schema": {
        "type": "object",
        "properties": {
            "titulo": {
                "type": "string",
                "description": "Título oficial do trabalho acadêmico."
            },
            "autores": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Lista com os nomes dos autores do artigo."
            },
            "ano": {
                "type": "integer",
                "description": "Ano de publicação do trabalho."
            }
        },
        "required": ["titulo", "autores", "ano"],
        "additionalProperties": False
    }
}

def extrair_metadados(caminho_md: Path) -> dict:
    conteudo_markdown = caminho_md.read_text(encoding="utf-8")
    
    prompt = f"""
    Extraia as informações solicitadas do seguinte artigo acadêmico:
    
    {conteudo_markdown}
    """

    resposta = client.chat.completions.create(
        model="openai/gpt-4o",  # Modelo compatível com Structured Outputs no OpenRouter
        max_tokens=1500,        # Limita o uso de tokens para evitar estouro de créditos
        messages=[
            {"role": "system", "content": "Você é um assistente especializado em extração estruturada de metadados de documentos."},
            {"role": "user", "content": prompt}
        ],
        response_format={
            "type": "json_schema",
            "json_schema": schema_metadados
        }
    )

    return json.loads(resposta.choices[0].message.content)

if __name__ == "__main__":
    # Pega o diretório onde este script está (AULA_02)
    pasta_atual = Path(__file__).parent
    
    # Varre todos os arquivos .md da pasta
    for arquivo_md in pasta_atual.glob("*.md"):
        if arquivo_md.name.lower() == "readme.md":
            continue
            
        print(f"Processando arquivo: {arquivo_md.name}...")
        
        dados_json = extrair_metadados(arquivo_md)
        
        # Cria um arquivo .json com o mesmo nome do markdown correspondente
        arquivo_saida = arquivo_md.with_suffix(".json")
        arquivo_saida.write_text(
            json.dumps(dados_json, indent=4, ensure_ascii=False), 
            encoding="utf-8"
        )
        
        print(f"Salvo com sucesso em: {arquivo_saida.name}\n")