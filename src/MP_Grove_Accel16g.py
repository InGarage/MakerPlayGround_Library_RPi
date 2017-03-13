from adxl345 import ADXL345
  
class MP_Accel16g:	
        
	def __init__(self):
                global adxl345
                adxl345 = ADXL345()
	def accel_x(self,opt,treshold,unit):
		  try:
			allRead = adxl345.getAxes(True)
			sensorRead = allRead['x']

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


	def accel_y(self,opt,treshold,unit):
		  try:
			allRead = adxl345.getAxes(True)
			sensorRead = allRead['y']

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
	def accel_z(self,opt,treshold,unit):
		  try:
			allRead = adxl345.getAxes(True)
			sensorRead = allRead['z']

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
