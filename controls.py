import pygame
import sys

class Controls: 

	def __init__(self, ship): 
		self.ship = ship

	def _check_events(self): 
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				sys.exit()
			elif event.type == pygame.KEYDOWN: 
				self._keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._keyup_events(event)

	def _keydown_events(self,event):
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
		elif event.key == pygame.K_SPACE: 
			self.ship._fire_bullet()

	def _keyup_events(self, event): 
		if event.key == pygame.K_RIGHT: 
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT: 
			self.ship.moving_left = False
		elif event.key == pygame.K_UP: 
			self.ship.moving_up = False
		elif event.key == pygame.K_DOWN: 
			self.ship.moving_down = False

	