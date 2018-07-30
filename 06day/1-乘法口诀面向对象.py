class Table():
	def printTable(self):
		print(Table)
		for i in range(1,10):
			for j in range(1,i+1):
				print(str(j)+"*"+str(i)+"="+str(j*i),end=" ")
table = Table()
table.printTable()
 
