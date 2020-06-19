#https://www.acmicpc.net/problem/4344
def meanpercent (scores):
    t=0
    s=len(scores)
    m=sum(scores)/s
    for i in range(0,s):
        if scores[i]>m:
            t+=1
    return(t*100/s)
        
    
result=[]
for i in range(0,int(input(''))):
    n=[int(j) for j in input().split()]
    del n[0]
    result.append(meanpercent(n))
for i in result:
    print('%0.3f%%'%(i))
        
