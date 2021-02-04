import pygame
from pygame.sprite import Sprite

class Superbullet(Sprite):
	'''Class for controlling ship bullets'''
	
	def __init__(self, ai_game):
		'''Creating bullet object at the ship current position'''
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.superbullet_color
		
		#Creating superbullet at (0, 0) and assigning right position
		self.rect = pygame.Rect(0, 0, self.settings.superbullet_width,
			self.settings.superbullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop
		
		#Storing superbullet position in float
		self.y = float(self.rect.y)
		
	def update(self):
		'''Moves object upwards'''
		
		#Renewing superbullet position in float format
		self.y -= self.settings.superbullet_speed
		
		#Renewing rect position
		self.rect.y = self.y
		
	def draw_superbullet(self):
		'''Superbullets screen display'''
		pygame.draw.rect(self.screen, self.color, self.rect)
		
