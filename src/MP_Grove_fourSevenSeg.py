import time
import grovepi


class MP_FourSevenSeg:	
        
	def __init__(self,pin):
                global display
                display = pin
               
		grovepi.pinMode(display,"OUTPUT")
		time.sleep(1)		
	
	def convert(text):
		if text == '0':
			return 63
		elif text == '1':
			return 6
		elif text == '2':
			return 91
		elif text == '3':
			return 79
		elif text == '4':
			return 102
		elif text == '5':
			return 109
		elif text == '6':
			return 125
		elif text == '7':
			return 7
		elif text == '8':
			return 127
		elif text == '9':
			return 111
		elif text == 'A' || text == 'a':
			return 119
		elif text == 'B' || text == 'b':
			return 124
		elif text == 'C' || text == 'c':
			return 57	
		elif text == 'D' || text == 'd':
			return 94
		elif text == 'E' || text == 'e':
			return 121
		elif text == 'F' || text == 'f':
			return 113		

	def show(self,num1,num2,num3,num4,isColon):
		grovepi.fourDigit_segment(display,0,convert(num1)) 
        grovepi.fourDigit_segment(display,1,convert(num2)) # 121 = E
        if isColon:
        	grovepi.fourDigit_segment(display,2,convert(num3)+128) # 118 = H
        else:
        	grovepi.fourDigit_segment(display,2,convert(num3)) # 118 = H
        grovepi.fourDigit_segment(display,3,convert(num4)) # 121 = E
	
	def dim(self,percentage):
		grovepi.fourDigit_brightness(display,int((255*percentage)/100))

	def off(self):
		grovepi.fourDigit_segment(display,0,0)
		grovepi.fourDigit_segment(display,1,0)
		grovepi.fourDigit_segment(display,2,0)
		grovepi.fourDigit_segment(display,3,0)

