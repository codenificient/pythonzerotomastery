#strings 
#can be thought of as a sentence
print(type("hi, hello there 24!"))
username = 'supercoder'
password = 'supersecret'
long_string = '''
wow
O O
---
'''

print (long_string)
first_name = 'Christianus'
last_name = 'Silvastano'
full_name = first_name + ' '+ last_name

print(full_name)

#string concatenation
#adding strings together
print ('hello'+ ' '+'Andrei')

#more on strings
print(type(int(str (100))))

#another way to looking at the previous example
a = str(100)
b = int(a)
c = type(b)
print(c)
#this is called a type conversions



#Escape Sequence
weather = 'Its sunny' # creates an issue because of single quotation
weather = "It's sunny" #this works
#in order to use single quotes, backslash \ is added

weather = 'It\'s "kind of" sunny'
print(weather)

#backlash \t adds a new tab before printing the string
weather = "\t It's kind of sunny "
print(weather)
#backlash \n add a new license

weather = "\t it's kind of sunny \n \thope you have a good day!"
print (weather)


#formatted strings

name = 'Johnny'
age = 60
print ('\n hi ' + name + '. You are ' + str(age) + ' years old')

#that was too many pieces (and formatting errors)
#let's learn a better way :)

name = 'Johnny'
age = 59
print(f'\n hi {name}. You are {age} years old')


#introducing .format
#you can set your own values, or call previous variables with a string
print ('\n Hi {}. You are {} years old'.format('Sweetie', '12')) # I set my own variables Sweetie and 12
name = 'Johnny'
age = 11
print ('\n Hi {}. You are {} years old.' .format(name, age)) # I called the name and age variables stored above

#i can mix and match the order to result in more giberish
name = 'Backwards'
age = 17
print ('\n Hi {1}. You are {0} years old.' .format(name, age)) #notice i have added 0 and 1 in the brackets for the fun

#assigning new names will use the correct new names
name = 'Backwards'
age = 17
print ( '\n Hi {new_name}. You are {age} years old.\n' .format(new_name='Sally', age=100))

#str is an ordered sequence of characters. Each shelf corresponds to a value


#str are accessed based on the Index
selfish = 'me me me'
         # 01234567
print(selfish)
print('\n')
selfish = 'me me me'
         # 01234567
print(selfish[6])

#start:stop
selfish = 'me me me'
         # 01234567
print(selfish[0:2])

#stepover

selfish = '01234567'
         # 01234567
print(selfish[0:8:2]) #will grab all numbers in sequence and skip each 2nd number

selfish = '01234567'
         # 01234567
print(selfish[2:]) #this will start at 2 and go till the end of sequence; since no end indicated

selfish = '01234567'
         # 01234567
print(selfish[:5]) #will start from beginning, but stop at 5

selfish = '01234567'
         # 01234567
print(selfish[::2]) #will start and end by default, but skipping 2 each

selfish = '01234567'
         # 01234567
print(selfish[-3]) #will start from the end. Third from the end is 5

selfish = '01234567'
         # 01234567
print(selfish[::-1]) #we get the reverse of the sequence

selfish = '01234567'
         # 01234567
print(selfish[::-2]) #gives the reverse, but skipping by 2

#start;stop;stepover is referred to as String Slicing



#IMMUTABILITY . means that we cannot change strings.
selfish = '01234567'
         # 01234567
# selfish[0]= 8 #error messages

#we can only reassign a new value to the long_string

selfish = '01234567'
         # 01234567
selfish = selfish + '8'
print (selfish) #this adds 8 to the string, making it longer new string



print('\n')

#string length
print(len('heelloooo'))

greet = 'heellooo'
print(greet[0:len(greet)])


#string methods
quote = 'to be or not to be'
print(quote.upper())


quote = 'to be or not to be'
print(quote.capitalize())

quote = 'remember me my good friend, until our paths cross again'

print(quote.find('paths'))

#replace
quote = 'Forget about me, my dear ex, the world has moved on'

print(quote.replace('about me', 'you pretty face, I am rich and married now'))

print('\n')
quote = 'Belle marquise, tes beaux yeux me font mourir d\'amour'
quote1 = 'D\'amour me font mourir, belle marquise, tes beaux yeux'
print(quote.replace('tes beaux yeux me font mourir d\'amour', 'd\'amour me font mourir tes beaux yeux'))
print(quote)
print(quote1)