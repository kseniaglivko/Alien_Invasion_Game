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
		
		#Bullet settings
		self.bullet_speed = 1.5
		self.bullets_allowed = 3
		
		#SuperBullet settings
		self.superbullet_speed = 2.5
		self.superbullets_allowed = 1
		
		#Alien settings
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		#fleet_direction = 1 means going to the right, -1 - to the left
		self.fleet_directions = 1
