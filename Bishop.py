#location has to be the index of the list board 
def Bishop(piece, location, board, active_indx):
	
	this = []	#All possible places that can be moved to
	S_E = []	#Movement DOWN + RIGHT
	N_E = []	#Movement UP + RIGHT
	S_W = []	#Movement DOWN + LEFT
	N_W = []	#Movement UP + LEFT
	
	if piece > 0:
		i = 1
		while True:
			SE_loc = location + i * 10
			if board[SE_loc] > 0 or SE_loc not in active_indx:
				break
			elif board[SE_loc] < 0:
				S_E.append(SE_loc)
				break
			S_E.append(SE_loc)
			i += 1
		
		j = 1	
		while True:
			NW_loc = location - j * 10
			if board[NW_loc] > 0 or NW_loc not in active_indx:
				break
			elif board[NW_loc] < 0:
				N_W.append(NW_loc)
				break
			N_W.append(NW_loc)
			j += 1
		
		k = 1	
		while True:
			NE_loc = location - k * 8
			if board[NE_loc] > 0 or NE_loc not in active_indx:
				break
			elif board[NE_loc] < 0:
				N_E.append(NE_loc)
				break
			N_E.append(NE_loc)
			k += 1
			
		l = 1
		while True:
			SW_loc = location + l * 8
			if board[SW_loc] > 0 or SW_loc not in active_indx:
				break
			elif board[SW_loc] < 0:
				S_W.append(SW_loc)
				break
			S_W.append(SW_loc)
			l += 1
			
		this.extend(S_E)
		this.extend(N_E)
		this.extend(S_W)
		this.extend(N_W)
		return this
		
	elif piece < 0:
		i = 1
		while True:
			SE_loc = location + i * 10
			if board[SE_loc] < 0 or SE_loc not in active_indx:
				break
			elif board[SE_loc] > 0:
				S_E.append(SE_loc)
				break
			S_E.append(SE_loc)
			i += 1
		
		j = 1	
		while True:
			NW_loc = location - j * 10
			if board[NW_loc] < 0 or NW_loc not in active_indx:
				break
			elif board[NW_loc] > 0:
				N_W.append(NW_loc)
				break
			N_W.append(NW_loc)
			j += 1
		
		k = 1	
		while True:
			NE_loc = location - k * 8
			if board[NE_loc] < 0 or NE_loc not in active_indx:
				break
			elif board[NE_loc] > 0:
				N_E.append(NE_loc)
				break
			N_E.append(NE_loc)
			k += 1
			
		l = 1
		while True:
			SW_loc = location + l * 8
			if board[SW_loc] < 0 or SW_loc not in active_indx:
				break
			elif board[SW_loc] >0:
				S_W.append(SW_loc)
				break
			S_W.append(SW_loc)
			l += 1
			
		this.extend(S_E)
		this.extend(N_E)
		this.extend(S_W)
		this.extend(N_W)
		return this
		
