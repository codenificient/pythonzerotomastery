#creating own own objects
class PlayerCharacter:
	def __init__(self, name='Marcus', age='21'):
		self.name = name
		self.age = age
		

	def run(self):
		print('run')
	
player1 = PlayerCharacter('Cindy', 44)
player2 = PlayerCharacter('Tom', 23)

print(player1.name, player1.age)
print(player2.name, player2.age)
