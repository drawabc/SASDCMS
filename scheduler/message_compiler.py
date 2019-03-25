from api.Email.email import EmailSend

def send_report():
    print("ASDAFSFA")
    e = EmailSend()
    server = e.startServer()
    print(e.send_email(server, ['echristo001@e.ntu.edu.sg'], 'this is report', 'CMS Updates'))
    e.quitServer(server)

