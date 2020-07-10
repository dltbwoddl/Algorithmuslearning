n=[int(i) for i in input().split()]
nl=[i for i in range(1,n[0]+1)]
global j
j=n[1]
r=0

def bt(nl,r):
    if r==j:
        print()
        return
    else:
        #전에 있는 지역함수인 nl에는 영향을 주지 않으면서 필요없는 것이 걸러진 nl이 새로 들어가야 한다.
        for i in nl:
            print(i,"",end='')
            ind=nl.index(i)
            bt(nl[:ind]+nl[ind+1:],r+1)
bt(nl,r)
#print부분 수정하기.
