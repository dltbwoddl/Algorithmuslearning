#https://www.acmicpc.net/problem/11399
n=int(input(""))
s=[int(i) for i in input("").split()]
s.sort()
result=0
r=0
for i in s:
    result=result+i
    r+=result
print(r)
