#https://www.acmicpc.net/problem/1541
#런타임에러(0으로 시작할 수 있다.)
n=input("")
result=''
if '-' in n:
    for i in n:
        if '-' in result:
            if i =='-':
                result+=')'
        if i =='-':
            result+='-('
        else:
            if i=='0':
                if len(result)==0:
                    pass
                elif result[-1] in '+-()':
                    pass
                else:
                    result+=i
            else:
                result+=i
    if result.count('(')!=result.count(')'):
        result+=')'
        print(eval(result))
else:
    print(eval(n))
#너무 길다. 좀더 짧게 만들어보자. STRING 함수 사용해서
