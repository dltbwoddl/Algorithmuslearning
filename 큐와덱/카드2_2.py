def card_2(n):
    len_n=len(n)
    while len_n!=1:
        k=[]
        if len_n%2==0:
            for i in range(1,len_n,2):
                k.append(n[i])
            len_n=int(len_n/2)
        else:
            k.append(n[-1])
            for i in range(1,len_n,2):
                k.append(n[i])
            len_n=len_n//2+1
        n=k 
    return(n[0])
n=[i for i in range(1, int(input(""))+1)]
print(card_2(n))
