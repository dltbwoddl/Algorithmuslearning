#1
zero=0
one=0
def fibonacci(n):
    global zero, one
    if n==0:
        zero+=1
        return(0)
    elif n==1:
        one+=1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n=int(input())
for i in range(n):
    k=int(input())
    fibonacci(k)
    print("%d %d"%(zero, one))
    zero=0
    one=0
    
#2
n=int(input())
for i in range(n):
    k=int(input())
    a,b=1,0
    for j in range(k):
        a,b=b,a+b
    print("%d %d"%(a,b))


#3
n=int(input())
for i in range(n):
    a,b=1,0
    exec("a,b=b,a+b;"*int(input()))
    print("%d %d"%(a,b))

#4
exec('a,b=1,0;exec("a,b=b,a+b;"*int(input()));print("%d %d"%(a,b));'*int(input()))
