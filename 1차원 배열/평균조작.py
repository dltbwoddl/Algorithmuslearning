#1
def meanmanipulate(n,t):
    t.sort()
    m=t[n-1]
    r=0
    for i in t:
       r+=i/m*100
    return(r/n) 
n=int(input(""))
t=[int(i) for i in input().split()]
print(meanmanipulate(n,t))

#2
def meanmanipulate_2(n,t):
    m=max(t)
    r=0
    for i in t:
        r+=i/m*100
    return(r/n)
print(meanmanipulate_2(n,t))
        
#3
def meanmanipulate_3(n,t):
    m=max(t)
    return (sum(map(lambda x:x/m*100,t))/n)
print(meanmanipulate_3(n,t))

#4
def meanmanipulate_4(n,t):
    m=max(t)
    return (sum(t)/m*100/n)
print(meanmanipulate_4(n,t))
