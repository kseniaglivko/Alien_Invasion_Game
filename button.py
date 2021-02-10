import pygame

class Button:
	
	def __init__(self, ai_game):
		'''Initialising button attributes'''
		self.screen = ai_game.screen
		self.screen_rect = self.screen.get_rect()
		
		self.image = pygame.image.load('images/play_button.png')
		self.rect = self.image.get_rect()
		
		#Button placement
		self.rect.center = self.screen_rect.center
		
	def draw_button(self):
		'''Drawing play button on the screen'''
		self.screen.blit(self.image, self.rect)
