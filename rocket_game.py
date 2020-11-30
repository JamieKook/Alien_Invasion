import pygame
import sys
from settings import Settings
from controls import Controls

from ship import Ship


class RocketGame: 
	"""overall class to manage the game assets and behavior"""

	def __init__(self):
		#Initialize the game 
		pygame.init()
		self.settings = Settings()


		
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Rocket Game")

		self.ship = Ship(self)
		self.controls = Controls(self.ship)


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

#####
	def _updated_screen(self): 
		self.screen.blit(self.settings.bg_image, (0,0))
		self.ship.blitme()



if __name__ == '__main__': 
	rg = RocketGame()
	rg.run_game()
