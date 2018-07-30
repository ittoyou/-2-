def A(fn):
	def B():
		return '<b>' + fn() +'</b>'
	return B
def C(fn):
	def B():
		return '<i>' + fn() +'</i>'
	return B
@A
def test1():
	return 'well done-1'
@C
def test2():
	return 'well done-2'
@A
@C
def test3():
	return 'well done-3'
print(test1())
print(test2())
print(test3())























