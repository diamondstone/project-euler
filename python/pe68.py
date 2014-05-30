import pickle
from math import sqrt,factorial

# Functions for dealing with permutations

def baseftonum(basef): #computes the number with "base" factorial representation basef
    num=0
    l=len(basef)
    for i in range(l): num+=factorial(l-i)*basef[i]
    return num
    

def numtobasef(num,l): # computes the l-"digit" "base" factorial representation of num
    # there's probably a real name for this
    basef=[0]*l
    for i in range(l):
        basef[i]=num/factorial(l-i)
        num-=basef[i]*factorial(l-i)
    return basef

def baseftoperm(basef): # converts a base-factorial representation to the corresponding permutation
    basef.append(0)
    l=len(basef)
    perm=[0]*l
    for i in range(l):
        while perm[i] in perm[:i]: perm[i] += 1
        for j in range(basef[i]):
            perm[i]+=1
            while perm[i] in perm[:i]: perm[i] += 1
    return perm

def permtobasef(perm): # converts a base-factorial representation to the corresponding permutation
    l=len(perm)-1
    basef=perm[:l]
    for i in range(l):
        for j in range(basef[i]):
            if j in perm[:i]: basef[i] -= 1
    return basef

def permtonum(perm): return baseftonum(permtobasef(perm))

def numtoperm(num,l): return baseftoperm(numtobasef(num,l-1))

def nextperm(perm):
    l=len(perm)
    num=permtonum(perm)+1
    if num==factorial(l): return None
    return numtoperm(num,l)

def solutionset(i): #takes a permutation of 0...9, maps it to a permutation of 1...10 by changing x to 10-x, and then maps it to the solution set it represents: [[0,9,1],[2,1,3],[4,3,5],[6,5,7],[8,7,9]]
    perm=map(lambda x:10-x,numtoperm(i,10))
    solution=[perm[0],perm[9],perm[1],perm[2],perm[1],perm[3],perm[4],perm[3],perm[5],perm[6],perm[5],perm[7],perm[8],perm[7],perm[9]]
    mini=0
    for i in range(3,15,3):
        if solution[i]<solution[mini]: mini=i
    solution=solution[mini:]+solution[:mini]
    solution=int(reduce(lambda x,y:x+y,map(str,solution)))
    return solution
    
candidates=[]
for i in xrange(362880):
    perm=numtoperm(i,10)
    if sum(perm[1:4])==sum(perm[3:6]) and sum(perm[1:4])==sum(perm[5:8]) and sum(perm[1:4])==sum(perm[7:10]) and sum(perm[2:4])==perm[9]+perm[0]: candidates.append(i)
solutions = map(solutionset,candidates)
solutions.sort()
print solutions
