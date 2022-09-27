import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def alerta_inicio():
    fromaddr = "python.ujb@gmail.com"
    toaddr1 = 'artur.souza955@gmail.com'
    toaddr2 = 'felipe.silva@unijaguaribe.edu.br'
    toaddr3 = 'fillypi.monteiro@unijaguaribe.edu.br'
    msg = MIMEMultipart()

    msg['From'] = fromaddr 
    msg['To'] = toaddr1
    msg['To'] = toaddr2
    msg['To'] = toaddr3 
    msg['Subject'] = "ALERTA"
    
    lista = [toaddr1, toaddr2, toaddr3]
    body = "\n O upload das biometrias foi iniciado"

    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "ylspgkyfaqefxfbx")
    text = msg.as_string()
    server.sendmail(fromaddr, lista, text)
    server.quit()
    print('\nEmail enviado com sucesso!')
