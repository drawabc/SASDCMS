from CMSApp.api.Email import email
from CMSApp.api.Haze import Haze1
from CMSApp.api.Dengue import dengue_api
from CMSApp.api.sms import SMS
from CMSApp.api.Twitter import twitter
from CMSApp.api.Telegram import telegram_api
#import random

class FacadeAPI(object):
    def __init__(self):
        self.haze = Haze1.HazeAPI()
        self.dengue = dengue_api.Dengue()
        self.SMS = SMS.SMSAPI()
        self.twitter = twitter.TwitterAPI()
        self.email = email.EmailSend()
        self.server = email.EmailSend.startServer()
        self.telegram_api = telegram_api.TelegramAPI()
        
    def getHaze(self):
        return self.haze.getJSON()
    
    def getDengue(self):
        self.dengue_data = self.dengue.get_polygon_data()
        return self.dengue_data
    
    def saveDengue(self,title='dengue_location.json'):
        if self.dengue_data != None:
            return self.dengue.write_json_file(title)
        
    def sendSMS(self,textMessage, sender, receiver):
        return self.SMS.sendSMS(textMessage, sender, receiver)
    
    def sendTwitter(self,message):
        return self.twitter.sendTweet(message)
    
    def sendEmail(self, recipient, msg, subject):
        return self.email.send_email(self.server,recipient,msg,subject)
    def sendTelegram(self,message):
        return self.telegram_api.sendTelegramMessage(message)
if __name__ == "__main__":
    API = FacadeAPI()

    #Get the JSON for haze
    #print(API.getHaze())

    #Get the JSON for dengue
    #print(API.getDengue())

    #Save the JSON file for dengue
    # print(API.saveDengue('dengue_location.json'))

    #Sending SMS
    print(API.sendSMS("this is a test message",'+12565769037','+65 9657 9895'))

    #Sending Tweet
    #print(API.sendTwitter("This is a test Message"))

    #Sending Email
#print(API.sendEmail(['rainscindo@gmail.com'], "Greetings","Subject Title"))

    #Sending message on telegram
    print(API.sendTelegram('This is a test message'))
