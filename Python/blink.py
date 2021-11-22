import RPi.GPIO as GPIO #imports easier way to talk to pins
from time import sleep #imports the ability to have it slow down for a period
GPIO.setmode(GPIO.BCM) #sets the numbering of pins on cobbler correctly
GPIO.setup(21, GPIO.OUT) #sets pin 21 as an output
GPIO.setup(12, GPIO.OUT) 
def goLed(x,y,):
	GPIO.output(21,x) #sets the status of the pin as either having a high status (led is on) or low status (led is off)
	if x == 1:
		print("green on!")
	GPIO.output(12,y) #does the same with the other pin
	if y == 1:
		print("red on!")
	sleep(.25)
while True:
	goLed(1,0)
	goLed(0,1)
