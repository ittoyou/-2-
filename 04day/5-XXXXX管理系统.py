class Student():
	def __init__(self,stuId,name,age,sex):
		self.stuId = stuId
		self.name = name
		self.age = age
		self.sex = sex
	def listenClass(self):
		print("上课")
	def __str__(self):
		return "我的学号是%s我的名字是%s我的年龄是%d我的性别是%s"%(self.stuId,self.name,self.age,self.sex)
class Manager():
	def __init__(self):
		self.list = []
	def add(self,student):
		self.list.append(student)
		for i in self.list:
			print(i)
	def find(self):
		pass
	def update(self):
		pass
	def remove(self):
		pass
class Menu():
	def __init__(self):
		self.m = Manager()
	def print_menu(self):
		print("欢迎来到学生管理系统")
		while True:
			fun == int(input("请选择功能1:添加,2:查找,3:修改,4:删除,5:打印信息"))
			if fun == 1:
				d = {}
				stuId = input("请输入学生学号")	
				name = input("请输入学生姓名")
				age = input("请输入学生年龄")
				sex = input("请输入学生性别")
				s = Student(stuId,name,age,sex)
				self.m.add(s)
			elif fun == 2:
				name = input("请输入要查找的学生姓名")
				flag = False
				for i in list:
					if name == i["name"]:
						print("学号:%s\n姓名:%s\n年龄:%d\n性别:%s"%(i["stuId"],i["name"],i["age"],i["sex"]))
						flag = True
						break
				if flag == False:
					print("查无此人")
			elif fun == 3:
				name = input("请输入要修改的学生姓名")
				flag = False
				for i in list:
					if name == i["name"]:
						print("1:修改学生学号")
						print("2:修改学生姓名")
						print("3:修改学生年龄")
						print("4:修改学生性别")
						num1 = int(input("请选择功能"))
						if num1 == 1:
							new_stuId = input("请输入新的学生学号")
							i["stuId"] = new_stuId
						elif num1 == 2:
							new_name = input("请输入新的学生姓名")
							i["name"] = new_name
						elif num1 == 3:
							new_age = input("请输入新的学生年龄")
							i["age"] = new_age
						elif num1 == 4:
							new_sex = input("请输入新的学生性别")
							i["sex"] = new_sex
			elif fun == 4:
				name = input("请输入要删除的学生姓名")
				flag = False
				for position,i in enumerate(list):
					if name == i["name"]:
						flag = True
						print("1:确认删除")
						print("2:取消删除")
						num2 = int(input("请选择功能"))
						if num2 == 1:
							list.pop(position)
						break
				if flag == False:
					print("查无此人")
			elif fun == 5:
				print("学号\t姓名\t年龄\t性别")
				for i in list:
					print(""+i["stuId"]+"\t "+i["name"]+"\t "+i["age"]+"\t "+i["sex"])
m = Menu
m.print_menu
		
