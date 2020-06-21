#https://www.acmicpc.net/problem/2798
a=[int(i) for i in input("").split()]
b=[int(i) for i in input("").split()]
max=a[1]
n=a[0]
result=0
ans=0
for i in range(0,n):
    result+=b[i]
    for j in range(0,n):
        if j==i:
            pass
        else:
            result_1=result
            result=result_1+b[j]
            for k in range(0,n):
                if k==j or k==i:
                    pass
                else:
                    result_2=result
                    result=result_2+b[k]
                    if max>=result and result>ans:
                        ans=result
                    result=result_2
            result=result_1
    result=0

print(ans)
