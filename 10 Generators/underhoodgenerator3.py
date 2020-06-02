#gen with waffle
class smallWaffle():
	order = 3
	def __init__(self, paid):
		self.paid = paid

	def __iter__(self):
		return self
	
	def __next__(self):
		if smallWaffle.order < self.paid:
			cost = smallWaffle.order
			smallWaffle.order +=2
			return cost
		raise StopIteration
Breakfast = smallWaffle(20)
for maple_syr in Breakfast:
	print(maple_syr)