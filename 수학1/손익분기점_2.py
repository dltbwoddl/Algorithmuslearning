def Break_even_point(A,B,C):
    if B>=C:
        return(-1)
    else:
        return(A//(C-B)+1)

A,B,C=map(int, input().split())

print(Break_even_point(A,B,C))
