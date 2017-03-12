from MP_Grove_fourSevenSeg import *
import time

if __name__ == "__main__":		
	m= MP_FourSevenSeg(5)
	while True:
                m.dim(30)
		m.show('1','c','b','0',1)	
		time.sleep(1)
		
		time.sleep(1)
		m.dim(90)
		m.off()
		time.sleep(1)
		m.show('','c','A','',0)	
		time.sleep(1)
