#finding duplicates some list  
some_list = ['a', 'b', 'c', 'd', 'b','c', 'm', 'n', 'n']

duplicates = []
for value in some_list:
	if some_list.count(value) > 1:
		if value not in duplicates:
			duplicates.append(value)
print(duplicates)
new_list = some_list.romove(duplicates)
print(new_list)