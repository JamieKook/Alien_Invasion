import pygame

class KeyboardControls: 
	#Class that manages keyboard input

	def check_events(self): 
		for event in pygame.event.get(): 
			if event.type == pygame.MOUSEBUTTONDOWN:
				pass
			elif event.type == pygame.KEYDOWN: 
				pass
			elif event.type == pygame.KEYUP:
				pass