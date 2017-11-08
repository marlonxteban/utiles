"""
Probado con GMAIL con puerto 465 smtpserver smtp.gmail.com, probado con outlook puerto 587 smtpserver smtp.office365.com
"""
#from smtplib import SMTP_SSL as SMTP # esta es la opcion correcta para gmail, comentar esta linea para outlook.com, el servidor smtp de outlook.com es smtp.office365.com
from smtplib import SMTP #esta es la opcion correcta para outlook, comentar para gmail
import logging
import logging.handlers
import sys
from email.mime.text import MIMEText

def enviar_mail():
    text = '''
    Hello,

    Here is your test email.

    saludos
    '''
    print("texto listo")        
    msg = MIMEText(text, 'plain')
    msg['Subject'] = "test email"
    print("asunto listo") 
    me ='xxx@outlook.com'
    msg['To'] = 'xxx@gmail.com'
    print("de, para --> listos")
    puerto_smtp=587 #outlook 587, gmail 465
    usuario = 'xxx@outlook.com'
    password = 'xxx'
    try:
        print("intentando conectar")
        conn = SMTP('smtp.office365.com', puerto_smtp)
        conn.ehlo() #solo para outlook
        conn.starttls()  # solo para outlook
        conn.ehlo() #solo para outlook
        print("conexion exitosa")
        conn.set_debuglevel(True)
        print("autenticando")
        conn.login(usuario, password)
        try:
            print("intentando enviar mail")
            conn.sendmail(me, msg['To'], msg.as_string())
            print('mail enviado')
        finally:
            conn.close()

    except Exception as exc:
        print("error")
        logger.error("ERROR!!!")
        logger.critical(exc)
        sys.exit("Mail failed: {}".format(exc))


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    enviar = True

    if enviar:
        print("inicia proceso")
        enviar_mail()