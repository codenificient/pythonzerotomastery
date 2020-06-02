#tuple
#enumerate
for i,char in enumerate('Hellooo'):
	print(i, char) #iterate index number

#list
for i,char in enumerate(['a','b','c']):
	print(i, char)

#tuple
for i,char in enumerate((1,2,3)):
	print(i, char)

#exercise
for i,char in enumerate(list(range(100))):
	if char == 50:
		print(f'the index of 50 is: {i}') #review the format option