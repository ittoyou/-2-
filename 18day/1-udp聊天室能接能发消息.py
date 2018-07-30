from threading import Thread
from socket import *
s = None
ip = ''
port = 0
def send():
	while True:
		content = input('请输入发送内容:')
		s.sendto(content.encode('gb2312'),(ip,port))
def recv():
	while True:
		msg = s.recvfrom(1024)
		print('\r\s----%s\n请输入内容'%(msg[0].decode('gb2312'),msg[1][0]),end='')
		
def main():
	global s
	global ip
	global port
	port = int(input('请输入对方端口:'))
	ip = input('请输入对方ip:')
	s = socket(AF_INET,SOCK_DGRAM)
	s.bind(('',8888))
	t = Thread(target=send)
	t1 = Thread(target=recv)
	t.start()
	t1.start()
	t.join()
	t1.join()
if __name__ == '__main__':
	main()
