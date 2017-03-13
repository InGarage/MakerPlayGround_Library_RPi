import grovepi

class MP_Button:	
        
	def __init__(self,pin):
                global button
                button = pin
               
		grovepi.pinMode(button,"INPUT")
		

	def release(self):
	
		try:
			sensor= grovepi.digitalRead(button)
			if sensor==0 or sensor==1:	# check if reads were 0 or 1 it can be 255 also because of IO Errors so remove those values
				if sensor==1:
					return 1
				else:
					return 0
		except IOError:
			print ("Error")

	def doubleRelease(self):
	
		try:
			returnVal=0
			if grovepi.digitalRead(button)==1:
				while(grovepi.digitalRead(button)==1):
					count=0
				while(count<500):
					count=count+1
					if(grovepi.digitalRead(button)==1):
						returnVal+=1
				while(grovepi.digitalRead(button)==1):
					pass
				if returnVal>1:
					return 1
			return 0

		except IOError:
			print ("Error")		