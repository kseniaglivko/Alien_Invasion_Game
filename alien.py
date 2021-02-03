import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	'''Class to create one alien'''
	
	def __init__(self, ai_game):
		'''Initializing alien and its starting point'''
		super().__init__()
		self.screen = ai_game.screen
		
		#Loading alien image and assigning rect attribute
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		
		#Assigning staarting position
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#Saving the exact horizontal position
		self.x = float(self.rect.x)
		
		
