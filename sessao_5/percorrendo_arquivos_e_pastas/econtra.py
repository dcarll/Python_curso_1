import os
from utils import  formata_tamanho

caminho_procura = input("Digite um caminlho: ")
# caminho_procura = r'D:\Jogos'
termo_procura = input("Nome do arquivo: ")



cont = 0
for raiz, diretorios, arquivos in os. walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                cont +=1
                caminho_completo = os.path.join(raiz, arquivo)
                # nome_arquivo, ext_arquivo = os.path.splitext(caminho_completo)
                nome_arquivo, ext_arquivos = os.path.splitext(arquivo)
                # print(nome_arquivo, ext_arquivos, sep='---')
                #print(nome_arquivo, ext_arquivo)
                # print(caminho_completo)
                # print(arquivo)

                tamanho_arquivo = os.path.getsize(caminho_procura)

                # print(tamanho_arquivo)

                print()
                print('Encontreo o arquivo:', arquivo)
                print('Nome: ', nome_arquivo)
                print('Extensão: ', ext_arquivos)
                print('Ramanho: ', tamanho_arquivo)
                print("Tamanho formatado:", formata_tamanho(tamanho_arquivo))
            except PermissionError as e:
                print('Sem permissões')
            except FileNotFoundError as e:
                print("Arquivo não encontrado")
            except Exception as e:
                print("Erro desconhecido:", e)

print()
print(f'{cont} arquivos encontrados')