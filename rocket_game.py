import pygame
from settings import Settings
from keyboard_controls import KeyboardControls


class RocketGame: 
	"""overall class to manage the game assets and behavior"""

	def __init__(self):
		#Initialize the game 
		pygame.init()
		self.settings = Settings()
		self.keyboard = KeyboardControls()
		
		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Rocket Game")


	def run_game(self): 
		#Main loop for the game
		while True: 
			#See what has happened
			self._check_events()

			#create new screen display
			self._updated_screen()

			#Make that new screen visible
			pygame.display.flip()

	def _check_events(self): 
		#Watch for keyboard and mouse events: 
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				sys.exit()
			else:
			 self.keyboard.check_events()

	def _updated_screen(self): 
		self.screen.blit(self.settings.bg_image, (0,0))


if __name__ == '__main__': 
	rg = RocketGame()
	rg.run_game()
