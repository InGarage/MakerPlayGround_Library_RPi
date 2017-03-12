from grove_rgb_lcd import *

class MP_RGBLcd:	
        
	def __init__(self):
		setRGB(255,255,255)	

	def backlight_off(self):
		setRGB(0,0,0)	

	def backlight_on(self):
		setRGB(255,255,255)	
	
	def show(self,text):
		setText(text)

	def clear(self):
		setText("                                 ")

	def backlight_color(self,color):
		r = int("0x"+color[1:3],16)
		g = int("0x"+color[3:5],16)
		b = int("0x"+color[5:7],16)
		setRGB(r,g,b)
