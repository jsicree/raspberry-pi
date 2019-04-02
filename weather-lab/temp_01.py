# ***************************************
# weather_lab03.py - Loops and sleep
# ***************************************

# Import SenseHat from the SenseHat Emulator library
from sense_emu import SenseHat

# Import the sleep function from the time library
from time import sleep

sense = SenseHat()

print("Temperature, Pressure, Humidity")

while True:
    temperature = sense.temperature
    humidity = sense.humidity
    pressure = sense.pressure
    print(temperature,",",pressure,",",humidity)
    sleep(5)

