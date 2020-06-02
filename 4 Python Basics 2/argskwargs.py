# *args and **kwargs

def super_func(*args): 
	#need to add a *
	print(*args)
	print(args)
	return sum(args)

print(super_func(1,2,3,4,5))

def super_func(*args, **kwargs):
	total = 0
	for items in kwargs.values():
		total += items 
	print(kwargs)
	return sum(args) + total

print(super_func(1,2,3,4,5, num1=6, num2=10))

#Rules: params, *args, default parameters, **kwargs