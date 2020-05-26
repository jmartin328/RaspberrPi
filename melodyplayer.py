#!/usr/bin/env python

import pygame
from midiutil import MIDIFile
from numpy.random import seed
from numpy.random import shuffle
from numpy.random import randint

def get_input():
	text = input("Repeat? : ")
	if (text == "y"):
		return 1
	else:
		return 0


def generate_melody(length, root):
	#seed the randome number generator
	seed()

	base = int(root)
	len = int(length)
	#prepare a major scale array based off the root, C4 is 60
	notes = [base+0, base+2, base+4, base+5, base+7, base+9, base+11, base+12]

	degrees = []
	#generate a sequence of the length
	for i in range(0, len):
		degrees.append(notes[randint(0,7)])

	track    = 0
	channel  = 0
	time     = 0 #in beats
	duration = randint(1,4,len) #in beats 
	tempo    = 100 #in BPM
	volume   = 100 #0-127, as per the MIDI standard

	MyMIDI = MIDIFile(1) #one track, defaults to format 1(tempo track created auto)

	MyMIDI.addTempo(track,time,tempo)
	current = 0

	for i, pitch in enumerate(degrees):
		MyMIDI.addNote(track, channel, pitch, current, duration[i], volume)
		current = current + duration[i]

	with open("generated.mid", "wb") as output_file:
		MyMIDI.writeFile(output_file)
	
def play_melody(music):
	clock = pygame.time.Clock()
	try:
		pygame.mixer.music.load(music)
	except pygame.error:
		print ("File not found")
		return
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy():
		clock.tick(30)
		
	
midi_file = 'generated.mid'
freq = 44100
bitsize = -16
channels = 2
buffer = 1024
pygame.mixer.init(freq, bitsize, channels, buffer)

pygame.mixer.music.set_volume(0.8)
try:
	#infinite loop 
	while (1):
		#get the length
		len = input ("Enter a length : ")
		#get the root
		roo = input ("Enter a root : ")
		#generate a new melody
		generate_melody(len, roo)
		#play the new melody for the first time
		play_melody(midi_file)
		#find if they want a repeat
		flag = get_input()
		#while they still want a repeat, keep playing the same melody
		while (flag == 1):
			play_melody(midi_file)
			flag = get_input()

except KeyboardInterrupt:
	pygame.mixer.music.fadeout(1000)
	pygame.mixer.music.stop()
	raise SystemExit

