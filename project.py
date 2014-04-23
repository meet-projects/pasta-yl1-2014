import pygame
import button
import sys
import pastaclasses
import label
	
def drawpastascreen(main_screen):
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

	global ab
	ab = pastaclasses.Pasta("Fusilli","10","Fusilli.jpg")
	main_screen.blit(ab.picture, a.rec)
	global bb
	bb = pastaclasses.Pasta("Penne","8", "Penne_rigate.jpg")
	main_screen.blit(bb.picture, b.rec)
	global cb
	cb = pastaclasses.Pasta("Farfalle","7","Farfalle.JPG")
	main_screen.blit(cb.picture, c.rec)
	global db
	db = pastaclasses.Pasta("Maccheroni","9","Maccheroni.jpg")
	main_screen.blit(db.picture, d.rec)
	global eb
	eb = pastaclasses.Pasta("Cenneroni","12","cenn.jpg")
	main_screen.blit(eb.picture, e.rec)


def drawsaucescreen(main_screen):
	screen = "Sauces"
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

	fb=pastaclasses.Pasta_sauces("Fresh Tomato Sauce",2,"Fresh_Tomato_Sauce.jpg")
	main_screen.blit(fb.picture, a.rec)
	gb=pastaclasses.Pasta_sauces("White Bean Sauce",3,"white_bean_sauce.jpg")
	main_screen.blit(gb.picture, b.rec)
	hb=pastaclasses.Pasta_sauces("Sauteed Garlic Sauce",4,"sauteedgarlic.jpg")
	main_screen.blit(hb.picture, c.rec)
	ib=pastaclasses.Pasta_sauces("Caprese Sauce",1,"capresesauce.jpg")
	main_screen.blit(ib.picture, d.rec)
	jb=pastaclasses.Pasta_sauces("Carbonara Sauce",5,"carbonarasauce.jpg")
	main_screen.blit(jb.picture, e.rec)
	pastasauces = label.Label(175, 60, 700, 120, "Pasta Sauces", (255, 95, 84), 100)
	pastasauces.draw(main_screen)

def drawextrasscreen(main_screen):
	screen = "Extras"
	global a
	a = button.Button(50, 175, 200, 150)
	a.draw(main_screen)
	global b
	b = button.Button(300, 175, 200, 150)
	b.draw(main_screen)
	global c
	c = button.Button(550, 175, 200, 150)
	c.draw(main_screen)
	global d
	d = button.Button(170, 410, 200, 150)
	d.draw(main_screen)
	global e
	e = button.Button(420, 410, 200, 150)
	e.draw(main_screen)
	
	kb=pastaclasses.Extra_for_pasta("Sweet Potato",1,"sweet-potato.jpg")
	main_screen.blit(kb.picture, a.rec)
	lb=pastaclasses.Extra_for_pasta("Mushroom",2,"mushroom.jpg")
	main_screen.blit(lb.picture, b.rec)
	mb=pastaclasses.Extra_for_pasta("Cheese",3,"cheese.jpg")
	main_screen.blit(mb.picture, c.rec)		
	bn=pastaclasses.Extra_for_pasta("Olives",1,"olives.jpg")
	main_screen.blit(bn.picture, d.rec)
	ob=pastaclasses.Extra_for_pasta("Tuna",4,"tuna.jpeg")
	main_screen.blit(ob.picture, e.rec) 
	


	next=label.Label(530, 730, 150, 58,"Next ===>",(255, 95, 84),56)
	next.draw(main_screen)

	back=label.Label(130, 730, 150, 58,"<=== Back",(255, 95, 84),56)
	back.draw(main_screen)

	pasta = label.Label(300, 60, 700, 120, "Pasta", (255, 95, 84), 100)
	pasta.draw(main_screen)
	



if __name__ == "__main__":
	pygame.init()
	main_screen = pygame.display.set_mode((800,800))
	main_screen.fill((255, 95, 84))

	screen = "Pasta"

	drawpastascreen(main_screen)
	drawsaucescreen(main_screen)
	drawextrasscreen(main_screen)

	order=[]
	sausess =[]
	extrass = []

	while True:
		ev = pygame.event.poll()
		if ev.type == pygame.QUIT:
			sys.exit()
		if ev.type == pygame.MOUSEBUTTONDOWN:
			x, y = ev.pos
			if a.rec.collidepoint(x, y):
				if screen == "Pasta":
					print "You ordered Fusilli"
					order.append(ab.name)
				elif screen == "Sauces":
					print "You ordered Fresh Tomato Sauce"
					sausess.append(fb.name)
				else:
					print "You ordered Sweet Potato"
					extrass.append(kb.name)
			if b.rec.collidepoint(x, y):
				if screen == "Pasta":
					print "You ordered Penne"
					order.append(bb.name)
				elif screen == "Sauces":
					print "You ordered White Bean Sauce"
					sausess.append(gb.name)
				else:
					print "You ordered Mushrooms"
					extrass.append(lb.name)
			if c.rec.collidepoint(x, y):
				if screen == "Pasta":
					print "You ordered Farfalle"
					order.append(cb.name)
				elif screen == "Sauces":
					print "You ordered Sauteed Garlic"
					sausess.append(hb.name)
				else :
					print "You ordered Cheese"
					extrass.append(mb.name)
			if d.rec.collidepoint(x, y):
				if screen == "Pasta":
					print "You ordered Maccheroni"
					order.append(db.name)
				elif screen == "Sauces":
					print "You ordered Caprese Sauce"
					sausess.append(ib.name)
				else:
					print "You ordered Olives"
					extrass.append(bn.name)
			if e.rec.collidepoint(x, y):
				if screen == "Pasta":
					print "You ordered Cenneroni"
					order.append(eb.name)
				elif screen == "Sauces":
					print "You ordered Carbonara Sauce"
					sausess.append(jb.name)
				else:
					print "You ordered Tuna"
					extrass.append(ob.name)
			#if next.rec.collidepoint(x, y):
				#if screen == "Pasta":
					#print "Keep going to Pasta Sauces!"
			#if back.rec.collidepoint(x,y):
			#	if screen == "Pasta_sauces":

			#		print "Back to Pasta"

					
				if screen == "Sauces":
					print "Keep going to Extras!"
					next=label.Label(110, 730, 150, 58,"    CHECK OUT  ",(255, 95, 84),56)
					next.draw(main_screen)




					pastasauces = label.Label(175, 60, 700, 120, "Pasta  Extras ", (255, 95, 84), 100)
					pastasauces.draw(main_screen)
					
					
					screen = "check"
				elif screen == "check":
					
					main_screen.fill((255, 95, 84))
					pastasauces = label.Label(2, 60, 700, 120, "You ordered:" , (255, 95, 84),60)
					pastasauces.draw(main_screen)

				    #xindex = 0
					#for x in order:
					#	xx = label.Label(2+xindex, 180, 700, 120, x , (255, 95, 84),60)
					#	xx.draw(main_screen)
					#	xindex += 120
					#	Wiith = label.Label(2, 300, 700, 120, "With" , (255, 95, 84),60)
					#	Wiith.draw(main_screen)

					#yindex = 0
					#for y in sausess:
					#	yy = label.Label(2+yindex, 420, 700, 120,  y , (255, 95, 84),60)
					#	yy.draw(main_screen)
					#	yindex+= 240
					#	Annd = label.Label(2, 540, 700, 120, "And" , (255, 95, 84),60)
					#	Annd.draw(main_screen)

					#uindex = 0
					#for u in extrass:
					#	uu = label.Label(2+ uindex, 660, 700, 120,   u , (255, 95, 84),60)
					#	uu.draw(main_screen)
					#	uindex+= 360
					#next=label.Label(200, 730, 150, 58,"BON APPETIT",(125, 22, 22),56)
					#next.draw(main_screen)

				




		pygame.display.flip()
