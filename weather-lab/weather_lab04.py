# *****************************************************
# weather_lab04.py - More loops and if-then statements
# *****************************************************

# Import SenseHat from the SenseHat Emulator library
from sense_emu import SenseHat

# Import the sleep function from the time library
from time import sleep

# Instantiate (create) a variable to access the SenseHat Emulator
sense = SenseHat()

# Define the number of readings to take
maxReadings = 10

# Define a counter. In programming, most counters begin at 0
counter = 0

# Create a variable to hold the high temperature
highTemp = 0.00

# Print a header
print("#, Temperature, Pressure, Humidity, High Temp")

# This while loop will execute the indented lines under it
# forever or until you press Ctrl-C
while counter < maxReadings:

    # Read temperature, humidity and pressure into local variables
    temperature = sense.temperature
    humidity = sense.humidity
    pressure = sense.pressure

    # If the temperature is greater than the current high temp,
    # set the high temp to that value
    if temperature > highTemp:
        highTemp = temperature
        
    # Print the data to the screen separated by commas
    print(counter,",",temperature,",",pressure,",",humidity,",",highTemp)

    # Sleep for 5 seconds
    sleep(5)

    #Increment the loop counter
    counter = counter + 1
    
