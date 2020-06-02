#map
def take_the_square(item):
	return item**2
print(list(map(take_the_square, [2, 5, 7])))

my_list = [2, 4, 6]
def triple_bass(item):
	return item*3
print(list(map(triple_bass, my_list)))
print(my_list)
