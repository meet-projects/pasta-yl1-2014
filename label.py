import pygame

class Label(object):
	def __init__(self, rec1, rec2, surface1, surface2,text,bc,letter):
		self.rec = pygame.Rect(rec1, rec2, surface1, surface2)
		orderlabel = pygame.font.Font(None,letter)
		self.label = orderlabel.render(text, 1, (0, 0, 0), bc)


	def draw(self, screen):
		screen.blit(self.label,self.rec)




	
	# 630, 730, 150, 50