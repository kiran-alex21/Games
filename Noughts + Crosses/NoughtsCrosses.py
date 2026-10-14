board = [['-', '-', '-'], ## empty spaces should be '-'
		 ['-', '-', '-'],
		 ['-', '-', '-']]
player1 = 'O'
player2 = 'X'

def printBoard(board):
	print("1  2  3")
	for i, row in enumerate(board):
		print(row[0]," ", row[1]," ", row[2]," ", (i+1))

# check if move if playable
def moveConflict(move, board):
	col = move[0]
	row = move[1]
	if board[row][col] != '-':
		print("This space has already been taken, choose another space")
		return True
	else:
		return False

# checks if game is won
def won(board):
	won = False
	winner = None
	#row
	for row in board:
		if row[0] == row[1] == row[2]:
			won = True
			winner = row[0]
	#first column
	if board[0][0] == board[1][0] == board[2][0]:
		won = True
		winner = board[0][0]
	#second column
	elif board[0][1] == board[1][1] == board[2][1]:
		won = True
		winner = board[0][1]
	#third column
	elif board[0][2] == board[1][2] == board[2][2]:
		won = True
		winner = board[0][2]
	#diagonal 1
	if board[0][0] == board[1][1] == board[2][2]:
		won = True
		winner = board[0][0]
	#diagonal 2
	elif board[0][2] == board[1][1] == board[2][0]:
		won = True
		winner = board[0][2]
	#verify true winner, not empty board
	if won == True:
		if winner == '-':
			won = False
			winner = None
		else:
			print("The winner is", winner)
	return won

# check for draw TODO: FIX THIS
def draw(board):
	draw = False
	if not any('-' for row in board):
		draw = True
	return draw

# gets move from player until valid
def playerTurn(player, board):
	move = None
	print(f"It is {player}'s turn.")
	while move == None:
		col = input("What column number? (1, 2, or 3) ")
		row = input("What row number? (1, 2 or 3) ")
		try:
			move = [int(col)-1, int(row)-1] # conver individual strings to list of ints
			if move[0]>2 or move[1]>2: # check number within parameters
				move = None
				print("Please enter the row and column numbers 1, 2 or 3")
		except:
			move = None
			print("Please enter the column and row numbers as digits")
		if move != None:
			if moveConflict(move, board): # check for conflict
				move = None
	return move

# single turn
def round(player, board):
	move = playerTurn(player, board) # gets players move
	board[move[1]][move[0]] = player #updates board with move
	win= won(board) # check win
	drew = draw(board) # check draw
	if win:
		playing = False
	if drew:
		print("It is a Draw")
		playing = False
	else:
		playing = True
	printBoard(board) # prints board
	print("-------------------------------------------------")
	return playing

#main play loop
print("Welcome to Noughts and Crosses")
print("This is the play board:")
printBoard(board)
print("The game is 2 player, and alternates between moves until there is a winner.")
print("Have fun, and good luck!")
print("-------------------------------------------------")
playing = True
while playing == True:
	playing = round(player1, board)
	if not playing:
		break
	playing = round(player2, board)
print("Thank you for playing Noughts and Crosses")

# debug prints
# printBoard(board)
# print(won(board))
# print(draw(board))