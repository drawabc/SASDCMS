#The socialMedia only outputs the changes in PSI for now.
from api import Facade_API

class SocialMedia(object):
    def __init__(self):
        self.API = Facade_API.FacadeAPI()
    def create_message(self,messages):
        if messages == None:
            haze_details = self.API.getHaze()
            air_status = haze_details['air_status']
            pm25 = haze_details['pm25']
            psi = haze_details['psi']
            psi_message = ""
            pm25_message = ""
            for k,v in psi.items():
                psi_message = psi_message + " "+ k + " - " + str(v)
            for k,v in pm25.items():
                pm25_message = pm25_message + " "+ k + " - " + str(v)
            return "The air quality is " + air_status + ".\nThe psi is: " + psi_message + ".\nThe pm25 is: " + pm25_message
        else:
            #Add stuff here
            return messages
    def sendSocialMedia(self,sender = '+12565769037',receiver_list = ['+6583676240','+6596579895'],extra_messages=None):
        #We can add additional details using extra_messages
        #Craft a message to send to all social medias

        message = self.create_message(extra_messages)
        #Sending to all social Medias
        for receiver in receiver_list:
           self.API.sendSMS(message, sender, receiver)
        self.API.sendTwitter(message)
        self.API.sendTelegram(message)
        
if __name__ == "__main__":
    socialMedia = SocialMedia()
    socialMedia.sendSocialMedia()
"""
OUTPUT:
The air quality is healthy.
The psi is:  national - 61 east - 57 south - 58 central - 61 west - 55 north - 52.
The pm25 is:  national - 21 east - 18 south - 18 central - 21 west - 15 north - 13
"""
