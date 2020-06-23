#https://www.acmicpc.net/problem/10828
list=[]
ans=[]
def push(list,number):
    list.append(number)
def pop(list):
    if len(list)==0:
        return(-1)
    else:
        return(list.pop())
def size(list):
    return(len(list))
def empty(list):
    if len(list)==0:
        return(1)
    else:
        return(0)
def top(list):
    if len(list)==0:
        return(-1)
    else:
        return(list[-1])
for i in range(0,int(input(''))):
    ask=input()
    if 'push' in ask:
        ask=ask.split()
        push(list,int(ask[1]))
    else:
        ans.append(eval(ask+'(list)'))
for i in range(0,len(ans)):
    print(ans[i])
