class Person():
	def makemoney(self):
		print("打工挣钱")
class Father(Person):
	def makemoney(self):
		print("在电业局上班挣钱")
class Son(Person):
	def makemoney(self):
		print("在电子厂上班挣钱")
f = Father()
f.makemoney()
s = Son()
s.makemoney()
