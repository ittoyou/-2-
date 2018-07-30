class Plant():
	def __init__(self,name='植物',color='红色'):
		self.__name = name
		self.color = color
	def __test(self):
		print(self.__name)
		print(self.color)
	def test(self):
		print(self.__name)
		print(self.color)
class Flower(Plant):
	def flowerTest1(self):
		print(self.color)
	def flowerTest2(self):
		self.test()
P = Plant()
print(P.color)
P.test()
F = Flower(name = "玫瑰花",color ="蓝色")
F.flowerTest1()
F.flowerTest2()
