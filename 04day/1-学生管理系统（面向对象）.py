class Student():
	def __init__(self,stuID,name,age):
		self.stuID = stuID
		self.name = name
		self.age = age 
	def studentoop(self):
		pass
new_stuID = ""
new_name = ""
new_age = ""
class Sys():
	def __init__(self):
		pass
	def show_menu(self):
		print("=" * 60)
		print("学生管理系统".center(50," "))
		print("1:添加用户信息".center(50," "))
		print("2:查询用户信息".center(50," "))
		print("3:修改用户信息".center(50," "))
		print("4:删除用户信息".center(50," "))
		print("5:显示用户信息".center(50," "))
		print("6:退出系统".center(50," "))
		print("=" * 60)
	def getinfo(self):
		global new_stuID
		global new_name
		global new_age
		new_stuID = input("请输入学号:")
		new_name = input("请输入名字:")
		new_age = input("请输入年龄:")
	def add_stus(self):
		self.getinfo()
		students[new_stuID] = Student(new_stuID,new_name,new_age)
		print("ID:%s"% students[new_stuID].stuID,"Name:%s"% students[new_stuID].name,"Age:%s"% students[new_stuID].age)
	def find_stus(self):
		find_nameID = input("请输入要查找的学号:")
		if find_nameID in students.keys():
			print("学号:%s\t名字:%s\t年龄:%s"% (students[new_stuID].stuID,students[new_stuID].name,students[new_stuId].age))
		else:
			print("查无此人")
	def alter_stus(self):
		alterID = input("请输入要修改的学生学号:")
		self.getinfo()
		if alterID in students.keys():
			students[new_stuID] = Student(new_stuID,new_name,new_age)
			del students[alterID]
		else:
			print("查无此人")
	def del_stus(self):
		cut_nameID = input("请输入要删除的学生学号:")
		if cut_nameID in students.keys():
			del students[cut_nameID]
		else:
			print("查无此人")
	def show_stus(self):
		for new_stuID in students:
			print("ID:%s"% students[new_stuID].stuID,"Name:%s"% students[new_stuID].name,"Age:%s"% students[new_stuID].age)

	def exit_stus(self):
		print("欢迎下次使用")
		exit()
sys = Sys()
students = {}
while True:
	sys.show_menu()
	choice = int(input("请选择功能:"))
	if choice == 1:
		sys.add_stus()
	elif choice == 2:
		sys.find_stus()
	elif choice == 3:
		sys.alter_stus()
	elif choice == 4:
		sys.del_stus()
	elif choice == 5:
		sys.show_stus()
	elif choice == 6:
		sys.exit_stus()
	else:
		print("输入有误，请重新输入")













