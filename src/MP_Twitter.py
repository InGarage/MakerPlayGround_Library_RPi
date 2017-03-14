import twitter
import time
import grovepi
import math


class MP_Twitter:		
	def __init__(self):
		global beSetup
		global intro_str		
		beSetup = 0

	def setup(self,consumer_k,consumer_s,access_token_k,access_token_s,intro_s):
	
		intro_str = intro_s
		global api
		api = twitter.Api(
    consumer_key= consumer_k,
    consumer_secret=consumer_s,
    access_token_key=access_token_k,
    access_token_secret=access_token_s
    )				
		
		

	def tweet(self,text):
                        try:
                                api.PostUpdate(text)
                        except IOError:
                                print("Error")
                        except KeyboardInterrupt:
                                exit()
                        except:
                                print("Duplicate Tweet or Twitter Refusal")
		
