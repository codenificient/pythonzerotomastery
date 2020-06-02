#@class methods
class PlayerCharacter:
	membership = True
	def __init__(self, name, age):
		self.name = name 
		self.age = age
	
	def shout(self):
		print(f'my name is {self.name}')

	@classmethod
	def adding_things(cls, num1, num2): #cls added within
		return num1 + num2

print(PlayerCharacter.adding_things(12, 34))