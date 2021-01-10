#Temperature and Humity project using a DHT22 sensor
#Created: January 10, 2021

import Adafruit_DHT
import time

#Defines sensor object
DHT_SENSOR = Adafruit_DHT.DHT22
#Defines GPIO pin that we are using
DHT_PIN = 4

def run_it():
    #create infinite loop (gathering ALL the data)
    while True:
        #caputure current temp and humi
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        #checking to see if it worked
        if humidity is not None and temperature is not None:
            #if it did work it will print temp and humi to screen
            print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
        else:
            #if it didn't work, check your cabeling
            print("Sensor failure. Don't panic. Check wiring.");
        #DHT22 can only check temp and humi every second 
        #so waiting 3 sec before gathering more data
        time.sleep(3);
    
if __name__ == "__main__":
    run_it()
