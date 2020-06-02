#iterables
user = {
  'name' : 'Golem',
  'age' : 5006,
  'can_swim' : False
}
for item in user:
  print (item)

  #keys and values
  user = {
  'name' : 'Golem',
  'age' : 5006,
  'can_swim' : False
}
for item in user.items():
  print (item)

for item in user.values():
  print (item)

for item in user.keys():
  print (item)

for item in user.items(): #unpacking
  key, value = item;
  print(key, value)

for key, value in user.items(): #shorthand way
  print(key, value)