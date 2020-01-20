import RPi.GPIO as GPIO
from pygame import mixer

mixer.init()

sound = mixer.Sound('Soulful Atmospheric Groove Guitar Backing Track Jam in E.wav')

GPIO.setmode(GPIO.BOARD)

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
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


sound = 0

try:
    while True:
        GPIO.output(7, True)
        # if(GPIO.input(11)):
            # sound.play()
finally:     
    GPIO.cleanup()
	
def handle(pin)
	#assign sound to the active pin
	sound = pin
	print(sound)

	
GPIO.add_event_detect(C, GPIO.RISING, handle)	
GPIO.add_event_detect(G, GPIO.RISING, handle)


while True:

	