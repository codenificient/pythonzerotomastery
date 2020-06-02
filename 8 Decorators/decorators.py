#decorators
def hello():
	print('Helloooooooooooo')

greet = hello
del hello
print(greet())



def hello(func):
	func()
def greet():
	print('still here')

a = hello(greet)
print(a)