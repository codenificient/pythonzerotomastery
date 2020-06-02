#sets, unordered collection of UNIQUE objects
my_set = {1, 2, 3, 4, 5}
print (my_set)

my_set = {1, 2, 3, 4, 5, 4, 5}
print (my_set)

my_set = {1, 2, 3, 4, 5, 4, 5}
my_set.add(100)
my_set.add(2)
print (my_set) #will ignore duplicates 2 and 5

#turn lists into sets
my_list = [1,2,3,4,5,5]
my_sets = set(my_list)
print(my_sets)

#unordered, unindexed
my_set = {1,2,3,4,5,5}
print(2 in my_set)
#will not print if using an index
