import tkinter as tk
from tkinter import filedialog


class Janela2:
    def __init__(self, master, root):
        self.nova = master
        self.nova.title('Janela Secindária')

        self.origem = root

        self.btn = tk.Button(self.nova, text='Voltar para a tela prncipal', command=self.voltar)
        self.btn.pack(padx=20, pady=20)

    def voltar(self):
        self.origem.deiconify()
        self.nova.destroy()


class Tela:
    def __init__(self, master):
        self.nossa_tela = master
        self.nossa_tela.title('Janela Principal')

        self.btn = tk.Button(self.nossa_tela, text = 'Abrir interface', command= self.abrir)
        self.btn.pack(padx=20, pady=20)

    def abrir(self):
        self.nossa_tela.withdraw()
        # self.nossa_tela.iconify()
        self.nova_tela = tk.Toplevel(self.nossa_tela)
        Janela2(self.nova_tela, self.nossa_tela)






janela_raiz = tk.Tk()
Tela(janela_raiz)
janela_raiz.mainloop()

