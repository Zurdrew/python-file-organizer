import os
import shutil

def organizar_pasta(caminho_pasta):
    # Dicionário mapeando extensões para pastas
    extensoes = {
        'Imagens': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documentos': ['.pdf', '.docx', '.txt', '.xlsx', '.csv'],
        'Instaladores': ['.exe', '.msi'],
        'Compactados': ['.zip', '.rar', '.tar.gz']
    }

    if not os.path.exists(caminho_pasta):
        print(f"Erro: A pasta {caminho_pasta} não existe.")
        return

    # Lista todos os arquivos na pasta
    for arquivo in os.listdir(caminho_pasta):
        caminho_arquivo = os.path.join(caminho_pasta, arquivo)

        # Ignora se for uma pasta
        if os.path.isdir(caminho_arquivo):
            continue

        _, extensao = os.path.splitext(arquivo)
        
        # Encontra a categoria correta para a extensão
        pasta_destino = 'Outros'
        for categoria, exts in extensoes.items():
            if extensao.lower() in exts:
                pasta_destino = categoria
                break

        # Cria a pasta de destino se não existir
        caminho_destino = os.path.join(caminho_pasta, pasta_destino)
        if not os.path.exists(caminho_destino):
            os.makedirs(caminho_destino)

        # Move o arquivo
        shutil.move(caminho_arquivo, os.path.join(caminho_destino, arquivo))
        print(f"Movido: {arquivo} -> {pasta_destino}/")

if __name__ == "__main__":
    # Substitua pelo caminho da pasta que deseja organizar
    pasta_alvo = r"C:\Users\SeuUsuario\Downloads"
    organizar_pasta(pasta_alvo)
    print("Organização concluída.")