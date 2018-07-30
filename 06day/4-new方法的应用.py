class Dog(object):
	def __init__(self):
		print("init")
		self.name = "欧迪"
	def __new__(cls):
		print("new")
		return object.__new__(cls)
dog = Dog()
print(dog)

