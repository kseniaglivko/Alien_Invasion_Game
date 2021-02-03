import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	'''Class for controlling ship bullets'''
	
	def __init__(self, ai_game):
		'''Creating bullet object at the ship current position'''
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color
		
		#Creating bullet at (0, 0) and assigning right position
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
			self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop
		
		#Storing bullet position in float
		self.y = float(self.rect.y)
		
	def update(self):
		'''Moves object upwards'''
		
		#Renewing bullet position in float format
		self.y -= self.settings.bullet_speed
		
		#Renewing rect position
		self.rect.y = self.y
		
	def draw_bullet(self):
		'''Bullets screen display'''
		pygame.draw.rect(self.screen, self.color, self.rect)
		
