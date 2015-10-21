#location has to be the index of the list board 
def Knight(piece, location, board, active_indx):
	#Define the two 'special' indices where the knight can be
	left_invalid = range(0, 72, 9)
	right_invalid = range(7, 79, 9)
	#Define possible indices where the knight can move
	a = location + (2 * 9) + 1
	b = location + (2 * 9) - 1
	c = location - (2 * 9) + 1
	d = location - (2 * 9) - 1 
	e = location + 11
	f = location - 7
	g = location + 7
	h = location - 11
	
	if piece > 0:
		if location in left_invalid:
			new_indxs = [a, b, d, c, e, f]
		elif location in right_invalid:
			new_indxs = [b, d, g, h]
		else:
			new_indxs = [a, b, c, d, e, f, g, h] 
			
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
		j = 0
		for unit in piece_ID:
			if	unit <= 0 and unit != 'null':
				this.append(new_indxs[j])
			j += 1
		return this
	
	elif piece < 0:
		if location in left_invalid:
			new_indxs = [a, b, d, c, e, f]
		elif location in right_invalid:
			new_indxs = [b, d, g, h]
		else:
			new_indxs = [a, b, c, d, e, f, g, h] 
			
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
		j = 0
		for unit in piece_ID:
			if	unit >= 0 and unit != 'null':
				this.append(new_indxs[j])
			j += 1
		return this
		
			
			
