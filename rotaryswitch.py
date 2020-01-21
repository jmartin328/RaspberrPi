import RPi.GPIO as GPIO
import time
from pygame import mixer

GPIO.setmode(GPIO.BOARD)

#Initialize pygame mixer
mixer.init()

mixer.music.load('/home/pi/Desktop/Tracks/Emaj.wav')

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
#on/off
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#selector
GPIO.setup(13, GPIO.IN)
GPIO.setup(15, GPIO.IN)

def handle(pin):
    #assign sound to the active pin
    if (pin == C):
        mixer.music.load('/home/pi/Desktop/Tracks/Emaj.wav')
    elif (pin == G):
        mixer.music.load('/home/pi/Desktop/Tracks/Emin.wav')
    print(pin)

	
GPIO.add_event_detect(C, GPIO.BOTH, callback=handle, bouncetime=3)	
GPIO.add_event_detect(G, GPIO.BOTH, callback=handle, bouncetime=3)


try:
    while True:
        GPIO.output(7, True)
        mixer.music.play(-1)
finally:     
    GPIO.cleanup()
	

