#https://www.acmicpc.net/problem/1931
times=[]
for i in range(0,int(input(""))):
    times.append([int(i) for i in input('').split()])
s=len(times)
for i in range(0,s):
    for j in range(i+1,s):
        if times[i][1]>times[j][1]:
            t=times[i]
            times[i]=times[j]
            times[j]=t
b=0
n=1
for i in range(0,len(times)):
    if times[b][1]<=times[i][0]:
        b=i
        n+=1
print(n)
