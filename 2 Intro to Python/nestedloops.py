#Looping
for items in 'Zero to Mastery':
  print(items)

print('\n')

for item in [1, 6]:
  print(item *2) #wow, i was expecting 1 1 3 3 6 6 instead we got 2 6 12
  print(item + 5)

#nesting
for Mood in ['Happy', 'Merry', 'Sweet']:
  for Occasion in ['birthday', 'Christmas', 'Sixthteen']:
    print(Mood, Occasion)
	
	#iterable can be list, dict, tuple, string
	#iterated ->one by one check each item in the collection
  #can be iterated, can be checked item by item