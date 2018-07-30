#coding=utf-8
import os
import time
pid = os.fork()
if pid == 0:
	print("你好")
else:
	print("他挺好")
pid = os.fork()
if pid == 0:
	print("他好")
else:
	print("我也很好")
time.sleep(2)
