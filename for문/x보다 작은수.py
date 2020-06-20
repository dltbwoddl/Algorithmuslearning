#https://www.acmicpc.net/problem/10871
a=[int(i) for i in input('').split()]
b=[int(i) for i in input('').split()]
s=a[1]
result=''
for i in range(0,a[0]):
    if b[i]<s:
        result+=str(b[i])+' '
print(result)
