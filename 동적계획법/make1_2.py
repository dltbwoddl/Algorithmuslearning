n=int(input(""))
c=n
def make1(n,r):
    global c
    if r>c:
        pass
    elif n==1:
        if r<c:
            c=r
    else:
        if n%3==0:
            make1(n/3,r+1)
        if n%2==0:
            make1(n/2,r+1)
        if n>1:
            make1(n-1,r+1)

make1(n,0)
print(c)
