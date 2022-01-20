import tkinter as tk
from tkinter import filedialog

class Tela:
    def __init__(self, master):
        self.nossa_tela = master

        self.barra_menu = tk.Menu(self.nossa_tela)
        self.nossa_tela.config(menu=self.barra_menu)
        self.barra_menu.add_command(label='Salvar', command=self.salvar)
        self.barra_menu.add_command(label='Salvar no diretorio', command=self.salvar_no_diretorio)

    def salvar(self):
        self.arquivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                                filetypes = (('Arquivos python', '*.py'),("Arquivos de texto",'*.txt')))

        if self.arquivo is not None:
            print('Arquivo Criado')

            self.arquivo.write("print('Ola mundo')")
            self.arquivo.close()
        else:
            print('Erro')

    def salvar_no_diretorio(self):
        self.arquivo2 = filedialog.asksaveasfilename(defaultextension='.txt', initialdir='\Desktop')
        print(self.arquivo2)




janela_raiz = tk.Tk()
Tela(janela_raiz)
janela_raiz.mainloop()

