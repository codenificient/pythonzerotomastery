#polymorphism  
class User(object):
	def __init__(self, email):
		self.email = email

	def sign_in(self):
		print('Signed in')
	
	
class Wizard(User):
	def __init__(self, name, power, email):
		User.__init__(self, email)
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

#polymorphism
wizard1 = Wizard('Merlin', 60, 'merlin@wizard.com')
archer1 = Archer('Robin', 30)

print(wizard1.email)