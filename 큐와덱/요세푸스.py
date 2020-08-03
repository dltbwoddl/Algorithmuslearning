def ysfs(n,k):
    olist=[i for i in range(1,n+1)]
    rlist=[]
    while True:
        if len(olist)>=3:
            rlist.append(olist.pop(2))
            olist=olist[2:]+olist[:2]
        elif 2<=len(olist):
            rlist.append(olist.pop(0))
        else:
            rlist.append(olist.pop())
            return rlist
n=[int(i) for i in input().split()]
print(ysfs(n[0],n[1]))
