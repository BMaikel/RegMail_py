import smtplib
from email.message import EmailMessage

class SendMail():
    def __init__(self):
        self.mensage = EmailMessage()
        self.server = smtplib.SMTP("smtp.gmail.com", '587')
    
    def definiendo_remitente(self, email_asunto, email_remitente, email_receptor):
        self.mensage['Subject'] = email_asunto 
        self.mensage['From'] = email_remitente
        self.mensage['To'] = email_receptor
    
    def contenido_correo(self, contenido):
        self.mensage.set_content(contenido)
    
    def enviando_correo(self, email_remitente, email_pass):
        try:
            self.server.ehlo()
            self.server.starttls()
            self.server.login(email_remitente, email_pass) 
            self.server.send_message(self.mensage)
            self.server.quit()

        except:
            raise

# email_asunto = "Prueba de correo electrónico desde Python uwu" 
# email_remitente = "20210824@lamolina.edu.pe"
# email_pass = "Tortugarte-26" 
# email_receptor = "alexis.michael147@gmail.com" 

# mensaje = SendMail()
# mensaje.definiendo_remitente(email_asunto, email_remitente, email_receptor)
# mensaje.contenido_correo("Buenos dias desde Python :3")
# mensaje.enviando_correo(email_remitente, email_pass, "Buenos dias desde Python :3")