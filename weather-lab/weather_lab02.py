# *********************************************
# weather_lab02.py - Introducing the SenseHat
# *********************************************

# Import SenseHat from the SenseHat Emulator library
# Also, import the time library
from sense_emu import SenseHat
import time

# Instantiate (create) a variable that represents the SenseHat 
sense = SenseHat()

# Print a header line  
print("Temperature, Pressure, Humidity")

# Get the current values from the SenseHat Emulator
temperature = sense.temperature
humidity = sense.humidity
pressure = sense.pressure

# Print the data to the screen
print(temperature,",",pressure,",",humidity)

