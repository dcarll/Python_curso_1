'''
https://www.youtube.com/watch?v=fU0oI6RwlnU&list=PL72uMH0hlJzoahdsn_Jpp8OjY8sW4C4FA&index=15&ab_channel=PythonFEI
'''

import tkinter as tk

class Tela:
    def __init__(self, master):
        self.nossa_tela = master

        self.barra_menu = tk.Menu(self.nossa_tela)
        self.nossa_tela.config(menu = self.barra_menu)

        self.arquivo = tk.Menu(self.barra_menu, tearoff=0)

        self.arquivo.add_command(labe='Novo')

        self.arquivo.add_separator()

        self.abrir = tk.Menu(self.arquivo)
        self.abrir.add_command(label='Escolher diretótio')
        self.arquivo.add_cascade(labe='Abrir', menu=self.abrir)

        self.barra_menu.add_cascade(label='File', menu=self.arquivo)
        self.barra_menu.add_command(label='Editar')
        self.barra_menu.add_command(label='Ajuda')

janela_raiz = tk.Tk()
Tela(janela_raiz)
janela_raiz.mainloop()