#lambda functions
#only use them once, not store
#lambda param: action(param)
from functools	import reduce
my_list = [5,2,3]
print(list(map(lambda item: item*2, my_list)))
print(my_list)

print(list(filter(lambda item: item % 2 != 0, my_list)))

print(reduce(lambda acc, item: acc+item, my_list))