import csv

with open('clientes.csv', 'r') as arquivo:
    # dados = csv.reader(arquivo)
    dados = [x for x in csv.DictReader(arquivo)] #transfrma em dicionario. Para poder utilitar essa varieavel com os dados fora do escopo do "with" precisa está dentro de uma listComprehension


    # next(dados) #faz iterar a primeira linha, dessa forma no laço for só será apresentado a partir da segunda linha
    '''
    for dado in dados:
        print(dado)
    '''
    # for dado in dados:
        # print(dado['Nome'], dado['Sobrenome'])
        # print(dado["Nome"], dado["Sobrenome"], dado["E-mail"], dado["Telefone"])

with open("clientes2.csv", "w") as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )
    print(dados[0])

    for dado in dados:
        escreve.writerow([
            dado["Nome"],
            dado["Sobrenome"],
            dado["E-mail"],
            dado["Telefone"]
        ])

    print(dados[0])

"""
Aula do curso


Comma Separated Values - CSV (Valores separados por vírgula)
É um formato de dados muito usado em tabelas (Excel, Google Sheets), bases de
dados, clientes de e-mail, etc...

import csv

with open('clientes.csv', 'r') as arquivo:
    dados = [x for x in csv.DictReader(arquivo)]

with open('cliente2.csv', 'w') as arquivo:
    escreve = csv.writer(
        arquivo,
        delimiter=',',
        quotechar='"',
        quoting=csv.QUOTE_ALL
    )

    chaves = dados[0].keys()
    chaves = list(chaves)
    escreve.writerow(
        [
            chaves[0],
            chaves[1],
            chaves[2],
            chaves[3]
        ]
    )

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone']
            ]
        )

"""