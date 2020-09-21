#1
kg=[]
cm=[]
t=int(input())
for i in range(t):
    n=[int(i) for i in input().split()]
    kg.append(n[0])
    cm.append(n[1])
def size(kg,cm,t):
    r=""
    for i in range(t):
        k=1
        for j in range(t):
            if kg[i]<kg[j]:
                if cm[i]<cm[j]:
                    k+=1
        r+=str(k)+" "
    return(r)
print(size(kg,cm,t))

#2
kgcm=[]
t=int(input())
for i in range(t):
    kgcm.append([int(i) for i in input().split()])

def size_2(kgcm,t):
    r=""
    for i in range(t):
        k=1
        for j in range(t):
            if kgcm[i][0]<kgcm[j][0]:
                if kgcm[i][1]<kgcm[j][1]:
                    k+=1
        r+=str(k)+" "
    return(r)
print(size_2(kgcm,t))

#3
n=[list(map(int,input().split())) for i in range(int(input()))]
for i,j in n:
    print(len([t for t in n if i<t[0] and j<t[1]])+1,end=" ")
