#Clean Code
def is_odd_or_even(num):
	if num % 2 == 0:
		print(f'{num} is even')
	elif num % 2 != 0:
		print(f'{num} is odd')

is_odd_or_even(50)
is_odd_or_even(69)