from email import encoders
from email.mime.base import MIMEBase
from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import  formatdate
import smtplib

from Emails.configuracion import datos_email


def enviarEmail(destinatarios=[], asunto="", mensaje="", archivos=[], is_html=False):
    msg = MIMEMultipart()
    msg['From'] = datos_email['usuario']
    msg['To'] = ", ".join(destinatarios)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = asunto
    if is_html:
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(mensaje)
    else:
        msg.attach(MIMEText(mensaje))
    if archivos:
        for path in archivos:
            part = MIMEBase('application', "octet-stream")
            with open(path, 'rb') as file:
                part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', 'attachment; filename="{}"'.format(Path(path).name))
                msg.attach(part)

    smtp = smtplib.SMTP(datos_email['servidor_smtp'], datos_email['puerto'])
    if datos_email['use_tls']:
        smtp.starttls()
    smtp.login(datos_email['usuario'], datos_email['password'])
    smtp.sendmail(datos_email['usuario'],destinatarios, msg.as_string())
    smtp.quit()

