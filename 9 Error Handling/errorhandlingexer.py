#error handling
while True:
	try:
		age = int(input('What is your age? '))
		print(age)
	except ValueError:
		print('Please enter a number')
	except ZeroDivisionError:
		print('please enter age higher than 0')
	else:
		print('Thank you!')
		break

#more errors 
def sum(num1, num2):
	try:
		return num1 / num2
	except (TypeError, ZeroDivisionError) as er1:
		print(f'Please enter numbers {er1}')
print(sum('1', 3))
print(sum(3, 0))