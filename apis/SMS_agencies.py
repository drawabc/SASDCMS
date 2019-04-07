#This is used when a report is being made by emergencies
#Concurrently sent to this script when updating database

#Example report
#Name, Mobile, Location, Postal_code, Type, Time
# Taking example of report = {Name:'tan jun en', mobile:'+12565769037',
# location:'Pasir Ris', Postal_code: '510181', Type: 'EA', Time: '23:59'}

import Facade_API
import latitudelongitude

class SMSToAgency(object):
    def __init__(self):
        self.api = Facade_API.FacadeAPI()
        #Caution: Dummy Values!
        self.emergency_mapping_num = {
            'EA' : '+6596579895',
            'RE' : '+6596579895',
            'FF' : '+6596579895',
            'GL' : '+6596579895'
            }
        self.emergency_type = {
            'EA' : 'Ambulance',
            'RE' : 'Rescue and Evacuation',
            'FF' : 'Fire Fighting',
            'GL' : 'Gas Leak Control'
            }
    def sendSMS(self, report):
        sender_phone_num = str(report['mobile'])
        receiver_phone_num = str(self.emergency_mapping_num[report['Type']])
        def draftSMS(report):
            time = str(report['Time'])
            name = str(report['Name'])
            postal_code = str(report['Postal_code'])
            Coord = latitudelongitude.get_latlng(postal_code)
            emergency_type = self.emergency_type[report['Type']]
            return name + " reported on " + time + " requiring the service of the following agency: " + \
                   emergency_type + " at the following location: lat: " + Coord['lat'] + \
                   " lng: " + Coord['lng'] + " with the postal code: " + postal_code
        message = draftSMS(report)
        #Replace this with the commented return message after the API is done
        #return message + "\nsender: " + sender_phone_num + " receiver: " + receiver_phone_num
        return self.api.sendSMS(message, sender_phone_num, receiver_phone_num)

if __name__ == "__main__":
    report = {'Name':'tan jun en', 'mobile':'+12565769037',\
              'location':'Pasir Ris', 'Postal_code': '510181', 'Type': 'EA', 'Time': "23:59"}
    smsEmergency = SMSToAgency()
    print(smsEmergency.sendSMS(report))


"""
OUTPUT:

{'lng': '103.960572120493', 'lat': '1.36439754319682'} 510181
tan jun en reported on 23:59 requiring the service of the following agency: Ambulance at the following location: lat: 1.36439754319682 lng: 103.960572120493 with the postal code: 510181
sender: +12565769037 receiver: 929
"""
