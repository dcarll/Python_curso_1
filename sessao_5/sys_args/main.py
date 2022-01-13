"""
#!/usr/bin/env python3
"""
import sys
import os

argumentos = sys.argv
qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print("Faltando argumentos")
    print("-a", "para listar todos os arquivos nesta pastas", sep="\t")
    print("-d", "para listar todos os diretórios", sep="\t")
    print("-all", "para listar todos tudo", sep="\t")
    sys.exit()

so_arquivos = False
so_diretorios = False
toos = False
if '-a' in argumentos:
    so_arquivos = True

if '-d' in argumentos:
    so_diretorios = True
if 'all' in argumentos:
    toos = True



for arquivo in os.listdir('.'):
    if so_arquivos:
        if os.path.isfile(arquivo):
            print(arquivo)
    if so_diretorios:
        if os.path.isdir(arquivo):
            print(arquivo)
    if toos:
        if os.path.isfile(arquivo):
            print(arquivo)
        if os.path.isdir(arquivo):
            print(arquivo)
