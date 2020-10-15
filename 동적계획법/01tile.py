n=int(input(""))
def tile01(n,a_1,a_2):
    if n==1:
        return(a_1)
    for i in range(n-2):
        a_1,a_2=a_2%15746,(a_1+a_2)%15746
    return(a_2)
print(tile01(n,1,2))
#숫자자체가 커지다 보니 나중에 나눠주면 나머지를 구하는 시간이 오래걸려 시간초과가 나온다.
