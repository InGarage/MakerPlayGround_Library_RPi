from MP_Grove_GeneralLed import *
import time

if __name__ == "__main__":		
	m= MP_GeneralLed(5)
	while True:
		m.on()	
		time.sleep(1)
		m.dim(0.3)
		time.sleep(1)
