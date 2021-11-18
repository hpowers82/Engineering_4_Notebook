import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
import board
GPIO setup(21, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
x=1
y=0
var=0
def flip(var,x,y):
	var=x
	x=y
	y=var

while True:
	GPIO.output(21, x)
	GPIO.output(12, x-y)
	flip(var,x,y)
	sleep(.25)
