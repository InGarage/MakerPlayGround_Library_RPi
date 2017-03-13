import grovepi
import math

class MP_Dht_Blue:	
        
	def __init__(self,pin):
                global sensor
                sensor = pin
               
		[temp,humidity] = grovepi.dht(sensor,blue)
		

	def checkTemp(self,opt,treshold,unit):
		  try:
        # Read sensor value from potentiometer
			[temp,humidity] = grovepi.dht(sensor,blue)
			sensorRead = temp
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

	def humidity(self,opt,treshold,unit):
			try:
			# Read sensor value from potentiometer
				[temp,humidity] = grovepi.dht(sensor,blue)
				sensorRead = humidity
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

