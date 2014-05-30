from math import sqrt

for k in range(10000):
    D=(k*(3*k-1))/2  # We check all possible pentagonal differences D=P_i-P_j, in increasing order of D, to ensure that a pair P_i,P_j with P_i-P_j minimal is output first.

    #Given D, we next search for i,j such that P_(j+i)-P_j=D. We use the fact that P_(j+i)=P_j+P_i+3ij, and hence that i is part of an integer solution to P_(j+i)-P_j=D iff (D-P_i)%3i==0, in which case j=(D-P_i)/3i    
    i=1
    M=D-(i*(3*i-1))/2 
    while M>0:
        if M%(3*i)==0:
            j=M/(3*i)
            p=(j*(3*j-1))/2
            q=(i+j)*(3*(i+j)-1)/2 
            l=int((sqrt(1+24*(p+q))+1)/6)
            if p+q==(l*(3*l-1))/2:
                print "numbers are:",p,q
                print "D=",D
                print "indices are:",j,i+j
                quit()
        i+=1
        M=D-(i*(3*i-1))/2
