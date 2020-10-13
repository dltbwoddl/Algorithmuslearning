triangle=[ [int(j) for j in input().split()] for i in range(int(input()))]

def ltriangle(t,ind_1):
    if ind_1==(len(t)-1):
        print(t[ind_1][0]+max(t[ind_1-1][0],t[ind_1-1][1]))
    else:
        for i in range(0,len(t[ind_1])):
            t[ind_1][i]+=max(t[ind_1-1][i],t[ind_1-1][i+1])
        ltriangle(t,ind_1+1)
triangle.reverse()
ltriangle(triangle,1)
        
