# *****************************************************
# weather_lab03a.py - Adding low temperature logic
# *****************************************************

# Import SenseHat from the SenseHat Emulator library
# and sleep from the time library
from sense_emu import SenseHat
from time import sleep

# Instantiate (create) a variable to access the SenseHat Emulator
sense = SenseHat()

# Define the number of readings to take
maxReadings = 10

# Define a counter. In programming, most counters begin at 0
counter = 0

# Create two variables to hold the high and low temperatures
highTemp = 0.00
lowTemp = 999.00 # Why set it to 999?

# Print a header
print("#, Temperature, Pressure, Humidity, High Temp, Low Temp")

# This while loop will execute NUM_READINGS times
while counter < maxReadings:

    # Read temperature, humidity and pressure into local variables
    temperature = sense.temperature
    humidity = sense.humidity
    pressure = sense.pressure

    if temperature > highTemp:
        highTemp = temperature

    if temperature < lowTemp:
        lowTemp = temperature
        
    # Print the data to the screen separated by commas
    print(counter,",",temperature,",",pressure,",",humidity,",",highTemp,",",lowTemp)

    # Sleep for 5 seconds
    sleep(5)

    #Increment the loop counter
    counter = counter + 1

# The following line is not indented, so it will run after the loop finishes.
print("Finished with the loop!")
