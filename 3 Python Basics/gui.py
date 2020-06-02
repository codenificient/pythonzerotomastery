#functions revisited, def
def say_hello():
	print("Hello hommies!!")

say_hello()
print('\n')
picture = [
	[0,0,0,0,1,0,0,0,0],
	[0,0,1,1,1,1,0,0,0],
	[0,1,1,1,1,1,1,1,0],
	[1,1,1,1,1,1,1,1,1],
	[0,0,0,0,1,0,0,0,0],
	[0,0,0,0,1,0,0,0,0],
	[0,0,0,0,1,0,0,0,0],
	[0,0,0,1,1,1,0,0,0]
]

def show_tree():
	for row in picture:
		for value in row:
			if (value == 1):
				print('*', end='')
			else:
				print(' ', end='')
		print('')

show_tree()
print('\n')
show_tree()