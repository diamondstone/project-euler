# PE 96: solving sudoku puzzles
# puzzles are lists of lines, each line being a 10-char string where chars are digits, and 0 represents a blank square

def firstblank(puzzle): #finds location of first blanks, returns as pair (i,j). Returns (-1,-1) if there are no blanks.
    for i in range(9):
        for j in range(9):
            if puzzle[i][j]=='0': return (i,j)
    return (-1,-1)

def legalmoves(puzzle,i,j): #takes a puzzle as input, returns a set representing legal moves for location (i,j) (that don't conflict with something in the current row/column/square; no searching for global solvability)
    moves=set([str(n) for n in range(1,10)])
    row=set(list(puzzle[i]))
    column=set([puzzle[k][j] for k in range(9)])
    moves=moves.difference(row)
    moves=moves.difference(column)
    for k in mask[i%3]:
        for l in mask[j%3]:
            moves=moves.difference(set(puzzle[i+k][j+l]))
    return moves

def solve(puzzle): #takes a puzzle as input, repairs a pair (boolean,solution). Assumes puzzle has no duplicates in any row/column/square. If puzzle is solvable, then boolean is True, and solution is some valid solution (not assuming the existence of unique solution, and just trying to find any solution). If puzzle is unsolvable, then boolean is false, and solution is original puzzle.
    (i,j)=firstblank(puzzle) # find the first blank location
    if (i,j)==(-1,-1):
        return True, puzzle # If no blanks, then puzzle is already solved
    moves=legalmoves(puzzle,i,j) # If there is a blank, find legal moves for that blank
    newpuzzle=puzzle[:] #take slice copy to avoid changing during recursion
    for d in moves: #try each move
        newpuzzle[i]=list(newpuzzle[i])
        newpuzzle[i][j]=d
        newpuzzle[i]=reduce(lambda a,b:a+b,newpuzzle[i])
#        print i,j,moves,d,newpuzzle
        (test,solution)=solve(newpuzzle)
        if test==True: return True, solution
    return False, puzzle # No legal moves, or all legal moves lead to dead ends

mask={0:(1,2), 1:(-1,1), 2:(-2,-1)} #given index mod 3, gives values to add to index to get other indices in same square
file = open('pe96sudoku.txt')
lines=file.readlines() # list of lines of the form "123456789\n"
lines=map(lambda x: x.strip('\n'),lines)
puzzles=[]
total=0
for i in range(50):
    puzzle=lines[10*i+1:10*i+10]
    test,solution=solve(puzzle)
    code=int(solution[0][:3])
    print code
    total+=code
print total
