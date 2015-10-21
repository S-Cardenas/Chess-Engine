#location has to be the index of the list board 
def Rook(piece, location, board, active_indx):
	
	this = []	#All possible places that can be moved to
	UP = []	#Movement UP
	DN = []	#Movement DOWN
	LT = []	#Movement LEFT
	RT = []	#Movement RIGHT
	
	if piece > 0:
		i = 1
		while True:
			UP_loc = location - i * 9
			if board[UP_loc] > 0 or UP_loc not in active_indx:
				break
			elif board[UP_loc] < 0:
				UP.append(UP_loc)
				break
			UP.append(UP_loc)
			i += 1
			
		j = 1	
		while True:
			DN_loc = location + j * 9
			if board[DN_loc] > 0 or DN_loc not in active_indx:
				break
			elif board[DN_loc] < 0:
				DN.append(DN_loc)
				break
			DN.append(DN_loc)
			j += 1
			
		k = 1	
		while True:
			RT_loc = location + k * 1
			if board[RT_loc] > 0 or RT_loc not in active_indx:
				break
			elif board[RT_loc] < 0:
				RT.append(RT_loc)
				break
			RT.append(RT_loc)
			k += 1
			
		l= 1	
		while True:
			LT_loc = location - l * 1
			if board[LT_loc] > 0 or LT_loc not in active_indx:
				break
			elif board[LT_loc] < 0:
				LT.append(LT_loc)
				break
			LT.append(LT_loc)
			l += 1
		
		this.extend(UP)
		this.extend(DN)
		this.extend(RT)
		this.extend(LT)
		return this
		
	elif piece < 0:
		i = 1
		while True:
			UP_loc = location - i * 9
			if board[UP_loc] < 0 or UP_loc not in active_indx:
				break
			elif board[UP_loc] > 0:
				UP.append(UP_loc)
				break
			UP.append(UP_loc)
			i += 1
			
		j = 1	
		while True:
			DN_loc = location + j * 9
			if board[DN_loc] < 0 or DN_loc not in active_indx:
				break
			elif board[DN_loc] > 0:
				DN.append(DN_loc)
				break
			DN.append(DN_loc)
			j += 1
			
		k = 1	
		while True:
			RT_loc = location + k * 1
			if board[RT_loc] < 0 or RT_loc not in active_indx:
				break
			elif board[RT_loc] > 0:
				RT.append(RT_loc)
				break
			RT.append(RT_loc)
			k += 1
			
		l= 1	
		while True:
			LT_loc = location - l * 1
			if board[LT_loc] < 0 or LT_loc not in active_indx:
				break
			elif board[LT_loc] > 0:
				LT.append(LT_loc)
				break
			LT.append(LT_loc)
			l += 1
			
		this.extend(UP)
		this.extend(DN)
		this.extend(RT)
		this.extend(LT)
		return this
