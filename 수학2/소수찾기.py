#https://www.acmicpc.net/problem/1978
def primenumber(n):
    for i in range(2,n):
        if n%i==0:
            return 0
    if n==1:
        return 0
    return 1
a=int(input(''))
r=0
al=[int(i) for i in input('').split(' ')]
for i in al:
    r+=primenumber(i)
print(r)
