from Chess import *

def main():
	
	# setup game
	# alternate turns
	# check if win or end
	# quit and show the board
	
	#Print Instructions
	print_instruction()
	
	#Creates list of playable (active) indices
	active_indx = create_active_indices()
	
	#Creates a dictionary mapping chess 'address' to playable index  (ie., A1 = 0; B1 = 1)
	address_key = address_to_index(active_indx)
	
	#Creates the starting position of pieces on chess board
	board = start_board()
	
	win = False
	turn = 0
	while not win:
		
		#print the board
		display_board(board)
		print "Turn number: " + str(turn)
		if turn % 2 == 0:
			user = 'white'
			print "The current user is:", user
		else:
			user = 'black'
			print "The current user is:", user
		
		possible_move = []
		while len(possible_move) == 0:
			#Ask the user for the piece he wants to move. (piece = piece ID; location = index)
			piece, location = select_piece(user, board, address_key)
			#Verify that the selected piece can be moved and return list of possible moves
			possible_move = select_move(piece, location, board, active_indx)
			if len(possible_move) == 0:
				print "The selected piece can not be moved. Please select another piece."
		
		while True:
			try: 
				#Ask the user where he would like to move the piece
				move = str(raw_input("Where would you like to move the piece?\n"))
				if address_key[move] in possible_move:
					board = update_board(move, board, piece, location, address_key)
					break
				else:
					print "This piece can not move there!!"
					
			except Exception as e:
				print "This is not a valid move! Please try again.\n"
				
		#advance move and check end game condition
		turn += 1
		winner = check_win(board)		
		if winner == 'CHECK MATE':
			print "---------------------------------------"
			print "CHECKMATE!!!!"
			print "---------------------------------------"
			print "The winner is:", user
			exit_game(board)


if __name__ == "__main__":
	main()				
				
				
				
				
