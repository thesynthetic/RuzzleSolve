tree = {}

def addword(word, d):
	if word == '':
		d['1'] = 1
		return 1
	if word[0] in d:
		addword(word[1:], d[word[0]])
	else:
		d[word[0]] = {}
		addword(word[1:], d[word[0]])

def isword(word, d):
	if word == '':
		if '1' in d:
			return True
		else:
			return False
	if word[0] in d:
		return isword(word[1:], d[word[0]])
	else:
		return False

#Fill Tree Map with Dictionary
if True:
	ins = open( "english.txt", "r" )
	for line in ins:
		if '?' or "'" not in line:
			addword(line.strip(),tree)
	ins.close()



#Adjacency Matrix
adj = {}
adj[1] = [2,5,6]
adj[2] = [1,3,5,6,7]
adj[3] = [2,4,6,7,8]
adj[4] = [3,7,8]
adj[5] = [1,2,6,9,10]
adj[6] = [1,2,3,5,7,9,10,11]
adj[7] = [2,3,4,6,8,10,11,12]
adj[8] = [3,4,7,11,12]
adj[9] = [5,6,10,13,14]
adj[10] = [5,6,7,9,11,13,14,15]
adj[11] = [6,7,8,10,12,14,15,16]
adj[12] = [7,8,11,15,16]
adj[13] = [9,10,14]
adj[14] = [9,10,11,13,15]
adj[15] = [10,11,12,14,16]
adj[16] = [11,12,15]

#Get Puzzle from User Input
puzzle_string = raw_input('Enter puzzle: ')
puzzle = [999]
for i in puzzle_string:
	puzzle = puzzle + [i]

max_length = 8

#Recursive Solve
def solve(puzzle, prefix, level, history, node):
	win = []
	
	prefix = prefix + puzzle[node]

	if level < max_length -1:
		for i in adj[node]:
			if i not in history:
				word = prefix + puzzle[i]
				#print 'Testing word ' + word, i 
				if isword(word,tree):
					win.append(word)
				win = win + solve(puzzle,prefix,level + 1,history + [i], i)
	return win

#Solver Wrapper
def solve_and_print():
	win = []
	sortedwin = {}
	for i in range(1,17):
		win = win + solve(puzzle, '',0, [i], i)
	for i in win:
		if len(i) not in sortedwin:
			sortedwin[len(i)] = []
		sortedwin[len(i)] = sortedwin[len(i)] + [i]
	for i in range(max_length, 1, -1):
		if i in sortedwin:
			for j in sortedwin[i]:
				print j


solve_and_print()

