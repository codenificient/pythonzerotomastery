#polymorphism  
class User:
	def sign_in(self):
		print('Signed in')
	
	def attack(self):
		print('Katniss Do Nothing Everdeen')
	#attack method duplicated across the code
	
class Wizard(User):
	def __init__(self, name, power):
		self.name = name
		self.power = power

	def attack(self):
		User.attack(self) #another form
		print(f'{self.name} is attacking with power of {self.power}')

class Archer(User):
	global num_arrows
	def __init__(self, name, num_arrows):
		self.name = name
		self.num_arrows = num_arrows
	
	def attack(self):
			print(f'{self.name} is attacking with arrows: arrows left- {self.num_arrows}')

#polymorphism
wizard1 = Wizard('Merlin', 60)
archer1 = Archer('Robin', 30)

def player_attack(char):
	char.attack()

player_attack(wizard1)
player_attack(archer1)

#with for loops

for char in [wizard1, archer1]:
	char.attack()