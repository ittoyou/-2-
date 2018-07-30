class ParentClass(object):
	'''创建一个计算机运行的父类'''
	def __init__(self,x,y):
		self.x = x
		self.y = y
		pass
	def operation(self):
		'''
		定义一个操作函数
		:return:
		'''
		pass
class AddOp(ParentClass):
	'''加法'''
	def __init__(self,x,y):
		super(AddOp,self).__init__(x,y)
		pass
	def operation(self):
		return self.x +self.y
class JianOp(ParentClass):
	'''减法'''
	def __init__(self,x,y):
		super(JianOp,self).__init__(x,y)
		pass
	def operation(self):
		return self.x - self.y
class FactoryClass(object):
	'''创建工厂类'''
	def __init__(self):
		pass
	def create_class(self,op,x,y):
		if op == '+':
			return AddOp(x,y)
		elif op == '-':
			return JianOp(x,y)
if __name__ == '__main__':
	factory = FactoryClass()
	add = factory.create_class('+',7,8)
	print(add.operation())
	jian = factory.create_class('-',5,13)
	print(jian.operation())
