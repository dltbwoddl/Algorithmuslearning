while True:
    n=[int(i) for i in input().split()]
    if n==[0,0,0]:
        break
    m=max(n)
    n.remove(m)
    r=0
    for i in n:
       r+=i*i
    if r==m*m:
        print("right")
    else:
        print("wrong")
