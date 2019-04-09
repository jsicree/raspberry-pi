# *******************************************************
# weather_lab05.py - The Internet of Things!!
# *******************************************************

# Import SenseHat from the SenseHat Emulator library
# and the sleep function from the time library
from sense_emu import SenseHat
from time import sleep

# Import the WeatherServiceAdapter from our own weather_tools library
from weather_tools import WeatherServiceAdapter

# Define the sleep time in seconds
SLEEP_TIME_S = 5

# The station id
MY_STATION_ID = "WJOE" 

# Create a variable to access the SenseHat Emulator
sense = SenseHat()

# Create a variable to access the WeatherServiceAdapter, which
# will allow you to send weather data to the weather dashboard
weather_service = WeatherServiceAdapter()


# The station location id. Please ask your instructor for the
# id you should use for this lab.
my_location_id = WeatherServiceAdapter.STATION_LOC_BURLINGTON

# The station location. The WeatherServiceAdapter defines a number of locations to choose from
my_station_location = weather_service.getStationLocation(my_location_id)

# Print information about the weather station
print("My weather station id: ", MY_STATION_ID)
print("My weather station location: ", my_station_location)

# Print a header
print("#, Temperature, Pressure, Humidity")

# Loop continuously
while True:
    # Read temperature, humidity and pressure into local variables
    temperature = sense.temperature
    humidity = sense.humidity
    pressure = sense.pressure

    # Print the data to the screen separated by commas
    print(MY_STATION_ID,",",temperature,",",pressure,",",humidity)

    # Call the sendReading() function of our WeatherAdapterService to
    # send our data to the data analysis dashboard on AWS
    weather_service.sendReading(MY_STATION_ID, my_station_location, temperature, pressure, humidity)
    
    # Sleep for 5 seconds
    sleep(SLEEP_TIME_S)


