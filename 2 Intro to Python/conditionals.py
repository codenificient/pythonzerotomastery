is_old = True
is_licensed = True

if is_old:
  print('you are old enough to drive')

else:
  print('You cannot drive this Maserati! Try a Pontiac instead')

#elif
is_old = False
is_licensed = True

if is_old:
  print('you are old enough to drive')

elif is_licensed:
  print('You are licensed, but you are not old enough to drive this Lambo! A golf cart might be in order')

#both
is_old = True
is_licensed = False

if is_old and is_licensed:
  print('You are old enough to drive and you are licensed to drive any car you want!')

else:
  print('You may be old enough, but you need a license to drive!')

  #truthy or Falsey
  is_old = 'hello'
  is_licensed = 5

print (bool('hello'))
print(bool(None))

#falsy is any blank, or zero, empty, false, None, etc

password = '123'
username = 'johnny'
if password and username:
  print('you are cool enough to drive')