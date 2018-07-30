from socket import *
s = socket(AF_INET,SOCK_DGRAM)#创建一个udp套接字
s.bind(('',8888))#绑定端口
#发送
s.sendto('呵呵嘿嘿'.encode('gb2312'),('192.168.43.145',8080))
while True:
	msg = s.recvfrom(1024)
	print('消息是:%s 来自ip:%s'%(msg[0].decode('gb2312'),msg[1][0]))
s.close()
