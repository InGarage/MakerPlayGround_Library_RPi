from MP_Twitter import *
import time

if __name__ == "__main__":		
	m= MP_Twitter()
	while True:
		m.setup("6aJsA4Lf7pANIheZ0WVjqV8oW","3AsuqFYgaWozD0azSorkKojmETNO1x3uX63wP3HgUttlFN6YhL","301425044-1hSnErgwxZ3lNHmgAkuwQs0AeTTad76Uy08JUJyD","dLzdelh5haqs7LdO4o9UJzuJErSC38BnzoEgMCt5BBMu8","mpg")
		time.sleep(1)
		
		m.tweet("EIEI GUM")
		time.sleep(1)
	
