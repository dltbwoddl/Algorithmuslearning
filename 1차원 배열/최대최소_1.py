n=int(input())
s=input()
si=[int(i) for i in s.split()]
si.sort()
print('%d %d'%(si[0], si[n-1]))
