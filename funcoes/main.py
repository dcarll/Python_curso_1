produtos = ['ABC123', 'adb012', 'ABS111', 'abD222']

def trata_texto(texto):
    #texto = texto.upper() #maiusculo
    #texto = texto.strip() #retira os espaços em branco
    #return texto
    pass

for i, produto in enumerate(produtos):
    produtos[i] = trata_texto(produtos)

print(produtos)

nome = 'Diego'

print(nome)