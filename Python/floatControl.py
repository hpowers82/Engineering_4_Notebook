import time
import adafruit_mpl3115a2
import board
from gpiozero import Servo, Button
import os
import picamera


sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60) 
sensor.sealevel_pressure = 102250
i2c = board.I2C()
servo = Servo(18) # servo pin is 18
directory = "../pictures" # will save photos in the picture folder
initialTime = time.time() # gets the time at which it launches
camera = picamera.PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

servo.max # makes sure that the servo is in place
altitudeRec[] 
tempratureRec[]
pressureRec[]
while True: 
  altitudeRec.append(sensor.altitude)
  tempratureRec.append(sensor.temprature)
  pressureRec.append(sensor.pressure) # records data into lists to be 
  if altitudeRec[-1] >= altitudeRec[0] + 20 or time.time() >= initialTime + 120: # defines the maximum altitude, and deflates the variable balloon once it reaches it.
    camera.capture('../pictures/image + '.jpg')
    servo.min

    
  
