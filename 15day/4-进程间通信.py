'''
from multiprocessing import Queue
q=Queue(3)
q.put('ab')
q.put('bc')
print(q.full())
q.put('cd')
print(q.full())
try:
	q.put('de',True,2)
except:
	print("字母列队已满，现有字母数量:%s"%q.qsize())
try:
	q.put_nowait('de')
except:
	print('字母列队已满，现有字母数量:%s'%q.qsize())
if not q.full():
	q.put_nowait('de')
if not q.empty():
	for i in range(q.qsize()):
		print(q.get_nowait())
'''
from multiprocessing import Manager,Pool

