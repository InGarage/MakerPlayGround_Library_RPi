from MP_Grove_GeneralLed import *
import time

if __name__ == "__main__":		
	m= MP_GeneralLed(4)
	while True:
		m.on()	
		time.sleep(1)
		m.off()
		time.sleep(1)
