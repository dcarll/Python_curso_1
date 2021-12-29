import os
import shutil

caminho_original = r'C:\Users\Mestre\OneDrive\Documentos\videos'
caminho_novo = r'C:\Users\Mestre\OneDrive\Documentos\videos2'

try:
    os.mkdir(caminho_novo)
except FileExistsError as e:
    print(f'Pasta {caminho_novo} já existe')

for root, dirs, files in os.walk(caminho_novo):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(caminho_novo, file)

        if '.mp4' in file:
            os.remove(new_file_path)
            print(f'O arquivos {file} foi apagado')

        # if '.mp4' in file:
        #     shutil.copy(old_file_path, new_file_path)
        #     print(f'Arquivo {file} movido com sucesso!')