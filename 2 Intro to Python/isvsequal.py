#is vs ==
print(True == 1) #true
print('' == 1) #false
print([]==1) #false
print(10 == 10.0) #false
print([]== []) #true
#pause video and guess outcome

#is vs ==
#actual outcome
print(True == 1) #true
print('' == 1) #False
print([]==1) #false
print(10 == 10.0) #True
print([]== []) #true
#one wrong

#is
#is vs ==
print(True is 1) #true
print('' is 1) #false
print([] is 1) #false
print(10 is 10.0) #false
print([] is []) #true
#is looks for place in memory. usually not the same
print('\n')
#is vs ==
print(True == True) #true
print('1' is '1') #true
print([]==1) #false
print(10 is 10.0) #false
print(10 is 10) #true
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b) #false, different locations
print(a == b) #true for values
