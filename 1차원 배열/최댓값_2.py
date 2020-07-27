m=0
j=1
id=0
for i in range(9):
    num=int(input())
    if m<num:
        m=num
        id=j
    j+=1
           
print(m)
print(id)
