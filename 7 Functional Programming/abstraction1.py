#principle of Abstraction
#private variables
class PlayerCharacter:
	def __init__(self, name, age): #underscore is a Dunder method, we never write our own in Python
		self._name = name
		self._age = age
#the underscore marks it as private, however might later be able to access
	def run(self):
		print('Run!')

	def speak(self):
		print(f'My name is {self._name}, and I am {self._age} years old')
	
player1 = PlayerCharacter('Chris', 130)
print(player1.speak())

player1 = PlayerCharacter('Christus', 114)
player1.name = '!!!'
player1._speak = 'BOOOO'
print(player1._speak)
#we can still change reassign BOOO to the value of speak