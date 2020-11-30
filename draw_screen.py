import pygame

class Display: 

	def __init__(self, game):
		self.settings = game.settings
		self.screen = game.screen

	def _updated_screen(): 
		self.screen.blit(self.settings.bg_image, (0,0))