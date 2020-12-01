import pygame
from random import randint
from star import Star


class StarGrid: 

	def __init__(self, game): 
		self.stars = pygame.sprite.Group()
		self.game = game
		self.settings = game.settings
		self.screen = game.screen
		self.grid = self._create_grid()


	def _create_grid(self): 
		star = Star(self.game)
		star_width= star.rect.width
		available_space_x = self.settings.screen_width - (2 * star_width)
		number_stars_x = available_space_x// (2*star_width)

		for star_number in range(number_stars_x): 
			self._create_star()


	def _create_star(self): 
		star = Star(self.game)
		star.x = self.game.ship.rect.width + randint(0, 1000)
		star.rect.x = star.x
		star.y = randint(0,600)
		star.rect.y = star.y
		self.stars.add(star)

	def _update_stars(self): 
		for star in self.stars:
			randomizer_x = randint(-10, 10)
			randomizer_y = randint(-10, 10)
			star.update(randomizer_x, randomizer_y)
		self.check_edges()

	def check_edges(self): 
		screen_rect = self.screen.get_rect()
		for star in self.stars.copy(): 
			if star.rect.left >= screen_rect.right: 
				self.stars.remove(star)
				self._create_star()
			elif star.rect.right <= screen_rect.left: 
				self.stars.remove(star)
				self._create_star()
			elif star.rect.bottom <= screen_rect.top: 
				self.stars.remove(star)
				self._create_star()
			elif star.rect.top >= screen_rect.bottom: 
				self.stars.remove(star)
				self._create_star()
