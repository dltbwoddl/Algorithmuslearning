n=int(input())
s=input()
si=[int(i) for i in s.split()]
mi=si[0]
ma=si[0]
for i in si[1:]:
    if mi>i:
        mi=i
    elif ma<i:
        ma=i
print("%d %d" %(mi, ma))
    
