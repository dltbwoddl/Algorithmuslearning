#https://www.acmicpc.net/problem/2884
#시간:64ms 코드길이:249B
a=[int(i) for i in input('').split()]
if a[0]==0:
    if a[1]<=44:
        a[1]=60 - (45-a[1])
        a[0]=23
    else:
        a[1]-=45
else:
    if a[1]<=44:
        a[1]=60 - (45-a[1])
        a[0]-=1
    else:
        a[1]-=45
print(a[0],a[1])

#시간:68ms 코드길이:136B
a=[int(i) for i in input('').split()]
a[1]=a[1]-45
if a[1]<0:
    a[0]-=1
    a[1]+=60 
    if a[0]<0:
        a[0]=23
print(a[0],a[1])
