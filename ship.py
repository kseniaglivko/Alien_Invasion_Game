import pygame

class Ship:
	'''Class to control the ship'''
	def __init__(self, ai_game):
		'''Initializing the ship and its starting position'''
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()
		
		#Load ship image and get the rectangle
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()
		
		#Each new ship appears at the bottom of the screen
		self.rect.midbottom = self.screen_rect.midbottom
		
		#Save floating coordinates of the center of the ship
		self.x = float(self.rect.x)
		
		#Flag for moving
		self.moving_right = False
		self.moving_left = False
		
		
	def update(self):
		'''Update ship position'''
		#Renew x attribute, not rect
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		
		#Renew rect attribute based on self.x
		self.rect.x = self.x
			
	def blitme(self):
		'''Draws the ship at the current position'''
		self.screen.blit(self.image, self.rect)
		
	def center_ship(self):
		'''Position ship in the midbottom of the screen'''
		self.rect.midbottom = self.screen_rect.midbottom
		self.x = float(self.rect.x)
