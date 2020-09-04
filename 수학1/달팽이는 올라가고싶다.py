import math
n=[int(i) for i in input().split()]
a=n[0]
b=n[1]
v=n[2]
print(math.ceil((v-a)/(a-b))+1)
