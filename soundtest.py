import time
import RPi.GPIO as GPIO
from pygame import mixer

#Initialize pygame mixer
mixer.init()

#Load the sounds
sound = mixer.Sound('applause-1.wav')

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)

try:
    while True:
        GPIO.output(7, True)
        #sound.play()

finally:
    GPIO.cleanup()
    
