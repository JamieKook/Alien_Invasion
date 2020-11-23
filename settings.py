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
		self.ship_limit = 3

		#Bullet settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (16, 230, 205)

		#Alien settings
		self.fleet_drop_speed = 10

		#How quickly the game speeds up
		self.speedup_scale = 1.1
		self.score_scale = 1.5

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 1.0
		self.bullets_allowed = 3

		self.fleet_direction = 1
		self.alien_points = 50 

	def increase_speed(self): 
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.bullets_allowed = int(self.bullets_allowed * self.score_scale)
		self.alien_points = int(self.alien_points * self.score_scale)
