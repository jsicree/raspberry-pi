# *******************************************************
# weather_lab04.py - Visualizing results with matplotlib
# *******************************************************

# Import SenseHat from the SenseHat Emulator library
# and sleep from the time library
from sense_emu import SenseHat
from time import sleep

# Import the matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Define the text labels for the graph
TEMP_PLOT_TITLE = "Temperature"
TEMP_PLOT_YLABEL = "Temperature (C)"
PLOT_XLABEL = "Reading"

# Define the number of readings to take
NUM_READINGS = 10

# Define the sleep time in seconds
SLEEP_TIME_S = 5

# *************************************************
# A function to plot an array of temperature values
# *************************************************
def plotData(title, y_axis_label, dataArray):
    plt.title(title)
    plt.xlabel(PLOT_XLABEL)
    plt.ylabel(y_axis_label)
    plt.plot(dataArray)
    plt.show()

# Create a variable to access the SenseHat Emulator
sense = SenseHat()
    
# Define a counter. In programming, most counters begin at 0
counter = 0

# Create an array to hold temperature values to plot.
tempArray = []

# Print a header
print("#, Temperature, Pressure, Humidity")

# This while loop will execute NUM_READINGS times
while counter < NUM_READINGS:
    # Read temperature, humidity and pressure into local variables
    temperature = sense.temperature
    humidity = sense.humidity
    pressure = sense.pressure

    # Print the data to the screen separated by commas
    print(counter,",",temperature,",",pressure,",",humidity)

    # Add the current temperature to the end of the temperature array
    tempArray.append(temperature)            

    # Sleep for 5 seconds
    sleep(SLEEP_TIME_S)

    #Increment the loop counter
    counter = counter + 1

# Call the plotTemperature() function to graph the data    
plotData(TEMP_PLOT_TITLE, TEMP_PLOT_YLABEL, tempArray)
