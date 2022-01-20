import tkinter as tk
from tkinter import scrolledtext

class Tela:
    def __init__(self, master):
        self.nossa_tela = master

        self.txtArea = scrolledtext.ScrolledText(self.nossa_tela)
        self.txtArea.pack(expand=True, fill=tk.X)

        self.btn = tk.Button(self.nossa_tela, text='Clique Aqui', command=self.test)
        self.btn.pack(pady=20)

    def test(self):
        conteudo = self.txtArea.get('1.0', tk.END)
        self.txtArea.delete('1.0', tk.END)
        print(conteudo)
        self.txtArea.insert('1.0', 'Python FEI')
        self.txtArea.insert(tk.INSERT, 'Pythonjá')

janela_raiz = tk.Tk()
Tela(janela_raiz)
janela_raiz.mainloop()

