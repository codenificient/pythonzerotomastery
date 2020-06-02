
def make_list(num):
	result = []
	for i in range(num):
		result.append(i*2)
	return result

my_list = make_list(100)
print(my_list)


def gen_fn(num):
	for i in range(num):
		yield i

for item in gen_fn(10):
	print(item**2)


def gen_fn(num):
	for i in range(num):
		yield i**3

g = gen_fn(13)
next(g)
next(g)
print(next(g))