def bs(n):
    i=1
    j=1
    if n==1:
        return "1/1"
    while n>i:
        j+=1
        i+=j
    if n==i:
        if j%2==0:
            return str(j)+"/"+str(1)
        else:
            return str(1)+"/"+str(j)
    else:
        if j%2==0:
            return str(j-(i-n))+"/"+str(1+i-n)
        else:
            return str(1+i-n)+"/"+str(j-(i-n))
n=int(input(""))
print(bs(n))
