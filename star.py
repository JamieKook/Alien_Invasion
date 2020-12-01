import pygame
from pygame.sprite import Sprite

class Star(Sprite): 

	def __init__(self, game): 
		super().__init__()
		self.screen = game.screen
		self.settings = game.settings

		self.image = pygame.image.load('images/star.jpg')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.y = float(self.rect.y)
		self.x = float(self.rect.x)

	def update(self, x, y): 
		self.x += self.settings.star_speed_x * x
		self.y += self.settings.star_speed_y * y
		self.rect.x = self.x
		self.rect.y = self.y
