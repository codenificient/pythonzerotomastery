#scope, what variable do i have access to?
if True:
	x = 10

def some_rando_func():
	total = 100
	print (x)
#will not print x inside the function  
print(x)

print('\n')
a = 1
#Scope Rules
def confusion():
	a = 5
	return a

print(a)
print(confusion())
print('\n')
a = 1

#let's make it confusing
def more_confusion():
	a = 5
	return a

print(more_confusion())
print(a)
#python only has access to a within the function, but not from outside the function due to scope
'''
THE RULES OF SCOPE
1 - start with local
2 - parent local scope?
3 - global, no indentation
4 - built in python functions
'''
