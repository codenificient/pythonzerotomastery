#GIU graphical user interface
picture = [
	[0,0,0,0,1,0,0,0,0],
	[0,0,1,1,1,1,0,0,0],
	[0,1,1,1,1,1,1,1,0],
	[1,1,1,1,1,1,1,1,1],
	[0,0,0,0,1,0,0,0,0],
	[0,0,0,0,1,0,0,0,0],
	[0,0,0,0,1,0,0,0,0]
]
for row in picture:
	for value in row:
		if (value == 1):
			print('*', end='')
		else:
			print(' ', end='')
	print('')