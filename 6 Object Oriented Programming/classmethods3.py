#@class methods
class PlayerCharacter:
	membership = True
	def __init__(self, name, age):
		self.name = name 
		self.age = age
	
	def shout(self):
		print(f'my name is {self.name}')
	@classmethod
	def adding_thing(cls, num1, num2):
		return cls('Teddy', num1 + num2)
player3 = PlayerCharacter.adding_thing(7, 9)
print(player3.age)

@staticmethod
def adding_thing2(num1, num2):
		return num1 + num2
player3 = PlayerCharacter.adding_thing2(27, 2)
print(player3.age)