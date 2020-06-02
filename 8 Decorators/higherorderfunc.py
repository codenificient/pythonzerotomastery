#Higher Order Function HOC
def greet(func):
	func()

def greet2():
	def func():
		return 5
	return func

#decorators2
def my_decorator(func):
	def wrap_func(greeting):
		print('*'*len(greeting))
		func(greeting)
		print('#'*len(greeting))
	return wrap_func

@my_decorator
def hello(greeting):
	print(greeting)
hello('you are mi favorita for life')
@my_decorator
def bye(greeting):
	print(greeting)

bye('See ya later!')

def my_decorator1(func):
	def wrap_func(*args, **kwargs):
		func(*args, **kwargs)
	return wrap_func

@my_decorator1
def say_hello(greeting, emoji=':('):
	print(greeting, emoji)

say_hello('hey you!')