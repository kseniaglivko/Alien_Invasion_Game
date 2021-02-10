class GameStats:
	'''Collecting statistics for the game'''
	
	def __init__(self, ai_game):
		'''Initialising statistics'''
		self.settings = ai_game.settings
		self.reset_stats()
		
		#Game starts in non-active state
		self.game_active = False
		
	def reset_stats(self):
		'''Initialising statistics, changing in game process'''
		self.ships_left = self.settings.ship_limit
