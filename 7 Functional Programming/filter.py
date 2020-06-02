#filter function
my_list = [1, 2, 4, 3, 6, 9]

def odds_only(item):
	return item % 2 != 0

print(list(filter(odds_only, my_list)))
print(my_list)