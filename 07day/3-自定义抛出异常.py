class ShowError(Exception):
	def __init__(self,name):
		self.name = name
def main():
	try:
		n = input("请输入1.老王，2.老孙 :")
		if n == 1:
			raise ShowError(n)
	except ShowError as result:
		print("ShowError:输入的名字是%s"%(result.name))
	else:
		print("无异常")
main()
