from MP_Grove_fourSevenSeg import *
import time

if __name__ == "__main__":		
	m= MP_FourSevenSeg(5)
	while True:
		m.show('A','c','b','0',1)	
		time.sleep(1)
		m.dim(30)
		time.sleep(1)
		m.off()
