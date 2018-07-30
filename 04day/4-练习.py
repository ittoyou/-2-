class Cat():
	def __init__(self,name):
		self.name = name
	def __str__(self):
		return "我的名字是%s"%self.name
	def __del__(self):
		print("给点水口渴了")
	def wark(self):
		print("喵喵")
tom = Cat("tom")
tom1 = tom
del tom
print("欧弟，快点过来")	
	
