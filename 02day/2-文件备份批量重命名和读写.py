def print_menu():
	print("1.文件备份")
	print("2.文件批量重命名")
	print("3.文件读取")
	print("4.文件写入")
	fun = int(input("请选择功能"))
	if fun == 1:
		name = input("请输入要备份的文件名字:")
		f = open(name,"r")
		position = name.rfind(".")
		newname = name[:position]+name[position:]
		f1 = open(newname,"w")
		while True:
			content = f.read(1024)
			f1.write(content)
			if content == "": #len(content) == 0
				break
		f.close()
		f1.close()
	if fun == 2:
		import os
		dir_name = input("请输入要重命名的文件")
		files = os.listdir(dir_name)
		for file in files:
			position = file,rfind(".")
			new_name = file[:position]+file[position:]
			os.rename(file,new_name)
	if fun == 3:
		name = input("请输入要读取的文件")
		f = open(name,"r")
		content = f.read()
		print(content)
	if fun == 4:
		name = input("请输入要写入的文件")
		f =open(name,"w")
		f.write(content)
		f.close











