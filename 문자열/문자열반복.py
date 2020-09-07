n=int(input(""))
for i in range(n):
    a=''
    s=input("").split()
    for k in s[1]:
        for j in range(int(s[0])):
            a+=str(k)
    print(a)
    a=''
