#object oriented programming revision
class PlayerCharacter():
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def run(self):
		return self
	
player1 = PlayerCharacter('Chris', 100)
print(player1.run())