class People():
	def __init__(self,newname,newheight,newweight):
		self.name = newname
		self.height = newheight
		self.weight = newweight
	def introduce(self):
		print("我的名字是%s 我的身高是%d 我的体重是%d"%(self.name,self.height,self.weight))
name = input("请输入名字")
height = int(input("请输入身高"))
weight = int(input("请输入体重"))
litian = People(name,height,weight)
litian.introduce()












