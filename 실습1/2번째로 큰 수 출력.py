#https://www.acmicpc.net/problem/10817
#배열로 풀기.
a=[int(i) for i in input().split()]
for j in range(0,2):
    for i in range(0,2):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
print(a[1])
