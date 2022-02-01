import sqlite3

class AgendaBD():
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()


    def inserir(self, nome, telefone):
        consulta = 'INSERT OR IGNORE INTO agenda (nome, telefone) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, nome, telefone, id):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id, ))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')

        for linha in self.cursor.fetchall():
            id, nome, telefone = linha
            print(f'ID: {id}\t',
                  f'Nome: {nome}\t',
                  f'\tTelefone: {telefone}')


    def buscar(self, valor):
        consulta = 'SELECT * FROM agenda WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%',))
        for linha in self.cursor.fetchall():
            id, nome, telefone = linha
            print(f'ID: {id}\t',
                  f'Nome: {nome}\t',
                  f'\tTelefone : {telefone}')


    def fechar(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    agenda = AgendaBD('agenda.bd')
    agenda.buscar('João')

