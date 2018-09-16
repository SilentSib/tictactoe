import grid

def main():
	print('Welcome to SilentSib\'s Tic-Tac-Toe game developed in Python!\n')
	print('Please find below the grid as you will use it in your game. When you want to play where 5 is located, you will need to input 5, and so on.\n')
	grid.exampleGrid()
	c = [''] * 9
	while True:
		try: 
			choice = int(input('\nIt\'s time to play. Where would you like to place your symbol at? '))
			a = 0
			for i in range(3):
				for j in range(3):
					if a==choice:
						c[a] = 'X'
					a+=1
			grid.playingGrid(c)
		except: 
			print('Incorrect value, please try again')

		

main()