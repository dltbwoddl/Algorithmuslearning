a=[]
while a!=[0,0]:
    a=[int(i) for i in input().split()]
    if a==[0,0]:
        break
    print(sum(a))
