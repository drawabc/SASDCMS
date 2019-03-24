import smtplib
import traceback

class EmailSend:
    def __init__(self, username = "cmshelp10@gmail.com", password = "US@123454321"):
        self.username= username 
        self.password = password
        
    def send_email(self, server, recipient, msg, subject):
        try:
            server.login(self.username, self.password)
            message = 'Subject: {}\n\n{}'.format(subject, msg)
            for m in recipient:
                server.sendmail(self.username, m, message)
            return "Sucess: Email sent!"
        except Exception:
            traceback.print_exc()
            return "Email failed to send"

    def startServer(self):
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        return server

    def quitServer(self, server):
        server.quit()



if __name__ =='__main__':
    recipient = ['rainscindo@gmail.com']
    subject= "Test"
    msg= "Hi!"

    server = EmailSend.startServer()

    mail = EmailSend()
    mail.send_email(server, recipient, msg, subject)
    
    EmailSend.quitServer(server)
