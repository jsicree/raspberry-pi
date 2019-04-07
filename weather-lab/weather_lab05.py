# *******************************************************
# weather_lab05.py - The Internet of Things!!
# *******************************************************

# Import SenseHat from the SenseHat Emulator library
# and the sleep function from the time library
from sense_emu import SenseHat
from time import sleep

from weather_tools import WeatherServiceAdapter

# The station id
STATION_ID = "WJOE" 

# The station location. The WeatherServiceAdapter defines a number of locations to choose from
MY_LOCATION = WeatherServiceAdapter.STATION_LOC_BHS_FOOTBALL

# Create a variable to access the SenseHat Emulator
sense = SenseHat()

# Create a variable to access the WeatherServiceAdapter, which
# will allow you to send weather data to the weather dashboard
weather_service = WeatherServiceAdapter()

print("My weather station id: ", STATION_ID)
print("My weather station location: ", weather_service.getStationLocation(MY_LOCATION)

# Print a header
print("#, Temperature, Pressure, Humidity")

# Loop continuously
while True:
    # Read temperature, humidity and pressure into local variables
    temperature = sense.temperature
    humidity = sense.humidity
    pressure = sense.pressure

    # Print the data to the screen separated by commas
    print(STATION_ID,",",temperature,",",pressure,",",humidity)

    weather_service.sendReading(STATION_ID, MY_LOCATION, temperature, pressure, humidity)
    
    # Sleep for 5 seconds
    sleep(5)


