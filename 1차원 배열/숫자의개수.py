#내 풀이 : 받은 숫자를 곱한 것을 string으로 처리하여 string을 count했다.
#결과 : 72ms
def numbercount(n):
    n=str(n)
    for i in range(10):
        print(n.count(str(i)))
n=1
for i in range(3):
    n*=int(input(""))
numbercount(n)

#다른 방식 숫자의 곱 숫자 하나하나를 map함수를 이용해 숫자 리스트로 만든뒤
#리스트에서 숫자를 카운트 한다.
#같은 숫자일 경우 문자열로 바꾸어 요소를 count하는 것보다. 숫자로 바꾸어 count하는 것이 더 빠르다.
#결과 : 64ms
def numbercount_2(n):
    n=list(map(int,str(n)))
    for i in range(10):
        print(n.count(i))
n=1
for i in range(3):
    n*=int(input(""))
numbercount_2(n)
