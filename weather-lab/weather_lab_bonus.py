# *****************************************
# bonus_lab.py - A bonus lab that reads the
# humidity value from the emulator and then
# sets the 8x8 LED display accordingly.
# This example can be found in the Sense
# HAT Emulator application along with other
# examples.
# *****************************************
from sense_emu import SenseHat

sense = SenseHat()

# Define the LED colors (RGB values)
GREEN = (0,255,0)
WHITE = (255,255,255)

while True:
    # Read the humidity
    humidity = sense.humidity

    # Convert the humidity values from
    # a percent to a value from 0 to 64
    humidity_value = 64 * humidity / 100

    # Set the pixels with values less than
    # the humidity values GREEN, or else WHITE
    pixels = [
        GREEN if i < humidity_value else WHITE for i in range(64)]

    # Set the pixel array on the emulator
    sense.set_pixels(pixels)

