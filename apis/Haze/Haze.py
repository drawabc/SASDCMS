import json
import urllib.request as ur
import pprint

class HazeAPI:   
    def getJSON(self):
        url = "https://api.data.gov.sg/v1/environment/psi"
        url_parser = ur.urlopen(ur.Request(url))
        json_object = url_parser.read()
        json_dict = json.loads(json_object.decode('utf-8'))
        air_status = json_dict['api_info']['status']
        timestamp = json_dict['items'][0]['update_timestamp']
        psi_readings = json_dict['items'][0]['readings']['psi_twenty_four_hourly']
        pm25 = json_dict['items'][0]['readings']['pm25_twenty_four_hourly']
        location = {}
        json_returner = {}
        for item in json_dict['region_metadata']:
            location[item['name']] = item['label_location']
        json_returner['air_status'] = air_status
        json_returner['timestamp'] = timestamp
        json_returner['psi'] = psi_readings
        json_returner['pm25'] = pm25
        json_returner['location'] = location
        return json_returner
