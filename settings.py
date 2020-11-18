import pygame

class Settings: 
	""" A class to store all settings for Alien Invasion. """

	def __init__(self): 
		"""Initialize the game's settings."""
		#Screen Settings
		self.screen_width = 1200
		self.screen_height = 650
		self.bg_color = (255, 201, 247)
		self.bg_image = pygame.image.load('images/landscape-4032192_1920.bmp')

		# Ship settings
		self.ship_speed = 1.5

		#Bullet settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (16, 230, 205)
		self.bullets_allowed = 3
