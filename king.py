#location has to be the index of the list board 
def King(piece, location, board, active_indx):
	#Define possible indices where the knight can move
	a = location - 10
	b = location - 9
	c = location - 8
	d = location - 1
	e = location + 1
	f = location + 8
	g = location + 9
	h = location + 10
	
	if piece > 0:
		IDs1 = range(1,7)
		IDs2 = range(-6,0)
	elif piece < 0:
		IDs1 = range(-6,0)
		IDs2 = range(1,7)
		
	possibles = [a, b, c, d, e, f, g, h]
	new_indxs = []
	
	for item in possibles:
		if item not in active_indx:
			new_indxs.append('null')
		else:
			new_indxs.append(item)
		
	
	this = []
	for unit in new_indxs:
		if unit != 'null' and board[unit] not in IDs1:
			this.append(unit)
			
	return this
