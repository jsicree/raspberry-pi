'''
WeatherServiceAdapter 
@author: joseph_sicree
'''
import json
import requests
import datetime

class WeatherServiceAdapter(object):
    
    # Define some global variables 
    # The URL of the RESTful Web Service
    WEATHER_URL_ = "https://jvypfbgwl0.execute-api.us-east-1.amazonaws.com/default/weatherGateway" 
    # Request headers indicating that the request will be JSON
    WEATHER_REQ_HEADERS = {'Content-type': 'application/json'}

    LOC_NAME="name"
    LOC_COORDINATES="coordinates"

    # The remote station latitude and longitude
    STATION_LOC_REC_FIELDS = 0
    STATION_LOC_BHS_FOOTBALL = 1
    STATION_LOC_BURLINGTON_COMMON = 2
    STATION_LOC_SIMONDS_PARK = 3

    STATION_LOCS = [
        {
            "name" : "Burlington Rec Fields", 
            "coordinates" : "42.504514, -71.189193"
        },
        {
            "name" : "Burlington High School Football Field", 
            "coordinates" : "42.500309, -71.195582"
        },
        {
            "name" : "Burlington Town Common", 
            "coordinates" : "42.505434, -71.194981"
        },
        {
            "name" : "Burlington Simonds Park", 
            "coordinates" : "42.505579, -71.197056"
        }        
    ]

    # The readingDate date and time format
    READING_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"


    def sendReading(self, station_id, station_loc, temperature, pressure, humidity):
    
        # Get the current date and time
        now = datetime.datetime.now()
        
        # Define a structure containing the weather data.
        # This is an example of a type of structure called a dict.
        # It consists of a set of name/value pairs
        req = {
            "stationId" : station_id,
            "temperature" : temperature,
            "pressure" : pressure,
            "humidity" : humidity,
            "readingDate" : now.strftime(WeatherServiceAdapter.READING_DATE_FORMAT),
            "location" : station_loc
        }
    
        # Convert the dict to JSON.
        data_json = json.dumps(req)
    
        # Print the JSON request    
        print("REST request (JSON):", data_json)
        
        # Do a HTTP POST request using the predefined URL and headers, plus
        # the JSON data structure
        response = requests.post(WeatherServiceAdapter.WEATHER_URL_, data=data_json, headers=WeatherServiceAdapter.WEATHER_REQ_HEADERS)    
        
        # Print the JSON response
        print("REST response (JSON):", response.text)
    
    
    def getStationLocation(self, index):
        return WeatherServiceAdapter.STATION_LOCS[index]
    
    def getAllStationLocations(self):
        return WeatherServiceAdapter.STATION_LOCS