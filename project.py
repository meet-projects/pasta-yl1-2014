import pygame
import button
import sys
import pastaclasses
import label
	
if __name__ == "__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((800,800))
	main_screen.fill((255, 95, 84))

	screen = "Pasta"


	a = button.Button(50, 175, 200, 150)
	a.draw(main_screen)
	b = button.Button(300, 175, 200, 150)
	b.draw(main_screen)
	c = button.Button(550, 175, 200, 150)
	c.draw(main_screen)
	d = button.Button(170, 410, 200, 150)
	d.draw(main_screen)
	e = button.Button(420, 410, 200, 150)
	e.draw(main_screen)

	next=label.Label(630, 730, 150, 58,"next ---->",(255, 95, 84),56)
	next.draw(main_screen)

	pasta = label.Label(300, 60, 700, 120, "Pasta!", (255, 95, 84), 100)
	pasta.draw(main_screen)

	ab = pastaclasses.Pasta("Fusilli","10","Fusilli.jpg")
	main_screen.blit(ab.picture, a.rec)
	bb = pastaclasses.Pasta("Penne","8", "Penne_rigate.jpg")
	main_screen.blit(bb.picture, b.rec)
	cb = pastaclasses.Pasta("Forfalle","7","Farfalle.JPG")
	main_screen.blit(cb.picture, c.rec)
	db = pastaclasses.Pasta("Maccheroni","9","Maccheroni.jpg")
	main_screen.blit(db.picture, d.rec)
	eb = pastaclasses.Pasta("Cenneroni","12","cenn.jpg")
	main_screen.blit(eb.picture, e.rec)

	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT:
			sys.exit()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x, y = ev.pos
			if a.rec.collidepoint(x, y):
				if screen == "Pasta":
					print "You ordered Fusilli"
				elif screen == "Sauces":
					print "You ordered Fresh Tomato Sauce"
				elif screen == "Extras"
			if b.rec.collidepoint(x, y):
				if screen == "Pasta":
					print "You ordered Penne"
				elif screen == "Sauces":
					print "You ordered White Bean Sauce"
			if c.rec.collidepoint(x, y):
				if screen == "Pasta":
					print "You ordered Forfalle"
				elif screen == "Sauces":
					print "You ordered Sauteed Garlic"
			if d.rec.collidepoint(x, y):
				if screen == "Pasta":
					print "You ordered Maccheroni"
				elif screen == "Sauces":
					print "You ordered Caprese Sauce"
			if e.rec.collidepoint(x, y):
				if screen == "Pasta":
					print "You ordered Cenneroni"
				elif screen == "Sauces":
					print "You ordered Carbonara Sauce"
			if next.rec.collidepoint(x, y):
				if screen == "Pasta":
					print "Keep going to Pasta Sauces!"
				if screen == "Sauces":
					print "Keep going to Extras!"

				fb=pastaclasses.Pasta_sauces("fresh tomato",2,"Fresh_Tomato_Sauce.jpg")
				main_screen.blit(fb.picture, a.rec)
				gb=pastaclasses.Pasta_sauces("white bean",3,"white_bean_sauce.jpg")
				main_screen.blit(gb.picture, b.rec)
				hb=pastaclasses.Pasta_sauces("sauteed_garlic",4,"sauteedgarlic.jpg")
				main_screen.blit(hb.picture, c.rec)
				ib=pastaclasses.Pasta_sauces("caprese",1,"capresesauce.jpg")
				main_screen.blit(ib.picture, d.rec)
				jb=pastaclasses.Pasta_sauces("carbonara",5,"carbonarasauce.jpg")
				main_screen.blit(jb.picture, e.rec)
				
				screen = "Sauces"
				screen = "Extras"
				
				kb=Extra_for_pasta("sweet potato",1,"sweet-potato.jpg")
				main_screen.blit(kb.picture, a.rec)
				lb=Extra_for_pasta("mushroom",2,"mushroom1.jpg")
				main_screen.blit(lb.picture, b.rec)
				mb=Extra_for_pasta("cheese,3,""cheese1.jpg")
				main_screen.blit(mb.picture, c.rec)
				bn=Extra_for_pasta("olives",1,"olives1.jpg")
				main_screen.blit(bn.picture, d.rec)
				ob=Extra_for_pasta("tuna",4,"tuna1.jpg")
				main_screen.blit(ob.picture, e.rec) 

				pastasauces = label.Label(175, 60, 700, 120, "Pasta Sauces!", (255, 95, 84), 100)
				pastasauces.draw(main_screen)
		

		pygame.display.flip()
