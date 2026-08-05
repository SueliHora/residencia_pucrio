import os

# Desativa otimizações problemáticas do PyTorch no Windows
os.environ["TORCHDYNAMO_DISABLE"] = "1"
os.environ["TORCH_COMPILE_DISABLE"] = "1"

from pathlib import Path
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from pypdf import PdfReader

# Configuração leve do Docling para economizar memória
pipeline_options = PdfPipelineOptions()
pipeline_options.do_ocr = False
pipeline_options.do_table_structure = False

converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
    }
)

pasta_arquivos = Path("Aula02_arquivos")
arquivos_pdf = [
    "bioetica_e_ia.pdf",
    "escrita_academica_ia.pdf",
    "twitter_algoritmo.pdf",
]

for nome_pdf in arquivos_pdf:
  caminho_pdf = pasta_arquivos / nome_pdf
  caminho_md = pasta_arquivos / nome_pdf.replace(".pdf", ".md")
  print(f"\nProcessando: {nome_pdf}")

  try:
    # Tenta usar o Docling primeiro
    resultado = converter.convert(caminho_pdf)
    markdown_output = resultado.document.export_to_markdown()

    with open(caminho_md, "w", encoding="utf-8") as f:
      f.write(markdown_output)
    print(f"Sucesso com Docling! Salvo como {caminho_md}")

  except Exception as e:
    # Se o Docling falhar por limite de memória, usa o pypdf como plano B seguro
    print(
        "Aviso: Arquivo complexo detectado. Usando extrator alternativo"
        " seguro..."
    )
    reader = PdfReader(caminho_pdf)
    texto_completo = ""

    for i, pagina in enumerate(reader.pages):
      texto = pagina.extract_text()
      if texto:
        texto_completo += f"\n\n## Página {i+1}\n\n{texto}"

    with open(caminho_md, "w", encoding="utf-8") as f:
      f.write(texto_completo)
    print(f"Sucesso com plano B! Salvo como {caminho_md}")

print("\nProcesso concluído para todos os arquivos!")