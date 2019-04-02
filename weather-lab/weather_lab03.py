# ********************************************
# weather_lab03.py - Infinite loops and sleep
# ********************************************

# Import SenseHat from the SenseHat Emulator library
from sense_emu import SenseHat

# Import the sleep function from the time library
from time import sleep

# Instantiate (create) a variable to access the SenseHat Emulator
sense = SenseHat()

# Print a header
print("Temperature, Pressure, Humidity")

# This while loop will execute the indented lines under it
# forever or until you press Ctrl-C
while True:

    # Read temperature, humidity and pressure into local variables
    temperature = sense.temperature
    humidity = sense.humidity
    pressure = sense.pressure

    # Print the data to the screen separated by commas
    print(temperature,",",pressure,",",humidity)

    # Sleep for 5 seconds
    sleep(5)

