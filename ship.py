import pygame
from pygame.sprite import Sprite
from bullet import Bullet

class Ship(Sprite): 
	""" A class to manage the ship."""

	def __init__(self, game): 
		"""Initialize the shipe and set its starting position."""
		super().__init__()
		self.screen = game.screen
		self.settings = game.settings
		self.screen_rect = game.screen.get_rect()
		self.bullets = game.bullets
		self.game = game

		#Load the ship image and get its rect. 
		self.image = pygame.image.load('images/characters.jpg')
		self.rect = self.image.get_rect()

		#Start each new ship at the center of the screen.
		self.rect.midleft = self.screen_rect.midleft

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
			self.rect.x += self.settings.ship_speed
		elif self.moving_left == True and self.rect.left > 0: 
			self.rect.x -= self.settings.ship_speed
		elif self.moving_up == True and self.rect.top > 0: 
			self.rect.y -= self.settings.ship_speed
		elif self.moving_down == True and self.rect.bottom < self.screen_rect.bottom: 
			self.rect.y += self.settings.ship_speed

	def _fire_bullet(self):
		if self.settings.bullet_number > len(self.bullets):
			new_bullet = Bullet(self.game)
			self.bullets.add(new_bullet)



