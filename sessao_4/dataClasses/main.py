from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    sobrenome: str

p1 = Pessoa("Luiz", "Otavio")
print(p1)

