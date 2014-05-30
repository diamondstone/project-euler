print sum(n for n in range(2,354294) if n==sum(map(lambda x: int(x)**5,list(str(n)))))
