#counter
my_list = [1,2,3,4,5,6,7,8,9,10]
counter = 0 #need variable outside loop
for item in my_list:
	counter = counter + item
print(counter) #not part of the indentation. else, will loop over each item