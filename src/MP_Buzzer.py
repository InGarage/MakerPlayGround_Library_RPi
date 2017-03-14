import grovepi
import time
from grovepi import *



class MP_buzzer:	
        
	def __init__(self,pin):
                global buzzer
                buzzer = pin
               
		grovepi.pinMode(buzzer,"OUTPUT")
		

	def beep(self,percentage,dur):
		grovepi.analogWrite(buzzer,int(255*(percentage/100.0)))
		time.sleep(dur/1000.0)
