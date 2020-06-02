#default arguments
def say_hello(name, emoji):
	print(f'hello {name} {emoji}')

#positional arguments
say_hello('Mark', '😊')
say_hello('Gloria', '😍')
say_hello('Mario', '😜')

print('\n')
#keyword arguments
say_hello(emoji='💖', name='Sara')

#now by default
def say_hello(name='Darth Vader', emoji='🍒'):
	print(f'hello {name} {emoji}')

#positional arguments
say_hello('Mark', '😊') #both provided
say_hello('Gloria', ) #will use default emoji
say_hello(emoji='🏃‍♂️') #will use default name

print('\n')
#keyword arguments
say_hello(emoji='💖', name='Sara')
say_hello('Timmy') #will use default emoji