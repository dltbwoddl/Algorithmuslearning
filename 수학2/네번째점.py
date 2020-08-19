x=[]
y=[]
for k in range(0,3):
    n=[int(i) for i in input().split()]
    x.append(n[0])
    y.append(n[1])
def a(j):
    for i in j:
        if j.count(i)==1:
            print(i)
            return i
    
print(str(a(x))+" "+str(a(y)))
