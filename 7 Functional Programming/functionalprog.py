#functional programming
#what is a pure function? give the same input, always return the same output. function should not produce any side effects

def multiply_by2(li):
	new_list = []
	for item in li:
		new_list.append(item*2)
	return new_list

print(multiply_by2([2,4,5]))

def take_the_square(li):
	list1 = []
	for item in li:
		list1.append(item*item)
	return list1

print(take_the_square([2, 5, 23]))

#in other words
def square_dat_as(li):
	list1 = []
	for item in li:
		list1.append(item**2)
	return list1

print(square_dat_as([3, 8, 15]))