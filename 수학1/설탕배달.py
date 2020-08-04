n=int(input())
ans=n//3+1
bans=0

for i in range(0,n//5+1):
    bans=(n-i*5)%3
    if bans==0:
        if ans>i+(n-i*5)//3:
            ans=i+(n-i*5)//3
if ans!=n//3+1:
    print(ans)
else:
    print(-1)
