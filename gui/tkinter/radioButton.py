import tkinter as tk

class Tela:
    def __init__(self, master):
        self.nossa_tela = master

        #IntVar, StringVar oou BooleanVar

        self.cnt = tk.IntVar()

        self.rb1 = tk.Radiobutton(self.nossa_tela, text='Opção 1',
                                  variable = self.cnt, value=1, indicatoron = 0)
        self.rb1.pack()

        self.rb2 = tk.Radiobutton(self.nossa_tela, text='Opção 1',
                                  variable = self.cnt, value =2)
        self.rb2.pack()
        #self.rb2.select()
        #self.rb2.deselect()

        self.btn = tk.Button(self.nossa_tela, text='Confirm', command= self.func)
        self.btn.pack(side=tk.BOTTOM)


    def func(self):
        print(self.cnt.get())


janela_raiz = tk.Tk()
Tela(janela_raiz)
janela_raiz.mainloop()
