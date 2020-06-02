#exercise

def highest_even(li):
	even = []
	for items in li:
		if items % 2 == 0:
			even.append(items)
	return max(even)

print('The highest even number is this list [10,2,3,4,8,11] is', highest_even([10,2,3,4,8,11]))
