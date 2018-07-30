def w(type):
	def w1(fun):
		def inner():
			if type == 1:
				print("验证CF帐号信息")
			elif type == 2:
				print("验证LOL帐号信息")
			fun()
		return inner
	return w1
@w(1)
def player1():
	print("lw")
@w(2)
def player2():
	print("sp")
player1()
player2()
