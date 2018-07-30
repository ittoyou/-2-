class Cat():
	__instance = None
	__flag = False
	def __new__(cls,*args,**kwargs):
		if not cls.__instance:
			cls.__instance = object.__new__(cls)
		return cls.__instance
	def __init__(self,name):
		if not self.__flag:
			self.name = name
			self.__flag = True

a = Cat("加菲猫")
b = Cat("汤姆猫")
print(id(a))
print(id(b))			
		
