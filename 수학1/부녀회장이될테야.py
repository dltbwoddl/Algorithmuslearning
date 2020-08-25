# 1 2 3
# 1 3 6
# 1 4 10
n=int(input())
r=[]
for i in range(n):
    k=int(input())
    t=int(input())
    r=[[i for i in range(1,t+1)]]
    for i in range(1,k+1):
        r.append([])
        for j in range(1,t+1):
            r[i].append(sum(r[i-1][:j]))
    print(r[k][t-1])
