import grovepi

class MP_AnalogRead:	
        
	def __init__(self,pin):
                global potentiometer
                potentiometer = pin
               
		grovepi.pinMode(potentiometer,"INPUT")
		

	def analogRead(self,opt,treshold,unit):
		  try:
        # Read sensor value from potentiometer
			sensor_value = grovepi.analogRead(potentiometer)
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

