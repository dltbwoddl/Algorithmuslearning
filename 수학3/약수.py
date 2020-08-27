#진짜 약수의 개수가 짝수일 때 혹은 홀수일 때로 나누어 푼다.
n=int(input(""))
t=[int(i) for i in input().split()]
t.sort()
if n%2!=0:
    print(1)
    i=t[len(t)//2]
    print(i*i)
else:

    print(t[0]*t[len(t)-1])
