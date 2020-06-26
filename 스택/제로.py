#https://www.acmicpc.net/problem/10773
#시간 매우 오래걸림.
n=int(input(''))
alist=[]
for i in range(0,n):
    a=int(input(''))
    if a==0:
        alist.pop()
    else:
        alist.append(a)
print(sum(alist))
