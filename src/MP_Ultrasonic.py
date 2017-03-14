import grovepi

class MP_Ultrasonic:	
        
	def __init__(self,pin):
                global sensor
                sensor = pin
  

	def distance(self,opt,treshold,unit):
		  try:
			sensorRead = grovepi.ultrasonicRead(sensor)

			if(opt=='>='):
				if sensorRead >= treshold:
					return 1
				else:
					return 0
			elif(opt=='>'):
				if sensorRead > treshold:
					return 1
				else:
					return 0
			elif(opt=='='):
				if sensorRead == treshold:
					return 1
				else:
					return 0
			elif(opt=='<'):
				if sensorRead < treshold:
					return 1
				else:
					return 0
			elif(opt=='<='):
				if sensorRead <= treshold:
					return 1
				else:
					return 0
			elif(opt=='!='):
				if sensorRead != treshold:
					return 1
				else:
					return 0
	   	  except IOError:
			print ("Error")
