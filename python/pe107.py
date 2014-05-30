import itertools

def zeromatrix(n): #returns an nxn zero matrix without duplicate rows.
    row=[0]*n
    matrix=[]
    for i in xrange(n):
        matrix.append(row[:])
    return matrix

def lightest(network, set1, set2):
    best=sum([sum(row) for row in network])/2
    for i in set1:
        for j in set2:
            if 0<network[i][j]<best:
                best=network[i][j]
                besti,bestj=i,j
    return besti,bestj

def optimize(network):
    n=len(network)
    newnetwork=zeromatrix(n)
    connected=set([0])
    while len(connected)<n:
        i,j=lightest(network,connected,set(range(n)).difference(connected))
        newnetwork[i][j]=newnetwork[j][i]=network[i][j]
        connected.add(j)
    return newnetwork

def main():
    file = open('pe107network.txt')
    network=[]
    for line in file:
        network.append(map(int,line.replace('-','0').strip().split(',')))
    newnetwork=optimize(network)
    oldweight=sum([sum(row) for row in network])/2
    newweight=sum([sum(row) for row in newnetwork])/2
    savings=oldweight-newweight
    print savings

def test():
    m=zeromatrix(4)
    print m
    m[1][1]=1
    print m
    
main()
