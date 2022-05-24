import time
import adafruit_mpl3115a2
import board
from gpiozero import Servo

sensor = adafruit_mpl3115a2.MPL3115A2(i2c, address=0x60)
sensor.sealevel_pressure = 102250
i2c = board.I2C()
servo = Servo(18)

deflate = False

initialTime = time.time()
initialAlt = sensor.altitude

servo.max
altitudeRec[]
while True:
  altitude = sensor.altitude
  temperature = sensor.temperature
  pressure = sensor.pressure
  altitudeRec.append(sensor.altitude)
  if altitude >= initialAlt + 20 and deflate = False:
    servo.min
    deflate = True
  elif altitude >= initialAlt + 20 and deflate = True:
    time.sleep(3)
  if deflate = True and max(altitudeRec) 
    
    
  
