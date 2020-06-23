alist=[]
ans=[]
for i in range(0,int(input(''))):
    ask=input()
    if 'push' in ask:
        ask=ask.split()
        alist.append(int(ask[1]))
    elif 'size' == ask:
        ans.append(len(alist))
    elif 'empty' == ask:
        if len(alist)==0:
            ans.append(1)
        else:
            ans.append(0)
    elif 'top'==ask:
        if len(alist)==0:
            ans.append(-1)
        else:
            ans.append(alist[-1])
    else:
        if len(alist)==0:
            ans.append(-1)
        else:
            ans.append(alist.pop())
for i in range(0,len(ans)):
    print(ans[i])
        
