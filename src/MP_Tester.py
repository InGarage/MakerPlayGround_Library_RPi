from MP_Grove_RGBLcd import *
import time

if __name__ == "__main__":		
	m= MP_RGBLcd()
	while True:
		time.sleep(1)
		m.show("Hello dude!")	
		m.backlight_color("#123ABC")
		time.sleep(1)
		m.backlight_off()
		time.sleep(1)
		m.show("Hello !")	
		time.sleep(1)
		setText("                                 ")
		m.backlight_on()
		time.sleep(1)
	
