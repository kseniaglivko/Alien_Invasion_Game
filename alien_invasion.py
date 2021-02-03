import sys

import pygame

from settings import Settings
from ship import Ship

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
		
	def run_game(self):
		'''Lauching main cycle of the game'''
		while True:
			self._check_events()
			self.ship.update()
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
			
	def _check_keyup_events(self, event):
		'''Reaction to keyup'''
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
						
		
				
	def _update_screen(self):
		#Trace screen for every cycle
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()

		#Display of the last traced screen
		pygame.display.flip()


if __name__ == "__main__":
	#Creating game object and launch
	ai = AlienInvasion()
	ai.run_game()
