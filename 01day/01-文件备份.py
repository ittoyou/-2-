name = input("请输入要备份的文件名字")
f = open(name,"r")
while True:
	if f.read(1024) == "":
		break
		content = f.read(1024)
p = name.rfind(".")
f1 = open(name[:p]+"back"+name[p:],"w")
f1.write(content)
f.close()
f1.close()





















