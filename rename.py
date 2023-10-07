import os

# Listar todos os arquivos no diretório atual
arquivos = os.listdir()

# Inicializar um contador para adicionar números aos nomes dos arquivos
contador = 1

# Iterar sobre os arquivos no diretório atual
for arquivo in arquivos:
    # Verificar se o arquivo é uma imagem (por extensão)
    if arquivo.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        # Construir o novo nome do arquivo
        novo_nome = f'lulu_{contador}.jpg'

        # Renomear o arquivo
        os.rename(arquivo, novo_nome)

        # Incrementar o contador
        contador += 1

print("Renomeação concluída com sucesso!")
