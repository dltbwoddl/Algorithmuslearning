#https://www.acmicpc.net/problem/1065
#함수내 전역변수 사용하기 global 활
def hansu(i):
    global n
    b=0
    for j in range(1,len(i)-1):
            if k==(i[j]-i[j+1]):
                pass
            else:
                return
    n+=1
a=int(input(""))
b=[]
global n
n=0
for i in range(1,a+1):
    b.append(str(i))
for i in b:
    if len(i)<=2:
        n+=1
    else:
        i=[int(k) for k in i]
        k=i[0]-i[1]
        hansu(i)
print(n)
