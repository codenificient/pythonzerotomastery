#list, set, dictionary comprehension
my_list = []

for char in 'helloo':
	my_list.append(char)

print(my_list)

#my_list = [char for char in 'param']
my_list1 = [char for char in 'never forget']
print(my_list1)

my_list3 = [num for num in range(0,10)]
print(list(map(lambda num: num*2, my_list3)))

#better way
my_list4 = [num*8 for num in range(0,10)]
print(my_list4)

#filter only evens
my_list5 = [num**2 for num in range(0, 10) if num % 2 == 0]
print(my_list5)

simple_dctn = {
	'a': 9,
	'b': 2
}
my_dctn = {k:y**2 for k,y in simple_dctn.items()}
print(my_dctn)

a = [2,4,6]
my_dctn1 = {k:k*2 for k in a}
print(my_dctn1)