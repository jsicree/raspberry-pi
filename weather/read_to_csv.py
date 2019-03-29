from sense_emu import SenseHat
import time

sense = SenseHat()

print("Temp,Pressure,Humidity")

readingList = []

i = 0;

while i < 4:
    temperature = sense.temperature
    humidity = sense.humidity
    pressure = sense.pressure
    reading = (temperature, humidity, pressure)
    readingList.append(reading)
    print(i,": ",reading)
    time.sleep(5)
    i += 1
    
for reading in readingList:
    print(reading)

    
