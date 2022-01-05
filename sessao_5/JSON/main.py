"""
JavaScript Object Notation - JSON
JSON (JavaScript Object Notation) é um formato de troca de dados entre sistemas
e programas muito leve e de fácil utilização. Muito utilizado por APIs

DUMPS / Dump
######################
Python          JSON
dict	        object
list, tuple	    array
str	            string
int, float  	number
True        	true
FALSE	        False
None	        null

LOADS / Load
######################
JSON	        Python
object	        dict
array	        list
string	        str
number (int)	int
number (real)	float
true	        True
false	        False
null	        None

"""

from dados import *
import json

lista = [1,2,3,4,5,6]

# converte de python para json
# dado_json = json.dumps(lista)
# print(type(dado_json))

# dados_json = json.dumps(clientes_dicionario, indent=4)
# print(dados_json)

# dicionario = json.loads(clientes_json)
#
# for chave, valor in dicionario.items():
#     print(chave)
#     print(valor)


# with open('clientes_json', 'w') as arquivo:
#     # converte o de json para json
#     json.dump(clientes_dicionario, arquivo, indent=4)

with open("clientes_json", "r") as arquivo:
    dados= json.load(arquivo)

for chave, valor in dados.items():
    print(chave)
    print(valor)
