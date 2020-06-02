#transition to logical operators
print(4 == 5)
print(4 > 5)
print (4 < 5)

#cannot use the equal sign because it is part of python key words 
print('hello'== 'hello')
print('a' == 'b')
#last example probably false because string values do not equal each other
print('a'> 'b') #it says false?
print('a'> 'A') #it says true, wth?

#logical operators should be used with numbers

print(1<2<3<4)
print(1<2>3<4)
print(1>=0)
print(0 <= 0)
print(1 != 2) #1 not equal to 2

#Not
print(not(True))
print(not(1 == 2))