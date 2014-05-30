file = open('pe59cipher.txt')
ciphertext=file.readline().strip('\r\n').split(',')
ciphertext=map(int,ciphertext)
bestratio=0
for i in range(97,123):
    for j in range(97,123):
        for k in range(97,123):
            plaintext=ciphertext[:]
            l=len(plaintext)
            for n in range(0,l,3):
                plaintext[n]=plaintext[n]^i
            for n in range(1,l,3):
                plaintext[n]=plaintext[n]^j
            for n in range(2,l,3):
                plaintext[n]=plaintext[n]^k
            count=0.0
            plaintext2=reduce(lambda x,y:x+y, map(chr,plaintext))
            for n in range(l):
                if plaintext2[n].isalpha(): count+=1.0
            if count/l>.76:
                print plaintext2
                print i,j,k
                print sum(plaintext)
