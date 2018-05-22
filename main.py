#  main.py
 
import pygame
from time import sleep

pygame.init()
pygame.mixer.init()

PHONE_SOUNDS = {
	'ring': 'telephone-ring-01a.wav',
	'dial': '',
	'click': '',
	'hangup': '',
}

ARCHIVE_RECORDINGS = {
	24051970: '',
}


class Telephone():
	"""
	Handles input from the GPIO and plays the right sounds at the right time
	"""
	
	def __init__(self):
		pass
	
	def dialtone(self):
		pass
	
	def parse_input(self):
		pass
	
	def play_recording(self, phone_number):
		recording = pygame.mixer.Sound(ARCHIVE_RECORDINGS[phone_number])
		recording.play()
		sleep(recording.get_length())
		recording.stop()
	
