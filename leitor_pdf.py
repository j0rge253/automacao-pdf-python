import os
import re
import time
from PyPDF2 import PdfReader

# --- CONFIGURAÇÕES ---
PASTA_ORIGEM = "./documentos_recebidos"

def extrair_texto_pdf(caminho_pdf):
    """Extrai o texto da primeira página do PDF para análise."""
    try:
        leitor = PdfReader(caminho_pdf)
        if len(leitor.pages) > 0:
            return leitor.pages[0].extract_text()
        return ""
    except Exception as e:
        print(f"❌ Erro ao ler {caminho_pdf}: {e}")
        return ""

def buscar_data(texto):
    """
    Usa REGEX para encontrar datas no formato DD/MM/AAAA.
    Isso mostra para o recrutador que você domina manipulação de strings.
    """
    padrao_data = r"\d{2}/\d{2}/\d{4}"
    datas_encontradas = re.findall(padrao_data, texto)
    return datas_encontradas[0].replace("/", "-") if datas_encontradas else "sem_data"

def processar_arquivos():
    # Cria a pasta se ela não existir
    if not os.path.exists(PASTA_ORIGEM):
        os.makedirs(PASTA_ORIGEM)
        print(f"📂 Pasta '{PASTA_ORIGEM}' criada. Adicione arquivos PDF nela.")
        return

    arquivos = [f for f in os.listdir(PASTA_ORIGEM) if f.lower().endswith(".pdf")]
    
    if not arquivos:
        print("📭 Nenhum PDF encontrado para processar.")
        return

    print(f"🤖 Iniciando processamento de {len(arquivos)} arquivos...\n")

    for arquivo in arquivos:
        caminho_completo = os.path.join(PASTA_ORIGEM, arquivo)
        texto_pdf = extrair_texto_pdf(caminho_completo)
        
        # Identificação por Palavras-Chave
        categoria = "Documento_Generico"
        if "ESTACIO" in texto_pdf.upper():
            categoria = "Mensalidade_Estacio"
        elif "NATURA" in texto_pdf.upper() or "AVON" in texto_pdf.upper():
            categoria = "Pedido_Revenda"
        elif "FORTALEZA" in texto_pdf.upper():
            categoria = "Ingresso_Fortaleza"

        # Extração de Data e Gerador de ID Único
        data_doc = buscar_data(texto_pdf)
        id_unico = int(time.time() * 100) % 1000 # Pequeno sufixo para evitar duplicatas
        
        novo_nome = f"{categoria}_{data_doc}_{id_unico}.pdf"
        novo_caminho = os.path.join(PASTA_ORIGEM, novo_nome)

        try:
            os.rename(caminho_completo, novo_caminho)
            print(f"✅ RENOMEADO: {arquivo} ➡️ {novo_nome}")
        except Exception as e:
            print(f"⚠️ Erro ao renomear {arquivo}: {e}")

if __name__ == "__main__":
    processar_arquivos()
    print("\n🚀 Automação finalizada com sucesso!")