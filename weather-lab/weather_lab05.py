# *******************************************************
# weather_lab05.py - Visualizing results with matplotlib
# *******************************************************

# Import SenseHat from the SenseHat Emulator library
from sense_emu import SenseHat

# Import the sleep function from the time library
from time import sleep

# Import the matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Define the text labels for the graph
TEMP_PLOT_TITLE = "Temperature"
TEMP_PLOT_XLABEL = "Reading"
TEMP_PLOT_YLABEL = "Temperature (C)"

# Define the number of readings to take
NUM_READINGS = 10

# Instantiate (create) a variable to access the SenseHat Emulator
sense = SenseHat()

# ********************************
# A function to plot an array of
# temperature values
# ********************************
def plotTemperature(temperatureArray):
    plt.title(TEMP_PLOT_TITLE)
    plt.xlabel(TEMP_PLOT_XLABEL)
    plt.ylabel(TEMP_PLOT_YLABEL)
    plt.plot(temperatureArray)
    plt.show()

# Define a counter. In programming, most counters begin at 0
counter = 0

# Create an array to hold temperature values to plot
tempArray = []

# Print a header
print("#, Temperature, Pressure, Humidity")

# This while loop will execute NUM_READINGS times
while counter < NUM_READINGS:

    # Read temperature, humidity and pressure into local variables
    temperature = sense.temperature
    humidity = sense.humidity
    pressure = sense.pressure

    # Add the current temperature to the temperature array
    tempArray.append(temperature)            
    # Print the data to the screen separated by commas
    print(counter,",",temperature,",",pressure,",",humidity)

    # Sleep for 5 seconds
    sleep(5)

    #Increment the loop counter
    counter = counter + 1

# Call the plotTemperature() function to graph the data    
plotTemperature(tempArray)
