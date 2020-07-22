r=''
n=[int(i) for i in input()]
n.sort()
for i in n[::-1]:
    r+=str(i)
print(r)
