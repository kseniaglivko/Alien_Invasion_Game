import pygame

from scoreboard import Scoreboard

class Button:
	
	def __init__(self, ai_game, effect):
		'''Initialising button attributes'''
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		
		if effect == "play":
			self.image = pygame.image.load('images/play_button.png')
		elif effect == "sound":
			self.image = pygame.image.load('images/sound_button.png')
		elif effect == "mute":
			self.image = pygame.image.load('images/mute_button.png')
			
		self.rect = self.image.get_rect()
		
		#Button placement
		if effect == "play":
			self.rect.center = self.screen_rect.center
		elif effect == "sound":
			self.rect = self.image.get_rect()
			self.rect.right = self.screen_rect.right - 525
			self.rect.top = 20
		elif effect == "mute":
			self.rect = self.image.get_rect()
			self.rect.right = self.screen_rect.right - 475
			self.rect.top = 20
		
		
	def draw_button(self):
		'''Drawing play button on the screen'''
		self.screen.blit(self.image, self.rect)
