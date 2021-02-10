import pygame
from pygame.sprite import Sprite

class Explosion(Sprite):
	'''Class to create an explosion'''
	
	def __init__(self, ai_game, center, size):
		super().__init__()
		
		#Creating a list to store explosion images to create animation
		self.images = []
		for num in range(1, 6):
			img = pygame.image.load(f"images/exp{num}.png")
			if size == "small":
				img = pygame.transform.scale(img, (80, 80))
			if size == "big":
				img = pygame.transform.scale(img, (120, 120))
			if size == "super_big":
				img = pygame.transform.scale(img, (200, 200))
			self.images.append(img)
		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		
		#Assigning explosion position
		self.rect.center = center

		self.counter = 0
	
	def update(self):
	
		explosion_speed = 15
		
		#Updating explosion animation
		self.counter += 1

		if self.counter >= explosion_speed and self.index < len(self.images) - 1:
			self.counter = 0
			self.index += 1
			self.image = self.images[self.index]

		#If the animation is complete, explosion desappears
		if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
			self.kill()
