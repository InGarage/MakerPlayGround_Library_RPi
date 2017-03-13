import grovepi

class MP_PIR:	
        
	def __init__(self,pin):
                global pir_sensor
                pir_sensor = pin
               
		grovepi.pinMode(pir_sensor,"INPUT")
		

	def motion(self):
		motion = 0
		try:
			motion=grovepi.digitalRead(pir_sensor)
			if motion==0 or motion==1:	# check if reads were 0 or 1 it can be 255 also because of IO Errors so remove those values
				if motion==1:
					return 1
				else:
					return 0
		except IOError:
			print ("Error")
