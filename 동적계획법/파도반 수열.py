#1
def padoban(n):
    a,b,c=1,1,1
    for j in range(n-3):
        a,b,c=b,c,a+b
    return c

for i in range(int(input(""))):
    a,b,c=1,1,1
    n=int(input(""))
    print(padoban(n))

#2 리스트로 풀어보기.
def padoban_3(n):
    a=[1,1,1,2,2]
    for i in range(n-5):
        ind=len(a)
        a+=[a[ind-2]+a[ind-3]]
    return(a[n-1])
for i in range(int(input(""))):
    print(padoban_3(int(input(""))))
