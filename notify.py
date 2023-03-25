import requests
import smtplib
import time

url = 'http://pedddesc.tecnm.mx/'

email_address = 'mymail@mydomain.com'
email_password = 'mypassword'
recipient_address = 'recipient@domain.com'

def check_site(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("ONLINE - ENVIANDO CORREO DE NOTIFICACIÓN")
            return True
        else:
            print("OFFLINE - VERIFICAR EN 10 MINUTOS")
            return False
    except:
        print("EXCEPCIÓN, TARDANZA EN RESPUESTA, QUIZÁ OFFLINE - VERIFICAR EN 10 MINUTOS")
        return False

def send_email():
    with smtplib.SMTP('smtp-mail.outlook.com', 587) as smtp:
        smtp.starttls()
        smtp.login(email_address, email_password)

        subject = 'La pagina PEDDDESC esta en linea'
        body = f'La pagina de EDD esta en linea, sube rapidamente tus documentos antes que se vuelva a caer'

        message = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(email_address, recipient_address, message)
        print("Mensaje Enviado")

# Ejecuta la comprobación cada 10 minutos y envía un correo electrónico si la página está en línea
while True:
    if check_site(url):
        send_email()
    time.sleep(600) # espera 10 minutos antes de volver a verificar la página
