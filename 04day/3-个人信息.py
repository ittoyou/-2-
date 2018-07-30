class Infor():
	def __playGame(self,time):
		if time < 2:
			print("合理安排游戏时间")
		else:
			print("游戏时间过长，请让眼睛休息一会")
	def playGame(self,time):
		self.__playGame(time)
infor = Infor()
infor.playGame(8)
