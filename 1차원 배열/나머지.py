n=[]
for i in range(10):
    n.append(int(input("")))

#1
def remainder(n):
    r=[]
    for i in n:
        r.append(i%42)
    r=set(r)
    return(len(r))
print(remainder(n))

#2
def remainder_2(n):
    r=[]
    for i in n:
        if i%42 in r:
            pass
        else:
            r.append(i%42)
    return(len(r))
print(remainder_2(n))

#3
print(len(set([int(input())%42 for i in range(10)])))
