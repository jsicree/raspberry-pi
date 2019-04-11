'''
Created on Apr 2, 2019

@author: joseph_sicree
'''
from weather_tools import WeatherServiceAdapter
import random 
from time import sleep

WS_ID_FIELD_NAME = "stationId"
WS_LOC_FIELD_NAME = "location"

weather_stations = [
    {
        "stationId" : "WAND",
        "location" :  WeatherServiceAdapter.STATION_LOC_ANDOVER
    },
    {
        "stationId" : "WARL",
        "location" :  WeatherServiceAdapter.STATION_LOC_ARLINGTON
    },
    {
        "stationId" : "WBED",
        "location" :  WeatherServiceAdapter.STATION_LOC_BEDFORD
    },
    {
        "stationId" : "WBIL",
        "location" :  WeatherServiceAdapter.STATION_LOC_BILLERICA
    },
    {
        "stationId" : "WBUR",
        "location" :  WeatherServiceAdapter.STATION_LOC_BURLINGTON
    },
    {
        "stationId" : "WCAR",
        "location" :  WeatherServiceAdapter.STATION_LOC_CARLISLE
    },
    {
        "stationId" : "WCON",
        "location" :  WeatherServiceAdapter.STATION_LOC_CONCORD
    },
    {
        "stationId" : "WLEX",
        "location" :  WeatherServiceAdapter.STATION_LOC_LEXINGTON
    },
    {
        "stationId" : "WLIN",
        "location" :  WeatherServiceAdapter.STATION_LOC_LINCOLN
    },
    {
        "stationId" : "WREA",
        "location" :  WeatherServiceAdapter.STATION_LOC_READING
    },
    {
        "stationId" : "WSUD",
        "location" :  WeatherServiceAdapter.STATION_LOC_SUDBURY
    },
    {
        "stationId" : "WWAL",
        "location" :  WeatherServiceAdapter.STATION_LOC_WALTHAM
    },
    {
        "stationId" : "WWIL",
        "location" :  WeatherServiceAdapter.STATION_LOC_WILMINGTON
    },
    {
        "stationId" : "WWOB",
        "location" :  WeatherServiceAdapter.STATION_LOC_WOBURN
    }
]    
    
    
weather_service = WeatherServiceAdapter()
    
while True:
    index = random.randint(0, len(weather_stations)-1)    
    name = weather_stations[index][WS_ID_FIELD_NAME]
    location = weather_service.getStationLocation(weather_stations[index][WS_LOC_FIELD_NAME])
    print("Weather Station ID: ", name)
    print("Weather Station Location: ", location)   
    weather_service.sendReading(name, location[WeatherServiceAdapter.LOC_COORDINATES], random.uniform(0.00, 20.00), random.uniform(900.00, 1100.00), random.uniform(30.00, 75.00))
    sleep(random.uniform(1, 2))

