#booleans, can either be true or False
True
False

name = 'Christian'
is_cool = False

is_cool = True #overrides previous boolean

print (name)
print(bool(is_cool))

print('\n')
print(bool(0))
print(bool(1))


#Sample Facebook profile

name = 'FB User John Doe'
age = 47

print('\n')
relationship_status = 'Single'

relationship_status = 'it\'s complicated'

print(relationship_status)


#Practice time, Let's write a program that will ask someone's year of birth, and can calculate the age

print('\n')
birth_year = input('What year were you born') 
operator = int(birth_year) #converts the input into an integer
age = 2019 - operator 
print(str(age)) 


#Instructor response

birth_year = input('What year were you born?')
age = 2019 - int(birth_year)
print(f'your age is: {age}')


#Exercise, Password Checker

#input(jayjay)
#input(secret)
username = input(" please enter your username ")
password = input(" Please enter Password ")
passwordlength = len(str(password))
hidden_password ='*' * passwordlength   #added per the instructor
print('{}, your password {} is {} letters long' .format (username, hidden_password, passwordlength))