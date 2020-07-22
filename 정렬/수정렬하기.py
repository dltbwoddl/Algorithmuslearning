n=int(input(""))
global nl
nl=[]
for i in range(n):
    nl.append(int(input("")))
def sort_1(num,n):
    j=num
    if num==n-1:
        return 
    for i in range(num,n):
        if nl[j]>nl[i]:
            t=nl[j]
            nl[j]=nl[i]
            nl[i]=t
    sort_1(num+1,n)

sort_1(0,n)
for i in nl:
    print(i)
#런타임에러