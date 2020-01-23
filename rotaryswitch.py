import RPi.GPIO as GPIO
import time
from pygame import mixer

GPIO.setmode(GPIO.BOARD)

#Initialize pygame mixer
mixer.init()



current = 13
new = 0

# assign pins to keys
C = 13
G = 15
D = 16
A = 18
E = 22
B = 29
Fs = 31
Db = 32
Ab = 33
Eb = 36
Bb = 37
##F = 

#power
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, True)

#on/off
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#switch output
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)
# GPIO.setup(16, GPIO.IN)
# GPIO.setup(18, GPIO.IN)
# GPIO.setup(22, GPIO.IN)
# GPIO.setup(29, GPIO.IN)
# GPIO.setup(31, GPIO.IN)
# GPIO.setup(32, GPIO.IN)
# GPIO.setup(33, GPIO.IN)
# GPIO.setup(36, GPIO.IN)
# GPIO.setup(37, GPIO.IN)
# GPIO.setup(, GPIO.IN)

if(GPIO.input(13)):
    print("start 13")
    current = 13
    mixer.music.load('/home/pi/Desktop/Tracks/Emaj.wav')
elif(GPIO.input(15)):
    print("start 15")
    current = 15
    mixer.music.load('/home/pi/Desktop/Tracks/Emin.wav')

def handle(pin):
    global new, current
    
    #update currently playing
    #unload, and load new music
    if (pin == 13 and current != pin):
        new = pin
        mixer.music.load('/home/pi/Desktop/Tracks/Emaj.wav')
    elif (pin == 15 and current != pin):
	new = pin
        mixer.music.load('/home/pi/Desktop/Tracks/Emin.wav')
    #print the pin that is being handled
    print("New is: " + str(new))
    print("Current is: " + str(current))

	
GPIO.add_event_detect(13, GPIO.RISING, callback=handle, bouncetime=3000)	
GPIO.add_event_detect(15, GPIO.RISING, callback=handle, bouncetime=3000)

while True:
    #if there is a different pin active, start player
    if current != new:
        print("hi")
        current = new
        mixer.music.play()

