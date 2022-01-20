import tkinter as tk
from tkinter import  messagebox

class Tela:
    def __init__(self, master):
        self.nossa_tela = master

        self.btn = tk.Button(self.nossa_tela, text='Clique aqui', command=self.caixa)
        self.btn.pack(padx=30, pady=30)

    def caixa(self):
        #--> showinfo, showwarnig, showerror, askquestion, askokcancel, askretrycancel, askyeso, askyesnocancel
        # self.caixa = messagebox.showinfo('Informação', 'Realmente temos essa informação')
        # self.caixa = messagebox.showwarning('Informação', 'Cuidado')
        # self.caixa = messagebox.showerror('Informação', 'Erro')
        # self.caixa = messagebox.askquestion('Pergunta', 'Vc tem certeza')
        # print(self.caixa)
        # if self.caixa =='yes':
        #     print('Escola certa')
        # self.caixa = messagebox.askokcancel('Perguna', 'Vc tem certeza')
        # print(self.caixa)
        # if self.caixa == 'True':
        #     print('Escolha certa')

        # self.caixa = messagebox.askretrycancel('Perguna', 'Vc tem certeza')
        # print(self.caixa)
        # if self.caixa == 'True':
        #     print('Escolha certa')

        self.caixa = messagebox.askyesnocancel('Perguna', 'Vc tem certeza')
        print(self.caixa)
        if self.caixa == 'True':
            print('Escolha certa')


janela_raiz = tk.Tk()
Tela(janela_raiz)
janela_raiz.mainloop()