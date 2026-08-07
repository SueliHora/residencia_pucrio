# Aula 02 - Conversão de PDFs para Markdown com Docling

Este diretório contém a solução para a Aula 02, focada em converter artigos acadêmicos em PDF para o formato Markdown (`.md`) de forma automatizada usando Python.

## O Desafio
O objetivo era extrair o texto de três artigos (*Bioética e IA*, *Escrita Acadêmica com IA* e *Algoritmo do Twitter*). Durante o processo, lidamos com desafios reais de infraestrutura e limitações de hardware que afetam bibliotecas pesadas de IA, problemas que fizeram os scripts padrão falharem.

## Problemas Resolvidos (Troubleshooting)

1. **Erro de Compilação do PyTorch (`InductorError / cl is not found`):**
   - **Causa:** O Docling utiliza modelos do PyTorch que tentam compilar código C++ no Windows para otimizar a execução, mas falham se o compilador nativo (`cl.exe`) não estiver instalado.
   - **Solução:** Injetamos variáveis de ambiente (`TORCHDYNAMO_DISABLE=1` e `TORCH_COMPILE_DISABLE=1`) no script para desativar a compilação dinâmica e forçar a execução no modo seguro.

2. **Estouro de Memória (`std::bad_alloc`):**
   - **Causa:** O motor de layout C++ do Docling estourou a memória disponível ao tentar processar páginas graficamente densas em um dos PDFs.
   - **Solução:** 
     - Desativamos o OCR e a estruturação de tabelas pesada.
     - Implementamos uma arquitetura de **Fallback (Plano B)** usando `try...except`. Se o processamento via IA falhar por limite de hardware, o script aciona instantaneamente a biblioteca mais leve `pypdf` para garantir a extração do texto sem quebrar o programa.

## Como Executar

O projeto utiliza o gerenciador de pacotes `uv` para máxima eficiência.

```bash
# Executa o conversor
uv run python converter.py
```
Estrutura do Código
O script converter.py foi desenhado com foco em resiliência:

Leitura em lote: Processa todos os PDFs da pasta sequencialmente.

Tratamento de Exceções: Continua o processamento mesmo se um arquivo apresentar problemas críticos.

Mecanismo de fallback inteligente: Alterna entre a ferramenta pesada (Docling) e a leve (PyPDF) automaticamente, garantindo 100% de entrega.
---
## Tarefa 2: Extração de Metadados com Structured Outputs

Processamento dos arquivos `.md` gerados na Tarefa 1 para extração de dados estritos via API.

- **Objetivo:** Extrair o título, os autores (como lista de strings) e o ano de publicação em formato JSON estrito.
- **Implementação (`extrator.py`):** Utilização da API do OpenRouter compatível com OpenAI, aplicando `response_format` com `json_schema` e `strict=True`.
- **Ajuste Técnico (Tokens):** Configuração explícita de `max_tokens=1500` para otimizar a requisição e evitar o erro de limite de créditos na API.

### Como Executar o Extrator:
```bash
uv run python extrator.py