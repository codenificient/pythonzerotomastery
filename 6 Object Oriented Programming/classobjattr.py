#class object Attribute 
class PlayerCharacter:
	membership = True 
	def __init__(self, name, age):
		if (PlayerCharacter.membership):
			self.name = name
			self.age = age

	def shout(self):
		print(f'My name is {self.name}, and I am {self.age}🤓')

player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 23)

print(player1.shout())
print(player2.shout())