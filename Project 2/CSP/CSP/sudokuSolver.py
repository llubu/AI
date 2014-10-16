# SUDOKU SOLVER

import sys
from time import time
from sudokuUtil import *
import util

# Please implement function solve_puzzle
# input puzzle: 2D list, for example:
# [ [0,9,5,0,3,2,0,6,4]
#   [0,0,0,0,6,0,1,0,0]
#   [6,0,0,0,0,0,0,0,0]
#   [2,0,0,9,0,3,0,0,6]
#   [0,7,6,0,0,0,0,0,3]
#   [3,0,0,0,0,0,0,0,0]
#   [9,0,0,5,0,4,7,0,1]
#   [0,5,0,0,2,1,0,9,0]
#   [0,0,8,0,0,6,3,0,5] ]
# Return a 2D list with all 0s replaced by 1 to 9.
# You can utilize argv to distinguish between algorithms
# (basic backtracking or with MRV and forward checking).
# For example: python sudokuSolver.py backtracking

from copy import copy, deepcopy
# Head ends here
def remove_possibilities(a): #for MRV check
  change = True
  while change:
    change = False
    for i in range(9):
        for j in range(9):
          if(len(a[i][j])>1):
            x,y=3*(i/3),3*(j/3)
            vals=a[i][:]+[row[j] for row in a]+[a[x][y],a[x+1][y],a[x+2][y],a[x][y+1],a[x+1][y+1],a[x+2][y+1],a[x][y+2],a[x+1][y+2],a[x+2][y+2]]
            #print "the main grid is"
            #print a
            #print "vals is"
            #print vals
            vals[:]=(value for value in vals if len(value)==1)
            for value in vals:
              if(value[0] in a[i][j]):
                change=True
                a[i][j].remove(value[0])

def find_singleton(a):
  #print "input to singleton is"
  #print a
  for i in range(9):
    j = 0
    row = a[i][:]
    col=[row[i] for row in a]
    row = a[i][:]
    x,y=3*(i/3),3*(i%3)
    box = [a[x][y],a[x][y+1],a[x][y+2],a[x+1][y],a[x+1][y+1],a[x+1][y+2],a[x+2][y],a[x+2][y+1],a[x+2][y+2]]
    freq=[0,0,0,0,0,0,0,0,0,0]
    for elems in row:
      if(len(elems)>1):
        for elem in elems:
          freq[elem]+=1
    if( 1 in freq):
      index = freq.index(1)
      for elems in row:
          if index in elems:
            a[i][j]=[index];
            #print "singleton in row ",i, "with value ", index,j, row
            remove_possibilities(a)
            return True;
          j=j+1;
    freq=[0,0,0,0,0,0,0,0,0,0]
    for elems in col:
      if(len(elems)>1):
        for elem in elems:
          freq[elem]+=1
    if( 1 in freq):
      index = freq.index(1)
      for elems in col:
          if index in elems:
            a[j][i]=[index];
            #print "singleton in col ",i, "with value ", index,j,col
            remove_possibilities(a)
            return True;
          j=j+1;
    freq=[0,0,0,0,0,0,0,0,0,0]
    for elems in box:
      if(len(elems)>1):
        for elem in elems:
          freq[elem]+=1
    if( 1 in freq):
      index = freq.index(1)
      for elems in box:
        if index in elems:
           a[x+(j/3)][y+(j%3)]=[index];
           #print "singleton in box ",i, "with value ", index,j, box
           remove_possibilities(a)
           return True;
        j=j+1;
  return False

def clean(grid):
  
  remove_possibilities(grid)
  
  for i in range(9):
    for j in range(9):
      if(len(grid[i][j])==0):
         #print "a contradiction found in upper one ",i,j, grid[i][j]
         return False
  while True:
    if(find_singleton(grid) == False):
      break
    for i in range(9):
      for j in range(9):
        if(len(grid[i][j])==0):
           #print "a contradiction found in lower ones"
           return False
  return grid

def sudoku_solve(grid):

  if all(len(grid[i/9][i%9]) == 1 for i in range(81)):
    #print "Solved it"
    #print grid
    return grid

  n,i = min( (len(grid[i/9][i%9]),i) for i in range(81) if len(grid[i/9][i%9]) > 1)
  #print grid
  #print n,i,grid[i/9][i%9]

  seq = list();
  elems = grid[i/9][i%9]
  temp_grid=[];
  new=[];
  for d in elems:
    temp_grid=deepcopy(grid);
    #print "assigning ",d," to ",i, "for grid"
    #print grid
    #print "temp_grid = "
    temp_grid[i/9][i%9]=[d]
    #print temp_grid
    if( clean(temp_grid) != False):
      x = sudoku_solve(temp_grid)
      if(x):
        return x
      #seq.append(sudoku_solve(temp_grid))
    else:
      seq.append(False)
      #print "grid is false while assigning ",d," to ",i
 
  #print "seq for ",n,i,elems, grid[i/9][i%9]," is ", seq
  for e in seq:
    if e: 
      print "e is "
      print e
      return e
  return False;

# Check if a given val is valid for the puzzle
def isValid(puzzle, row, col, val):
	
	for index in range(9):
		if ( puzzle[row][index] == val and index != col ):
#			print 'RET FALSE FOR COL', index
			return False
		if ( puzzle[index][col] == val and index != row ):
#			print 'RET FALSE FOR ROW', index
			return False
	
	x = (row/3)*3
	y = (col/3)*3
	#print "BOX", row, col, x, y
	
	for xi in range(3):
		for yi in range(3):
			if puzzle[x+xi][y+yi] == val:
				#print 'RET FALSE FOR BOX', xi, yi
				return False
	return True
	
def sudokuBT(puzzle):
	#print "Entering BT"
	row = 0
	col = 0
	val = 1
	end = 10
	rcList = [0, 0]
	state = util.Stack()
	last = []
	flag = False
	find = True
	dump = open('dump.txt', 'w')
	while True:
		while val < end:
			flag = False
			#i = 0, j = 0
			if find:
				for i in range(9):
					for j in range(9):
						if puzzle[j][i] == 0:
							row = j
							col = i
							flag = True
							find = False
							dump.write("Found AN EMPTY CELL"+str(row)+str(col)+'\n')
							#print 'FOUND EMPTY CELL', row, col
							break
					if flag:
						break
				if not flag:
					dump.write( 'Sudoku DONE\n')
					print " DONE", puzzle
					return puzzle
				
			if isValid(puzzle, row, col, val):
				#dump.write( 'valid for' + str(row)+ str(col) + str(val) +'\n')
				#print 'VALID FOR', row, col, val,
				puzzle[row][col] = val
				state.push([row, col, val]) # Keep track of the state for Backtracking
				dump.write( 'Pushing State' + str(row) + str(col) + str(val) +'\n')
				#print 'PUSHING', row, col, val
				val = 1
				find = True
			else:
				#dump.write( 'Not valid for' + str(row)+ str(col) + str(val)+'\n')
				if val >= 9: #No solution found for this backtrack now
					dump.write( 'Not valid for ANY _ BT NOW' + str(row)+ str(col) + str(val)+'\n')
					#print 'Not valid for', row, col, val
					if not state.isEmpty():
						boo = state.peek()
						if boo[2] == 9:
							last = state.pop()
							dump.write('Poping State - for 9-' + str(last) + '\n')
							puzzle[last[0]][last[1]] = 0 #Backtracking
						last = state.pop()
						#print 'DOING BT', last
						dump.write('Poping State' + str(last) + '\n')
						puzzle[last[0]][last[1]] = 0 #Backtracking
						val = last[2] + 1
						if val > 9:
							val = 1
						find = True
				else:
					val += 1
							
	dump.close()
	
	
def solve_puzzle(puzzle, argv):
	"""Solve the sudoku puzzle."""
	print "Entering Solving"
	
	if argv[1] == "backtracking":
		print "Starting BT"
		puzzle = sudokuBT(puzzle)
		#print "BT", puzzle
		return puzzle
	
	if argv[1] == "MRV":
		print "Starting MRV"
		for k in range(9):
			for l in range(9):
				if puzzle[k][l] == 0:
					puzzle[k][l]=[1,2,3,4,5,6,7,8,9]
				else:
					puzzle[k][l]=[puzzle[k][l]]
		#print "NEW PRINT", "\n", puzzle
		clean(puzzle)
        sol = sudoku_solve(puzzle)
		
	print "END OF MRV"
	
	print sol, '\n\n'
	ret_sol = []
	print sol
	for line in sol:
		nl = []
		for vl in line:
			nl.append(vl[0])
		ret_sol.append(nl)
	return ret_sol
	

#===================================================#
puzzle = load_sudoku('puzzle.txt')

print "solving ..."
print puzzle
t0 = time()
solution = solve_puzzle(puzzle, sys.argv)
t1 = time()
print "completed. time usage: %f" %(t1 - t0), "secs."

save_sudoku('solution.txt', solution)

