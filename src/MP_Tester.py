from MP_Grove_Relay import *
import time

if __name__ == "__main__":		
	m= MP_Relay(5)
	while True:
		m.on()
		time.sleep(1)
		
		m.off()
		time.sleep(1)
	
