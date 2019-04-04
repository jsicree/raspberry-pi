# *******************************************************
# weather_lab06.py - The Internet of Things!!
# *******************************************************

# Import SenseHat from the SenseHat Emulator library
from sense_emu import SenseHat

# Import the sleep function from the time library
from time import sleep

# Import a JSON library to create the message
import json

# Import the requests library to handle the web service call
import requests

# Import datetime to format the timestamp
import datetime


# The URL of the RESTful Web Service
WEATHER_URL = "https://jvypfbgwl0.execute-api.us-east-1.amazonaws.com/default/weatherGateway" 

# Request headers indicating that the request will be JSON
WEATHER_REQ_HEADERS = {'Content-type': 'application/json'}

# The remote station latitude and longitude
STATION_LAT_LON = "40.715, -74.011"

# The station id
STATION_ID = "WJOE" 

# The readingDate date and time format
READING_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S"

# *****************************************************
# A Python function to send weather data to a RESTful
# web service. 
# *****************************************************
def sendReading(readingDateStr, temperature, pressure, humidity):

    # Get the current date and time
    now = datetime.datetime.now()
    
    # Define a structure containing the weather data.
    # This is an example of a type of structure called a dict.
    # It consists of a set of name/value pairs
    req = {
        "stationId" : STATION_ID,
        "temperature" : temperature,
        "pressure" : pressure,
        "humidity" : humidity,
        "readingDate" : readingDateStr,
        "location" : STATION_LAT_LON
    }

    # Convert the dict to JSON.
    data_json = json.dumps(req)

    # Print the JSON request    
    #print("REST request (JSON):", data_json)
    
    # Do a HTTP POST request using the predefined URL and headers, plus
    # the JSON data structure
    response = requests.post(WEATHER_URL, data=data_json, headers=WEATHER_REQ_HEADERS)    
    
    # Print the JSON response
    #print("REST response (JSON):", response.text)


# Instantiate (create) a variable to access the SenseHat Emulator
sense = SenseHat()

# Print a header
print("#, Temperature, Pressure, Humidity")

while True:

    # Get the current date and time
    now = datetime.datetime.now()
    readingDateString = now.strftime(READING_DATE_FORMAT)

    # Read temperature, humidity and pressure into local variables
    temperature = sense.temperature
    humidity = sense.humidity
    pressure = sense.pressure

    # Print the data to the screen separated by commas
    print(readingDateString,",",temperature,",",pressure,",",humidity)

    sendReading(readingDateString, temperature, pressure, humidity)
    
    # Sleep for 5 seconds
    sleep(5)


