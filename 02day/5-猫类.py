class Cat():
	def eat(self):
		print("猫吃鱼和老鼠")
	def play(self):
		print("猫玩毛线球")
	def introduce(self):
		print("我的名字是:",self.name,"我的颜色是:",self.color,"我的性别是:",self.sex)
b = Cat()
b.eat()
b.play()
b.name = "jiafeimao"
b.color = "yellow"
b.sex = "male"
b.name = "bosimao"
b.color = "brown"
b.sex = "female"
b.introduce()










