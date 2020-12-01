import pygame
from pygame.sprite import Sprite

class Wormhole(Sprite): 

	def __init__(self,game): 

		super().__init__()
		self.screen = game.screen
		self.settings = game.settings
		self.screen_rect = game.screen.get_rect()

		self.image = pygame.image.load('images/wormhole.jpg')
		self.rect = self.image.get_rect()

		self.rect.topright = self.screen_rect.topright


	def blitme(self): 
		self.screen.blit(self.image, self.rect)
