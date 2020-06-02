#Inheritance from game  
class User:
	def sign_in(self):
		print('Signed in')
	
class Wizard(User):
	def __init__(self, name, power):
		self.name = name
		self.power = power

	def attack(self):
		print(f'{self.name} is attacking with power of {self.power}')

class Archer(User):
	global num_arrows
	def __init__(self, name, num_arrows):
		self.name = name
		self.num_arrows = num_arrows
	
	def attack(self):
			print(f'{self.name} is attacking with arrows: arrows left- {self.num_arrows}')

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Katniss', 150)
wizard1.attack()
archer1.attack()
archer1.attack()
