import pygame
import sys
from random import randint
from settings import Settings
from controls import Controls

from ship import Ship
from bullet import Bullet
from stars import StarGrid
from wormhole import Wormhole


class RocketGame: 
	"""overall class to manage the game assets and behavior"""

	def __init__(self):
		#Initialize the game 
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Rocket Game")
		self.screen_rect = self.screen.get_rect()

		self.bullets = pygame.sprite.Group()
		self.ship = Ship(self)
		self.controls = Controls(self.ship)
		self.star_grid = StarGrid(self)
		self.wormholes = pygame.sprite.Group()
		self.wormhole = Wormhole(self)
		self.wormholes.add(self.wormhole)

	def run_game(self): 
		#Main loop for the game
		while True: 
			#See what has happened
			self.controls._check_events()

			# Update components
			self._update_pieces()

			#create new screen display
			self._updated_screen()

			#Make that new screen visible
			pygame.display.flip()

			
##### step 2: update components
	
	def _update_pieces(self): 
		self.ship.update()
		self._update_bullets()
		self.star_grid._update_stars()
		self._collisions()
		

	def _update_bullets(self): 
		#Move bullets
		self.bullets.update()
		#Delete off screen bullets
		for bullet in self.bullets.copy(): 
			if bullet.rect.right >= self.screen_rect.right: 
				self.bullets.remove(bullet)
		
	def _collisions(self): 
		#Detect bullet collisions with stars
		collisions = pygame.sprite.groupcollide(self.bullets, self.star_grid.stars, True, True)
		#Detect star collisions with ship
		if pygame.sprite.spritecollideany(self.ship, self.star_grid.stars):
			self.ship._restart()

		if pygame.sprite.spritecollide(self.ship, self.wormholes, True): 
			print('win!')


##### step 3: draw new screen 
	def _updated_screen(self): 
		self.screen.blit(self.settings.bg_image, (0,0))
		self.wormholes.draw(self.screen)
		self.ship.blitme()
		for bullet in self.bullets.sprites(): 
			bullet.draw_bullet()
		self.star_grid.stars.draw(self.screen)




if __name__ == '__main__': 
	rg = RocketGame()
	rg.run_game()
