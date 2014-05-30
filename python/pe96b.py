# PE 96: solving sudoku puzzles
# puzzles are lists of lines, each line being a 10-char string where chars are digits, and 0 represents a blank square

from copy import deepcopy

def legalmoves(puzzle,i,j): #takes a puzzle as input, returns a set representing legal moves for location (i,j) (that don't conflict with something in the current row/column/square; no searching for global solvability)
    moves=set([str(n) for n in range(1,10)])
    row=set(puzzle[i])
    column=set([puzzle[k][j] for k in range(9)])
    moves=moves.difference(row)
    moves=moves.difference(column)
    for k in mask[i%3]:
        for l in mask[j%3]:
            moves=moves.difference(set(puzzle[i+k][j+l]))
    return moves

def forced(puzzle): #input: puzzle, output: bool (indicating apparent solvability), puzzle with force moves filled in
    newpuzzle=deepcopy(puzzle)
    for i in range(9):
        for j in range(9):
            if newpuzzle[i][j]=='0':
                moves=legalmoves(puzzle,i,j)
                if len(moves)==0:
                    return False,puzzle # the puzzle is unsolvable
                if len(moves)==1:
                    for d in moves:
                        newpuzzle[i][j]=d
    if puzzle==newpuzzle: # no forced moves made, so we're finished
        return True,newpuzzle
    return forced(newpuzzle) # we made forced moves, so try again

def solve(puzzle): #input: puzzle, output: bool (indicating solvability), solution (or initial puzzle if unsolvable)

    puzzle=deepcopy(puzzle) #take copy to avoid changing parent's puzzle
    (test,puzzle)=forced(puzzle)
    if test==False:
        return test,puzzle
    
    #find square with fewest legal moves
    fewest=10
    besti=-1
    bestj=-1
    for i in range(9):
        for j in range(9):
            if puzzle[i][j]=='0': #only consider legal moves on blanks
                moves=legalmoves(puzzle,i,j)
                if len(moves)<fewest:
                    fewest=len(moves)
                    besti=i
                    bestj=j
    (i,j)=(besti,bestj)
    if (i,j)==(-1,-1):
        return True, puzzle # Only true if no blanks
    moves=legalmoves(puzzle,i,j) # If there is a blank, find legal moves for that blank
    for d in moves: #try each move
        puzzle[i][j]=d
        (test,solution)=solve(puzzle)
        if test==True: return True, solution
    return False, puzzle # No legal moves, or all legal moves lead to dead ends

mask={0:(1,2), 1:(-1,1), 2:(-2,-1)} #given index mod 3, gives values to add to index to get other indices in same square
file = open('pe96sudoku.txt')
lines=file.readlines() # list of lines of the form "123456789\n"
lines=map(lambda x: list(x.strip()),lines)
puzzles=[]
total=0
for i in range(50):
    puzzle=lines[10*i+1:10*i+10]
    test,solution=solve(puzzle)
    code=int(reduce(lambda a,b:a+b, solution[0][:3]))
    print code
    total+=code
print total
