#performance generators
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
def long_time():
	print('1')
	for i in range(1000000):
		i*5

@perf
def long_time2():
	print('2')
	for i in list(range(1000000)):
		i*5

long_time()
long_time2()

#generator function
def gener_fun(num):
	for i in range(num):
		yield i

for item in gener_fun(100):
	print(item)