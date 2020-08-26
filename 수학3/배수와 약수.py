while True:
    n=[int(i) for i in input().split()]
    r=0
    if n==[0,0]:
        break
    n_1=n[0]
    n_2=n[1]
    if n_1%n_2!=0:
        if n_2%n_1==0:
            print("factor")
        else:
            print("neither")
    else:
        if n_1>n_2:
            print("multiple")
