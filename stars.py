import pygame
from random import randint
from star import Star


class StarGrid: 

	def __init__(self, game): 
		self.stars = pygame.sprite.Group()
		self.game = game
		self.settings = game.settings
		self.grid = self._create_grid()


	def _create_grid(self): 
		star = Star(self.game)
		star_width= star.rect.width
		available_space_x = self.settings.screen_width - (2 * star_width)
		number_stars_x = available_space_x// (2*star_width)

		for star_number in range(number_stars_x): 
			star = Star(self.game)
			star.x = self.game.ship.rect.width + randint(0, 1000)
			star.rect.x = star.x
			star.y = randint(0,600)
			star.rect.y = star.y
			self.stars.add(star)