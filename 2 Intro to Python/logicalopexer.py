#coding game
#is expert magician
is_magician = True
is_expert = True

if is_magician and is_expert:
  print('Well done! You are an expert magician!')
elif is_magician and not is_expert:
  print('At least, you\'re getting there')
else:
  print('You need magic powers')

#what if beginner magician
is_magician = True
is_expert = False

if is_magician and is_expert:
  print('You are an expert magician!')
elif is_magician and not is_expert:
  print('Keep going! At least, you\'re getting there')
elif not is_magician:
  print('You need magic powers')

#not a magician
is_magician = False
is_expert = False

if is_magician and is_expert:
  print('You are an expert magician!')
elif is_magician and not is_expert:
  print('At least, you\'re getting there')
else:
  print('Sorry, You need magic powers to play this game')