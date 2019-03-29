from sense_emu import SenseHat
import time

sense = SenseHat()

print("Temp,Pressure,Humidity")

while True:
    temperature = sense.temperature
    humidity = sense.humidity
    pressure = sense.pressure
    print(temperature,",",pressure,",",humidity)
    time.sleep(5)

