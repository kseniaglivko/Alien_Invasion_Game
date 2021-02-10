import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	'''Class to create one alien'''
	
	def __init__(self, ai_game):
		'''Initializing alien and its starting point'''
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		
		#Loading alien image and assigning rect attribute
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		
		#Assigning starting position
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#Saving the exact horizontal position
		self.x = float(self.rect.x)
		
	def check_edges(self):
		'''Returns True if alien if at the edge of the screen'''
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True
			
	def update(self):
		'''Moving alien to the right or left'''
		self.x += (self.settings.alien_speed_factor * self.settings.fleet_direction)
		self.rect.x = self.x

		
		


