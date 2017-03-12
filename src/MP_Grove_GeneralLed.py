import grovepi
from grovepi import *



class MP_GeneralLed:	
        
	def __init__(self,pin):
                global led
                led = pin
               
		grovepi.pinMode(led,"OUTPUT")
		

	def on(self):
		digitalWrite(led,1)
	

	def off(self):
		digitalWrite(led,0)

	def dim(self,percentage):
		grovepi.analogWrite(led,int(255*(percentage/100.0)))
