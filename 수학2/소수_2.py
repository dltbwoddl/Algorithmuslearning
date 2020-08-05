def primenumber(n):
    if n==1:
        return
    for i in range(2,n):
        if n%i==0:
            return
    return(n)
n_1=int(input(""))
n_2=int(input(""))
result=[]
for i in range(n_1,n_2+1):
    j=primenumber(i)
    if j:
        result.append(j)

if result:
    print(sum(result))
    print(result[0])
else:
    print(-1)
