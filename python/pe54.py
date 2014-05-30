### Poker hand ranks:
# 8: straight flush
# 7: 4kind
# 6: full house
# 5: flush
# 4: straight
# 3: 3kind
# 2: 2pair
# 1: pair
# 0: nada

def rank(hand): #expects list of 5 2-char card names, from 2C...AS. Returns rank of hand, followed by rank of most important aspect (high card of straight, high card of 4/3 of kind, high card of (highest) pair, or simply high card if no straights or tuples), followed (if applicable) by rank of next most important aspect, padded with 0s to length 6
    rank=[0]*6
    values=map(lambda x:x[0],hand)
    suits=map(lambda x:x[1],hand)
    if len(set(suits))==1: flush=1
    else: flush=0 #At this point we can discard suit information, as all we care about is whether there was a flush
    for i in range(len(values)):
        if values[i]=='T': values[i]=10
        elif values[i]=='J': values[i]=11
        elif values[i]=='Q': values[i]=12
        elif values[i]=='K': values[i]=13
        elif values[i]=='A': values[i]=14
        else: values[i]=int(values[i])
    values.sort() #At this point values is a sorted list of card values
    straight=1
    for i in range(1,5):
        if values[i]-values[0]!=i: straight=0
    plicities=[1]
    redvalues=[]
    redvalues.append(values[0])
    for i in range(1,5):
        if values[i]==values[i-1]: plicities[-1]+=1
        else:
            plicities.append(1)
            redvalues.append(values[i])
    if straight*flush:
        rank[0]=8
        rank[1]=values[4]
    elif plicities==[1,4]:
        rank[0]=7
        rank[1]=redvalues[1]
        rank[2]=redvalues[0]
    elif plicities==[4,1]:
        rank[0]=7
        rank[1]=redvalues[0]
        rank[2]=redvalues[1]
    elif plicities==[2,3]:
        rank[0]=6
        rank[1]=redvalues[1]
        rank[2]=redvalues[0]
    elif plicities==[3,2]:
        rank[0]=6
        rank[1]=redvalues[0]
        rank[2]=redvalues[1]
    elif flush:
        rank[0]=5
        for i in range(1,5):
            rank[i]=values[5-i]
    elif straight:
        rank[0]=4
        rank[1]=values[4]
    elif plicities==[3,1,1]:
        rank[0]=3
        rank[1]=redvalues[0]
        rank[2]=redvalues[2]
        rank[3]=redvalues[1]
    elif plicities==[1,3,1]:
        rank[0]=3
        rank[1]=redvalues[1]
        rank[2]=redvalues[2]
        rank[3]=redvalues[0]
    elif plicities==[1,1,3]:
        rank[0]=3
        rank[1]=redvalues[2]
        rank[2]=redvalues[1]
        rank[3]=redvalues[0]
    elif plicities==[1,2,2]:
        rank[0]=2
        rank[1]=redvalues[2]
        rank[2]=redvalues[1]
        rank[3]=redvalues[0]
    elif plicities==[2,1,2]:
        rank[0]=2
        rank[1]=redvalues[2]
        rank[2]=redvalues[0]
        rank[3]=redvalues[1]
    elif plicities==[2,2,1]:
        rank[0]=2
        rank[1]=redvalues[1]
        rank[2]=redvalues[0]
        rank[3]=redvalues[2]
    elif plicities==[2,1,1,1]:
        rank[0]=1
        rank[1]=redvalues[0]
        rank[2]=redvalues[3]
        rank[3]=redvalues[2]
        rank[4]=redvalues[1]
    elif plicities==[1,2,1,1]:
        rank[0]=1
        rank[1]=redvalues[1]
        rank[2]=redvalues[3]
        rank[3]=redvalues[2]
        rank[4]=redvalues[0]
    elif plicities==[1,1,2,1]:
        rank[0]=1
        rank[1]=redvalues[2]
        rank[2]=redvalues[3]
        rank[3]=redvalues[1]
        rank[4]=redvalues[0]
    elif plicities==[1,1,1,2]:
        rank[0]=1
        rank[1]=redvalues[3]
        rank[2]=redvalues[2]
        rank[3]=redvalues[1]
        rank[4]=redvalues[0]
    else:
        for i in range(5): rank[5-i]=values[i]
    return rank

def better(hand1,hand2): #expects list of 5 2-char card names, from 2C...AS. Returns 1 if hand1 represents a better poker hand, and 0 if hand2 does.
    rank1=rank(hand1)
    rank2=rank(hand2)
    if rank1[0]>rank2[0]:
        return 1
    elif rank1[0]<rank2[0]:
        return 0
    elif rank1[1]>rank2[1]:
        return 1
    elif rank1[1]<rank2[1]:
        return 0
    elif rank1[2]>rank2[2]:
        return 1
    elif rank1[2]<rank2[2]:
        return 0
    elif rank1[3]>rank2[3]:
        return 1
    else: return 0

file = open('pe54pokerhands.txt')
count=0
for n in range(1000):
    hands=file.readline().strip('\r\n').split(' ')
    hand1=hands[:5]
    hand2=hands[5:]
    print "1:",hand1,"2:",hand2
    print "hand 1 rank:",rank(hand1)
    print "hand 2 rank:",rank(hand2)
    if better(hand1,hand2):
        count+=1
        print "hand 1 wins"
    else: print "hand 2 wins"
print "Player 1 wins",count,"hands"
