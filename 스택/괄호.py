#https://www.acmicpc.net/problem/9012
ans=0
result=[]
for i in range(0,int(input(""))):
    s=[i for i in input("")]
    while s:
        i=s.pop()
        if i==")":
            ans+=1
        else:
            ans-=1
        if ans<0:
            result.append("NO")
            break
    if ans>0:
        result.append("NO")
    elif ans==0:
        result.append("YES")
    ans=0
for i in result:
    print(i)
