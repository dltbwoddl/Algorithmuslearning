def ysfs(n,k):
    ind=0
    k-=1
    nlist=[i for i in range(1,n+1)]
    result="<"
    while n!=1:
        if (ind+k)<n-1:
            print(1111111)
            result+=str(nlist.pop(ind+k))+", "
            ind+=k
        elif (ind+k)>(n-1):
            print(222222, ind,n, result)
            ind=ind+k-n
            if ind>(n-1):
                ind-=n*(ind//n)
            result+=str(nlist.pop(ind))+", "
        elif (ind+k)==n-1:
            print(333)
            result+=str(nlist.pop(k+ind))+", "
            ind=0
        print(result)
        n-=1
    result+=str(nlist.pop())+">"
    return(result)

i=[int(i) for i in input().split()]
print(ysfs(i[0],i[1]))
