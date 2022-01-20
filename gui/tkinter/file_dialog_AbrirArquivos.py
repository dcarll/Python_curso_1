import tkinter as tk
from tkinter import filedialog

class Tela:
    def __init__(self, master):
        self.nossa_tela = master

        self.barra_menu = tk.Menu(self.nossa_tela)
        self.nossa_tela.config(menu=self.barra_menu)
        self.barra_menu.add_command(label='Ler Arquivo', command=self.ler_arquivo)
        self.barra_menu.add_command(label='Abrir Diretório do arquivo', command=self.abre_dir)

    '''
    askopenfilename não retorna o conteudo do arquivo, retorna somente o caminho
    '''
    def ler_arquivo(self):
        self.arquivo = filedialog.askopenfile(mode='r', initialdir='/Desktop',
                                              title='Selecione um arquivo',
                                              filetypes=(('Arquivos de texto', '*.txt'),
                                                        ('Arqvuivos Python', '*.py')))
        self.conteudo = self.arquivo.read()
        print(self.conteudo)

    def abre_dir(self):
        self.arquivo2 = filedialog.askopenfilename(initialdir='/Desktop',
                                              title='Selecione um arquivo',
                                              filetypes=(('Arquivos de texto', '*.txt'),
                                                        ('Arqvuivos Python', '*.py')),
                                                   initialfile='teste.txt')
        print(self.arquivo2)

    '''      
         ('Arqvuivos Python', '*.*py'))  )  cola o '*' após o ponto se quiser q todas as extens~es sejam v´lodas                                                    
        #r = leitura,  '/'= Dico 
    '''



janela_raiz = tk.Tk()
Tela(janela_raiz)
janela_raiz.mainloop()

