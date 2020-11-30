import pygame
from pygame.sprite import Sprite

class Bullet(Sprite): 
	""" A class to manage bullets fired from the ship"""

	def __init__(self, game): 
		"""Create a bullet object at the ship's current position"""
		super().__init__()
		self.screen = game.screen
		self.settings = game.settings
		
		self.image = pygame.image.load('images/bullet.jpg')
		self.rect = self.image.get_rect()

		# Create a bullet rect at (0,0) and then set correct position. 
		self.rect.midright = game.ship.rect.midright

		self.x = float(self.rect.x)

	def update(self): 
		self.x += self.settings.bullet_speed
		self.rect.x = self.x

	def draw_bullet(self): 
		self.screen.blit(self.image, self.rect)