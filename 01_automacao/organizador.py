import os
import shutil

# Defina a pasta que o robô vai vigiar
DOWNLOADS_PATH = os.path.expanduser("~/Downloads")

# Mapeamento de pastas
MAPA_EXTENSOES = {
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Imagens": [".jpg", ".png", ".jpeg", ".gif"],
    "Executaveis": [".exe", ".msi"],
    "Compactados": [".zip", ".rar"]
}

def organizar():
    for arquivo in os.listdir(DOWNLOADS_PATH):
        nome, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()
        
        for pasta, extensoes_alvo in MAPA_EXTENSOES.items():
            if extensao in extensoes_alvo:
                # Cria a subpasta se não existir
                caminho_destino = os.path.join(DOWNLOADS_PATH, pasta)
                os.makedirs(caminho_destino, exist_ok=True)
                
                # Move o arquivo
                origem = os.path.join(DOWNLOADS_PATH, arquivo)
                destino = os.path.join(caminho_destino, arquivo)
                shutil.move(origem, destino)
                print(f"✅ Movido: {arquivo} -> {pasta}")

if __name__ == "__main__":
    organizar()