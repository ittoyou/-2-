def fib(times):
	n = 0
	a,b = 0,1
	while n<times:
		yield b
		#print(b)
		a,b = b,a+b
		n+=1
	return 'return'