n=int(input(""))
result=[n]
def make1(n,r):
    global result
    if r>result[0]:
            pass
    else:
        if n==1:
            result.append(r)
            if result:
                if result[0]>r:
                    result[0]=r
        else:
            if n%3==0:
                make1(n/3,r+1)
            if n%2==0:
                make1(n/2,r+1)
            if n>1:
                make1(n-1,r+1)

make1(n,0)
print(min(result))
