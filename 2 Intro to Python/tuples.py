#Tuples
my_tuple = (1, 2, 3, 4, 5)
new_tuple = my_tuple[1:2]
print(new_tuple)
#prints with coma at the end

my_tuple = (1, 2, 3, 4, 5)
new_tuple = my_tuple[1:4]
print(new_tuple)

my_tuple = (1, 2, 3, 4, 5)
x = my_tuple[0]
y = my_tuple[1]
print(x, y)

x,y,z, *other = (1, 2, 3, 4, 5, 6) 
print(other)

#tuple methods; count(), index()
my_tuple = (1, 2, 3, 4, 5, 6, 5) 
print(my_tuple.count(5)) #can only count occurence of values in tuple, do not confuse with len function
print(len(my_tuple))