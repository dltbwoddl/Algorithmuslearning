def pbn():
    n=int(input(""))-1
    n_1=0
    n_2=1
    r=0
    if n==-1:
        print(0)
        return
    if n==0:
        print(1)
        return
    for i in range(n):
        r=n_1+n_2
        n_1=n_2
        n_2=r
    print(r)
pbn()
