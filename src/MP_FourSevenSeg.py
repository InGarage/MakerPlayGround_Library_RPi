import time
import grovepi

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
	elif (text == 'A') | (text == 'a'):
		return 119
	elif (text == 'B') | (text == 'b'):
		return 124
	elif (text == 'C') | (text == 'c'):
		return 57	
	elif (text == 'D') | (text == 'd'):
		return 94
	elif (text == 'E') | (text == 'e'):
		return 121
	elif (text == 'F') | (text == 'f'):
		return 113
	else:
                return 0
                
class MP_FourSevenSeg:	
        
	def __init__(self,pin):
                global display
                display = pin
               
		grovepi.pinMode(display,"OUTPUT")
		time.sleep(1)		
	
	

	def show(self,num1,num2,num3,num4,isColon):
		grovepi.fourDigit_segment(display,0,convert(num1)) 
                grovepi.fourDigit_segment(display,2,convert(num3)) 
                if isColon==1:
                        grovepi.fourDigit_segment(display,1,convert(num2)+128) 
                else:
                        grovepi.fourDigit_segment(display,1,convert(num2)) 
                grovepi.fourDigit_segment(display,3,convert(num4)) 
	
	def dim(self,percentage):
		grovepi.fourDigit_brightness(display,int(7*(percentage/100.0)))
		

	def off(self):
		grovepi.fourDigit_segment(display,0,0)
		grovepi.fourDigit_segment(display,1,0)
		grovepi.fourDigit_segment(display,2,0)
		grovepi.fourDigit_segment(display,3,0)

