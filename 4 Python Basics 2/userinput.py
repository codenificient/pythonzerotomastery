#next level, ask for user input
def is_even(num):
	number = input('Pick a number')
	num = int(number)
	if num % 2 == 0:
		print(f'{num} is an even number')
	elif num % 2 != 0:
		print(f'{num} is an odd number')
is_even(8)