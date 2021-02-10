class Settings:
	'''Class to store all the game settings'''
	
	def __init__(self):
		'''Initializing static game settings'''
		#Screen parameters 
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (16, 16, 61)
		
		#Ship settings
		self.ship_limit = 3
		
		#Bullet settings
		self.bullets_allowed = 3
		
		#SuperBullet settings
		self.superbullets_allowed = 1
		
		#Alien settings
		self.fleet_drop_speed = 10
		#fleet direction: 1 - to the right, -1 - to the left
		self.fleet_direction = 1
		
		#Game speed acceleration
		self.speedup_scale = 1.1
		
		self.initialize_dynamic_settings()
	
	def initialize_dynamic_settings(self):
		'''Initialize settings, that change during the game'''
		self.ship_speed_factor = 1.0
		self.bullet_speed_factor = 2.5
		self.superbullet_speed_factor = 3.0
		self.alien_speed_factor = 1.0
		
	def increase_speed(self):
		'''Increase speed settings'''
		self.ship_speed_factor *= self.speedup_scale
		self.bullet_speed_factor *= self.speedup_scale
		self.superbullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
