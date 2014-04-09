import pygame
#import button
import sys

if __name__ =="__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((600, 600))
	main_screen.fill((235,171,178))

	button_rec1 = pygame.Rect(10 ,40 ,80 ,60)
	button_sq = pygame.Surface([80 ,60])
	#button.fill((133 , 49, 57))
	main_screen.blit (button_sq, button_rec1)

	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT:
			sys.exit()
		if ev.type == pygame.MOUSEBUTTONDOWN :
			x, y = ev.pos
			if button_rec1.collidepoint(x ,y):
				print "Pastaaaas"
		pygame.display.flip()
	
