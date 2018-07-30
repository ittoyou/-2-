import random
class PetShop(object):
	def __init__(self,animal_factory = None):
		self.pet_factory = animal_factory
	def show_pet(self):
		pet = self.pet_factory.get_pet()
		print('We have a lovely {}'.format(pet))
		print('It says {}'.format(pet.speak()))
		print('We also have {}'.format(self.pet_factory.get_food()))
class Dog():
	def speak(self):
		return "wolf"
	def __str__(self):
		return 'Dog'
class Cat():
	def speak(self):
		return("meow")
	def __str__(self):
		return 'Cat'
class DogFactory():
	def get_pet(self):
		return Dog()
	def get_food(self):
		return 'dog food'
class CatFactory():
	def get_pet(self):
		return Cat()
	def get_food(self):
		return 'cat food'
def get_factory():
	return random.choice([DogFactory,CatFactory])()
for i in range(3):
	shop = PetShop(get_factory())
	shop.show_pet()
	print('=' * 20)
