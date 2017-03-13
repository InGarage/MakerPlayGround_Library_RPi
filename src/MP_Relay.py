import grovepi
from grovepi import *



class MP_Relay:	
        
	def __init__(self,pin):
                global relay
                relay = pin
               
		grovepi.pinMode(relay,"OUTPUT")
		

	def on(self):
		digitalWrite(relay,1)
	

	def off(self):
		digitalWrite(relay,0)

