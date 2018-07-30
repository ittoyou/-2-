import os
import time
num = 0
pid = os.fork()
if pid == 0:
	num+=1
	print("好好的---num=%d"%num)
else:
	time.sleep(3)
	num+=1
	print("好好的---num=%d"%num)
