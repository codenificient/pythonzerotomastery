#dunder exercises 

class SuperList(list):
	def __len__(self):
		return 1000

list1 = SuperList()
print(len(list1))
list1.append(6)
print(list1[0])
print(issubclass(SuperList, list))