import RPi.GPIO as GPIO
import time
from pygame import mixer

#Initialize pygame mixer
mixer.init()

#Load the sounds
soundC
soundG
soundD
soundA
sound = mixer.Sound('Soulful Atmospheric Groove Guitar Backing Track Jam in E.wav')


GPIO.setmode(GPIO.BOARD)

GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_UP)
played = 0

def play_sound(name):
    global played
    print(name)
    #sound = mixer.Sound("track" + ".wav")
    played = 1

def 

GPIO.add_event_detect(

try:
    while True:
        GPIO.output(7, True)
        if(GPIO.input(11)and (not played)):
            #sound.play()
            #sound.set_volume(0.5)
            track
            if(GPIO.input(13):
               track = "C"
            elif(GPIO.input(15)
               track = "G"
            elif(GPIO.input(16)
               track = "D"
            elif(GPIO.input(18)
               track = "A"
            elif(GPIO.input(22)
               track = "E"
            elif(GPIO.input(29)
               track = "B"
            elif(GPIO.input(31)
               track = "F#"
            elif(GPIO.input(31)
               track = "Db"
            elif(GPIO.input(32)
               track = "Ab"
            elif(GPIO.input(33)
               track = "Eb"
            elif(GPIO.input(36)
               track = "Bb"
            elif(GPIO.input(37)
               track = "F"
            play_sound(track)
        #else:
            #sound.fadeout(500)
finally:     
    GPIO.cleanup()


