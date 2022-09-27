
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

try:
   
    fromaddr = "python.ujb@gmail.com"
    toaddr1 = 'fillypi.monteiro@unijaguaribe.edu.br'
    toaddr2 = 'fillypi08@gmail.com'
    msg = MIMEMultipart()

    msg['From'] = fromaddr 
    msg['To'] = toaddr1
    msg['To'] = toaddr2
    msg['Subject'] = "Teste de envio de email"
    
    lista = [toaddr1, toaddr2]
    body = "\n ARYSTON ATIRADOR"

    msg.attach(MIMEText(body, 'plain'))

    # filename = 'teste.pdf'

    # attachment = open('teste.pdf','rb')


    # part = MIMEBase('application', 'octet-stream')
    # part.set_payload((attachment).read())
    # encoders.encode_base64(part)
    # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # msg.attach(part)

    # attachment.close()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "ylspgkyfaqefxfbx")
    text = msg.as_string()
    server.sendmail(fromaddr, lista, text)
    server.quit()
    print('\nEmail enviado com sucesso!')
except:
    print("\nErro ao enviar email")