#return, it exits the function. use indentation right after to allow code to run  
def sum(num1, num2):
	return num1 + num2

print(sum(4, 564))
#a function should do something very well
# a function should return something

def sum(num1, num2):
	def another_funct(n1, n2):
		return n1 + n2
	return another_funct(num1, num2)

total = sum(10,5) #result15
print(sum(180, total))

def sum(num1, num2):
	return num1 + num2
print(sum(4, 564))