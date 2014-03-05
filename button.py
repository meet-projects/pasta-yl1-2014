import pygame

class Button(object):
	def __init__(self, rec1, rec2, surface1, surface2):
		self.rec = pygame.Rect(rec1, rec2, surface1, surface2)
		self.surface = pygame.Surface([surface1, surface2])

	def draw(self, screen):
		screen.blit(self.surface, self.rec)
