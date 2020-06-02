#practice Recursion  
def countdown(x):
	if x == 0:
		print("Done")
		return
	else:
		print(x, "...")
		countdown(x-1)
	
countdown(6)

#countdown with multiples of 9
def countdown(x):
	if x == 0:
		prev = x
		print("Now Zero")
		return
	else:
		print('Not zero,', x, 'left')
		countdown(x-9)
	
countdown(99)

#review the use of / in mathematical operations