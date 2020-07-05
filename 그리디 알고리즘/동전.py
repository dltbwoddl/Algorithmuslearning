#https://www.acmicpc.net/problem/11047
a,b=[int(i) for i in input("").split(" ")]
m=[]
r=0
for i in range(0,a):
    m.append(int(input("")))
while b!=0:
    n=m.pop()
    j=b//n
    if j>0:
        r+=j
        b-=j*n
print(r)
    
