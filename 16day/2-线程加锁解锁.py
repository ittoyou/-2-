from threading import Thread,Lock
import time
num = 0
mutexFlag=mutex.acquire(True)
def work1():
	global num
	for i in range(1000):
		mutex.acquire(True)
		num += 1
		mutex.replease()
	print("线程一%d"%num)
def work2():
	global num
	for i in range(1000):
		mutex.acquire(True)
		num += 1
		mutex.replease()
	print("线程二%d"%num)
t = Thread(target=work1)
t.start()
 
#延时一会，保证t1线程中的事情做完
time.sleep(1) 
t1 = Thread(target=work2)
t1.start()

