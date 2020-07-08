#https://www.acmicpc.net/problem/1260
n=[int(i) for i in input().split()]
g={}
#이부분 graph나오는 과정 살피기.
for i in range(0, n[1]):
    c=[int(i) for i in input("").split()]
    if c[0] in g.keys():
        g[c[0]].append(c[1])
        g[c[0]].sort()
        print('a')
        print(g,i)
    else:
        g.update({c[0]:[c[1]]})
        print('b')
        print(g,i)
    if c[1] in g.keys():
        g[c[1]].append(c[0])
        g[c[1]].sort()
        print('c')
        print(g,i)
    else:
        g.update({c[1]:[c[0]]})
        print('d')
        print(g,i)
global p
p=[n[2]]
global key
key=list(g.keys())
def dfs(g,n):
    for i in g[n]:
        if i in p:
            pass
        else:
            p.append(i)
            dfs(g,i)
dfs(g,n[2])
print(p)

global b
b=[n[2]]
def bfs(n):
    if len(b)==len(key):
        return b
    for i in g[n]:
        if i in b:
            pass
        else:
            b.append(i)
    for i in g[n]:
        bfs(i)
bfs(n[2])
print(b)
# 런타임 에러 발생.
