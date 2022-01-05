import csv
import pandas as pd

"""
# Abrindo o arqvuivom com um gerenciado de contexto "with"

with open('advertising.csv', 'r') as arquivo:
    arquivo_csv = csv.reader(arquivo, delimiter=',')

    for i, linha in enumerate(arquivo_csv):
        if i == 0:
            print("Cabelho: " + str(linha))
        else:
            print("Valor:   " + str(linha))
"""

# abrindo o arqvuivo com o pandas

tabela = pd.read_csv('advertising.csv')
# print(tabela)

# tratamento dos dados
print(tabela["TV"].sum)
