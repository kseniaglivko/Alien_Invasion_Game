class Settings:
	'''Class to store all the game settings'''
	
	def __init__(self):
		'''Initializing game settings'''
		#Screen parameters 
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (16, 16, 61)
		
		#Ship settings
		self.ship_speed = 1.5
