class A():
	def printA(self):
		print("A")
class B():
	def printB(self):
		print("B")
class C(A,B):
	def printC(self):
		print("C")
c = C()
c.printA()
c.printB()
