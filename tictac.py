board = []

for i in range(3):
    board.append(["1"] * 3)

def back_board(board):
	for row in board:
		print "".join(row)

def check(row, col, board):
	if board[row][col] != "1":
		return False
	else:
		return True


def Win_check(board):
	if board[0][0] == board[0][1] == board[0][2] == "O" or board[0][0] == board[0][1] == board[0][2] == "X":
		return True
	elif board[1][0] == board[1][1] == board[1][2] == "O" or board[1][0] == board[1][1] == board[1][2] == "X":
		return True
	elif board[2][0] == board[2][1] == board[2][2] == "O" or board[2][0] == board[2][1] == board[2][2] == "X":
		return True
	elif board[0][0] == board[1][0] == board[2][0] == "O" or board[0][0] == board[1][0] == board[2][0] == "X":
		return True
	elif board[0][1] == board[1][1] == board[2][1] == "O" or board[0][1] == board[1][1] == board[2][1] == "X":
		return True
	elif board[0][2] == board[1][2] == board[2][2] == "O" or board[0][2] == board[1][2] == board[2][2] == "X":
		return True
	elif board[0][0] == board[1][1] == board[2][2] == "O" or board[0][0] == board[1][1] == board[2][2] == "X":
		return True
	elif board[0][2] == board[1][1] == board[2][0] == "O" or board[0][2] == board[1][1] == board[2][0] == "X":
		return True
	else:
		return False

def input_num(type):
	num = raw_input("%s :" % (type))
	if num.isdigit() == False:
		print "put number! do it again!"
		return input_num(type)
	else:
		if 1<= int(num) <=3:
			return int(num)-1
		else:
			print "put number between 1~3 do it again!"
			return input_num(type)
count = 0

while True :

	while True:
		player1_row = input_num('1_row')
		player1_col = input_num('1_col')
		if check(player1_row, player1_col, board) == True:
			board[player1_row][player1_col] = "O"
			back_board(board)
			break
		else:
			print "already picked!"

	if Win_check(board):
		print "Player 1 win!"
		break
	else:
		count += 1

	if count == 9:
		print "Tie!"
		break

	while True:
		player2_row = input_num('2_row')
		player2_col = input_num('2_col')
		if check(player2_row, player2_col, board) == True:
			board[player2_row][player2_col] = "X"
			back_board(board)
			break
		else:
			print "already picked!"
	
	if Win_check(board):
		print "Player 2 win!"
		break
	else:
		count += 1

	if count == 9:
		print "Tie!"
		break



# if board[player1_row()][player1_col()] != "1":
# 	print "joongbok!"
# else:
# 	board[player1_row()][player1_col()] = "O"
# 	print "no joongbok!"

# back_board(board)
# if board[player2_row()][player2_col()] != 1:
# 	print "joongbok!"
# else:
# 	pass
	


# def player2_select():
# 	p2_row = int(raw_input("P2 Guess Row :"))
# 	p2_col = int(raw_input("P2 Guess Col :"))


