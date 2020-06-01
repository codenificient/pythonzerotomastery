#fibonacci sequence
from time import time
def perf(fn):
	def wrapper(*args, **kwargs):
		t1 = time()
		result = fn(*args, **kwargs)
		t2 = time()
		print(f'took {t2-t1} seconds')
		return result
	return wrapper

@perf
def fib(number):
	a = 0
	b = 1
	for i in range(number):
		yield a
		temp = a
		a = b
		b = temp + b

for x in fib(30):
	print(x)

@perf
def fib2(number):
	a = 0
	b = 1
	result = []
	for i in range(number):
		result.append(a)
		temp = a
		a = b
		b = temp + b
	return result
print(fib2(30))