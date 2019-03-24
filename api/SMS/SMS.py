from twilio.rest import Client

class SMSAPI:
    def __init__(self):
        self.account_sid ='ACde62fa9f53ae3ad3c59be0b5390c79ba'
        self.auth_token = '7aac14b03379f9ae4746f644c0a7059c'
    def sendSMS(self,textMessage, sender, receiver):
        try:
            client = Client(self.account_sid, self.auth_token)
            message = client.messages \
                .create(
                        body=textMessage,
                        from_=sender,
                        to=receiver
                        )
            print(message.sid)
            return "SMS sent"
        except:
            return "SMS failed to send"
        
if __name__ =='__main__':
    print(SMSAPI().sendSMS("this is a test message",'+12565769037','+6583676240'))
