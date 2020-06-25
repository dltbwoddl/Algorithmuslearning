#https://www.acmicpc.net/problem/1712
#4번 틀린 이유 디테일하게 하게 예시 생각하지 않아서
#반올림이 아니라 내림으로 했어야 했다.
import math
def Bepoint(fc,vc,p):
    i=1
    if vc>=p:
        return -1
    return math.floor(fc/(p-vc)+1)
m=[float(i) for i in input().split(' ')]
fc=m[0]
vc=m[1]
p=m[2]
print(Bepoint(fc,vc,p))
