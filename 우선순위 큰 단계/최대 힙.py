#시간초과
#https://wiki.python.org/moin/TimeComplexity
#remove는 o(n)   
#https://www.acmicpc.net/problem/11279
n=int(input(""))
result=[]
alist=[]
for i in range(0,n):
    n_1=int(input(""))
    alist.append(n_1)
    if n_1==0:
        if result==[]:
            result.append(0)
        else:
            result.append(max(alist))
            alist.remove(max(alist))
for i in result:
    print(i)
