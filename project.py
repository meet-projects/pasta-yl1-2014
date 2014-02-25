import pygame
#import button
import sys

if __name__ == "__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((800,800))
	main_screen.fill((255, 95, 84))

	button_rec1 = pygame.Rect(100, 100, 100, 40)
	button_sq = pygame.Surface([100, 40])
	main_screen.blit(button_sq, button_rec1)

	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT:
			sys.exit()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x, y = ev.pos
			if button_rec1.collidepoint(x, y):
				print "You ordered a pasta! Bon Apetite!"
		pygame.display.flip()
