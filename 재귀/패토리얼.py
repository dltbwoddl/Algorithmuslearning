#https://www.acmicpc.net/problem/10872
def factorial(n):
    if n>=1:
        return n*factorial(n-1)
    else:
        return 1
num=int(input(""))
print(factorial(num))
