s=input("")
s=s.upper()
ss=set(list(s))
r=0
g=0
rs=""
for i in ss:
    sc=s.count(i)
    if r<sc:
        r=sc
        rs=i
        g=0
    elif r==sc:
        g+=1
if g>0:
    print("?")
else:
    print(rs)