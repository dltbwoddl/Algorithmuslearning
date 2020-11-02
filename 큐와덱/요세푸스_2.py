def ysfs(n,k):
    nlist=[i for i in range(1,n+1)]
    result="<"
    ind=0
    k-=1
    while n!=1:
        ind=ind+k-n*((ind+k)//n)
        result+=(str(nlist.pop(ind))+", ")
        n-=1
    result+=(str(nlist.pop())+">")
    return(result)

n,k=map(int, input().split())
print(ysfs(n,k)0
