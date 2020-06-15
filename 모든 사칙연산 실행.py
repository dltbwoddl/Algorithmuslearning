def all(a,b):
    v=['+','-','*','//','%']
    for i in v:
        print(eval(a+i+b))
s=input().split()
all(s[0],s[1])
