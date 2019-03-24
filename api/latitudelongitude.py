import requests

def get_latlng(postal_code):
    """Return a dictionary in the format {"lat" : latitude_string, "lng" : longitude_string}"""

    latitude_longitude = {"lat" : "NA", "lng" : "NA"}
    
    if postal_code == -1:
        return latitude_longitude

    # refer to OneMap API documentation for format
    response = requests.get("https://developers.onemap.sg/commonapi/search?searchVal=" +
                               postal_code + "&returnGeom=Y&getAddrDetails=Y")
        
    if response.status_code == 200:
        
        response_data = response.json()

        if response_data["found"] != 0:
            latitude_longitude["lat"] = response_data["results"][0]["LATITUDE"]                
            latitude_longitude["lng"] = response_data["results"][0]["LONGITUDE"]

        else:
            pass
            
    else:
        pass

    print(latitude_longitude, postal_code)
    return latitude_longitude

#test = get_latitude_longitude("636959")

#for element in test:
#    print(element)
