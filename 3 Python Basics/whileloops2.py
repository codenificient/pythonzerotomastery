#while Loops 2
#while or for?
for item in [1,2,3]:
	print(item)

i = 0
while i < len([1,2,3]):
	print(i)
	i += 1

print('\n')

#if we have a list	
my_list = [1,2,3]
for item in my_list:
	print(item)

i = 0
while i < len(my_list):
	print(my_list[i])
	i += 1


#simple, useful while Loop
while True:
	input('Say something: ')
	break
