#https://www.acmicpc.net/problem/2231
def bhh(number):
    for i in range(1,n):
        s=str(i)
        s_1=[int(i) for i in s]
        if int(s)+sum(s_1)==n:
            print(s)
            return
    print(0)
n=int(input(""))
bhh(n)
