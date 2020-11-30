import pygame

class Settings: 
	#A class to store all settings for RocketGame

	def __init__(self): 
		#Screen display
		self.screen_width = 1200
		self.screen_height = 650
		self.bg_color = (143, 155, 176)
		self.bg_image = pygame.image.load('images/stars.bmp')