def pbn(n_1,n_2,i,r):
    if n==0:
        print(0)
        return
    if i==r-1:
        print(n_2)
        return
    pbn(n_2,n_1+n_2,i+1,r)

n=int(input(""))
pbn(0,1,0,n)
