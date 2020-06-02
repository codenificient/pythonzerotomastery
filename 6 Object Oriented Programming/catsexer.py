#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
KatyCat = Cat("KatyCat", 3)
MeerCat = Cat("MeerCat", 5)
Whiskers = Cat("Whiskers", 7)


# 2 Create a function that finds the oldest cat
def get_oldest_cat(*args):
  return max(args)

#print(f'the oldest cat is {oldest}')

print(f'The oldest cat is {get_oldest_cat(KatyCat.age, MeerCat.age, Whiskers.age)} years old')