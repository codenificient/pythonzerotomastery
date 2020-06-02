#sets methods
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}

#difference
print(my_set.difference(your_set))
print(your_set.difference(my_set))


#discard
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}
print(my_set.discard(4))
print(my_set)
print(your_set.discard(9))
print(your_set)

#intersect, will be same from both pov
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}
print(my_set.intersection(your_set))
print(your_set.intersection(my_set))

#disjoint, boolean True means both have nothing in common
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}
print(my_set.isdisjoint(your_set))
print(your_set.isdisjoint(my_set))


#union, does not matter which order
my_set = {1,2,3,4,5}
your_set = {4,5,6,7,8,9,10}
print(my_set.union(your_set))
print(your_set.union(my_set))

#issubset, is part of another set in its entirety
my_set = {4,5}
your_set = {4,5,6,7,8,9,10}
print(my_set.issubset(your_set))
print(your_set.issubset(my_set))

#issuperset, contains one set in its entirety
my_set = {4,5}
your_set = {4,5,6,7,8,9,10}
print(my_set.issuperset(your_set))
print(your_set.issuperset(my_set))