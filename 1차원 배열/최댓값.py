numlist=[]
for i in range(9):
    numlist.append(int(input()))
m=max(numlist)
print(m)
print(numlist.index(m)+1)
