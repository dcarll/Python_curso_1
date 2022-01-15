import PyPDF2
import os

caminho_dos_pdf = r'pdf'
"""
novo_pdf = PyPDF2.PdfFileMerger()
for root, dirs, files in os.walk(caminho_dos_pdf):
    for file in files:
        caminho_completo_arquivo = os.path.join(root, file)

        arquivo_pdf = open(caminho_completo_arquivo, 'rb')
        novo_pdf.append(arquivo_pdf)
with open(f'{caminho_dos_pdf}/novo_arquivo.pdf', 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)
"""

with open('pdf/novo_arquivo.pdf', 'rb') as arquivo_pdf:
    read = PyPDF2.PdfFileReader(arquivo_pdf)
    num_paginas = read.getNumPages()

    for num_pagina in range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()
        paginal_ataul = read.getPage(num_pagina)
        escritor.addPage(paginal_ataul)

        with open(f'novos_pdfs/{num_pagina}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)



"""
Versão do curso

Documentação:
https://pythonhosted.org/PyPDF2/
Mais exemplos de uso:
http://www.blog.pythonlibrary.org/2018/06/07/an-intro-to-pypdf2/

pip install pypdf2 # virtualenv
pipenv install pypdf2 # pipenv

import PyPDF2
import os


# JUNTAS PDFs
caminho_dos_pdfs = 'pdf'

novo_pdf = PyPDF2.PdfFileMerger()
for root, dirs, files in os.walk(caminho_dos_pdfs):
    for file in files:
        caminho_completo_arquivo = os.path.join(root, file)

        arquivo_pdf = open(caminho_completo_arquivo, 'rb')
        novo_pdf.append(arquivo_pdf)

with open(f'{caminho_dos_pdfs}/novo_arquivo.pdf', 'wb') as meu_novo_pdf:
    novo_pdf.write(meu_novo_pdf)



# SEPARA PDFs
with open('pdf/novo_arquivo.pdf', 'rb') as arquivo_pdf:
    leitor = PyPDF2.PdfFileReader(arquivo_pdf)
    num_paginas = leitor.getNumPages()

    for num_pagina in range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()
        pagina_atual = leitor.getPage(num_pagina)
        escritor.addPage(pagina_atual)

        with open(f'novos_pdfs/{num_pagina}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)



"""