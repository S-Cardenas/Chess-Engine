from Pawn import Pawn
from Knight import Knight
from Bishop import Bishop
from Rook import Rook
from Queen import Queen
from King import King

#Creates the starting position of pieces on chess board
def start_board():
	#Addresses of coordinates and starting position of chess pieces
	Xdirection = ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH', 0]
	Ydirection = ['11', '22', '33', '44', '55', '66', '77', '88', 0]
	White_Royalty = [4, 2, 3, 5, 6, 3, 2, 4]
	White_Pawns = [1, 1, 1, 1, 1, 1, 1, 1]
	Black_Royalty = [-4, -2, -3, -5, -6, -3, -2, -4]
	Black_Pawns = [-1, -1, -1, -1, -1, -1, -1, -1]
	
	board = []
	for i in range(81):
		board.append(0)
	k = 0
	for i in range(9):
		for j in range(9):
			if i == 0:
				if j <= 7:
					board[k + j] = White_Royalty[j]
				else:
					board[k + j] = Ydirection[i]
			elif i == 1:
				if j <= 7:
					board[k + j] = White_Pawns[j]
				else:
					board[k + j] = Ydirection[i]
			elif i > 1 and i < 6:
				if j <= 7:
					board[k + j] = 0
				else:
					board[k + j] = Ydirection[i]
			elif i == 6:
				if j <= 7:
					board[k + j] = Black_Pawns[j]
				else:
					board[k + j] = Ydirection[i]
			elif i == 7:
				if j <= 7:
					board[k + j] = Black_Royalty[j]
				else:
					board[k + j] = Ydirection[i]
			else:
				board[k + j] = Xdirection[j]
		k += 9
	return board

#Algorithm that prints out the current chess piece positions
def display_board(board):
	# Chess Piece Dictionary Key
	# 0 = Empty
	# 1 = White Pawns (WP)
	# 2 = White Knights (WT)
	# 3 = White Bishops (WB)
	# 4 = White Rooks (WR)
	# 5 = White Queen (WQ)
	# 6 = White King (WK)
	# -1 = Black Pawns (BP)
	# -2 = Black Knights (BT)
	# -3 = Black Bishops (BB)
	# -4 = Black Rooks (BR)
	# -5 = Black Queen (BQ)
	# -6 = Black King (BK)
	
	Key = {-6: 'BK', -5: 'BQ', -4: 'BR', -3: 'BB', -2: 'BT', -1: 'BP', 0: '  ',
		1: 'WP', 2: 'WT', 3: 'WB', 4: 'WR', 5: 'WQ', 6: 'WK', 'AA': 'A ', 'BB': 'B ',
		'CC': 'C ', 'DD': 'D ', 'EE': 'E ', 'FF': 'F ', 'GG': 'G ', 'HH': 'H ',
		'11': '1', '22': '2', '33': '3', '44': '4', '55': '5', '66': '6', '77': '7', 
		'88': '8'}
		
	k = 0
	for i in range(9):
		print " ",
		for j in range(9):
			print Key[board[k + j]],
			
			if j != 8:
				print " | ",
		print
		
		if i != 8:
			print "-------------------------------------------------------------"
		else: 
			print
		k += 9
		
#Creates list of playable (active) indices
def create_active_indices():
	ind = 0
	del_key = []
	while ind < 8:
		del_key.append(8 + ind * 9)
		ind += 1

	active_indx = range(81)
	del active_indx[72:81]

	for index in sorted(del_key, reverse = True):
		del active_indx[index]
	return active_indx

#Creates a dictionary mapping chess 'address' to playable index  (ie., A1 = 0; B1 = 1)	
def address_to_index(active_indx):
	address_key = {}
	numbs = ['1', '2', '3', '4', '5', '6', '7', '8']
	letts = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
	
	i = 0
	for a in numbs:
		for b in letts:
			str = b + a
			address_key[str] = active_indx[i]
			i +=  1
	return address_key
			
			
#Prompts the user to select a piece to move			
def select_piece(user, board, address_key):
	valid = False
	while not valid:
	
		try:
			piece1 = str(raw_input("Which piece would you like to move?\n"))
			piece = board[address_key[piece1]]
			unit_info = []
			if user == 'white' and piece > 0:
				unit_info.append(piece)
				unit_info.append(address_key[piece1])
				return unit_info
			elif user == 'white' and piece <= 0:
				print "That piece is empty or not yours! Please try again."
			elif user == 'black' and piece < 0:
				unit_info.append(piece)
				unit_info.append(address_key[piece1])
				return unit_info
			else:
				print "That piece is empty or not yours! Please try again."
		
		except Exception as e:
			print "This is not a valid piece address! Please try again.\n"

def select_move(piece, location, board, active_indx):
	
	#select which function to use based off the piece (ID)
	if abs(piece) == 1:
		output = Pawn(piece, location, board, active_indx)
	elif abs(piece) == 2:
		output = Knight(piece, location, board, active_indx)
	elif abs(piece) == 3:
		output = Bishop(piece, location, board, active_indx)
	elif abs(piece) == 4:
		output = Rook(piece, location, board, active_indx)
	elif abs(piece) == 5:
		output = Queen(piece, location, board, active_indx)
	elif abs(piece) == 6:
		output = King(piece, location, board, active_indx)
	return output			

#Update the board based on the selected move	
def update_board(move, board, piece, location, address_key):
	board[address_key[move]] = piece
	board[location] = 0
	return board
	
#Check to see if the game has been won
def check_win(board):
	if 6 not in board or -6 not in board:
		return 'CHECK MATE'

#Exit Game Function		
def exit_game(board):
	display_board(board)
	quit()
		
#Print Instructions
def print_instruction():
	print "---------------------------------------------------------------------------"
	print "INSTRUCTIONS"
	print "---------------------------------------------------------------------------"
	print "Please select the piece you want to move by calling it out by its address: "
	print "(i.e., A1, E8, etc.)"
	print "---------------------------------------------------------------------------"
	print "This is the piece ID key:"
	print "---------------------------------------------------------------------------"
	print "White Pawns = WP"
	print "White Knights = WT"
	print "White Bishops = WB"
	print "White Rooks = WR"
	print "White Queen WQ"
	print "White King = WK"
	print "Black Pawns = BP"
	print "Black Knights = BT"
	print "Black Bishops = BB"
	print "Black Rooks = BR"
	print "Black Queen = BQ"
	print "Black King = BK"
		
