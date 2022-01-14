'''
#FIFO : First In First Out

livros = list()
livros.append('livro1')
livros.append('livro2')
livros.append('livros3')
livros.append('livros4')
livros.append('livros5')

print(livros)

#remove o úçtimo livro da pilha [lista]
remove_livro = livros.pop() #5
remove_livro = livros.pop() #4
remove_livro = livros.pop() #3
remove_livro = livros.pop() #2
remove_livro = livros.pop() #1
print(f'livros: {str(livros)})')
print(f'Livros removido: {remove_livro}')
print(f'Livros restantes: {livros}')
'''

# FILA : Firts In Last Out
from collections import deque

"""
fila = deque()
print(fila)
fila.append('Joãozinho')
fila.append('Marcos')
fila.append('Diego')

for nome in fila:
  print(nome, end=' --- ')

print()
print("-"*50)
print(f'{fila.popleft()} saiu da fila')
for nome in fila:
  print(nome, end=' --- ')
"""

"""
fila = deque(maxlen=5)
fila.append("Diego")
fila.append("João")
fila.append("Jacira")
fila.append("joniscleide")
fila.append("Donizete")
"""
"""
#outra forma de adicionara valores na fila
fila = deque(maxlen=5)
fila.extend(['Diego', 'João', 'José', 'Jacira', 'Tarcisio' ])

"""

# Se definir um tamnaho máximo para a fila, quando é #adicionado outro valor e supere o liimite da fila, #o primeira da lista é removido e para entar o #útimo"""
"""
fila.append('Donizete')


for i, nome in enumerate(fila):
  print(i, nome)
"""

from time import sleep

fila = deque(maxlen=10)

fila.extend(['Diego', 'Suzane', 'Xafu', 'Fornio'])
for i, nome in enumerate(fila):
    print(i, nome)

print('-' * 50)
fila.insert(2, 'Xafu de Cornio')
for i, nome in enumerate(fila):
    print(i, nome)

"""
for i in range(1000):
  fila.append(i)
  print(fila)

  sleep(1)
"""
