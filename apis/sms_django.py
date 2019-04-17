from twilio.rest import Client
import json
import requests

class SMSAPI:
    def __init__(self):
        self.account_sid ='ACa81b7b9e04c7af554434a5709cbcb7d4'
        self.auth_token = '9843de1aba89dd24ca1eaada537154e8'
    def sendSMS(self, textMessage, sender, receiver):
        try:
            client = Client(self.account_sid, self.auth_token)
            message = client.messages \
                .create(
                        body=textMessage,
                        from_=sender,
                        to=receiver
                        )
            return "SMS sent"
        except:
            return "SMS failed to send"

    def sendFormattedSMS(self, django_dict, sender, receivers):
        """django_dict = {'Type': "Gas Leak", "Description":"This is a description",
"Location":"Pasir Ris", "name": "Tan Jun En", "mobile": "+6596579895","time": "timing",
"operator":"Mr operator"}"""
        try:
            subject = "\nURGENT! Request for " + django_dict['Type']
            description = "Description: " + django_dict['Description']
            location = "Location: " + django_dict['Location']
            message = subject + "\n" + description + "\n" +  location + \
                      "\n" + "Requestor Name: " + django_dict["name"] + "\n"\
                      + "Requestor Mobile: " + django_dict["mobile"] + \
                      "\n" + "Sent from CMS"
            self.sendSMS(message, sender, receivers)
            return True
        except Exception as error:
            return False
    
        
if __name__ == "__main__":
    sender = '+12052939421'
    receiverAgency = ['+6584012250']
    django_dict = {'Type': "Gas Leak", "Description":"This is a description",
"Location":"Pasir Ris", "name": "Tan Jun En", "mobile": "+6596579895","postal":"650394"}
    print(SMSAPI().sendFormattedSMS(django_dict, sender, receiverAgency))
    
