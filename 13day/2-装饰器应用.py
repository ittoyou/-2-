def w1(fun):
	def inner():
		print(----验证登录信息----)
		fun()
	return inner
@w1
def test():
	print(----开始转账作业----)


test()
