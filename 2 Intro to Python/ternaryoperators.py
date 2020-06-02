#Ternary Operators or conditional expressions
#condition_if_true if condition else condition_if_else
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
print(can_message)

#go away
is_friend = False
can_message = "message allowed" if is_friend else "Sorry, but we're not friends. Please go away!"
print(can_message)

#introducing short Circuits
is_friend = True
is_user = True
print(is_friend and is_user)

#if not
is_friend = True
is_user = False
print(is_friend and is_user)

#circut cut
is_friend = True
is_user = True
if is_friend and is_user:
  print('Best friends forever')

is_friend = True
is_user = False
if is_friend and is_user:
  print('Best friends are we?')
else:
  print('I want to be besties some day')

print('\n')
is_friend = True
is_user = False
if is_friend or is_user:
  print('Long live the Besties')

