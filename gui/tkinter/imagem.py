import tkinter as tk
from PIL import ImageTk, Image
import os

class Tela:
    def __init__(self, master):
        self.nossa_tela = master
        self.nossa_tela.title('Janela Principal')
        img = Image.open(r'C:\Users\Mestre\OneDrive\Área de Trabalho\imagens\images.jpg')
        self.minha_imagem = ImageTk.PhotoImage(img)
        self.lbl = tk.Label(self.nossa_tela, image= self.minha_imagem,
                            compound = tk.TOP,
                            text= 'Imagem com tkinter!!!')
        self.lbl.image = self.minha_imagem
        self.lbl.pack()


janela_raiz = tk.Tk()
Tela(janela_raiz)
janela_raiz.mainloop()

