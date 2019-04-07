from twilio.rest import Client
import json
from shapely.geometry import shape, Point
import requests
import googlemaps

class PointLocater(object):
    def __init__(self):
        with open('map.geojson') as f:
            self.map = json.load(f)
    def getRegionName(self, latlng):
        point = Point(latlng["lng"],latlng["lat"])
        for feature in self.map['features']:
            polygon = shape(feature['geometry'])
            if polygon.contains(point):
                return(feature['properties']['Region Name'])
        return None

def get_latlng(postal_code):
    """Return a dictionary in the format {"lat" : latitude_string, "lng" : longitude_string}"""

    latitude_longitude = {"lat" : "NA", "lng" : "NA"}
    
    if postal_code == -1:
        return latitude_longitude
    # get lat lng using onemap
    latitude_longitude = get_latlng_onemap(postal_code)
    return latitude_longitude


def get_latlng_onemap(postal_code):
    
    latitude_longitude = {"lat" : "NA", "lng" : "NA"} #repetition of code
    
    # refer to OneMap API documentation for format
    response = requests.get("https://developers.onemap.sg/commonapi/search?searchVal=" +
                               postal_code + "&returnGeom=Y&getAddrDetails=Y")
        
    if response.status_code == 200:
        
        response_data = response.json()

        if response_data["found"] != 0:
            latitude_longitude["lat"] = float(response_data["results"][0]["LATITUDE"])                
            latitude_longitude["lng"] = float(response_data["results"][0]["LONGITUDE"])

    return latitude_longitude
  
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
                      + "\n" + "Sent from CMS"
            self.sendSMS(message, sender, receivers)
            return True
        except:
            return False

    def sendSMSToRegion(self, django_dict, sender, receivers_region):
        try:
            subject = "\nCaution! Emergency occured of type: " + django_dict['Type']
            description = "Description: " + django_dict['Description']
            message = subject + "\n" + description
            self.sendSMS(message, sender, receivers_region)
            return True
        except:
            return False
        
        
if __name__ == "__main__":
    sender = '+12052939421'
    receiverAgency = ['+6584012250']
    django_dict = {'Type': "Gas Leak", "Description":"This is a description",
"Location":"Pasir Ris", "name": "Tan Jun En", "mobile": "+6596579895","postal":"650394"}
    #Imagine receivers phone number in a particular region e.g. North
    receiver_region = {"WEST":"+6591746880","CENTRAL":"+6586502577","EAST":"+6598835026","NORTH":"+6582965839","NORTH-EAST":"+6591746880",}
    region = PointLocater().getRegionName(get_latlng(django_dict["postal"]))
    print(SMSAPI().sendFormattedSMS(django_dict, sender, receiverAgency))
    print(SMSAPI().sendSMSToRegion(django_dict, sender, receiver_region[region]))
