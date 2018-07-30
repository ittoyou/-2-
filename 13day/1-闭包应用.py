def test(a,b):
	def inner(x):
		return a*x+b
	return inner
t = test(1,1)
print(t(2))
print(t(3))
print(t(4))
