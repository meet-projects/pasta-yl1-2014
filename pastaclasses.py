class Pasta(object):
	def __init__(self,name ,price ,picture):

		self.name=name
		self.price=price
		self.picture=picture
a= Pasta("Fusilli",10,"fusilli.jpg"  )
b=Pasta("Penne",8, "penne_rigate.jpg")
c=Pasta("Forfalle",7,"Farfalle.jpg")
d=Pasta("Maccheroni",9,"Maccheroni.jpg")
e=Pasta("Cenneroni",12,"cenn.jpg")

class Pasta_sauces(object):
	def __init__(self,name,price,picture):
		self.name=name
		self.price=price
		self.picture=picture
f=Pasta_sauces("fresh tomato",2,"Fresh_Tomato_sauce.jpg")
g=Pasta_sauces("white bean",3,"white_bean_sauce.jpg")
h=Pasta_sauces("sauteed_garlic",4,"sauteed garlic.jpg")
i=Pasta_sauces("caprese",1,"caprese sauce.jpg")
j=Pasta_sauces("carbonara",5,"carbonara sauce.jpg")

class Extra_for_pasta(object):
	def __init__(self,name,price,picture):
		
		self.name=name
		self.price=price
		self.picture=picture

k=Extra_for_pasta("sweet potato",1,"sweet-potato.jpg)
l=Extra_for_pasta("mushroom",2,"mushroom1.jpg")
m=Extra_for_pasta("cheese,3,""cheese1.jpg)
n=Extra_for_pasta("olives",1,"olives1.jpg)
o=Extra_for_pasta("tuna",4,"tuna1.jpg)


