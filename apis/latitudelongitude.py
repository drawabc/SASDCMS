# author: Jason
# come look for me if there's something wrong with this portion of code

import requests
import googlemaps
#import pprint

def get_latlng(postal_code):
    """Return a dictionary in the format {"lat" : latitude_string, "lng" : longitude_string}"""

    latitude_longitude = {"lat" : "NA", "lng" : "NA"}
    
    if postal_code == -1:
        return latitude_longitude
    # get lat lng using onemap
    latitude_longitude = get_latlng_onemap(postal_code)

    # if onemap fails, try google geocode        
    """
    if latitude_longitude["lat"] == "NA":
        geocode_result = get_latlng_geocode(postal_code)
        if geocode_result is None:
            return latitude_longitude
        else:
            latitude_longitude["lat"] = str(geocode_result["lat"])
            latitude_longitude["lng"] = str(geocode_result["lng"])
    # if google geocode fails, I don't know what to do anymore
    """
    #print(type(latitude_longitude["lat"]))
    #print(latitude_longitude, postal_code) # helpful for tracing
    return latitude_longitude


def get_latlng_onemap(postal_code):
    
    latitude_longitude = {"lat" : "NA", "lng" : "NA"} #repetition of code
    
    # refer to OneMap API documentation for format
    response = requests.get("https://developers.onemap.sg/commonapi/search?searchVal=" +
                               postal_code + "&returnGeom=Y&getAddrDetails=Y")
        
    if response.status_code == 200:
        
        response_data = response.json()

        if response_data["found"] != 0:
            latitude_longitude["lat"] = response_data["results"][0]["LATITUDE"]                
            latitude_longitude["lng"] = response_data["results"][0]["LONGITUDE"]

    return latitude_longitude            


# https://github.com/googlemaps/google-maps-services-python/blob/master/googlemaps/geocoding.py
def get_latlng_geocode(postal_code):
    
    # pls don't abuse my API key
    gmaps = googlemaps.Client(key="AIzaSyCyOZQvPbapvjmUYcqUawu00vM8Ob1R5xE") 

    geocode_result = gmaps.geocode(components = {"country" : "SG", "postal_code" : postal_code})
    try:
        return geocode_result[0]["geometry"]["location"]
    except:
        return {"lat" : "NA", "lng" : "NA"}

    
#test = get_latlng("636959")

#for element in test:
#    print(element)

#test = get_latlng_geocode("636959")

#pp = pprint.PrettyPrinter()
#pp.pprint(test)


