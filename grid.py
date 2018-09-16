"""
----- ----- -----
| 1 | | 2 | | 3 |
----- ----- -----
| 4 | | 5 | | 6 |
----- ----- -----
| 7 | | 8 | | 9 |
----- ----- -----
"""

def exampleGrid():
	a = 1
	for i in range(3):
		print('----- ----- -----')
		for j in range(3):
			print('| ', a, ' |', sep='', end=' ')
			a+=1
		print('\n', end='')
	print('----- ----- -----')

def playingGrid(grid):
	a = 0
	for i in range(3):
		print('----- ----- -----')
		for j in range(3):
			if grid[a] == 'X':
				print('| ',  grid[a], ' |', sep='', end=' ')
			else:
				print('|   |', sep='', end=' ')
			a+=1
		print('\n', end='')
	print('----- ----- -----')
