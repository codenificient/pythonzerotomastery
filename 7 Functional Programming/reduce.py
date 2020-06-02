from functools import reduce
my_list = [2,3,5]

def accumulator(acc, item):
	print(acc, item)
	return acc + item

print(reduce(accumulator, my_list, 0))