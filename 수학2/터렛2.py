#두점사이의 거리를 기준으로 발생할 수 있는 경우의 수 나눈 것
#좀더 짧게 줄여보기.
def tr(ind):
    d=((ind[0]-ind[3])**2+(ind[1]-ind[4])**2)**0.5
    if ind[2]==ind[5]:
        if d>2*ind[2]:
            return 0
        elif d==2*ind[2]:
            return 1
        else:
            if d==0:
                return -1
            else:
                return 2
    else:
        if ind[2]>ind[5]:
            if d>ind[2]+ind[5]:
                return 0
            elif d==ind[2]+ind[5]:
                return 1
            else:
                if d==0:
                    return 0
                elif ind[5]+d==ind[2]:
                    return 1
                elif ind[5]+d<ind[2]:
                    return 0
                else:
                    return 2
                
        else:#ind[2]<ind[5]
            if d>ind[2]+ind[5]:
                return 0
            elif d==ind[2]+ind[5]:
                return 1
            else:
                if d==0:
                    return 0
                elif ind[2]+d==ind[5]:
                    return 1
                elif ind[2]+d<ind[5]:
                    return 0
                else:
                    return 2


n=int(input(""))
for i in range(n):
    ind=[int(j) for j in input().split()]
    print(tr(ind))
