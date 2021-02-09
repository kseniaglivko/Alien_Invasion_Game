import sys

import pygame

from random import randint

from settings import Settings
from ship import Ship
from bullet import Bullet
from superbullet import Superbullet
from alien import Alien
from star import Star
from explosion import Explosion

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
		self.superbullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()
		self.stars = pygame.sprite.Group()
		self.explosions = pygame.sprite.Group()
				
		self._create_fleet()
		self._create_starry_sky()
		
	def run_game(self):
		'''Lauching main cycle of the game'''
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()	
			self._update_superbullets()
			self._update_explosions()
			self._update_aliens()		
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
		elif event.key == pygame.K_RSHIFT:
			self._fire_superbullet()
						
	def _check_keyup_events(self, event):
		'''Reaction to keyup'''
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False
			
	def _fire_bullet(self):
		'''Creating new bullet and adding it into bullet group'''
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)
			
	def _fire_superbullet(self):
		'''Creating new superbullet and adding it into superbullet group'''
		if len(self.superbullets) < self.settings.superbullets_allowed:
			new_superbullet = Superbullet(self)
			self.superbullets.add(new_superbullet)
			
	def _update_bullets(self):
		'''Renewing bullets position and removing old ones'''
		#Renew
		self.bullets.update()

		#Remove bullets outside of the screen and upon collision
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
			collisions = pygame.sprite.spritecollide(bullet, self.aliens, True)
			
			#Run explosion animation
			for collision in collisions:
				bullet.kill()
				explosion = Explosion(self, collision.rect.center, "small")
				self.explosions.add(explosion)

	def _update_superbullets(self):
		'''Renewing superbullets position and removing old ones'''
		#Renew
		self.superbullets.update()
		
		#Removal of superbullets outside of the screen and upon collision
		for superbullet in self.superbullets.copy():
			if superbullet.rect.bottom <= 0:
				self.superbullets.remove(superbullet)
			collisions = pygame.sprite.spritecollide(superbullet, self.aliens, True)
			
			#Run explosion animation
			for collision in collisions:
				explosion = Explosion(self, collision.rect.center, "big")
				self.explosions.add(explosion)

	def _update_explosions(self):
		self.explosions.update()
				
	def _create_fleet(self):
		'''Creating invasion fleet'''
		#Creating an alien and counting number of aliens in the row
		#Interval between aliens ifs equal to width of one alien
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - alien_width
		number_of_aliens_x = available_space_x // (2 * alien_width)
		
		'''Assesing number of rows on the screen'''
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height - 
			(3 * alien_height) - ship_height)
		number_of_rows = available_space_y // (2 * alien_height)
		
		#Creating fleet
		for row_number in range(number_of_rows):
			for alien_number in range(number_of_aliens_x):
				self._create_alien(alien_number, row_number)
			
	def _create_alien(self, alien_number, row_number):
		'''Creating an alien and its placement in a row'''
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)
				
	def _check_fleet_edges(self):
		'''Reacts to alien's arrival to the edge of the screen'''
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break
				
	def _change_fleet_direction(self):
		'''Moves fleet down and changes its direction'''
		for alien in self.aliens.sprites():
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_directions *= -1
		
	def _update_aliens(self):
		'''Updating fleet position'''
		self._check_fleet_edges()
		self.aliens.update()
		
	def _create_starry_sky(self):
		'''Creating starry sky'''
		star = Star(self)
		star_width, star_height = star.rect.size
		
		available_space_x = self.settings.screen_width - star_width
		number_of_stars = available_space_x // star_width
		
		available_space_y = self.settings.screen_height - star_height
		number_of_rows = available_space_y // star_height
		
		#Creating sky
		for row_number in range(number_of_rows):
			for star_number in range(number_of_stars):
				self._create_star(star_number, row_number)
		
	def _create_star(self, star_number, row_number):
		'''Creating star and its placement'''
		star = Star(self)
		star_width, star_height = star.rect.size
		star.x = randint(-50, 50) + 5 * star_width * star_number 
		star.rect.x = star.x
		star.rect.y = randint(-50, 50) + 5 * star.rect.height * row_number
		self.stars.add(star)
										
	def _update_screen(self):
		#Trace screen for every cycle
		self.screen.fill(self.settings.bg_color)
		self.stars.draw(self.screen)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		for superbullet in self.superbullets.sprites():
			superbullet.draw_superbullet()
		self.explosions.draw(self.screen)	
		self.aliens.draw(self.screen)

		#Display of the last traced screen
		pygame.display.flip()

if __name__ == "__main__":
	#Creating game object and launch
	ai = AlienInvasion()
	ai.run_game()
