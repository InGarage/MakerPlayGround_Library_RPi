import grovepi

class MP_SoundSensor:	
        
	def __init__(self,pin):
                global sensorRead
                sensorRead = pin
               
		grovepi.pinMode(sensorRead,"INPUT")
		

	def checkVol(self,opt,treshold,unit):
		  try:
        # Read sensor value from sensorRead
			sensor_value = grovepi.analogRead(sensorRead)
			percentage = round((float)(sensor_value) * 100 / 1023, 2)
			if(opt=='>='):
				if percentage >= treshold:
					return 1
				else:
					return 0
			elif(opt=='>'):
				if percentage > treshold:
					return 1
				else:
					return 0
			elif(opt=='='):
				if percentage == treshold:
					return 1
				else:
					return 0
			elif(opt=='<'):
				if percentage < treshold:
					return 1
				else:
					return 0
			elif(opt=='<='):
				if percentage <= treshold:
					return 1
				else:
					return 0
			elif(opt=='!='):
				if percentage != treshold:
					return 1
				else:
					return 0
	   	  except IOError:
			print ("Error")

