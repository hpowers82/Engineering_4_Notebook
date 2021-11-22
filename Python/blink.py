import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
def goLed(x,y):
	GPIO.output(21,x)
	GPIO.output(12,y)
	if  x == 1:
		print("green on!")
	elif y == 1:
		print("red on!")
	sleep(.25)
while True:
	goLed(1,0)
	print("green on!")
	goLed(0,1)
	print("red on!")
