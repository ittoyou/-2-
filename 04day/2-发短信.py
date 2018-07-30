class Msg():
	def __sendMsg(self,money):
		if money > 0:
			print("可以发短信")
		else:
			print("余额不足，请及时充值")
	def sendMsg(self,money):
		self.__sendMsg(money)
msg = Msg()
msg.sendMsg(5)
