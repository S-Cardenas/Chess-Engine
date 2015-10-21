#location has to be the index of the list board 
def Queen(piece, location, board, active_indx):
	
	this = []	#All possible places that can be moved to
	UP = []		#Movement UP
	DN = []		#Movement DOWN
	LT = []		#Movement LEFT
	RT = []		#Movement RIGHT
	S_E = []	#Movement DOWN + RIGHT
	N_E = []	#Movement UP + RIGHT
	S_W = []	#Movement DOWN + LEFT
	N_W = []	#Movement UP + LEFT
	
	if piece > 0:
		IDs1 = range(1,7)
		IDs2 = range(-6,0)
	elif piece < 0:
		IDs1 = range(-6,0)
		IDs2 = range(1,7)
		
	i = 1				#UP movement
	while True:
		UP_loc = location - i * 9
		if board[UP_loc] in IDs1 or UP_loc not in active_indx:
			break
		elif board[UP_loc] in IDs2:
			UP.append(UP_loc)
			break
		UP.append(UP_loc)
		i += 1
			
	j = 1				#DN movement
	while True:
		DN_loc = location + j * 9
		if board[DN_loc] in IDs1 or DN_loc not in active_indx:
			break
		elif board[DN_loc] in IDs2:
			DN.append(DN_loc)
			break
		DN.append(DN_loc)
		j += 1
			
	k = 1				#Right movement	
	while True:
		RT_loc = location + k * 1
		if board[RT_loc] in IDs1 or RT_loc not in active_indx:
			break
		elif board[RT_loc] in IDs2:
			RT.append(RT_loc)
			break
		RT.append(RT_loc)
		k += 1
		
	l= 1				#Left movement
	while True:
		LT_loc = location - l * 1
		if board[LT_loc] in IDs1 or LT_loc not in active_indx:
			break
		elif board[LT_loc] in IDs2:
			LT.append(LT_loc)
			break
		LT.append(LT_loc)
		l += 1
		
	m = 1				#RIGHT + DOWN movement
	while True:
		SE_loc = location + m * 10
		if board[SE_loc] in IDs1 or SE_loc not in active_indx:
			break
		elif board[SE_loc] in IDs2:
			S_E.append(SE_loc)
			break
		S_E.append(SE_loc)
		m += 1
	
	n = 1				#UP + LEFT movement
	while True:
		NW_loc = location - n * 10
		if board[NW_loc] in IDs1 or NW_loc not in active_indx:
			break
		elif board[NW_loc] in IDs2:
			N_W.append(NW_loc)
			break
		N_W.append(NW_loc)
		n += 1
		
	o = 1				#UP + RIGHT movement
	while True:
		NE_loc = location - o * 8
		if board[NE_loc] in IDs1 or NE_loc not in active_indx:
			break
		elif board[NE_loc] in IDs2:
			N_E.append(NE_loc)
			break
		N_E.append(NE_loc)
		o += 1
			
	p = 1				#DOWN + LEFT movement
	while True:
		SW_loc = location + p * 8
		if board[SW_loc] in IDs1 or SW_loc not in active_indx:
			break
		elif board[SW_loc] in IDs2:
			S_W.append(SW_loc)
			break
		S_W.append(SW_loc)
		p += 1
		
	this.extend(UP)
	this.extend(DN)
	this.extend(RT)
	this.extend(LT)
	this.extend(S_E)
	this.extend(N_E)
	this.extend(S_W)
	this.extend(N_W)
	return this
