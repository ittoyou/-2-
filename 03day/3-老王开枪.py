import time
class Person():
	def __init__(self,name):
		self.name = name
		self.gun = None
		self.hp = 100
	def zhuangzidan(self,dan_jia,zi_dan):
		dan_jia.save_zidan(zi_dan)
	def zhuangdanjia(self,gun,dan_jia):
		gun.save_danjia(dan_jia)
	def takegun(self,gun):
		self.gun = gun
	def __str__(self):
		if self.hp > 0:
			if self.gun:
				return "%s的血量是:%d,他有枪!%s"%(self.name,self.hp,self.gun)
			else:
				return "%s的血量是:%d,他没有枪!"%(self.name,self.hp)
		else:
			return "%s已经死了..."%(self.name)
	def shoot(self,enemy):
		self.gun.fire(enemy)
	def diaoxue(self,hurt):
		self.hp -= hurt
class Gun():
	def __init__(self,name):
		self.name = name
		self.danjia = None
	def save_danjia(self,danjia):
		self.danjia = danjia
	def __str__(self):
		if self.danjia:
			return "枪的信息是:%s,%s"%(self.name,self.danjia)
		else:
			return "枪的信息是:%s,此枪无弹夹"%(self.name)
	def fire(self,enemy):
		receive_zidan = self.danjia.get_zidan()
		if receive_zidan:
			receive_zidan.dazhong(enemy)
		else:
			print("没子弹了...")
class Danjia():
	def __init__(self,max_num):
		self.max_num = max_num
		self.danjia_list = []
	def save_danjia(self,zidan):
		self.danjia_list.append(zidan)
	def __str__(self):
		return "弹夹信息是:%s/%s"%(len(self.danjia_list),self.max_num)
	def get_zidan(self):
		if self.danjia_list:
			return self.danjia_list.pop()
		else:
			return None
class Zidan():
	def __init__(self,hurt):
		self.hurt = hurt
	def dazhong(self,enemy):
		enemy.diaoxue(self.hurt)
laowang = Person("老王")
ak47 = Gun("AK47")
dan_jia = Danjia(30)
for i in range(15):
	zi_dan = Zidan(10)
	laowang.zhuangzidan(dan_jia,zi_dan)
laowang.zhuangdanjia(ak47,dan_jia)
print(dan_jia)
print(ak47)
laowang.takegun(ak47)
print(laowang)





































































































