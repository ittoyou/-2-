class Dog(object):
	__instance = None
	def __new__(cls,*args,**kwargs):
		if cls.__instance == None:
			cls.__instance = super().__new__(cls)
			return  cls.__instance
		else:
			return cls.__instance
	def __init__(self,name):
		
		self.name = name
dog1 = Dog("xiaoming")
print(dog1)
#print(id(dog1))
dog2 = Dog("xiaohong")
print(dog2)
#print(id(dog2))
