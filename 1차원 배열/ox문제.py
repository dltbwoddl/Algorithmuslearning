n=int(input(""))
oxlist=[]
for i in range(n):
    oxlist.append([j for j in input()])

r=0
s=0
for i in oxlist:
    for j in i:
        if j=="O":
            r+=1
            s+=r
        else:
            r=0
    print(s
          )
    r=0
    s=0
