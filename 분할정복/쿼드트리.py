def quadtree(n,k):
    global result
    a=[1 for i in range(n)]
    b=[0 for i in range(n)]
    a_r=1
    b_r=1
    for i in k:
        if i!=a:
            a_r=0
    for i in k:
        if i!=b:
            b_r=0
    if a_r:
        result+="1"
    elif b_r:
        result+="0"
    else:
        k_r=[]
        result+="("
        for i in range(4):
            k_r=[]
            n_2=int(n/2)
            for j in range(int(n_2)):
                if i<=1:
                    if i%2==0:
                        k_r.append(k[j][:n_2])
                    else:
                        k_r.append(k[j][n_2:])
                else:
                    if i%2==0:
                        k_r.append(k[n_2+j][:n_2])
                    else:
                        k_r.append(k[n_2+j][n_2:])
            quadtree(n_2,k_r)
        result+=")"
result=""
n=int(input(""))
k=[]
for i in range(n):
    k.append(list(map(int,input())))
quadtree(n,k)
print(result)
