a=[int(i) for i in input()]
s=a
if len(a)==1:
    a.append(0)
n=0
b=[]
while s!=b:
    b=[a[1],(a[0]+a[1])%10]
    a=b
    n+=1
print(n)
