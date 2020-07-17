n=int(input(""))
nl=[]
for i in range(n):
    nl.append(int(input("")))
for i in range(n):
    for j in range(i,n):
        if nl[i]>nl[j]:
            t=nl[i]
            nl[i]=nl[j]
            nl[j]=t
for i in nl:
    print(i)
#256ms