from gpiozero import Servo
from time import sleep
servo = Servo(18)

servo.min()
sleep(1)
servo.mid()
sleep(1)
servo.max()
sleep(1)
