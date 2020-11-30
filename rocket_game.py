import pygame
import sys
from settings import Settings

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


	def run_game(self): 
		#Main loop for the game
		while True: 
			#See what has happened
			self._check_events()

			# Update components
			self._update_pieces()

			#create new screen display
			self._updated_screen()

			#Make that new screen visible
			pygame.display.flip()


##### step 1: Check game events
#Key board interactions
	def _check_events(self): 
		#Watch for keyboard and mouse events: 
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._keyup_events(event)

# specific interactions
	def _keydown_events(self, event): 
		if event.key == pygame.K_RIGHT: 
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT: 
			self.ship.moving_left = True
		elif event.key == pygame.K_UP: 
			self.ship.moving_up = True
		elif event.key == pygame.K_DOWN: 
			self.ship.moving_down = True
		elif event.key == pygame.K_q:
			sys.exit()

	def _keyup_events(self, event): 
		if event.key == pygame.K_RIGHT: 
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT: 
			self.ship.moving_left = False
		elif event.key == pygame.K_UP: 
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN: 
			self.ship.moving_down = False


			
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
