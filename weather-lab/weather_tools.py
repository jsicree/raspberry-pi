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
    STATION_LOC_ANDOVER = 0
    STATION_LOC_ARLINGTON = 1
    STATION_LOC_BEDFORD = 2
    STATION_LOC_BILLERICA = 3
    STATION_LOC_BURLINGTON = 4
    STATION_LOC_CARLISLE = 5
    STATION_LOC_CONCORD = 6
    STATION_LOC_LEXINGTON = 7
    STATION_LOC_LINCOLN = 8
    STATION_LOC_READING = 9
    STATION_LOC_SUDBURY = 10
    STATION_LOC_WALTHAM = 11
    STATION_LOC_WILMINGTON = 12
    STATION_LOC_WOBURN = 13
    

    STATION_LOCS = [
        {
            "name" : "Andover", 
            "coordinates" : {"lat":"42.657601","lon": "-71.137176"}
        },
        {
            "name" : "Arlington",             
            "coordinates" : {"lat":"42.415476","lon": "-71.156852"}
        },
        {
            "name" : "Bedford", 
            "coordinates" : {"lat":"42.491271","lon": "-71.277295"}
        },
        {
            "name" : "Billerica", 
            "coordinates" : {"lat":"42.558589","lon": "-71.266567"}
        },
        {
            "name" : "Burlington", 
            "coordinates" : {"lat" : "42.505847", "lon" : "-71.197943"}
        },
        {
            "name" : "Carlisle", 
            "coordinates" : {"lat":"42.529419","lon": "-71.350845"}
        },
        {
            "name" : "Concord", 
            "coordinates" : {"lat":"42.460651","lon": "-71.348319"}
        },
        {
            "name" : "Lexington", 
            "coordinates" : {"lat":"42.447786","lon": "-71.227149"}
        },
        {
            "name" : "Lincoln", 
            "coordinates" : {"lat":"42.425571","lon": "-71.304208"}
        },
        {
            "name" : "Reading", 
            "coordinates" : {"lat":"42.525809","lon": "-71.096574"}
        },
        {
            "name" : "Sudbury", 
            "coordinates" : {"lat":"42.383335","lon": "-71.409973"}
        },        
        {
            "name" : "Waltham", 
            "coordinates" : {"lat":"42.376546","lon": "-71.234717"}
        },
        {
            "name" : "Wilmington", 
            "coordinates" : {"lat" : "42.549984", "lon" : "-71.175003"}
        },
        {
            "name" : "Woburn", 
            "coordinates" : {"lat":"42.478974","lon": "-71.151339"}
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
    
