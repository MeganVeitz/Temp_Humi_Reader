# Temperature and Humity project using a DHT22 sensor
# Created: January 10, 2021

#multiprocessing tool to run each sensor
#or 
#change run() and move the loop outside of the class 

import Adafruit_DHT
import time
import datetime

# gspread - looking into this library
# import json file - looking into this

# Defines sensor object
DHT_SENSOR = Adafruit_DHT.DHT22
# Defines GPIO pin that we are using
#DHT_PIN = 4

# create 2nd sensor

# making class to add additional sensor(s) later
class DHT22:
    # init method or constructor
    def __init__(self, name, pin):
        # instance variable
        self.name = name
        self.pin = pin

# Objects of DHT22 Class
# fridge_freezer = DHT22("freezer")
# chest = DHT22("chest")

    def run_it(self, time_sec=60):
        """
        time_sec is the time in seconds btwn temp/humi reading
        """
        # self.time_sec = 60
        # create infinite loop (gathering ALL the data)
        while True:
            # caputure current temp and humi
            humi, tempC = Adafruit_DHT.read(DHT_SENSOR, self.pin)
            dateTime = datetime.datetime.now()
            # checking to see if it worked
            if humi is not None and tempC is not None:
                # if working it will print temp and humi to screen
                print("Name is: {}".format(self.name))
                print("\tTemp= {0:0.1f} C \n\tHumidity= {1:0.1f}%".format(tempC, humi))
                # convert to F and display
                tempF = ((tempC * 1.8) + 32)
                print("\tTemp= {0:0.1f} F".format(tempF))
                # print current date and time
                print("\tDate and Time is {}\n".format(dateTime))
            else:
                # if not working, check your cabeling
                print("Sensor failure. Don't panic. Check wiring.")
    
            # DHT22 can only check temp and humi every second 
            time.sleep(time_sec)


if __name__ == "__main__":
    sensor1 = DHT22("table", 4)
    sensor1.run_it()

#    while True:
#        sensor1.run()
#        sensor2.run()
#        sleep
