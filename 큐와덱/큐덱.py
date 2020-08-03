#큐 공부하고 풀어보기  
#1.맨위의 것을 버린다.
#2.맨위에 있는 것을 맨아래로 옮긴다.
#3.이과정을 숫자 하나가 남을 때 까지 반복한다.

#pop(n)은 시간복잡도가 o(n)이다.pop()은 o(1)
def dequef(nlist):
    nlist.reverse()
    while len(nlist)>1:
        nlist.pop()
        t=nlist.pop()
        nlist=[t]+nlist
    ans=nlist.pop()
    return ans
#홀수 인덱스한 것을 버리고 reverse하는 것을 반복한다.
#그렇게 되면 한번에 절반을 버릴 수 있다.
def dequef_2(nlist):
    if len(nlist)==2:
        print(1)
        print(nlist)
        print(nlist[1])
        return
    elif len(nlist)%2==0:
        print(2)
        print(nlist)
        slist=[nlist[i] for i in range(1,len(nlist),2)]
        nlist=slist
        print(nlist)
    else :
        print(3)
        print(nlist)
        p=nlist[-1]
        slist=[nlist[i] for i in range(1,len(nlist),2)]
        slist=[p]+slist
        print(slist)
        nlist=slist
    dequef_2(nlist)
        

    
n=int(input(""))
if n==1:
    print(1)
else:
    nlist=[i for i in range(1,n+1)]
    dequef_2(nlist)

#홀수 인덱스 있는 것 버리고 reverse한다.
