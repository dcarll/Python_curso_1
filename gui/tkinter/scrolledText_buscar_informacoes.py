import tkinter as tk
from tkinter import scrolledtext

class Tela:
    def __init__(self, master):
        self.nossa_tela = master

        self.txtArea = scrolledtext.ScrolledText(self.nossa_tela)
        self.txtArea.pack(expand=True, fill=tk.X)

        self.btn = tk.Button(self.nossa_tela, text='Clique Aqui', command=self.test)
        self.btn.pack(pady=20)

        self.entry = tk.Entry(self.nossa_tela)
        self.entry.pack()

        self.btn_busca = tk.Button(self.nossa_tela, text='Buscar', command=self.buscar)
        self.btn_busca.pack()

    def buscar(self):
        busca = self.entry.get()
        tamanho = len(busca)
        contador = 0
        começo = '1.0'

        self.txtArea.tag_delete('encontrada')
        while True:
            posicao = self.txtArea.search(pattern= busca, index= começo, stopindex=tk.END, count=True)
            if not posicao:
                print('Pesquisa finalizada\n'f"{contador} localizado com: '{busca}'")
                break
            self.txtArea.tag_add('encontrada', posicao, (posicao + f'+{tamanho}c'))
            contador += 1
            começo = posicao + '+1c'

            self.txtArea.tag_config('encontrada', background='yellow')



    def test(self):
        conteudo = self.txtArea.get('1.0', tk.END)
        self.txtArea.delete('1.0', tk.END)
        print(conteudo)
        self.txtArea.insert('1.0', 'Python FEI')
        self.txtArea.insert(tk.INSERT, 'Pythonjá')

janela_raiz = tk.Tk()
Tela(janela_raiz)
janela_raiz.mainloop()

