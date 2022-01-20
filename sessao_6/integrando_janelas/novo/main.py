import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.btnEscolherArquivo.clicked.connect(self.abrir_imagem)
        self.btnRedimensionar.clicked.connect(self.redimensionar)
        self.btnSalvar.clicked.connect(self.salvar)


    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir Imagem'
            r'C:\Users\Mestre\OneDrive\Área de Trabalho\imagens',
            #options=QFileDialog.DontUseNativeDialog
        )
        self.inputAbriArquivo.setText(imagem)
        self.original_img = QPixmap(imagem)
        self.labelImg.setPixmap(self.original_img)
        self.inputLargura.setText(str(self.original_img.width()))
        self.inputAltura.setText(str(self.original_img.height()))

    def redimensionar(self):
        largura = int(self.inputLargura.text())
        self.nova_imagen = self.original_img.scaledToWidth(largura)
        self.labelImg.setPixmap(self.nova_imagen)
        self.inputLargura.setText(str(self.nova_imagen.width()))
        self.inputAltura.setText(str(self.nova_imagen.height()))

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar Imagem'
            r'C:\Users\Mestre\OneDrive\Área de Trabalho',
            # options=QFileDialog.DontUseNativeDialog
        )
        self.nova_imagen.save(imagem, 'PNG')


if __name__=='__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()
