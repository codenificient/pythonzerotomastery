#principle of encapsulation
class PlayerCharacter:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def run(self):
		print('Run!')

	def speak(self):
		print(f'My name is {self.name}, and I am {self.age} years old')
	
player1 = PlayerCharacter('Chris', 130)
player1.speak()
player1.name = '!!!'
player1.speak = 'BOOOO'

print(player1.speak)
'''
the tuple below has access to the count method, which can be called, although we do not need to know how Count is implemented
'''
print((2,1,2,4,2,3,2).count(2))
print(len((2,1,2,4,2,3,2)))
#encapsulation allows packaging info nicely for access later, adds meaning