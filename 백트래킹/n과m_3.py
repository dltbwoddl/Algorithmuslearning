#중간상태를 저장하는 변수 사용.
def nandm(MiddleState,numlist,count):
    if count==1:
        for i in numlist:
            print(MiddleState+str(i))
    else:
        for ind,i in enumerate(numlist):
            MiddleState+=(str(i)+" ")
            nandm(MiddleState,(numlist[:ind]+numlist[ind+1:]),count-1)
            MiddleState=MiddleState[:-2]
inp=[int(i) for i in input().split()]
nl=[i for i in range(1,inp[0]+1)]
mid=""
nandm(mid,nl,inp[1])
