class Tool():
	count = 0
	def __init__(self,name):
		self.name = name
		Tool.count += 1
	@classmethod
	def getCount(cls):
		return cls.count
tool1 = Tool("梯子")
tool2 = Tool("钳子")
tool3 = Tool("锯子")
t = Tool("梯子，钳子，锯子")
print(t.getCount())
print(Tool.getCount())
