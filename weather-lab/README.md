### Welcome to the Weather Lab
The Weather Lab is a collection of Python programs that introduce some basic Python using the SenseHat emulator to create a remote weather station. These programs were written to be used in a STEM program for high school students.

### The Weather Lab Modules
1. `weather_lab01.py` - First Python program, variables, printing to the screen
1. `weather_lab02.py` - The SenseHat emulator, printing temperature, pressure and humidity to the screen
1. `weather_lab03.py` - While loops, if-then statements, sleep(x)
1. `weather_lab04.py` - Functions, graphing data with matplotlib
1. `weather_lab05.py` - The Internet of Things, sending data over the Internet
1. `weather_bonus.py` - Using the Sense HAT LED display

### Other Files
`weather_tools.py` - A helper library containing a WeatherServiceAdapter class which will send data to an AWS API Gateway. A preset set of locations (name, lat+lon) and the endpoint for the API Gateway are defined within this library for ease of use during the class.
`weather_data_gen.py` - A simple data generator that randomly selects from a set of predefined weather stations and sends data to the Weather Dashboard via the `weather_tools.py` library.
