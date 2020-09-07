n=int(input(''))
r=""
for i in range(n):
    t=[int(j) for j in input().split()]
    if t[2]%t[0]==0:
        r+=str(t[0])
        p=str(t[2]//t[0])
        if len(p)==2:
            r+=p
        else:
            r+="0"+p
        
    else:
        a=str(t[2]//t[0]+1)
        r+=str(t[2]%t[0])
        if len(a)==2:
            r+=a
        else:
            r+="0"+a
    print(r)
    r=""
