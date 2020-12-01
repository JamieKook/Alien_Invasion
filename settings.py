import pygame
from random import randint

class Settings: 
	#A class to store all settings for RocketGame

	def __init__(self): 
		#Screen display
		self.screen_width = 1200
		self.screen_height = 650
		self.bg_color = (143, 155, 176)
		self.bg_image = pygame.image.load('images/stars.bmp')

		# Ship settings
		self.ship_speed = 1

		# Bullet settings
		self.bullet_speed = 0.5
		self.bullet_number = 3

		# Star settings
		self.star_speed_x = 1 
		self.star_speed_y = 1 