# Tweet the temperature, light, and sound levels with our Raspberry Pi
# http://www.dexterindustries.com/GrovePi/projects-for-the-raspberry-pi/raspberry-pi-twitter-sensor-feed/

# GrovePi + Sound Sensor + Light Sensor + Temperature Sensor + LED
# http://www.seeedstudio.com/wiki/Grove_-_Sound_Sensor
# http://www.seeedstudio.com/wiki/Grove_-_Light_Sensor
# http://www.seeedstudio.com/wiki/Grove_-_Temperature_and_Humidity_Sensor_Pro
# http://www.seeedstudio.com/wiki/Grove_-_LED_Socket_Kit

'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2015  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
'''

import twitter
import time
import grovepi
import math



# Connect to Twitter install lib yourself
api = twitter.Api(
    consumer_key='6aJsA4Lf7pANIheZ0WVjqV8o',
    consumer_secret='3AsuqFYgaWozD0azSorkKojmETNO1x3uX63wP3HgUttlFN6Yh',
    access_token_key='301425044-1hSnErgwxZ3lNHmgAkuwQs0AeTTad76Uy08JUJy',
    access_token_secret='dLzdelh5haqs7LdO4o9UJzuJErSC38BnzoEgMCt5BBMu'
    )


count=1
while True:
    # Error handling in case of problems communicating with the GrovePi
    try:
        count=count+1
        out_str = "Hello Twitter! I'm a bot in RaspPi. #ทวิตที่" + count +"ในรอบ5ปี" 
        print (out_str)
        api.PostUpdate(out_str)
        time.sleep(30)
    except IOError:
        print("Error")
    except KeyboardInterrupt:
        exit()
    except:
        print("Duplicate Tweet or Twitter Refusal")
