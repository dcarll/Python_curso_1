import random
import string

#gera um numero inteiro entre A e B
# inteiro = random.randint(10,20)

#gera um numero aleatorio usando a funcão range
inteiro = random.randrange(900, 1000, 10)
#gera um numero flutuante entre A  e B
#flutuante = random.uniform(10,20)


lista = ['Luiz', 'Diego', 'Mario', 'Danilo', 'jose']
sorteio = random.choice(lista)
sorteio2 = random.choices(lista, k=2) #pode repetir
sorteio3 = random.sample(lista, 2) #não repete
random.shuffle(lista) #embaralha a lista

"""
for i in range(1000):
    sorteio = random.sample(lista, 2)
    print(sorteio)
"""
#gera um numero flutuante entre 0 e 1
flutuante = random.random()

#gera senha aleatoria

letras = string.ascii_letters
digitos = string.digits
caracteres = "!@#$%¨&*_-"
geral = letras + digitos + caracteres
print(geral)

senha = ''.join(random.choices(geral, k=20))
print(senha)