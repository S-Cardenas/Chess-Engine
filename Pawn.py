#location has to be the index of the list board 
def Pawn(piece, location, board, active_indx):
	if piece > 0:
		if location >= 9 and location <= 16:
			a = location + 1 * 9
			b = location + 2 * 9
			c = location + (1 * 9) + 1
			d = location + (1 * 9) - 1
			new_indxs = [a, b, c, d]
			
			#Check if new location is an active index
			i = 0
			for item in new_indxs:
				if item not in active_indx:
					new_indxs[i] = 'null'
				i += 1
			
			#Define which piece ID is in the new_indxs
			piece_ID = []
			for indx in new_indxs:
				if indx == 'null':
					piece_ID.append('null')
				else:
					piece_ID.append(board[indx])
			
			this = []
			if piece_ID[0] == 0 and piece_ID[1] == 0:
				this.extend(new_indxs[0:2])
			elif piece_ID[0] == 0 and piece_ID[1] != 0:
				this.append(new_indxs[0])
			if piece_ID[2] < 0 and piece_ID[2] != 'null':
				this.append(new_indxs[2])
			if piece_ID[3] < 0 and piece_ID[3] != 'null':
				this.append(new_indxs[3])
			return this
				
		elif location >= 18 and location <= 61:
			a = location + 1 * 9
			c = location + (1 * 9) + 1
			d = location + (1 * 9) - 1
			new_indxs = [a, c, d]
			
			#Check if new location is an active index
			i = 0
			for item in new_indxs:
				if item not in active_indx:
					new_indxs[i] = 'null'
				i += 1
			
			#Define which piece ID is in the new_indxs
			piece_ID = []
			for indx in new_indxs:
				if indx == 'null':
					piece_ID.append('null')
				else:
					piece_ID.append(board[indx])
			
			this = []
			if piece_ID[0] == 0:
				this.append(new_indxs[0])
			if piece_ID[1] != 'null' and piece_ID[1] < 0:
				this.append(new_indxs[1])
			if piece_ID[2] != 'null' and piece_ID[2] < 0:
				this.append(new_indxs[2])
			return this
		else:
			this = []
			return this
			
	elif piece < 0:
		if location >= 54 and location <= 61:
			a = location - 1 * 9
			b = location - 2 * 9
			c = location - (1 * 9) + 1
			d = location - (1 * 9) - 1
			new_indxs = [a, b, c, d]
			
			#Check if new location is an active index
			i = 0
			for item in new_indxs:
				if item not in active_indx:
					new_indxs[i] = 'null'
				i += 1
			
			#Define which piece ID is in the new_indxs
			piece_ID = []
			for indx in new_indxs:
				if indx == 'null':
					piece_ID.append('null')
				else:
					piece_ID.append(board[indx])
			
			this = []
			if piece_ID[0] == 0 and piece_ID[1] == 0:
				this.extend(new_indxs[0:2])
			elif piece_ID[0] == 0 and piece_ID[1] != 0:
				this.append(new_indxs[0])
			if piece_ID[2] < 0 and piece_ID[2] != 'null':
				this.append(new_indxs[2])
			if piece_ID[3] < 0 and piece_ID[3] != 'null':
				this.append(new_indxs[3])
			return this
		
		elif location >= 9 and location <= 52:
			a = location - 1 * 9
			c = location - (1 * 9) + 1
			d = location - (1 * 9) - 1
			new_indxs = [a, c, d]
			
			#Check if new location is an active index
			i = 0
			for item in new_indxs:
				if item not in active_indx:
					new_indxs[i] = 'null'
				i += 1
			
			#Define which piece ID is in the new_indxs
			piece_ID = []
			for indx in new_indxs:
				if indx == 'null':
					piece_ID.append('null')
				else:
					piece_ID.append(board[indx])
			
			this = []
			if piece_ID[0] == 0:
				this.append(new_indxs[0])
			if piece_ID[1] != 'null' and piece_ID[1] < 0:
				this.append(new_indxs[1])
			if piece_ID[2] != 'null' and piece_ID[2] < 0:
				this.append(new_indxs[2])
			return this
		else:
			this = []
			return this
			
