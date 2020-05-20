#!/usr/bin/env python

import pygame
from midiutil import MIDIFile
from numpy.random import seed
from numpy.random import shuffle
from numpy.random import randint


def generate_melody():
	#seed the randome number generator
	seed()

	#prepare a major scale sequence
	base = 60 #C4
	degrees = [base+0, base+2, base+4, base+5, base+7, base+9, base+11, base+12]

	#shuffle the sequence
	shuffle(degrees)

	track    = 0
	channel  = 0
	time     = 0 #in beats
	duration = randint(1,4,8) #in beats 
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
		print ("Midi file loaded!")
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
	generate_melody()
	play_melody(midi_file)
except KeyboardInterrupt:
	pygame.mixer.music.fadeout(1000)
	pygame.mixer.music.stop()
	raise SystemExit

