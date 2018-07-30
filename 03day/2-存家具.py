class Home():
	def __init__(self,address,area):
		self.address = address
		self.area = area
		self.list = []
	def __str__(self):
		msg = "我的家在%s 面积是%d"%(self.address,self.area)
		return msg
	def zhuangjiaju(self,jiaju):
		if self.area < jiaju.area:
			print("不能再装了")
		else:
			self.list.append(jiaju)
			self.area = self.area - jiaju.area
	#def tellArea(return):
	#	return
class Bed():
	def __init__(self,brand,area):
		self.brand = brand
		self.area = area
	def __str__(self):
		msg = "床的品牌是%s 面积是%d"%(self.brand,self.area)
		return msg
laolijia = Home("北京市长安街10号",150)
print(laolijia)
shuangye = Bed("双叶",4)
for i in range(40):
	laolijia.zhuangjiaju(shuangye)













































