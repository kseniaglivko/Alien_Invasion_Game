import sys

import pygame

from settings import Settings

class AlienInvasion:
	'''Class to manage resources and game behaviour'''

	def __init__(self):
		'''Initialising game and game resources'''
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")
		

	def run_game(self):
		'''Lauching main cycle of the game'''
		while True:
			#Follow IO events
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
					
			#Trace screen for every cycle
			self.screen.fill(self.settings.bg_color)

			#Display of the last traced screen
			pygame.display.flip()

if __name__ == "__main__":
	#Creating game object and launch
	ai = AlienInvasion()
	ai.run_game()
