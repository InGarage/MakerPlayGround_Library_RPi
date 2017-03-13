

import twitter
import time
import grovepi
import math

# Connections


intro_str = "Makerplaygorund"

# Connect to Twitter
api = twitter.Api(
    consumer_key='6aJsA4Lf7pANIheZ0WVjqV8oW',
    consumer_secret='3AsuqFYgaWozD0azSorkKojmETNO1x3uX63wP3HgUttlFN6YhL',
    access_token_key='301425044-1hSnErgwxZ3lNHmgAkuwQs0AeTTad76Uy08JUJyD',
    access_token_secret='dLzdelh5haqs7LdO4o9UJzuJErSC38BnzoEgMCt5BBMu8'
    )
while True:
    # Error handling in case of problems communicating with the GrovePi
    try:        
        out_str = "Hello Twitter! I'm a bot in RaspPi." 
        print (out_str)
        api.PostUpdate(out_str)
        time.sleep(30)
    except IOError:
        print("Error")
    except KeyboardInterrupt:
        exit()
    except:
        print("Duplicate Tweet or Twitter Refusal")
