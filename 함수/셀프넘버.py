#https://www.acmicpc.net/problem/4673
def noselfnumber(n):
    s_n=[int(i) for i in str(n)]
    return n+sum(s_n)
all=[i for i in range(1,10001)]
sub=[]
for i in all:
    sub.append(noselfnumber(i))
ans=set(all)-set(sub)
ans=list(ans)
ans.sort()
for i in ans:
    print(i)
