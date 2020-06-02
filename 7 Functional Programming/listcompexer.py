#list, set, dictionary comprehension
my_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = list(set([x for x in my_list if my_list.count(x) > 1]))
print(duplicates)