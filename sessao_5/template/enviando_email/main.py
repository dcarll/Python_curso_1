'''
from string import Template
from datetime import datetime
from dados_email import meu_email, minha_senha

from email.mime.multipart import MIMEMultipart #assunto da mensagem, de quem e pra quem vai ser enviada
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.safe_substitute(nome='Diego', data= data_atual)

msg = MIMEMultipart()
msg['from']= 'Diego Carlos da Silva'
msg['to']= 'dcarloss111@gmail.com' #esse será o e-mail destino
msg['subject']= 'Atenção: este é um e-mail de teste'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)
print(meu_email)
print(minha_senha)


with smtplib.SMTP(host='smtp.live.com', port=25) as smtp:
# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('diego_carlos110@hotmail.com', 'Tirocerto111')
    smtp.send_message(msg)
    print('E-mail enviado com sucesso')
    '''

from string import Template
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

meu_email = 'jastoriomanote@gmail.com'
minha_senha = 'Tirocerto111'

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Luiz Otávio', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Diego'
msg['to'] = 'diego_carlos110@hotmail.com'  # Cliente
msg['subject'] = 'Atenção: este é um e-mail de teste'

corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

# ENVIO DE IMAGEM EM ANEXO
# with open('IMAGEM.JPG', 'rb') as img:
#     img = MIMEImage(img.read())
#     msg.attach(img)

with smtplib.SMTP(host='smtp.live.com', port=25) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso.')
    except Exception as e:
        print('E-mail não enviado...')
        print('Erro:', e)

