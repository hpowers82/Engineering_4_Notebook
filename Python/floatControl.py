import time
import adafruit_mpl3115a2
import board
from gpiozero import Servo, Button
import os
import picamera


sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60)
sensor.sealevel_pressure = 102250
i2c = board.I2C()
servo = Servo(18)
directory = "../pictures"
initialTime = time.time()
camera = picamera.PiCamera()
camera.resolution = (1024, 768)
camera.start_preview()

servo.max # makes sure that the servo is in place
altitudeRec[]
tempratureRec[]
pressureRec[]

while True:
  altitude = sensor.altitude
  temperature = sensor.temperature
  pressure = sensor.pressure
  altitudeRec.append(sensor.altitude)
  tempratureRec.append(sensor.temprature)
  pressureRec.append(sensor.pressure) # records data
  if altitudeRec[-1] >= altitudeRec[0] + 20 or time.time() < initialTime: # defines the maximum altitude, and deflates the variable balloon once it reaches it.
    camera.capture('../pictures/image + '.jpg')
    servo.min

    
  
