class Person():
	print("说话，吃饭，睡觉，听音乐，看视频")
class Man(Person):
	def makemoney(self):
		print("挣钱")
class Women(Person):
	def teachchildren(self):
		print("教育孩子")
man = Man()
man.makemoney()
women = Women()
women.teachchildren()	
