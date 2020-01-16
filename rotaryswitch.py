import RPi.GPIO as GPIO
from pygame import mixer

mixer.init()

sound = mixer.Sound('Soulful Atmospheric Groove Guitar Backing Track Jam in E.wav')

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        GPIO.output(7, True)
        if(GPIO.input(11)):
            sound.play()
finally:     
    GPIO.cleanup()
