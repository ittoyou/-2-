from socket import *
s = socket(AF_INET,SOCK_DGRAM)#创建一个udp套接字
s.sendto('呵呵嘿嘿'.encode('gb2312'),('192.168.43.145',8080))
s.close()
