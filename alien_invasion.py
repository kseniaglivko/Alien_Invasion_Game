import sys

import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
	'''Class to manage resources and game behaviour'''

	def __init__(self):
		'''Initialising game and game resources'''
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		
	def run_game(self):
		'''Lauching main cycle of the game'''
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()			
			self._update_screen()
					
	def _check_events(self):
		#Follow IO events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _check_keydown_events(self, event):
		'''Reaction to keydown'''
		if event.key == pygame.K_RIGHT:
			#Move ship to the right
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			#Move ship to the left
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()
						
	def _check_keyup_events(self, event):
		'''Reaction to keyup'''
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
			
	def _fire_bullet(self):
		'''Creating new bullet and adding it into bullets group'''
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)
			
	def _update_bullets(self):
		'''Renewing bullets position and removing old ones'''
		#Renew
		self.bullets.update()
		
		#Removal of bullets outside of the screen
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
							
	def _update_screen(self):
		#Trace screen for every cycle
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

		#Display of the last traced screen
		pygame.display.flip()


if __name__ == "__main__":
	#Creating game object and launch
	ai = AlienInvasion()
	ai.run_game()
