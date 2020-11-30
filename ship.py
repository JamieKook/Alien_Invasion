import pygame
from pygame.sprite import Sprite

class Ship(Sprite): 
	""" A class to manage the ship."""

	def __init__(self, ai_game): 
		"""Initialize the shipe and set its starting position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		#Load the ship image and get its rect. 
		self.image = pygame.image.load('images/ship.bmp')
		self.rect = self.image.get_rect()

		#Start each new ship at the center of the screen.
		self.rect.center = self.screen_rect.center

		#Current location
		self.moving_right = False
		self.moving_left = False
		self.moving_up = False
		self.moving_down = False
	
	def blitme(self): 
		"""Draw the ship at its current location."""
		self.screen.blit(self.image, self.rect)

	def update(self): 
		if self.moving_right == True and self.rect.right < self.screen_rect.right:
			self.rect.x += 1
		elif self.moving_left == True and self.rect.left > 0: 
			self.rect.x -=1
		elif self.moving_up == True and self.rect.top > 0: 
			self.rect.y -=1
		elif self.moving_down == True and self.rect.bottom < self.screen_rect.bottom: 
			self.rect.y +=1



