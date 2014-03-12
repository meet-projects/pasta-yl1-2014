class Pasta(object):
	def __init__(self,name ,price ,picture):

		self.name=name
		self.price=price
		self.picture = pygame.image.load(picture)

	
class Pasta_sauces(object):
	def __init__(self,name,price,picture):
		self.name=name
		self.price=price
		self.picture=pygame.image.load(picture)


class Extra_for_pasta(object):
	def __init__(self,name,price,picture):
		self.name=name
		self.price=price
		self.picture=pygame.image.load(picture)

kb=Extra_for_pasta("sweet potato",1,"sweet-potato.jpg")
lb=Extra_for_pasta("mushroom",2,"mushroom1.jpg")
mb=Extra_for_pasta("cheese,3,""cheese1.jpg")
bn=Extra_for_pasta("olives",1,"olives1.jpg")
ob=Extra_for_pasta("tuna",4,"tuna1.jpg") 

ab= Pasta("Fusilli",10,"fusilli.jpg"  )
bb=Pasta("Penne",8, "penne_rigate.jpg")
cb=Pasta("Forfalle",7,"Farfalle.jpg")
db=Pasta("Maccheroni",9,"Maccheroni.jpg")
eb=Pasta("Cenneroni",12,"cenn.jpg")

fb=Pasta_sauces("fresh tomato",2,"Fresh_Tomato_sauce.jpg")
gb=Pasta_sauces("white bean",3,"white_bean_sauce.jpg")
hb=Pasta_sauces("sauteed_garlic",4,"sauteed garlic.jpg")
ib=Pasta_sauces("caprese",1,"caprese sauce.jpg")
jb=Pasta_sauces("carbonara",5,"carbonara sauce.jpg")