def compute_T(s,p): # returns the expected number of tests for the optimal strategy for testing s sheep with probability p of being diseased. p should be a float in (0,1)
    if (s,p) in T_Dict.keys(): return T_Dict[(s,p)]
    if s==0:
        T_Dict[(s,p)]=0
        return 0
    if s==1:
        T_Dict[(s,p)]=1
        return 1
    possibilities=[]
    for i in range(1,s+1): #first test i sheep, then use the optimal test on i sheep (with known positive) with probability 1-(1-p)**i, then test the remaining s-i sheep
        possibilities.append(1+(1-(1-p)**i)*compute_T_known(i,p)+compute_T(s-i,p))
    m=min(possibilities)
    T_Dict[(s,p)]=m
    return m
    
def compute_T_known(s,p): # returns the expected number of tests for the optimal strategy for testing s sheep with probability p of being diseased, when at least one sheep is known to be sick. p should be a float in (0,1)
    if (s,p) in known_Dict.keys(): return known_Dict[(s,p)]
    if s==1:
        known_Dict[(s,p)]=0
        return 0
    possibilities=[]
    for i in range(1,s): #first test i sheep, then use the optimal test on i sheep (with known positive) with probability prob, then test the remaining s-i sheep (remaining sheep will be known to contain a positive if first test was negative)
        prob=(1-(1-p)**i)/(1-(1-p)**s)
        possibilities.append(1+prob*(compute_T_known(i,p)+compute_T(s-i,p))+(1-prob)*compute_T_known(s-i,p))
    m=min(possibilities)
    known_Dict[(s,p)]=m
    return m

T_Dict={}
known_Dict={}

total=0.0
for z in range(1,51):
    p=z/100.0
    Ts=[0,1] #replaces T_dict, for fixed p
    Tknowns=['undefined',0] #replaces known_Dict, for fixed p
    for s in xrange(2,10001): #we define Tknowns[i] then Ts[i]
        possibilities=[]
        for i in xrange(1,s):
            prob=(1-(1-p)**i)/(1-(1-p)**s)
            possibilities.append(1+prob*(Tknowns[i]+Ts[s-i])+(1-prob)*Tknowns[s-i])
        m=min(possibilities)
        Tknowns.append(m)
        possibilities=[]
        for i in xrange(1,s+1):
            possibilities.append(1+(1-(1-p)**i)*Tknowns[i]+Ts[s-i])
        m=min(possibilities)
        Ts.append(m)
    print Ts[10000]
    total+=Ts[10000]
print "total is",total
