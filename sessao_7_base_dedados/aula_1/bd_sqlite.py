import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

# cursor.execute('CREATE TABLE IF NOT EXISTS clientes ('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome TEXT,'
#                'peso REAL'
#                ')')

# cursor.execute('INSERT INTO clientes (nome, peso) VALUES("DIEGO CARLOS", 80.25)')
# conexao.commit()

# cursor.execute('INSERT INTO clientes (nome, peso) VALUES (?, ?)', ('Maria', 50))
# cursor.execute(
#     'INSERT INTO clientes (nome, peso) VALUES (:nome, :peso)',
#     {'nome': 'Joãozinho', 'peso': 25}
# )
#
# cursor.execute(
#     'INSERT INTO clientes VALUES(:id, :nome, :peso)',
#     {'id': None, 'nome': 'Diego', 'peso': 113}
# )
# conexao.commit()


# cursor.execute(
#     'UPDATE clientes SET nome=:nome WHERE id=:id',
#     {'nome': 'Joana', 'id': 2}
# )

# cursor.execute(
#     'DELETE FROM clientes WHERE id=:id',
#     {'id': 2}
# )
#
# cursor.execute(
#     'DELETE FROM clientes WHERE nome="Joana"'
# )

cursor.execute(
    'SELECT nome, peso FROM clientes WHERE peso > :peso',
    {'peso': 50}
)
# conexao.commit()
cursor.execute('SELECT * FROM clientes')
for linha in cursor.fetchall():
    idenificador, nome, peso = linha
    print(idenificador, nome, peso)


cursor.close()
conexao.close()