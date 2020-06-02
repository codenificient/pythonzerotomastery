#lambda functions
#only use them once, not store
#lambda param: action(param)
from functools	import reduce
#Square
my_list = [5,4,3]
print(list(map(lambda item: item*item, my_list)))
print(my_list)

#list sorting
a = [(0,3), (4,3), (9,9),(10,-1)]
a.sort(key=lambda x: x[1])
print(a)
