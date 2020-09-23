n=int(input(""))
#재귀로 풀기
def Fibonacci(a,b,n):
    if n==0:
        print(b)
        return
    Fibonacci(b,a+b,n-1)
Fibonacci(0,1,n-1)

#2루프로 풀기 while
def Fibonacci_2(a,b,n):
    while n!=0:
        t=b
        b+=a
        a=t
        n-=1
    print(b)
    return
Fibonacci_2(0,1,n-1)

#3루프 for로 풀기.
def Fibonacci_3(a,b,n):
    for i in range(n):
        a,b=b,a+b
    print(b)
Fibonacci_3(0,1,int(input())-1)

#4 다른 사람 코드 참조 exec기능학습
a,b=0,1;exec("a,b=b,a+b;"*int(input()));print(a)
