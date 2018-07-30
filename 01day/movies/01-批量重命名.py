import os
dir_name = input("请输入文件夹名字")
os.chdir(dir_name)
print(os.getcwd())
files = os.listdir(dir_name)
	for file in files:
		position = file.rfind(".")
		new_name = file[:position]+"必属精品"+file[position:]
		os.rename(file,new_name)


















